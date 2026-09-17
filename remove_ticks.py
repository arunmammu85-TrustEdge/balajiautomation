import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove the checkmark divs completely
html = html.replace('<div class="mark">✓</div>', '')

with open('index.html', 'w') as f:
    f.write(html)

print("Checkmarks removed.")
