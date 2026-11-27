# Google Play developer page assets: play-header.png (4096x2304, no alpha) and play-icon.png (512x512).
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
D = pathlib.Path(__file__).resolve().parent
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    p = b.new_page(viewport={"width": 2560, "height": 1440}, device_scale_factor=1.6)
    p.goto((D / "play-header.html").as_uri()); p.wait_for_timeout(800)
    p.screenshot(path=str(D / "play-header.png"))
    b.close()
h = Image.open(D / "play-header.png").convert("RGB"); h.save(D / "play-header.png")
i = Image.open(D / "social-avatar.png").convert("RGB").resize((512, 512), Image.LANCZOS); i.save(D / "play-icon.png")
for n in ("play-header.png", "play-icon.png"):
    im = Image.open(D / n); print(n, im.size, im.mode, (D / n).stat().st_size)
h.resize((1280, 720), Image.LANCZOS).save(D / "play-header-preview.png")
