import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace fonts
old_fonts = r'<link href="https://fonts.googleapis.com/css2.*?rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@600;700;800&display=swap" rel="stylesheet">'
html = re.sub(old_fonts, new_fonts, html, flags=re.DOTALL)

# Replace inline <style> block with external link
html = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="assets/css/style.css">', html, flags=re.DOTALL)

# Add loader and progress bar after <body>
loader_html = """
<div id="page-loader"><div class="spinner"></div></div>
<div id="scroll-progress"></div>
"""
html = re.sub(r'(<body[^>]*>)', r'\1' + loader_html, html)

# Modify counters
html = html.replace('<div class="num">1990</div>', '<div class="num" data-target="1990">0</div>')
html = html.replace('<div class="num">18+</div>', '<div class="num" data-target="18" data-suffix="+">0</div>')
html = html.replace('<div class="num">5+</div>', '<div class="num" data-target="5" data-suffix="+">0</div>')
html = html.replace('<div class="num">8+</div>', '<div class="num" data-target="8" data-suffix="+">0</div>')

# Add FABs before </body>
fabs_html = """
<div class="fab-container fab-left">
  <a href="https://wa.me/919008066215" class="fab fab-wa" target="_blank" rel="noopener" aria-label="WhatsApp">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
  </a>
</div>
<div class="fab-container">
  <button id="fab-top" class="fab fab-top" aria-label="Scroll to top">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </button>
  <a href="tel:+919008066215" class="fab fab-call" aria-label="Call">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
  </a>
</div>
<script src="assets/js/main.js"></script>
"""
html = re.sub(r'<script>.*?</script>', fabs_html, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("index.html refactored successfully.")
