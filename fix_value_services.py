import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the HTML block
old_html = """      </div>
      <div class="sec-head" style="margin-bottom:0;">
        <div class="eyebrow">VALUE SERVICES</div>
        <h2>What clients consistently ask us for.</h2>
      </div>"""

new_html = """      </div>
  </div>
</section>

<!-- ============ VALUE SERVICES ============ -->
<section id="value-services" style="background:#f1f5f9; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">VALUE SERVICES</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">What clients consistently ask us for.</h2>
    </div>"""

html = html.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(html)


# Update the CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

value_card_css = """
.value-item {
  background: #ffffff;
  padding: 32px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03);
  transition: all 0.3s ease;
  border: 1px solid var(--line-bright);
}
.value-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.06);
  border-color: var(--accent);
}
.value-item .mark { color: var(--accent); font-size: 24px; margin-bottom: 16px; font-weight: bold; }
.value-item h4 { font-size: 20px; color: var(--accent); margin-bottom: 16px; }
.value-item li { margin-bottom: 8px; color: var(--text-dim); line-height: 1.6; }
"""

# Replace the old styles if they exist, else append
if '.value-item' not in css:
    css += value_card_css
else:
    # Just in case, replace any generic .value-item rules
    css = re.sub(r'\.value-item \{.*?\}', '', css, flags=re.DOTALL)
    css += value_card_css

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Value services split into section and styled as cards.")
