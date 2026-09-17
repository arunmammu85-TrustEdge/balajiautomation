import os
import shutil
from PIL import Image

# 1. Convert new panoramic image to webp
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_tech_office_pano_1789665000601.png'
dest = 'assets/images/tech_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
        print("Converted pano image.")
    except Exception as e:
        print(f"Error converting pano: {e}")

# 2. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

old_css = """#technologies {
  background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.90)), url('../images/tech_bg.webp') center/cover fixed no-repeat;
  padding: 120px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}"""

new_css = """#technologies {
  background: linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.4)), url('../images/tech_bg.webp') top center/cover fixed no-repeat;
  padding: 120px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
#technologies .wrap {
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 48px;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.1);
  border: 1px solid rgba(255,255,255,0.8);
}"""

css = css.replace(old_css, new_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Technologies section updated.")
