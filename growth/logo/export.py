# Renders the official SL logo SVGs to PNG/ICO. Usage: py -3 export.py
import pathlib, io
from playwright.sync_api import sync_playwright
from PIL import Image
R = pathlib.Path(__file__).resolve().parents[2]
IMG = R / "img"
jobs = [  # (svg, out, width, height)
    ("favicon.svg", R/"apple-touch-icon.png", 180, 180),
    ("favicon.svg", IMG/"logo-512.png", 512, 512),
    ("favicon.svg", IMG/"logo-1024.png", 1024, 1024),
    ("logo-mark.svg", IMG/"logo-mark.png", 1025, 520),
    ("logo-mark-dark.svg", IMG/"logo-mark-dark.png", 1025, 520),
]
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    def render(svg, w, h):
        p = b.new_page(viewport={"width": w, "height": h})
        t = pathlib.Path(__file__).parent / "_export.html"
        t.write_text(f'<html><body style="margin:0;background:transparent"><img src="{(IMG/svg).as_uri()}" width="{w}" height="{h}" style="display:block"></body></html>')
        p.goto(t.as_uri()); p.wait_for_timeout(300); t.unlink()
        png = p.screenshot(omit_background=True); p.close(); return png
    for svg, out, w, h in jobs:
        out.write_bytes(render(svg, w, h)); print(out.name, w, h)
    # apple-touch-icon should be opaque: iOS fills transparency with black, so flatten on the tile colour
    a = Image.open(R/"apple-touch-icon.png").convert("RGBA"); bg = Image.new("RGBA", a.size, (16, 20, 24, 255)); bg.alpha_composite(a); bg.convert("RGB").save(R/"apple-touch-icon.png")
    big = Image.open(io.BytesIO(render("favicon.svg", 256, 256))).convert("RGBA")
    big.save(R/"favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]); print("favicon.ico")
    b.close()
