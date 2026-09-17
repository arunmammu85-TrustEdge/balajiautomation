with open('index.html', 'r') as f:
    html = f.read()

old_header = """<div id="gallery">
  <section class="hero" style="padding-top:56px;">
    <div class="wrap">
      <div class="eyebrow">GALLERY</div>
      <h1 style="font-size:clamp(28px,4vw,44px);">Products we manufacture.</h1>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">"""

new_header = """<section id="gallery" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">GALLERY</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Products we manufacture.</h2>
    </div>"""

html = html.replace(old_header, new_header)

old_footer = """      </div>
    </div>
  </section>
</div>

<!-- ============ CONTACT ============ -->"""

new_footer = """      </div>
  </div>
</section>

<!-- ============ CONTACT ============ -->"""

html = html.replace(old_footer, new_footer)

with open('index.html', 'w') as f:
    f.write(html)
print("Gallery unified for real.")
