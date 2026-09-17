import re

with open('index.html', 'r') as f:
    html = f.read()

# CSS updates for the new brand-grid
with open('assets/css/style.css', 'r') as f:
    css = f.read()

grid_css = """
/* Brand Grid */
.brand-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px; margin-top: 24px; }
.brand-card { background: #ffffff; border: 1px solid var(--line-bright); border-radius: 12px; padding: 24px; box-shadow: 0 4px 16px rgba(0,0,0,0.03); transition: all 0.3s ease; }
.brand-card:hover { transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0,0,0,0.06); border-color: var(--accent); }
.brand-card h4 { font-size: 20px; color: var(--accent); margin-bottom: 16px; border-bottom: 2px solid var(--line); padding-bottom: 12px; }
.brand-card .cat-row { margin-bottom: 12px; line-height: 1.6; font-size: 15px; color: var(--text-dim); }
.brand-card .cat-row:last-child { margin-bottom: 0; }
"""

if '.brand-grid' not in css:
    css += '\n' + grid_css
    with open('assets/css/style.css', 'w') as f:
        f.write(css)

# Function to parse table and convert to grid
def table_to_grid(match):
    table_html = match.group(0)
    
    # Extract rows
    rows = re.findall(r'<tr>(.*?)</tr>', table_html, flags=re.DOTALL)
    
    grid_out = '<div class="brand-grid">\n'
    
    for row in rows:
        if '<th' in row: continue # Skip header
        
        # Extract brand and range
        cols = re.findall(r'<td.*?>(.*?)</td>', row, flags=re.DOTALL)
        if len(cols) == 2:
            brand = cols[0].strip()
            ranges = cols[1].strip()
            
            # ranges currently has <br><span...> tags. We want to wrap each line in <div class="cat-row">
            # First, strip the spans we added earlier
            ranges = re.sub(r'<span.*?</span>', '', ranges)
            lines = [l.strip() for l in ranges.split('<br>') if l.strip()]
            
            if not lines:
                # Fallback if no <br> was found
                lines = [ranges]
            
            grid_out += f'  <div class="brand-card">\n    <h4>{brand}</h4>\n'
            for line in lines:
                grid_out += f'    <div class="cat-row">{line}</div>\n'
            grid_out += '  </div>\n'
            
    grid_out += '</div>'
    return grid_out

# Apply to both tab-hw and tab-sw
html = re.sub(r'<table class="tech-table">.*?</table>', table_to_grid, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Tables converted to beautiful block grids.")
