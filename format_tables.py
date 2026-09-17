import re

# 1. Update CSS to make the table gorgeous
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Replace existing tech-table CSS
css = re.sub(r'\.tech-table \{.*?\}', '.tech-table { width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 24px; border: 1px solid var(--line-bright); border-radius: 12px; overflow: hidden; background: #ffffff; box-shadow: 0 10px 30px rgba(0,0,0,0.04); }', css, flags=re.DOTALL)
css = re.sub(r'\.tech-table th \{.*?\}', '.tech-table th { text-align: left; font-size: 15px; color: #ffffff; background: linear-gradient(90deg, var(--accent), #0369a1); text-transform: uppercase; letter-spacing: 0.05em; padding: 20px 24px; border-bottom: 2px solid #075985; font-weight: 800; }', css, flags=re.DOTALL)
css = re.sub(r'\.tech-table td \{.*?\}', '.tech-table td { padding: 20px 24px; border-bottom: 1px solid var(--line-bright); font-size: 15px; color: var(--text); vertical-align: top; background: transparent; transition: background 0.2s; line-height: 1.8; }', css, flags=re.DOTALL)
css = re.sub(r'\.tech-table tr:hover td \{.*?\}', '.tech-table tr:hover td { background: #f8fafc; }', css, flags=re.DOTALL)

with open('assets/css/style.css', 'w') as f:
    f.write(css)


# 2. Update HTML to colorize the categories (PLCs, HMIs, VFDs, Servo, SCADA)
with open('index.html', 'r') as f:
    html = f.read()

# Function to wrap categories in colored badges
def colorize(match):
    text = match.group(0)
    # Define colors for different prefixes
    color_map = {
        'PLCs:': '#ea580c',
        'PLC:': '#ea580c',
        'HMIs:': '#0284c7',
        'HMI:': '#0284c7',
        'HMI, GOT &amp; GS': '#0284c7',
        'VFDs:': '#16a34a',
        'Servo:': '#9333ea',
        'SCADA/HMI:': '#0284c7'
    }
    col = color_map.get(text, 'var(--accent)')
    return f'<strong style="color:{col}; font-weight:800;">{text}</strong>'

# Apply regex to table cells only (roughly bounded by <div class="tab-panel">)
def process_table(html_chunk):
    # Match prefixes like 'PLCs:', 'HMIs:', 'VFDs:', 'Servo:', 'PLC:', 'HMI:', 'SCADA/HMI:'
    pattern = r'\b(PLCs:|PLC:|HMIs:|HMI:|VFDs:|Servo:|SCADA/HMI:|HMI, GOT &amp; GS)\b'
    return re.sub(pattern, colorize, html_chunk)

# Find the entire tabs section to replace inside
match = re.search(r'<div class="tabs">.*?<!-- ============ SERVICES ============ -->', html, flags=re.DOTALL)
if match:
    tabs_html = match.group(0)
    new_tabs = process_table(tabs_html)
    
    # Also center align the TECHNOLOGIES sec-head since we're fixing alignment issues
    new_tabs = new_tabs.replace('<div class="sec-head" style="margin-bottom:0;">', '<div class="sec-head" style="margin-bottom:24px; text-align:center; max-width:700px; margin: 0 auto;">')
    new_tabs = new_tabs.replace('<div class="eyebrow">TECHNOLOGIES</div>', '<div class="eyebrow" style="justify-content:center;">TECHNOLOGIES</div>')
    new_tabs = new_tabs.replace('<h2>Platforms we integrate with.</h2>', '<h2 style="font-size:clamp(32px,4vw,44px);">Platforms we integrate with.</h2>')

    html = html[:match.start()] + new_tabs + html[match.end():]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Tables formatted.")
else:
    print("Could not find tabs section.")
