with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Update header
old_header_bg = "background: linear-gradient(90deg, #f8fafc 0%, #dbeafe 100%);"
new_header_bg = "background: linear-gradient(90deg, #f8fafc 0%, #e2e8f0 100%);"
css = css.replace(old_header_bg, new_header_bg)

# Update footer
old_footer_bg = "background: linear-gradient(90deg, #f8fafc 0%, #dbeafe 100%);"
new_footer_bg = "background: linear-gradient(90deg, #f8fafc 0%, #e2e8f0 100%);"
css = css.replace(old_footer_bg, new_footer_bg)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Gradient updated to Sleek Silver/Slate.")
