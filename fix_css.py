with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Make sure background is perfectly white (#ffffff)
css = css.replace('--bg: #f8fafc;', '--bg: #ffffff;')

# Fix the fab text styles
css = css.replace('.fab-wa { background: #25D366; }', '.fab-wa { background: #25D366; width: auto; padding: 0 20px; border-radius: 28px; }')
css = css.replace('.fab-call { background: var(--accent); }', '.fab-call { background: var(--accent); width: auto; padding: 0 20px; border-radius: 28px; }')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("CSS updated.")
