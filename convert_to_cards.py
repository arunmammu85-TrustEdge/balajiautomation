with open('assets/css/style.css', 'r') as f:
    css = f.read()

import re

# We will remove the old block and replace it.
# The old block spans from `.brand-list {` to the end of `.brand-row .brand-logo { ... }`

old_css_part1 = ".brand-list { display: flex; flex-direction: column; border: 1px solid var(--line-bright); border-radius: 12px; overflow: hidden; margin-top: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.03); }"
new_css_part1 = ".brand-list { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; margin-top: 32px; border: none; background: transparent; box-shadow: none; overflow: visible; }"
css = css.replace(old_css_part1, new_css_part1)

old_css_part2 = ".brand-row { padding: 32px; border-bottom: 1px solid var(--line-bright); background: #ffffff; transition: background 0.3s; }"
new_css_part2 = ".brand-row { background: rgba(255, 255, 255, 0.95); padding: 32px; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.06); border: 1px solid rgba(0,0,0,0.05); transition: transform 0.3s ease, box-shadow 0.3s ease; }"
css = css.replace(old_css_part2, new_css_part2)

old_css_part3 = ".brand-row:last-child { border-bottom: none; }"
new_css_part3 = ".brand-row:last-child { border-bottom: 1px solid rgba(0,0,0,0.05); }"
css = css.replace(old_css_part3, new_css_part3)

old_css_part4 = ".brand-row:hover { background: #f8fafc; }"
new_css_part4 = ".brand-row:hover { background: #ffffff; transform: translateY(-4px); box-shadow: 0 16px 40px rgba(0,0,0,0.12); }"
css = css.replace(old_css_part4, new_css_part4)

# Replace logo size
old_logo = ".brand-row .brand-logo { height: 80px; width: auto; max-width: 280px; margin-bottom: 16px; display: block; object-fit: contain; }"
new_logo = ".brand-row .brand-logo { height: 40px; width: auto; max-width: 100%; margin-bottom: 24px; display: block; object-fit: contain; }"
css = css.replace(old_logo, new_logo)

# Also fix the "Omron Fuji LG" flex row which had gap:32px and inline flex in HTML
# I'll let it naturally flow since we removed inline max-heights, but the inline display:flex in HTML might mess up the grid card. Let's fix that inline style.

with open('assets/css/style.css', 'w') as f:
    f.write(css)

with open('index.html', 'r') as f:
    html = f.read()

# Remove the inline flex style from the "Others" row so it behaves like a normal card
html = html.replace('<div class="brand-row" style="display:flex; flex-direction:row; flex-wrap:wrap; align-items:center; gap:32px;">', '<div class="brand-row">')

with open('index.html', 'w') as f:
    f.write(html)

print("Converted rows to cards.")
