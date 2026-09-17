import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove inline styles from all brand logos to let CSS handle it
html = re.sub(r'class="brand-logo" alt="([^"]+)" style="[^"]+"', r'class="brand-logo" alt="\1"', html)

with open('index.html', 'w') as f:
    f.write(html)


with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Ensure brand logos are big (96px height)
old_css = ".brand-row .brand-logo { height: 32px; width: auto; max-width: 200px; margin-bottom: 16px; display: block; }"
new_css = ".brand-row .brand-logo { height: 80px; width: auto; max-width: 280px; margin-bottom: 16px; display: block; object-fit: contain; }"
css = css.replace(old_css, new_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Logos inline styles stripped and CSS size updated.")
