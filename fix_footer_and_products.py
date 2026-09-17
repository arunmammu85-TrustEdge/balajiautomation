import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Fix Footer
old_footer = """  <div class="wrap foot-row">
    <p>© 1990–<span id="year"></span> BALAJI AUTOMATION. ALL RIGHTS RESERVED.</p>
    <div class="foot-links">
      <a href="#home">Home</a>
      <a href="#products">Products</a>
      <a href="#services">Services</a>
      <a href="#contact">Contact</a>
    </div>
  </div>"""

new_footer = """  <div class="wrap foot-row">
    <p>© 1990–<span id="year"></span> BALAJI AUTOMATION. ALL RIGHTS RESERVED.</p>
    <div class="foot-links">
      <a href="#home">Home</a>
      <a href="#products">Products</a>
      <a href="#services">Services</a>
      <a href="#contact">Contact</a>
    </div>
    <p class="site-cred">Site by TrustWork | 9448610107</p>
  </div>"""

html = html.replace(old_footer, new_footer)


# 2. Fix Products Section Header
old_prod = """<div id="products">
  <section class="hero" style="padding-top:56px;">
    <div class="wrap">
      <div class="eyebrow">PRODUCTS</div>
      <h1 style="font-size:clamp(28px,4vw,44px);">Control panels built to client requirement.</h1>
    </div>
  </section>

      <div class="sec-head" style="margin-bottom:24px; text-align:center;">"""

new_prod = """<section id="products" style="background:#ffffff; border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">PRODUCTS</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Control panels built to client requirement.</h2>
    </div>

      <div class="sec-head" style="margin-bottom:24px; text-align:center;">"""

html = html.replace(old_prod, new_prod)

with open('index.html', 'w') as f:
    f.write(html)


with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Update Footer CSS
old_footer_css = """footer { border-top: 1px solid var(--line); padding: 40px 0; margin-top: 40px; background: #fff; }"""
new_footer_css = """footer { border-top: 1px solid var(--line); padding: 16px 0; background: #fff; }
.site-cred { color: var(--text-dim); font-size: 13px; margin: 0; text-align: right; font-weight: 600; }"""

css = css.replace(old_footer_css, new_footer_css)
css = css.replace('.foot-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px; }', '.foot-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; font-size: 13px; }')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Footer optimized and Products header unified.")
