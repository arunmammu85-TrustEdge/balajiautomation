import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Add fade-up animations if not exist
fade_css = """
/* Scroll Animations */
.fade-up {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease-out, transform 0.8s ease-out;
}
.fade-up.visible {
  opacity: 1;
  transform: translateY(0);
}
"""
if '.fade-up' not in css:
    css += fade_css
    
with open('assets/css/style.css', 'w') as f:
    f.write(css)


with open('assets/js/main.js', 'r') as f:
    js = f.read()

# Fix Scroll Spy Selector
old_selector = "const sections = document.querySelectorAll('div[id=\"home\"], div[id=\"about\"], div[id=\"products\"], div[id=\"services\"], div[id=\"gallery\"], div[id=\"contact\"]');"
new_selector = "const sections = document.querySelectorAll('#home, #about, #products, #services, #gallery, #contact');"

js = js.replace(old_selector, new_selector)

with open('assets/js/main.js', 'w') as f:
    f.write(js)

print("Scroll spy and animations fixed.")
