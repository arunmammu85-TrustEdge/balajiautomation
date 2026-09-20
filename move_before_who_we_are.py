import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Extract clients section
clients_match = re.search(r'<!-- ============ CLIENTS ============ -->\n\s*<section id="clients".*?</section>\n', content, re.DOTALL)
if clients_match:
    clients_str = clients_match.group(0)
    content = content.replace(clients_str, '')
else:
    print("Could not find clients")

# 2. Extract technologies section
tech_match = re.search(r'<section id="technologies".*?</section>\n', content, re.DOTALL)
if tech_match:
    tech_str = tech_match.group(0)
    content = content.replace(tech_str, '')
else:
    print("Could not find technologies")

# 3. Find who-we-are section
who_we_are_idx = content.find('<section id="who-we-are"')
if who_we_are_idx != -1:
    # insert them right before WHO WE ARE
    new_content = content[:who_we_are_idx] + clients_str + '\n' + tech_str + '\n' + content[who_we_are_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find who-we-are")
