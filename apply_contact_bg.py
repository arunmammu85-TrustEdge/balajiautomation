import os
import shutil
from PIL import Image

# 1. Convert to webp
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_reception_bg_1789664273387.png'
dest = 'assets/images/contact_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
    except Exception as e:
        print(f"Error converting: {e}")

# 2. Clean inline style from index.html
with open('index.html', 'r') as f:
    html = f.read()

old_contact_tag = 'id="contact" class="fade-up" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 40px 0;"'
new_contact_tag = 'id="contact" class="fade-up"'
html = html.replace(old_contact_tag, new_contact_tag)
with open('index.html', 'w') as f:
    f.write(html)

# 3. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

new_css = """
#contact {
  background: linear-gradient(to right, rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.75)), url('../images/contact_bg.webp') center/cover no-repeat;
  border-top: 1px solid rgba(255,255,255,0.05);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  padding: 80px 0;
  color: #ffffff;
}
#contact h2 { color: #ffffff !important; }
#contact p.lead { color: #cbd5e1 !important; }
#contact .eyebrow { color: #94a3b8 !important; }
#contact .contact-cell .lbl { color: #94a3b8 !important; }
#contact .contact-cell .val, #contact .contact-cell .val a { color: #ffffff !important; text-decoration: none; }
#contact .contact-cell .val a:hover { color: #60a5fa !important; }
"""

# Append to end of style.css
with open('assets/css/style.css', 'a') as f:
    f.write(new_css)

print("Contact section updated.")
