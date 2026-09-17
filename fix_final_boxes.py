import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Make all boxes transparent and remove borders
targets = ['.card', '.why-item', '.value-item', '.contact-cell', '.p-item', '.split img', '.tech-table', '.tabs']
for t in targets:
    # Just aggressively strip any background from these in the CSS
    css = re.sub(t + r' \{([^}]*?)background:\s*[^;{}]+;([^}]*)\}', t + r' {\1background: transparent;\2}', css)
    css = re.sub(t + r' \{([^}]*?)border:\s*[^;{}]+;([^}]*)\}', t + r' {\1border: none;\2}', css)
    css = re.sub(t + r' \{([^}]*?)box-shadow:\s*[^;{}]+;([^}]*)\}', t + r' {\1box-shadow: none;\2}', css)

# Make contact section smaller explicitly
css = re.sub(r'\.contact-grid \{.*?\}', '.contact-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; max-width: 800px; margin: 0 auto; }', css, flags=re.DOTALL)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Box backgrounds removed and contact section condensed.")
