import os
from PIL import Image

# 1. Convert pano to value_bg.webp
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_tech_office_pano_1789665000601.png'
dest = 'assets/images/value_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
        print("Converted pano to value_bg.webp")
    except Exception as e:
        print(f"Error converting: {e}")

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

old_val = '<section id="value-services" style="background:#f1f5f9; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">'
new_val = '<section id="value-services" class="fade-up">'
html = html.replace(old_val, new_val)

with open('index.html', 'w') as f:
    f.write(html)

# 3. Add CSS for value-services
with open('assets/css/style.css', 'r') as f:
    css = f.read()

new_css = """
/* Value Services Parallax */
#value-services {
  background: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.5)), url('../images/value_bg.webp') top center/cover fixed no-repeat;
  padding: 120px 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
#value-services > .wrap > div:first-child {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 32px;
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  border: 1px solid rgba(255,255,255,0.8);
  margin-bottom: 48px;
}
#value-services > .wrap > div:first-child h2 { color: #0f172a !important; }
#value-services .value-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 24px;
}
#value-services .value-item {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  border: 1px solid rgba(255,255,255,0.8);
  transition: transform 0.3s ease;
}
#value-services .value-item:hover { transform: translateY(-4px); }
#value-services .value-item h4 { color: #0f172a !important; font-weight: 700; margin-bottom: 16px; }
"""

# ensure we don't duplicate if already present
if "#value-services {" not in css:
    with open('assets/css/style.css', 'a') as f:
        f.write(new_css)
    print("Value services CSS added.")
else:
    print("CSS already exists for value-services.")

