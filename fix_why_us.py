import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove the massive inline margin on split
html = html.replace('<div class="split" style="margin-bottom: 80px;">', '<div class="split">')

# Split WHY CHOOSE US into its own section
old_html = """    </div>

    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">WHY CHOOSE US</div>"""

new_html = """    </div>
  </div>
</section>

<!-- ============ WHY CHOOSE US ============ -->
<section id="why-choose-us" style="background:#f8fafc; border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">WHY CHOOSE US</div>"""

html = html.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(html)


with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Update why-grid and why-item
old_grid = ".why-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; margin-top: 40px; }"
new_grid = ".why-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; margin-top: 40px; }"
css = css.replace(old_grid, new_grid)

old_item = """.why-item { background: transparent; padding: 24px 16px; border: none; transition: all 0.3s ease; }
.why-item:hover { transform: translateY(-4px); }
.why-item .tagnum { color: var(--accent-secondary); font-size: 14px; font-weight: 700; letter-spacing: 0.05em; }
.why-item h3 { margin-top: 12px; font-size: 20px; color: #0f172a; }
.why-item p, .why-item li { color: var(--text-dim); font-size: 15px; margin-top: 12px; }
.why-item ul { padding-left: 20px; margin: 12px 0 0; }
.why-item li { margin-bottom: 8px; }"""

new_item = """.why-item {
  background: #ffffff;
  padding: 32px;
  border-radius: 12px;
  border: 1px solid var(--line-bright);
  box-shadow: 0 4px 16px rgba(0,0,0,0.03);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}
.why-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.06);
  border-color: var(--accent);
}
.why-item .tagnum { color: var(--accent-secondary); font-size: 13px; font-weight: 800; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px; }
.why-item h3 { font-size: 20px; color: var(--accent); margin-bottom: 16px; border-bottom: 2px solid var(--line); padding-bottom: 12px; }
.why-item p, .why-item li { color: var(--text-dim); font-size: 15px; line-height: 1.6; }
.why-item ul { padding-left: 20px; margin: 0; }
.why-item li { margin-bottom: 8px; }
.why-item li:last-child { margin-bottom: 0; }"""

css = css.replace(old_item, new_item)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("WHY CHOOSE US split and cards applied.")
