# Renders the personal IG/TikTok story promo: story.png (still) and story.mp4 (8s, animated aura).
# Top ~250px and bottom ~300px are kept clear for the story app's own UI.
import pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
URL = (HERE / "story.html").as_uri()

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(URL); pg.wait_for_timeout(1500)
    pg.screenshot(path=str(HERE / "story.png"))
    # Video: record the live page so the glows drift and icons float.
    ctx = b.new_context(viewport={"width": 1080, "height": 1920},
                        record_video_dir=str(HERE / "_vid"), record_video_size={"width": 1080, "height": 1920})
    v = ctx.new_page(); v.goto(URL); v.wait_for_timeout(9500)
    path = v.video.path(); ctx.close(); b.close()

ff = shutil.which("ffmpeg")
if ff:
    # Skip the first 1.2s (font load), keep 8s, H.264 for IG/TikTok.
    subprocess.run([ff, "-y", "-loglevel", "error", "-ss", "1.2", "-i", path, "-t", "8", "-r", "30",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart",
                    str(HERE / "story.mp4")], check=True)
shutil.rmtree(HERE / "_vid", ignore_errors=True)
print("ok", bool(ff))
