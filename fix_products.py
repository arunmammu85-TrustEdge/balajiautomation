with open('index.html', 'r') as f:
    html = f.read()

old_header = """<div id="products">
  <section class="hero" style="padding-top:56px;">
    <div class="wrap">
      <div class="eyebrow">PRODUCTS</div>
      <h1 style="font-size:clamp(28px,4vw,44px);">Control panels built to client requirement.</h1>
      <p class="lead">We leverage long-term vendor partnerships to procure the highest-quality switchgear, drive and automation equipment, integrated smoothly.</p>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">"""

new_header = """<section id="products" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">PRODUCTS</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Control panels built to client requirement.</h2>
      <p class="lead" style="color:var(--text-dim); margin-top:16px;">We leverage long-term vendor partnerships to procure the highest-quality switchgear, drive and automation equipment, integrated smoothly.</p>
    </div>"""

html = html.replace(old_header, new_header)

# Notice: I need to replace the footer precisely for the Products section.
# The products section ends right before <!-- ============ SERVICES ============ -->
# But wait, there might be 2 closing divs or 3. Let's do a regex replacement for the footer block.

import re

# Match the end of the products section
old_footer = """    </div>
  </section>
</div>

<!-- ============ SERVICES ============ -->"""

new_footer = """  </div>
</section>

<!-- ============ SERVICES ============ -->"""

html = html.replace(old_footer, new_footer)

with open('index.html', 'w') as f:
    f.write(html)

print("Products section unified.")
