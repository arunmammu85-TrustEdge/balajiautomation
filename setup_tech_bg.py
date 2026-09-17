import os
from PIL import Image

# 1. Convert to webp
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_tech_office_bg_1789664903363.png'
dest = 'assets/images/tech_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
    except Exception as e:
        print(f"Error converting: {e}")

# 2. Clean HTML inline styles
with open('index.html', 'r') as f:
    html = f.read()

old_tag = '<section id="technologies" class="fade-up" style="background:#f8fafc; border-bottom:1px solid var(--line); padding: 80px 0;">'
new_tag = '<section id="technologies" class="fade-up">'
html = html.replace(old_tag, new_tag)

with open('index.html', 'w') as f:
    f.write(html)

# 3. Add CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

new_css = """
/* Technologies Parallax Background */
#technologies {
  background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.90)), url('../images/tech_bg.webp') center/cover fixed no-repeat;
  padding: 120px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
"""

with open('assets/css/style.css', 'a') as f:
    f.write(new_css)

print("Technologies background applied.")
