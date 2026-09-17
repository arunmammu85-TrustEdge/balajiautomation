import re

with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Remove the rigid box styles from elements
targets = [
    r'\.card\s*\{[^}]*\}',
    r'\.why-item\s*\{[^}]*\}',
    r'\.p-item\s*\{[^}]*\}',
    r'\.value-item\s*\{[^}]*\}',
    r'\.contact-cell\s*\{[^}]*\}',
    r'\.service-row\s*\{[^}]*\}'
]

# We will just rewrite their CSS to be transparent and borderless
css = re.sub(r'\.card \{.*?\}', '.card { background: transparent; padding: 24px 16px; border: none; transition: all 0.3s ease; }', css)
css = css.replace('.card:hover { transform: translateY(-6px); border-color: var(--line-bright); box-shadow: 0 20px 40px rgba(0,0,0,0.08); }', '.card:hover { transform: translateY(-6px); }')

css = re.sub(r'\.why-item \{.*?\}', '.why-item { background: transparent; padding: 24px 16px; border: none; transition: all 0.3s ease; }', css)
css = css.replace('.why-item:hover { border-color: var(--line-bright); transform: translateY(-4px); box-shadow: 0 12px 24px rgba(0,0,0,0.05); }', '.why-item:hover { transform: translateY(-4px); }')

css = re.sub(r'\.p-item \{.*?\}', '.p-item { background: transparent; border: none; overflow: hidden; transition: all 0.3s ease; }', css)
css = css.replace('.p-item:hover { transform: translateY(-6px); border-color: var(--line-bright); box-shadow: 0 20px 30px rgba(0,0,0,0.1); }', '.p-item:hover { transform: translateY(-6px); }')
css = css.replace('.p-item .cap { padding: 16px 20px; font-size: 15px; color: var(--text); font-weight: 600; position: relative; z-index: 2; background: var(--bg-panel); }', '.p-item .cap { padding: 16px 0; font-size: 15px; color: var(--text); font-weight: 600; position: relative; z-index: 2; background: transparent; }')

css = re.sub(r'\.service-row \{.*?\}', '.service-row { display: grid; grid-template-columns: 280px 1fr; gap: 40px; padding: 32px 0; border: none; border-bottom: 1px solid var(--line); transition: all 0.3s ease; background: transparent; }', css)
css = css.replace('.service-row:hover { border-color: var(--line-bright); transform: translateY(-4px); box-shadow: 0 16px 32px rgba(0,0,0,0.08); }', '.service-row:hover { transform: translateX(8px); border-bottom-color: var(--line-bright); }')

css = re.sub(r'\.value-item \{.*?\}', '.value-item { background: transparent; padding: 24px 16px; border: none; transition: all 0.3s ease; }', css)
css = css.replace('.value-item:hover { transform: translateY(-4px); border-color: var(--line-bright); box-shadow: 0 12px 24px rgba(0,0,0,0.06); }', '.value-item:hover { transform: translateY(-4px); }')

css = re.sub(r'\.contact-cell \{.*?\}', '.contact-cell { background: transparent; padding: 24px 16px; border: none; transition: all 0.3s ease; }', css)
css = css.replace('.contact-cell:hover { border-color: var(--line-bright); box-shadow: 0 12px 24px rgba(0,0,0,0.05); transform: translateY(-2px); }', '.contact-cell:hover { transform: translateY(-2px); }')

with open('assets/css/style.css', 'w') as f:
    f.write(css)
    
print("CSS updated to remove boxes.")
