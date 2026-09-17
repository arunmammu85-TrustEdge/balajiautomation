import re

with open('index.html', 'r') as f:
    html = f.read()

old_others = """  <div class="brand-row">
    <h4>Others</h4>
    <div class="cat-row">Omron, Fuji, LG</div>
  </div>"""

new_others = """  <div class="brand-row" style="display:flex; flex-direction:row; flex-wrap:wrap; align-items:center; gap:32px;">
    <img src="assets/images/logos/omron.svg" class="brand-logo" alt="Omron" style="margin:0; max-height:24px; width:auto;">
    <img src="assets/images/logos/fuji.svg" class="brand-logo" alt="Fuji Electric" style="margin:0; max-height:24px; width:auto;">
    <img src="assets/images/logos/lg.svg" class="brand-logo" alt="LG" style="margin:0; max-height:24px; width:auto;">
  </div>"""

html = html.replace(old_others, new_others)

with open('index.html', 'w') as f:
    f.write(html)

print("Others replaced with logos.")
