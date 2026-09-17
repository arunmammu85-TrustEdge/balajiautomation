import re

with open('index.html', 'r') as f:
    html = f.read()

# Update delta and fuji sources
html = html.replace('assets/images/logos/delta.svg', 'images/delta.webp')
html = html.replace('assets/images/logos/fuji.svg', 'images/fuji.webp')

with open('index.html', 'w') as f:
    f.write(html)

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Increase size by 2 times (from 32px to 64px)
css = css.replace('.brand-row .brand-logo { height: 32px; width: auto; max-width: 200px; margin-bottom: 16px; display: block; }', 
                  '.brand-row .brand-logo { height: 64px; width: auto; max-width: 250px; margin-bottom: 16px; display: block; object-fit: contain; }')

# For the "Others" row where we had max-height:24px inline styles:
# We should probably increase those too if they meant those. Let's do it in HTML.
