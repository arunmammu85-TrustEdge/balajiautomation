with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace Header Background
old_header_bg = "background: radial-gradient(circle at center, rgba(255,255,255,0.98) 0%, rgba(241,245,249,0.95) 100%);"
new_header_bg = "background: linear-gradient(90deg, #f1f5f9 0%, #e0f2fe 100%);"
css = css.replace(old_header_bg, new_header_bg)

# Replace Footer Background (it might have the same radial gradient)
css = css.replace("background: radial-gradient(circle at center, rgba(255,255,255,0.98) 0%, rgba(241,245,249,0.95) 100%);", "background: linear-gradient(90deg, #f1f5f9 0%, #e0f2fe 100%);")

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Applied Soft Cloud gradient.")
