import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update counters
html = html.replace('data-target="5"', 'data-target="15"')
html = html.replace('data-target="8"', 'data-target="20"')

# 2. Update logos in the Others section to be larger (48px instead of 24px)
old_others = """<img src="assets/images/logos/omron.svg" class="brand-logo" alt="Omron" style="margin:0; max-height:24px; width:auto;">
    <img src="assets/images/logos/fuji.svg" class="brand-logo" alt="Fuji Electric" style="margin:0; max-height:24px; width:auto;">
    <img src="assets/images/logos/lg.svg" class="brand-logo" alt="LG" style="margin:0; max-height:24px; width:auto;">"""

new_others = """<img src="assets/images/logos/omron.svg" class="brand-logo" alt="Omron" style="margin:0; max-height:48px; height:48px; width:auto; object-fit:contain;">
    <img src="images/fuji.webp" class="brand-logo" alt="Fuji Electric" style="margin:0; max-height:48px; height:48px; width:auto; object-fit:contain;">
    <img src="assets/images/logos/lg.svg" class="brand-logo" alt="LG" style="margin:0; max-height:48px; height:48px; width:auto; object-fit:contain;">"""
html = html.replace(old_others, new_others)

# 3. Ensure Delta uses the new webp image
html = html.replace('<img src="assets/images/logos/delta.svg"', '<img src="images/delta.webp"')

with open('index.html', 'w') as f:
    f.write(html)

print("Updates applied.")
