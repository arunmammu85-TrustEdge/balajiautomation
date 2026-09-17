import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

old_css = """.p-item { background: transparent; border: none; overflow: hidden; transition: all 0.3s ease; }
.p-item:hover { transform: translateY(-6px); }
.p-item img { width: 100%; height: 200px; object-fit: cover; border-bottom: 1px solid var(--line); transition: transform 0.5s ease; }
.p-item:hover img { transform: scale(1.05); }
.p-item .cap { padding: 16px 0; font-size: 15px; color: var(--text); font-weight: 600; position: relative; z-index: 2; background: transparent; }"""

new_css = """.p-item { background: #ffffff; border: 1px solid var(--line-bright); border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.03); overflow: hidden; transition: all 0.3s ease; display: flex; flex-direction: column; }
.p-item:hover { transform: translateY(-6px); box-shadow: 0 12px 30px rgba(0,0,0,0.06); border-color: var(--accent); }
.p-item img { width: 100%; height: 200px; object-fit: cover; border-bottom: 1px solid var(--line-bright); display: block; transition: transform 0.5s ease; }
.p-item:hover img { transform: scale(1.05); }
.p-item .cap { padding: 16px; font-size: 15px; color: var(--text); font-weight: 600; position: relative; z-index: 2; background: #ffffff; flex-grow: 1; }"""

css = css.replace(old_css, new_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Product items styled as aligned cards.")
