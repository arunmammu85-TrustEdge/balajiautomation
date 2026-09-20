import re

with open('index.html', 'r') as f:
    content = f.read()

# Extract technologies
tech_match = re.search(r'<section id="technologies".*?</section>\n', content, re.DOTALL)
if tech_match:
    tech_str = tech_match.group(0)
    content = content.replace(tech_str, '')
else:
    print("Could not find technologies")

# Extract value-services
value_match = re.search(r'<!-- ============ VALUE SERVICES ============ -->\n<section id="value-services".*?</section>\n', content, re.DOTALL)
if value_match:
    value_str = value_match.group(0)
    content = content.replace(value_str, '')
else:
    print("Could not find value-services")

# Insert before ABOUT
about_idx = content.find('<!-- ============ ABOUT ============ -->')
if about_idx != -1:
    # insert them right before ABOUT, with some newlines
    new_content = content[:about_idx] + tech_str + '\n' + value_str + '\n' + content[about_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find ABOUT")
