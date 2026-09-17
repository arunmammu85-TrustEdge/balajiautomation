with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace Header Background
old_header_bg = "background: linear-gradient(90deg, #f1f5f9 0%, #e0f2fe 100%);"
new_header_bg = "background: linear-gradient(90deg, #d1fae5 0%, #ecfdf5 100%);"
css = css.replace(old_header_bg, new_header_bg)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Applied Pista gradient.")
