import os
from PIL import Image

# 1. Convert to webp
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/domain_knowledge_bg_1789664612009.png'
dest = 'assets/images/domain_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
    except Exception as e:
        print(f"Error converting: {e}")

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

old_domain = '<section id="domain-knowledge" style="background:#ffffff; padding: 80px 0; border-bottom:1px solid var(--line);">'
new_domain = '<section id="domain-knowledge" class="fade-up">'
html = html.replace(old_domain, new_domain)
with open('index.html', 'w') as f:
    f.write(html)

# 3. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

new_css = """
/* Domain Knowledge Parallax Background */
#domain-knowledge {
  background: linear-gradient(to right, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.8)), url('../images/domain_bg.webp') center/cover fixed no-repeat;
  padding: 120px 0;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
#domain-knowledge h2 { color: #ffffff !important; }
#domain-knowledge p.lead { color: #cbd5e1 !important; }
#domain-knowledge .eyebrow { color: #94a3b8 !important; }
#domain-knowledge .strip .chip { 
  background: rgba(255,255,255,0.08); 
  border-color: rgba(255,255,255,0.15); 
  color: #ffffff; 
  backdrop-filter: blur(8px); 
  -webkit-backdrop-filter: blur(8px);
}
#domain-knowledge .strip .chip:hover {
  background: rgba(255,255,255,0.15); 
  border-color: rgba(255,255,255,0.3); 
}
"""

with open('assets/css/style.css', 'a') as f:
    f.write(new_css)

print("Domain knowledge section updated with parallax.")
