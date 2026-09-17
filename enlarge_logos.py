with open('index.html', 'r') as f:
    html = f.read()

# Replace 48px with 96px for Omron, Fuji, LG
html = html.replace('max-height:48px; height:48px;', 'max-height:96px; height:96px;')

with open('index.html', 'w') as f:
    f.write(html)

print("Logos enlarged.")
