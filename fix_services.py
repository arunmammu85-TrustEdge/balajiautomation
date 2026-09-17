import re

with open('index.html', 'r') as f:
    html = f.read()

# Extract the inner HTML of the second section (the services list)
match = re.search(r'<div id="services">\s*<section class="hero fade-up".*?>.*?<div class="wrap">\s*(.*?)\s*</div>\s*</section>\s*<section.*?>\s*<div class="wrap">\s*(.*?)\s*</div>\s*</section>\s*</div>', html, flags=re.DOTALL)

if match:
    hero_content = match.group(1)
    services_content = match.group(2)
    
    # We want to format the hero_content a bit tighter
    hero_content = hero_content.replace('<div class="eyebrow">OUR SERVICES</div>', '<div class="eyebrow" style="justify-content: center;">OUR SERVICES</div>')
    hero_content = hero_content.replace('<h1 style="font-size:clamp(28px,4vw,44px);">Engineering services from design to implementation.</h1>', '<h2 style="font-size:clamp(32px,4vw,44px);">Engineering services from design to implementation.</h2>')
    hero_content = hero_content.replace('<p class="lead">We work across Allen-Bradley', '<p class="lead" style="color:var(--text-dim); margin-top:16px;">We work across Allen-Bradley')
    
    hero_content = f'<div style="text-align: center; max-width: 700px; margin: 0 auto 64px;">\n{hero_content}\n</div>'

    new_services = f'<section id="services" class="fade-up" style="padding: 80px 0;">\n  <div class="wrap">\n    {hero_content}\n    {services_content}\n  </div>\n</section>'
    
    html = html[:match.start()] + new_services + html[match.end():]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Services section unified.")
else:
    print("Could not find the services section.")
