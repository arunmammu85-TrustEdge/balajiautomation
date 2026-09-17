with open('index.html', 'r') as f:
    html = f.read()

old_header = """  <section>
    <div class="wrap">
      <div class="sec-head">
        <div class="eyebrow">WHO WE ARE</div>
        <h2>Mission-critical control systems, delivered with engineering discipline.</h2>
        <p>Our engineering and project management approach positions us to deliver mission-critical automation projects at competitive prices and world-class quality. We continually strive to be a value-added partner whose work meaningfully improves our clients' operations.</p>
      </div>"""

new_header = """  <section id="who-we-are" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
    <div class="wrap">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
        <div class="eyebrow" style="justify-content: center;">WHO WE ARE</div>
        <h2 style="font-size:clamp(32px,4vw,44px);">Mission-critical control systems, delivered with engineering discipline.</h2>
        <p class="lead" style="color:var(--text-dim); margin-top:16px;">Our engineering and project management approach positions us to deliver mission-critical automation projects at competitive prices and world-class quality. We continually strive to be a value-added partner whose work meaningfully improves our clients' operations.</p>
      </div>"""

html = html.replace(old_header, new_header)

with open('index.html', 'w') as f:
    f.write(html)

print("WHO WE ARE aligned and boxed.")
