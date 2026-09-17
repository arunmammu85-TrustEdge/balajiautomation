import re

# 1. Update CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace the brand-grid css with brand-list css
old_css = """/* Brand Grid */
.brand-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; margin-top: 24px; }
.brand-card { background: #ffffff; border: 1px solid var(--line-bright); border-radius: 12px; padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.03); transition: all 0.3s ease; }
.brand-card:hover { transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0,0,0,0.06); border-color: var(--accent); }
.brand-card h4 { font-size: 20px; color: var(--accent); margin-bottom: 16px; border-bottom: 2px solid var(--line); padding-bottom: 12px; }
.brand-card .cat-row { margin-bottom: 12px; line-height: 1.6; font-size: 15px; color: var(--text-dim); }
.brand-card .cat-row:last-child { margin-bottom: 0; }"""

new_css = """/* Brand Rows */
.brand-list { display: flex; flex-direction: column; border: 1px solid var(--line-bright); border-radius: 12px; overflow: hidden; margin-top: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.03); }
.brand-row { padding: 24px 32px; border-bottom: 1px solid var(--line-bright); transition: background 0.3s ease; }
.brand-row:last-child { border-bottom: none; }
.brand-row:nth-child(odd) { background: #ffffff; }
.brand-row:nth-child(even) { background: #f8fafc; }
.brand-row:hover { background: #f1f5f9; }
.brand-row h4 { font-size: 20px; color: var(--accent); margin-bottom: 12px; }
.brand-row .cat-row { margin-bottom: 8px; line-height: 1.6; font-size: 15px; color: var(--text-dim); }
.brand-row .cat-row:last-child { margin-bottom: 0; }
"""

css = css.replace(old_css, new_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)


# 2. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('class="brand-grid"', 'class="brand-list"')
html = html.replace('class="brand-card"', 'class="brand-row"')
html = html.replace('border-bottom: 2px solid var(--line); padding-bottom: 12px;', '')

with open('index.html', 'w') as f:
    f.write(html)

print("Switched from cards to rows.")
