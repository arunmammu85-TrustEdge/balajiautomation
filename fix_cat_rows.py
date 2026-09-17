import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace the cat-row css
old_css = """.brand-row .cat-row { margin-bottom: 8px; line-height: 1.6; font-size: 15px; color: var(--text-dim); }
.brand-row .cat-row:last-child { margin-bottom: 0; }"""

new_css = """.brand-row .cat-row { margin-bottom: 6px; padding: 10px 14px; border-radius: 8px; line-height: 1.6; font-size: 15px; color: var(--text); }
.brand-row .cat-row:nth-child(odd) { background: rgba(0,0,0,0.02); border-left: 3px solid rgba(0,0,0,0.05); }
.brand-row .cat-row:nth-child(even) { background: transparent; border-left: 3px solid transparent; }
.brand-row .cat-row:last-child { margin-bottom: 0; }"""

css = css.replace(old_css, new_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Sub-rows now have alternating colors.")
