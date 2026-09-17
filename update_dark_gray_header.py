with open('assets/css/style.css', 'r') as f:
    css = f.read()

# 1. Update Header
old_header = """header {
  position: sticky; top: 0; z-index: 50;
  background: linear-gradient(90deg, #f8fafc 0%, #e2e8f0 100%);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  transition: all 0.3s ease;
}
.brand img { background: transparent; border-radius: 0; padding: 0; height: 50px; transition: height 0.3s ease; }"""

new_header = """header {
  position: sticky; top: 0; z-index: 50;
  background: linear-gradient(90deg, #334155 0%, #1e293b 100%);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
  transition: all 0.3s ease;
}
.brand img { background: #ffffff; border-radius: 4px; padding: 2px; height: 50px; transition: height 0.3s ease; }
header .brand-text .name { color: #ffffff !important; }
header .brand-text .tag { color: #94a3b8 !important; }
header nav a { color: #cbd5e1 !important; }
header nav a:hover { color: #ffffff !important; background: rgba(255,255,255,0.1) !important; }
header nav a.active { color: #ffffff !important; background: var(--accent) !important; box-shadow: 0 4px 12px var(--accent-glow) !important; }"""

css = css.replace(old_header, new_header)

# 2. Update Footer background
old_footer_bg = "background: linear-gradient(90deg, #f8fafc 0%, #e2e8f0 100%);"
new_footer_bg = "background: linear-gradient(90deg, #334155 0%, #1e293b 100%);"
css = css.replace(old_footer_bg, new_footer_bg)

# 3. Update Footer text colors
css = css.replace("footer p { color: var(--text-dim);", "footer p { color: #cbd5e1;")
css = css.replace("footer .foot-links a { color: var(--text-dim);", "footer .foot-links a { color: #cbd5e1;")
css = css.replace("footer .foot-links a:hover { color: var(--accent);", "footer .foot-links a:hover { color: #ffffff;")
css = css.replace(".site-cred { color: var(--text-dim);", ".site-cred { color: #cbd5e1;")

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Applied attractive dark gray header and footer.")
