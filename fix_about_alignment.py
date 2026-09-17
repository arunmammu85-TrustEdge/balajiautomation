import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the beginning of the about section
old_about = """<div id="about">
  <section class="hero" style="padding-top:56px;">
    <div class="wrap">
      <div class="eyebrow">ABOUT US</div>
      <h1 style="font-size:clamp(28px,4vw,44px);">Providing expert &amp; honest service for over 18 years.</h1>
    </div>
  </section>

  <section>
    <div class="wrap split">
      <div>
        <h2 style="color:#fff;font-size:22px;">Our history</h2>"""

new_about = """<section id="about" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">ABOUT US</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Providing expert &amp; honest service since 1990.</h2>
    </div>

    <div class="split" style="margin-bottom: 80px;">
      <div>
        <h3 style="font-size:22px; color:var(--accent);">Our history</h3>"""

html = html.replace(old_about, new_about)

# Now fix the left-aligned WHY CHOOSE US sec-head
old_why = """  <section class="tight">
    <div class="wrap">
      <div class="sec-head" style="margin-bottom:0;">
        <div class="eyebrow">WHY CHOOSE US</div>
        <h2>Value services clients consistently rely on.</h2>
      </div>
      <div class="why-grid">"""

new_why = """    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">WHY CHOOSE US</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Value services clients consistently rely on.</h2>
    </div>
    <div class="why-grid">"""

html = html.replace(old_why, new_why)

# And fix the closing of the About section
old_end = """      </div>
    </div>
  </section>
</div>

<!-- ============ PRODUCTS ============ -->"""

new_end = """    </div>
  </div>
</section>

<!-- ============ PRODUCTS ============ -->"""

html = html.replace(old_end, new_end)

with open('index.html', 'w') as f:
    f.write(html)
print("About section unified and centered.")
