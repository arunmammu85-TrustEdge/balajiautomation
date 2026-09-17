import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Make sure headbar and brand img have transitions for smooth shrinking
css = css.replace('.headbar {\n  display: flex; align-items: center; justify-content: space-between;\n  padding: 16px 0;\n}', 
                  '.headbar {\n  display: flex; align-items: center; justify-content: space-between;\n  padding: 16px 0;\n  transition: padding 0.3s ease;\n}')
css = css.replace('.brand img { background: transparent; border-radius: 0; padding: 0; }',
                  '.brand img { background: transparent; border-radius: 0; padding: 0; height: 50px; transition: height 0.3s ease; }')
css = css.replace('.brand img { height: 50px; width: auto; }', 
                  '.brand img { height: 50px; width: auto; transition: height 0.3s ease; }')

# Add the shrink classes
shrink_css = """
/* Header Shrink on Scroll */
header.shrink {
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}
header.shrink .headbar {
  padding: 6px 0;
}
header.shrink .brand img {
  height: 38px;
}
"""

if 'header.shrink' not in css:
    css += shrink_css

with open('assets/css/style.css', 'w') as f:
    f.write(css)


with open('assets/js/main.js', 'r') as f:
    js = f.read()

shrink_js = """
// Header Shrink on Scroll
const header = document.querySelector('header');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    header.classList.add('shrink');
  } else {
    header.classList.remove('shrink');
  }
});
"""

if 'header.classList.add(\'shrink\')' not in js:
    js += shrink_js

with open('assets/js/main.js', 'w') as f:
    f.write(js)

print("Header shrink on scroll added.")
