import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# 1. Update Header to dark gradient
old_header = """header {
  position: sticky; top: 0; z-index: 50;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
  transition: all 0.3s ease;
}"""

new_header = """header {
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
nav a.active { color: #ffffff !important; background: var(--accent) !important; box-shadow: 0 4px 12px var(--accent-glow) !important; }
"""

if 'linear-gradient(90deg, #0f172a' not in css:
    css = css.replace(old_header, new_header)

# 2. Update Chip Strip to centered gradient
old_chip = """/* Chip Strip */
.strip { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px; }
.chip {
  font-size: 14px; font-weight: 600; color: var(--text-dim); background: #fff;
  border: 1px solid var(--line-bright); padding: 10px 20px; border-radius: 30px;
  transition: all 0.3s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.chip:hover { border-color: var(--accent); color: var(--text); background: var(--accent); transform: translateY(-2px); box-shadow: 0 8px 16px var(--accent-glow); }"""

new_chip = """/* Chip Strip */
.strip { display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-top: 32px; }
.chip {
  font-size: 15px; font-weight: 700; color: #ffffff;
  background: linear-gradient(135deg, var(--accent), #0369a1);
  border: none; padding: 12px 24px; border-radius: 30px;
  transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
}
.chip:hover { transform: translateY(-4px) scale(1.05); box-shadow: 0 8px 24px rgba(2, 132, 199, 0.5); color: #ffffff; }"""

css = css.replace(old_chip, new_chip)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Styles updated.")
