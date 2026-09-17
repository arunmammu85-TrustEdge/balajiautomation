import os
import shutil
from PIL import Image

# 1. Convert to webp
src = '/home/arun/.gemini/antigravity/brain/42acad4c-0b31-458f-aff2-c5a7c24c8d86/balaji_bright_about_bg_1789664406539.png'
dest = 'assets/images/about_bg.webp'

if os.path.exists(src):
    try:
        im = Image.open(src).convert("RGB")
        im.save(dest, 'webp', quality=85)
    except Exception as e:
        print(f"Error converting: {e}")

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

old_about = """<section id="about" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">
  <div class="wrap">
    <div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">
      <div class="eyebrow" style="justify-content: center;">ABOUT US</div>
      <h2 style="font-size:clamp(32px,4vw,44px);">Providing expert &amp; honest service since 1990.</h2>
    </div>

    <div class="split">
      <div>
        <h3 style="font-size:22px; color:var(--accent);">Our history</h3>
        <p>Balaji Automation is a world-class expert in delivering industrial automation and control systems. Our engineering and project-management approach positions us to deliver mission-critical projects at competitive prices and world-class quality.</p>
        <p>This commitment to excellence extends across every stage of a project. Our domain knowledge across various industries, combined with our controls and engineering expertise, makes us the obvious choice for our customers.</p>
        <p>We continually strive to be a value-added company whose services significantly improve our clients' business.</p>
      </div>
      <img src="assets/images/img_37_SCADA.2.webp" alt="SCADA control system screen">
    </div>
  </div>
</section>"""

new_about = """<section id="about" class="fade-up">
  <div class="wrap">
    <div class="about-card">
      <div class="eyebrow">ABOUT US</div>
      <h2>Providing expert &amp; honest service since 1990.</h2>
      <h3>Our history</h3>
      <p>Balaji Automation is a world-class expert in delivering industrial automation and control systems. Our engineering and project-management approach positions us to deliver mission-critical projects at competitive prices and world-class quality.</p>
      <p>This commitment to excellence extends across every stage of a project. Our domain knowledge across various industries, combined with our controls and engineering expertise, makes us the obvious choice for our customers.</p>
      <p>We continually strive to be a value-added company whose services significantly improve our clients' business.</p>
    </div>
  </div>
</section>"""

html = html.replace(old_about, new_about)

with open('index.html', 'w') as f:
    f.write(html)

# 3. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

new_css = """
/* About Us Floating Card */
#about {
  padding: 120px 0;
  background: url('../images/about_bg.webp') center/cover fixed no-repeat;
  position: relative;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
.about-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 56px;
  border-radius: 16px;
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 0 20px 60px rgba(0,0,0,0.1);
  border: 1px solid rgba(255,255,255,1);
  text-align: center;
}
.about-card .eyebrow { justify-content: center; margin-bottom: 16px; }
.about-card h2 { font-size: clamp(28px, 4vw, 36px); margin-bottom: 40px; color: var(--text); line-height: 1.3; }
.about-card h3 { font-size: 20px; color: var(--accent); margin-bottom: 16px; font-weight: 600; text-align: left; }
.about-card p { font-size: 16px; color: var(--text-dim); line-height: 1.8; margin-bottom: 20px; text-align: left; }
.about-card p:last-child { margin-bottom: 0; }
@media (max-width: 768px) {
  .about-card { padding: 32px 24px; }
}
"""

with open('assets/css/style.css', 'a') as f:
    f.write(new_css)

print("About section updated with floating text card.")
