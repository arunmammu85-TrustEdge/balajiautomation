from PIL import Image
import os
import shutil

# 1. Copy and convert image
source_img = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_distant_hero_bg_1789664125808.png'
dest_png = 'assets/images/hero_bg.png'
dest_webp = 'assets/images/hero_bg.webp'

if os.path.exists(source_img):
    shutil.copy(source_img, dest_png)
    try:
        im = Image.open(dest_png).convert("RGB")
        im.save(dest_webp, 'webp', quality=85)
        print("Converted hero image to WebP.")
    except Exception as e:
        print(f"Error converting image: {e}")

# 2. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

old_hero_css = ".hero { padding: 100px 0 80px; position: relative; background: #fff; border-bottom: 1px solid var(--line); }"
new_hero_css = """.hero { 
  padding: 100px 0 80px; 
  position: relative; 
  background: linear-gradient(to right, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.6)), url('../images/hero_bg.webp') center/cover no-repeat; 
  border-bottom: 1px solid var(--line); 
}
.hero .eyebrow { color: #94a3b8 !important; }
.hero h1 { color: #ffffff !important; }
.hero h1 .hl { color: #60a5fa !important; }
.hero p.lead { color: #cbd5e1 !important; }
.hero .hero-meta .lbl { color: #94a3b8 !important; }"""

css = css.replace(old_hero_css, new_hero_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Hero section CSS updated.")
