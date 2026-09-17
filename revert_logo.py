with open('index.html', 'r') as f:
    html = f.read()

old_logo = 'src="assets/images/ba_logo.webp" style="border-radius: 6px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);"'
new_logo = 'src="assets/images/img_26_logo_cropped.webp"'

html = html.replace(old_logo, new_logo)

with open('index.html', 'w') as f:
    f.write(html)

print("Reverted to original logo in HTML.")
