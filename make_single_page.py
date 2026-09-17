import re

# 1. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('<div class="page" id="page-home">', '<div id="home">')
html = html.replace('<div class="page" id="page-about">', '<div id="about">')
html = html.replace('<div class="page" id="page-products">', '<div id="products">')
html = html.replace('<div class="page" id="page-services">', '<div id="services">')
html = html.replace('<div class="page" id="page-gallery">', '<div id="gallery">')
html = html.replace('<div class="page" id="page-contact">', '<div id="contact">')

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Remove page active stuff
css = re.sub(r'/\* Page Sections \*/.*?@keyframes fadeUp \{.*?\}', '/* Page Sections */', css, flags=re.DOTALL)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

# 3. Update main.js
with open('assets/js/main.js', 'r') as f:
    js = f.read()

# Replace the navigation setup with scrollspy
new_js = """
  // Navigation & Scrollspy
  const sections = document.querySelectorAll('div[id="home"], div[id="about"], div[id="products"], div[id="services"], div[id="gallery"], div[id="contact"]');
  const navLinks = document.querySelectorAll('nav a');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (window.scrollY >= (sectionTop - 200)) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(a => {
      a.classList.remove('active');
      if (a.getAttribute('href') === '#' + current) {
        a.classList.add('active');
      }
    });
  });

  // Smooth scroll click
  navLinks.forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = a.getAttribute('href').replace('#', '');
      const target = document.getElementById(targetId);
      if(target) {
        window.scrollTo({
          top: target.offsetTop - 80, // offset for fixed header
          behavior: 'smooth'
        });
      }
      const navMenu = document.getElementById('navMenu');
      if(navMenu) navMenu.classList.remove('open');
    });
  });
"""

# Replace old navigation setup
js = re.sub(r'// Navigation Setup.*?window\.addEventListener\(\'hashchange\', navigate\);\s*navigate\(\);', new_js, js, flags=re.DOTALL)

with open('assets/js/main.js', 'w') as f:
    f.write(js)

print("Single page layout applied.")
