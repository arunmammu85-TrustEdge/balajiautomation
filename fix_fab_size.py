with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Scale down FABs by ~30%
css = css.replace('.fab {\n  width: 56px; height: 56px;', '.fab {\n  width: 40px; height: 40px;')
css = css.replace('.fab-wa { background: #25D366; width: 56px; height: 56px;', '.fab-wa { background: #25D366; width: 40px; height: 40px;')
css = css.replace('.fab-call { background: var(--accent); width: 56px; height: 56px;', '.fab-call { background: var(--accent); width: 40px; height: 40px;')

# Let's also ensure the SVG scales down inside the fab
css += '\n.fab svg { width: 20px; height: 20px; }'

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("FABs reduced.")
