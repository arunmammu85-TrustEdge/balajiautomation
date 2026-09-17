with open('index.html', 'r') as f:
    html = f.read()

# Fix CSS
start_style = html.find('<style>')
end_style = html.find('</style>')
if start_style != -1 and end_style != -1:
    html = html[:start_style] + '<link rel="stylesheet" href="assets/css/style.css">' + html[end_style + 8:]
    print("CSS linked.")
else:
    print("Style tag not found.")

# Fix JS
start_script = html.find('<script>')
end_script = html.rfind('</script>')
if start_script != -1 and end_script != -1 and "assets/js/main.js" not in html[start_script:end_script]:
    html = html[:start_script] + '<script src="assets/js/main.js"></script>' + html[end_script + 9:]
    print("JS linked.")
else:
    print("Script tag not found or already linked.")

# Ensure loader and FABs are there
if 'id="page-loader"' not in html:
    html = html.replace('<body class="grid-bg">', '<body class="grid-bg">\n<div id="page-loader"><div class="spinner"></div></div>\n<div id="scroll-progress"></div>')
    print("Added loader.")

with open('index.html', 'w') as f:
    f.write(html)
