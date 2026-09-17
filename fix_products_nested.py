import re
with open('index.html', 'r') as f:
    html = f.read()

# Remove the nested <section><div class="wrap"> around "Products range"
html = html.replace('  <section>\n    <div class="wrap">\n      <div class="sec-head" style="margin-bottom:24px;">\n        <h2>Products range</h2>\n      </div>',
                    '      <div class="sec-head" style="margin-bottom:24px; text-align:center;">\n        <h3 style="font-size:24px; color:var(--accent);">Products range</h3>\n      </div>')

# Remove the end of Products range and start of Other products
html = html.replace('    </div>\n  </section>\n\n  <section class="tight">\n    <div class="wrap">\n      <div class="sec-head" style="margin-bottom:20px;">\n        <h2>Other products</h2>\n      </div>',
                    '      <div class="sec-head" style="margin-top:64px; margin-bottom:24px; text-align:center;">\n        <h3 style="font-size:24px; color:var(--accent);">Other products</h3>\n      </div>')

# Remove the end of Other products and start of Technologies
html = html.replace('    </div>\n  </section>\n\n  <section class="tight">\n    <div class="wrap">\n      <div class="sec-head"',
                    '      <div class="sec-head"')

with open('index.html', 'w') as f:
    f.write(html)
print("Nested sections removed.")
