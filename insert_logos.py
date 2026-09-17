with open('index.html', 'r') as f:
    html = f.read()

# Replace text headings with images
html = html.replace('<h4>Allen Bradley</h4>', '<img src="assets/images/logos/allen-bradley.svg" class="brand-logo" alt="Allen Bradley">')
html = html.replace('<h4>Siemens</h4>', '<img src="assets/images/logos/siemens.svg" class="brand-logo" alt="Siemens">')
html = html.replace('<h4>Schneider</h4>', '<img src="assets/images/logos/schneider.svg" class="brand-logo" alt="Schneider Electric">')
html = html.replace('<h4>Mitsubishi</h4>', '<img src="assets/images/logos/mitsubishi.svg" class="brand-logo" alt="Mitsubishi Electric">')
html = html.replace('<h4>Delta</h4>', '<img src="assets/images/logos/delta.svg" class="brand-logo" alt="Delta Electronics">')

with open('index.html', 'w') as f:
    f.write(html)

with open('assets/css/style.css', 'r') as f:
    css = f.read()

logo_css = """
.brand-row .brand-logo { height: 32px; width: auto; max-width: 200px; margin-bottom: 16px; display: block; }
"""
if '.brand-logo' not in css:
    css += logo_css

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Logos downloaded and inserted.")
