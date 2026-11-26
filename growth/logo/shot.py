# Screenshots logos.html (option sheet) to logos.png.
import pathlib
from playwright.sync_api import sync_playwright
H = pathlib.Path(__file__).parent
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome"); p = b.new_page(viewport={"width":1600,"height":900})
    p.goto((H/"logos.html").as_uri()); p.wait_for_timeout(1500)
    p.screenshot(path=str(H/"logos.png"), full_page=True); b.close()
print("ok")
