import re

# 1. Update CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Change vertical-align: top to vertical-align: middle
css = css.replace('vertical-align: top;', 'vertical-align: middle;')
# Ensure the first column has a specific width so it doesn't get squeezed
if 'tech-table td:first-child' not in css:
    css += '\n.tech-table th:first-child, .tech-table td:first-child { width: 200px; font-weight: 700; }\n'

with open('assets/css/style.css', 'w') as f:
    f.write(css)


# 2. Update HTML to replace dots with line breaks in the tables
with open('index.html', 'r') as f:
    html = f.read()

# Find the tables
match = re.search(r'<div class="tabs">.*?</section>', html, flags=re.DOTALL)
if match:
    table_block = match.group(0)
    
    # The categories are separated by ' · '
    # We will replace ' · ' with '<br>' only inside the tables
    table_block = table_block.replace(' · ', '<br><span style="display:inline-block; height:8px;"></span>')
    
    html = html[:match.start()] + table_block + html[match.end():]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Table alignment fixed and lines broken neatly.")
else:
    print("Table not found.")
