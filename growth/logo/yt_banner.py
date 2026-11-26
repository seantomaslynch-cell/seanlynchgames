# Renders yt-banner.html to yt-banner.png (2560x1440) plus a preview with the safe areas marked.
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw
D = pathlib.Path(__file__).resolve().parent
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    p = b.new_page(viewport={"width": 2560, "height": 1440})
    p.goto((D / "yt-banner.html").as_uri()); p.wait_for_timeout(800)
    p.screenshot(path=str(D / "yt-banner.png"))
    b.close()
im = Image.open(D / "yt-banner.png").convert("RGB")
print("size", im.size, "bytes", (D / "yt-banner.png").stat().st_size)
# preview: full TV view with the desktop (2560x423) and all-devices (1546x423) boxes, plus the phone crop
pv = im.copy(); d = ImageDraw.Draw(pv)
d.rectangle([0, 508, 2559, 931], outline=(80, 200, 255), width=6)
d.rectangle([507, 508, 2053, 931], outline=(255, 60, 60), width=6)
pv.resize((1280, 720)).save(D / "yt-banner-guides.png")
im.crop((507, 508, 2053, 931)).save(D / "yt-banner-phone.png")
