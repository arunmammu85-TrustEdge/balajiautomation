import re

# 1. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Remove the old .service-row CSS blocks
old_css_1 = """.service-row {
  display: grid; grid-template-columns: 280px 1fr; gap: 40px;
  padding: 40px; border: 1px solid var(--line); border-radius: var(--radius); margin-bottom: 24px;
  background: var(--bg-panel); transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.02);
}"""
old_css_2 = ".service-row:hover { transform: translateX(8px); border-bottom-color: var(--line-bright); }"
old_css_3 = "@media (max-width: 768px) { .service-row { display: grid; grid-template-columns: 1fr; gap: 24px; padding: 32px 0; border: none; border-bottom: 1px solid var(--line); transition: all 0.3s ease; background: transparent; } }"
old_css_4 = ".service-row img { border-radius: 8px; width: 100%; height: 180px; object-fit: cover; }"

css = css.replace(old_css_1, "")
css = css.replace(old_css_2, "")
css = css.replace(old_css_3, "")
css = css.replace(old_css_4, "")

# Append new grid card styles
new_css = """
.service-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 32px;
}
.service-row {
  display: flex;
  flex-direction: column;
  padding: 32px;
  background: #ffffff;
  border-radius: 16px;
  border: 1px solid var(--line);
  box-shadow: 0 8px 24px rgba(0,0,0,0.04);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  margin-bottom: 0;
}
.service-row:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 48px rgba(0,0,0,0.08);
}
.service-row img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 24px;
}
"""

with open('assets/css/style.css', 'a') as f:
    f.write(new_css)

# 2. Update index.html to wrap service rows in a grid
with open('index.html', 'r') as f:
    html = f.read()

# We need to find where the service rows start and end.
# They start after `<p class="lead" style="color:var(--text-dim); margin-top:16px;">We work across Allen-Bradley...`
# And end before `<!-- ============ WHY CHOOSE US ============ -->` wait, in this file, what is the next section?
# Let's just do a regex substitution to inject the wrapper.

# Find the header block of services
header_str = '<p class="lead" style="color:var(--text-dim); margin-top:16px;">We work across Allen-Bradley, Siemens and Schneider platforms, and provide value services that our clients rely on most.</p>\n    </div>'

# Find the start of the next section to know where to close the div
next_section_str = '</section>\n\n  <!-- ============ VALUE SERVICES ============ -->'
# Wait, let's just replace `</div>` and add `<div class="service-list">`
html = html.replace(header_str, header_str + '\n    <div class="service-list">')

# Now find the last `</div>` before the `</section>` of `#services`
# It's better to just manually inject `</div>` before `</section>`
old_close = '      </div>\n\n</section>\n\n<!-- ============ VALUE SERVICES ============ -->'
new_close = '      </div>\n    </div>\n</section>\n\n<!-- ============ VALUE SERVICES ============ -->'
if old_close in html:
    html = html.replace(old_close, new_close)
else:
    # try a more generic replacement
    html = html.replace('      </div>\n</section>\n\n<!-- ============ VALUE SERVICES ============ -->', '      </div>\n    </div>\n</section>\n\n<!-- ============ VALUE SERVICES ============ -->')

with open('index.html', 'w') as f:
    f.write(html)

print("Services section converted to responsive cards.")
