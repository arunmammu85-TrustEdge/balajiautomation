with open('index.html', 'r') as f:
    html = f.read()

old_html = """      </div>
      <div class="sec-head" style="margin-bottom:0;">
        <div class="eyebrow">DOMAIN KNOWLEDGE</div>
        <h2>Industries we serve.</h2>
        <p>Proven experience delivering mission-critical projects across five core sectors — currently operating mainstream production in plants that affect safety, quality and millions in revenue.</p>
      </div>"""

new_html = """      </div>
  </div>
</section>

<!-- ============ DOMAIN KNOWLEDGE ============ -->
<section id="domain-knowledge" style="background:#ffffff; padding: 80px 0; border-bottom:1px solid var(--line);">
  <div class="wrap">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 48px;">
      <div class="eyebrow" style="justify-content: center;">DOMAIN KNOWLEDGE</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Industries we serve.</h2>
      <p class="lead" style="color:var(--text-dim); margin-top:16px;">Proven experience delivering mission-critical projects across five core sectors — currently operating mainstream production in plants that affect safety, quality and millions in revenue.</p>
    </div>"""

html = html.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(html)

print("Domain knowledge separated and centered.")
