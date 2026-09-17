with open('index.html', 'r') as f:
    html = f.read()

fabs_html = """
<div class="fab-container fab-left">
  <a href="https://wa.me/919008066215" class="fab fab-wa" target="_blank" rel="noopener" aria-label="WhatsApp">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
    <span style="font-size:14px; font-weight:600;">WhatsApp</span>
  </a>
</div>
<div class="fab-container">
  <button id="fab-top" class="fab fab-top" aria-label="Scroll to top" style="width:56px; padding:0;">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </button>
  <a href="tel:+919008066215" class="fab fab-call" aria-label="Call">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
    <span style="font-size:14px; font-weight:600;">Call Us</span>
  </a>
</div>
<script src="assets/js/main.js"></script>
"""

if 'fab-wa' not in html:
    html = html.replace('<script src="assets/js/main.js"></script>', fabs_html)

with open('index.html', 'w') as f:
    f.write(html)
print("FABs added.")
