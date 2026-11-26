# Screenshots a logo sheet to PNG. Usage: py -3 shot.py [name]  (default: logos -> logos.html -> logos.png)
import pathlib, sys
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).parent
name = sys.argv[1] if len(sys.argv) > 1 else "logos"
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome"); p = b.new_page(viewport={"width":1600,"height":900})
    p.goto((H/f"{name}.html").as_uri()); p.wait_for_timeout(1500)
    p.screenshot(path=str(H/f"{name}.png"), full_page=True); b.close()
print("ok")
