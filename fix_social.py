import re

with open('index.html', 'r') as f:
    html = f.read()

fb_svg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>'
ig_svg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>'
x_svg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"></path></svg>'
in_svg = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M22.23 0H1.77C.8 0 0 .77 0 1.72v20.56C0 23.23.8 24 1.77 24h20.46c.98 0 1.77-.77 1.77-1.72V1.72C24 .77 23.2 0 22.23 0zM7.12 20.45H3.56V9h3.56v11.45zM5.34 7.43c-1.14 0-2.06-.92-2.06-2.06 0-1.14.92-2.06 2.06-2.06s2.06.92 2.06 2.06c0 1.14-.92 2.06-2.06 2.06zM20.45 20.45h-3.56v-5.56c0-1.33-.03-3.03-1.85-3.03-1.85 0-2.13 1.45-2.13 2.94v5.65H9.36V9h3.41v1.56h.05c.48-.9 1.63-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29z"></path></svg>'

html = html.replace('<a href="https://www.facebook.com/balajiautoin/" target="_blank" rel="noopener" aria-label="Facebook">f</a>', f'<a href="https://www.facebook.com/balajiautoin/" target="_blank" rel="noopener" aria-label="Facebook" style="display:flex; align-items:center; justify-content:center;">{fb_svg}</a>')
html = html.replace('<a href="https://www.instagram.com/balajiautoin/" target="_blank" rel="noopener" aria-label="Instagram">ig</a>', f'<a href="https://www.instagram.com/balajiautoin/" target="_blank" rel="noopener" aria-label="Instagram" style="display:flex; align-items:center; justify-content:center;">{ig_svg}</a>')
html = html.replace('<a href="https://twitter.com/balaji_autoin/" target="_blank" rel="noopener" aria-label="Twitter">x</a>', f'<a href="https://twitter.com/balaji_autoin/" target="_blank" rel="noopener" aria-label="Twitter" style="display:flex; align-items:center; justify-content:center;">{x_svg}</a>')
html = html.replace('<a href="https://www.linkedin.com/in/balajiautomation/" target="_blank" rel="noopener" aria-label="LinkedIn">in</a>', f'<a href="https://www.linkedin.com/in/balajiautomation/" target="_blank" rel="noopener" aria-label="LinkedIn" style="display:flex; align-items:center; justify-content:center;">{in_svg}</a>')

with open('index.html', 'w') as f:
    f.write(html)

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Make contact section smaller
css = css.replace('.contact-cell { background: transparent; padding: 24px 16px; border: none; transition: all 0.3s ease; }', '.contact-cell { background: transparent; padding: 8px 16px; border: none; transition: all 0.3s ease; }')
# Reduce gap in contact grid if it has gap
css = css.replace('.contact-grid { display: grid; gap: 24px;', '.contact-grid { display: grid; gap: 16px;')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Icons added and section made smaller.")
