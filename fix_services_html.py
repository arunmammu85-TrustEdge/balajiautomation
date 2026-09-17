with open('index.html', 'r') as f:
    html = f.read()

old_header = """<div id="services">
  <section class="hero" style="padding-top:56px;">
    <div class="wrap">
      <div class="eyebrow">OUR SERVICES</div>
      <h1 style="font-size:clamp(28px,4vw,44px);">Engineering services from design to implementation.</h1>
      <p class="lead">We work across Allen-Bradley, Siemens and Schneider platforms, and provide value services that our clients rely on most.</p>
    </div>
  </section>

  <section class="tight">
    <div class="wrap">"""

new_header = """<section id="services" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">OUR SERVICES</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Engineering services from design to implementation.</h2>
      <p class="lead" style="color:var(--text-dim); margin-top:16px;">We work across Allen-Bradley, Siemens and Schneider platforms, and provide value services that our clients rely on most.</p>
    </div>"""

# Replace the beginning of the services section
html = html.replace(old_header, new_header)

# Now we must find the closing of <div id="services"> and change it to </section>
# The end of the services section is where the gallery section begins.
# Let's just find the closing tags before <!-- ============ GALLERY ============ -->

old_footer = """    </div>
  </section>
</div>

<!-- ============ GALLERY ============ -->"""

new_footer = """  </div>
</section>

<!-- ============ GALLERY ============ -->"""

html = html.replace(old_footer, new_footer)

with open('index.html', 'w') as f:
    f.write(html)

print("Services section unified.")
