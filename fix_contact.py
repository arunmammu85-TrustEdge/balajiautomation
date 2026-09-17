import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace the split contact sections with a single section
# The current HTML has:
# <div id="contact">
#   <section class="hero fade-up" style="padding-top:56px;">
#     <div class="wrap"> ... </div>
#   </section>
#   <section class="tight fade-up">
#     <div class="wrap"> ... </div>
#   </section>
# </div>

# We will merge them.
new_contact = """
<section id="contact" class="fade-up" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 600px; margin: 0 auto 48px;">
      <div class="eyebrow" style="justify-content: center;">CONTACT US</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Let's talk about your project.</h2>
      <p class="lead" style="color:var(--text-dim); margin-top:16px;">Reach out for a quote, a site visit, or to discuss a control-systems project.</p>
    </div>
    
    <div class="contact-grid">
      <div class="contact-cell">
        <div class="lbl">Email</div>
        <div class="val"><a href="mailto:balajiautoin@gmail.com">balajiautoin@gmail.com</a></div>
      </div>
      <div class="contact-cell">
        <div class="lbl">Phone</div>
        <div class="val"><a href="tel:08028392666">080-2839 2666</a> &nbsp;·&nbsp; <a href="tel:+919008066215">+91 90080 66215</a></div>
      </div>
      <div class="contact-cell">
        <div class="lbl">Address</div>
        <div class="val" style="font-size:15px;">Balaji Automation<br>No. 5, 3rd Cross, Netajinagar, 100 Feet Road,<br>Near Peenya Jalahalli Cross, Bangalore 560057</div>
      </div>
      <div class="contact-cell">
        <div class="lbl">Follow</div>
        <div class="social-row">
          <a href="https://www.facebook.com/balajiautoin/" target="_blank" rel="noopener" aria-label="Facebook" style="display:flex; align-items:center; justify-content:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/2021_Facebook_icon.svg" alt="Facebook" style="width:28px; height:28px; border-radius:50%;"></a>
          <a href="https://www.instagram.com/balajiautoin/" target="_blank" rel="noopener" aria-label="Instagram" style="display:flex; align-items:center; justify-content:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram" style="width:28px; height:28px;"></a>
          <a href="https://twitter.com/balaji_autoin/" target="_blank" rel="noopener" aria-label="Twitter" style="display:flex; align-items:center; justify-content:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ce/X_logo_2023.svg" alt="X" style="width:28px; height:28px;"></a>
          <a href="https://www.linkedin.com/in/balajiautomation/" target="_blank" rel="noopener" aria-label="LinkedIn" style="display:flex; align-items:center; justify-content:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" alt="LinkedIn" style="width:28px; height:28px;"></a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

# Replace everything from <div id="contact"> to the end of its inner sections
html = re.sub(r'<div id="contact">.*?</section>\s*</div>', new_contact, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Contact section unified.")
