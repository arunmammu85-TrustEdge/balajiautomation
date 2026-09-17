import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace wrapper div
old_wrapper = '<div style="margin-top: 48px; width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.05);">'
new_wrapper = '<div style="margin-top: 48px; width: 100%; max-width: 500px; margin-left: auto; margin-right: auto; border-radius: 12px; overflow: hidden; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">'
html = html.replace(old_wrapper, new_wrapper)

# Replace iframe height
html = html.replace('width="100%" height="450"', 'width="100%" height="280"')

with open('index.html', 'w') as f:
    f.write(html)

print("Map reduced.")
