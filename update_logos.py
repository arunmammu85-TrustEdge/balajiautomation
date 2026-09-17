import re

with open('index.html', 'r') as f:
    html = f.read()

# The current HTML has these anchor blocks:
# <a href="..." target="_blank" rel="noopener" aria-label="Facebook" style="display:flex; align-items:center; justify-content:center;"><svg ...>...</a>

fb_img = '<img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/2021_Facebook_icon.svg" alt="Facebook" style="width:28px; height:28px; border-radius:50%;">'
ig_img = '<img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" style="width:28px; height:28px;">'
x_img = '<img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg" alt="X" style="width:28px; height:28px;">'
in_img = '<img src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" alt="LinkedIn" style="width:28px; height:28px;">'

# Replace entire SVG tag with IMG tag inside the anchors
html = re.sub(r'(aria-label="Facebook"[^>]*>)\s*<svg.*?</svg>\s*(</a>)', r'\1' + fb_img + r'\2', html, flags=re.DOTALL)
html = re.sub(r'(aria-label="Instagram"[^>]*>)\s*<svg.*?</svg>\s*(</a>)', r'\1' + ig_img + r'\2', html, flags=re.DOTALL)
html = re.sub(r'(aria-label="Twitter"[^>]*>)\s*<svg.*?</svg>\s*(</a>)', r'\1' + x_img + r'\2', html, flags=re.DOTALL)
html = re.sub(r'(aria-label="LinkedIn"[^>]*>)\s*<svg.*?</svg>\s*(</a>)', r'\1' + in_img + r'\2', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("Updated logos to official SVGs via wikimedia.")
