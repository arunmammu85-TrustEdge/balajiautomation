import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace existing footer text styles
old_p = "footer p { color: var(--text-dim); font-size: 14px; margin: 0; }"
new_p = "footer p { color: var(--text-dim); font-size: 13px; font-weight: 600; margin: 0; }"
css = css.replace(old_p, new_p)

old_a = "footer .foot-links a { color: var(--text-dim); font-size: 14px; font-weight: 600; transition: color 0.2s; }"
new_a = "footer .foot-links a { color: var(--text-dim); font-size: 13px; font-weight: 600; transition: color 0.2s; }"
css = css.replace(old_a, new_a)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Footer fonts unified.")
