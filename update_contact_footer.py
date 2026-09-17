with open('index.html', 'r') as f:
    html = f.read()

# 1. Make contact section smaller
html = html.replace('<section id="contact" class="fade-up" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 80px 0;">', '<section id="contact" class="fade-up" style="background:#ffffff; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding: 40px 0;">')

# 2. Reduce font size of "Let's talk about your project."
html = html.replace('<h2 style="font-size:clamp(32px,4vw,44px);">Let\'s talk about your project.</h2>', '<h2 style="font-size:clamp(22px,3vw,30px);">Let\'s talk about your project.</h2>')

with open('index.html', 'w') as f:
    f.write(html)

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# 3. Apply the same frosty gradient to the footer
old_footer_css = """footer { border-top: 1px solid var(--line); padding: 16px 0; background: #fff; }"""
new_footer_css = """footer { border-top: 1px solid var(--line); padding: 16px 0; background: linear-gradient(90deg, rgba(255,255,255,0.95), rgba(240,249,255,0.95)); }"""

css = css.replace(old_footer_css, new_footer_css)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Contact section and footer updated.")
