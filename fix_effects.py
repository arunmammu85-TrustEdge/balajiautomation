import re

# 1. Update style.css
with open('assets/css/style.css', 'r') as f:
    css = f.read()

effects_css = """
/* UI Effects */
#scroll-progress { position: fixed; top: 0; left: 0; height: 3px; background: var(--accent); z-index: 9999; width: 0%; transition: width 0.1s; }

header.shrink { background: rgba(255,255,255,0.98); box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
header.shrink .headbar { padding: 8px 0; }
header.shrink .brand img { height: 36px; }

.fade-up { opacity: 0; transform: translateY(30px); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }
.fade-up.visible { opacity: 1; transform: translateY(0); }

.hero-meta .num { transition: transform 0.3s ease, color 0.3s ease; display: inline-block; }
.hero-meta .num:hover { transform: scale(1.1) translateY(-4px); color: var(--accent); }
"""
if "#scroll-progress" not in css:
    css += "\n" + effects_css

with open('assets/css/style.css', 'w') as f:
    f.write(css)


# 2. Update main.js
with open('assets/js/main.js', 'r') as f:
    js = f.read()

effects_js = """
  // Header Shrink
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      if(header) header.classList.add('shrink');
    } else {
      if(header) header.classList.remove('shrink');
    }
  });

  // Dynamic Fade-Up Elements
  document.querySelectorAll('section, .card, .why-item, .p-item, .value-item, .contact-cell, .hero').forEach(el => {
    el.classList.add('fade-up');
  });

  const fadeObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target); // Only animate once
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -50px 0px' });
  
  document.querySelectorAll('.fade-up').forEach(el => fadeObserver.observe(el));
"""
if "Header Shrink" not in js:
    js = js.replace('// Set current year in footer', effects_js + '\n  // Set current year in footer')

with open('assets/js/main.js', 'w') as f:
    f.write(js)

print("Effects applied.")
