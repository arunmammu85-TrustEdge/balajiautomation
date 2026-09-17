with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace the dark header with a light icy gradient
old_header = """header {
  position: sticky; top: 0; z-index: 50;
  background: linear-gradient(90deg, #0f172a, #1e293b);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 20px rgba(0,0,0,0.2);
  transition: all 0.3s ease;
}
.brand img { background: #ffffff; border-radius: 6px; padding: 2px; } /* Ensures logo is visible */
.brand-text .name { color: #ffffff !important; }
.brand-text .tag { color: #94a3b8 !important; }
nav a { color: #cbd5e1 !important; }
nav a:hover { color: #ffffff !important; background: rgba(255, 255, 255, 0.1) !important; }
nav a.active { color: #ffffff !important; background: var(--accent) !important; box-shadow: 0 4px 12px var(--accent-glow) !important; }"""

new_header = """header {
  position: sticky; top: 0; z-index: 50;
  background: linear-gradient(90deg, rgba(255,255,255,0.95), rgba(240,249,255,0.95));
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  transition: all 0.3s ease;
}
.brand img { background: transparent; border-radius: 0; padding: 0; }
"""

css = css.replace(old_header, new_header)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Header gradient changed to light.")
