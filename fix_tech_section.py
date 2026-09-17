with open('index.html', 'r') as f:
    html = f.read()

old_block = """      </div>
      <div class="sec-head" style="margin-bottom:0;">
        <div class="eyebrow">TECHNOLOGIES</div>
        <h2>Platforms we integrate with.</h2>
        <p>We specialize in integrating control systems with instruments, sensors and transmitters (temperature, pressure, flow, level), analyzers, PID controllers, energy monitoring, wireless systems, RFIDs, and network &amp; communication devices.</p>
      </div>"""

# Notice the first </div> closes the product-grid.
# Then we close wrap and section for #products.
# Then we start a new section #technologies with a slightly different background (#f8fafc) to make it a distinct block.

new_block = """      </div>
  </div>
</section>

<section id="technologies" class="fade-up" style="background:#f8fafc; border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 48px;">
      <div class="eyebrow" style="justify-content: center;">TECHNOLOGIES</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Platforms we integrate with.</h2>
      <p class="lead" style="color:var(--text-dim); margin-top:16px;">We specialize in integrating control systems with instruments, sensors and transmitters (temperature, pressure, flow, level), analyzers, PID controllers, energy monitoring, wireless systems, RFIDs, and network &amp; communication devices.</p>
    </div>"""

html = html.replace(old_block, new_block)

with open('index.html', 'w') as f:
    f.write(html)

print("Technologies split into new section.")
