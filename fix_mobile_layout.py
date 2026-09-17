import re

# 1. Update index.html for hamburger menu
with open('index.html', 'r') as f:
    html = f.read()

old_menu = '<button class="nav-toggle" id="navToggle">MENU</button>'
new_menu = '<button class="nav-toggle" id="navToggle" aria-label="Menu"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg></button>'
html = html.replace(old_menu, new_menu)

# Ensure no other instances are missed
if old_menu not in html and new_menu not in html:
    print("WARNING: Could not find nav-toggle in HTML.")

with open('index.html', 'w') as f:
    f.write(html)


# 2. Update style.css for responsive fixes
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Fix Services mobile grid
old_service_mq = "@media (max-width: 768px) { .service-row { display: grid; grid-template-columns: 280px 1fr; gap: 40px; padding: 32px 0; border: none; border-bottom: 1px solid var(--line); transition: all 0.3s ease; background: transparent; } }"
new_service_mq = "@media (max-width: 768px) { .service-row { display: grid; grid-template-columns: 1fr; gap: 24px; padding: 32px 0; border: none; border-bottom: 1px solid var(--line); transition: all 0.3s ease; background: transparent; } }"
css = css.replace(old_service_mq, new_service_mq)

# Fix Contact mobile grid
old_contact_mq = "@media (max-width: 768px) { .contact-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; max-width: 800px; margin: 0 auto; } }"
new_contact_mq = "@media (max-width: 768px) { .contact-grid { display: grid; grid-template-columns: 1fr; gap: 24px; max-width: 800px; margin: 0 auto; } }"
css = css.replace(old_contact_mq, new_contact_mq)

# Add a safety overflow-x hidden to the body just in case
if "overflow-x: hidden;" not in css:
    css = css.replace("body {", "body {\n  overflow-x: hidden;")

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Mobile layout fixes applied.")
