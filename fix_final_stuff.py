import re

# 1. Update style.css header background
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Make header white and blurry
css = css.replace('background: rgba(9, 9, 11, 0.7);', 'background: rgba(255, 255, 255, 0.85);')
css = css.replace('color: #fff;', 'color: var(--text);') # Ensure text isn't forced white on a white header, though usually it's inherited.
css = css.replace('.brand-text .name { font-family: \'Outfit\'; font-weight: 800; font-size: 18px; letter-spacing: 0.03em; background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }', '.brand-text .name { font-family: \'Outfit\'; font-weight: 800; font-size: 18px; letter-spacing: 0.03em; background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }') # Already good

# Header link text color fix
css = css.replace('nav a.active { color: #fff;', 'nav a.active { color: #fff;')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

# 2. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

# Fix numbers
html = html.replace('<div class="num">1990</div>', '<div class="num" data-target="1990">0</div>')
html = html.replace('<div class="num">18+</div>', '<div class="num" id="exp-counter" data-target="18" data-suffix="+">0</div>')
html = html.replace('<div class="num">5+</div>', '<div class="num" data-target="5" data-suffix="+">0</div>')
html = html.replace('<div class="num">8+</div>', '<div class="num" data-target="8" data-suffix="+">0</div>')

# Fix Social Icons Colors
# Facebook: #1877F2
html = html.replace('aria-label="Facebook" style="display:flex; align-items:center; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">', 'aria-label="Facebook" style="display:flex; align-items:center; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="#1877F2">')
# Instagram: Needs a defs linearGradient, but let's just make it a pink-orange gradient or a flat pink #E1306C for simplicity in the SVG string, but they want real colors. Let's add a defs block.
ig_color = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="url(#ig-grad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><defs><linearGradient id="ig-grad" x1="2" y1="2" x2="22" y2="22"><stop offset="0%" stop-color="#f09433"/><stop offset="25%" stop-color="#e6683c"/><stop offset="50%" stop-color="#dc2743"/><stop offset="75%" stop-color="#cc2366"/><stop offset="100%" stop-color="#bc1888"/></linearGradient></defs><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'
html = re.sub(r'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect.*?</svg>', ig_color, html)

# Twitter X: Black
html = html.replace('aria-label="Twitter" style="display:flex; align-items:center; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">', 'aria-label="Twitter" style="display:flex; align-items:center; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="#0f1419">')

# LinkedIn: #0A66C2
html = html.replace('aria-label="LinkedIn" style="display:flex; align-items:center; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">', 'aria-label="LinkedIn" style="display:flex; align-items:center; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="#0A66C2">')

with open('index.html', 'w') as f:
    f.write(html)

print("Applied final fixes.")
