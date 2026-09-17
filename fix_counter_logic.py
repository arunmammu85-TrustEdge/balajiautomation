import re

# 1. Update JS easing to linear so small numbers look like they are running
with open('assets/js/main.js', 'r') as f:
    js = f.read()

# Replace the easing logic
old_logic = """      // easeOutExpo
      const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);

      const current = Math.floor(easeProgress * target);"""

new_logic = """      // Linear ease so small numbers tick evenly
      const current = Math.floor(progress * target);"""

js = js.replace(old_logic, new_logic)

with open('assets/js/main.js', 'w') as f:
    f.write(js)


# 2. Add the hover effect back to CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

if '.hero-meta .num:hover' not in css:
    css = css.replace('.hero-meta .num { font-family: \'Montserrat\'; font-size: 42px; color: var(--accent-secondary); font-weight: 800; line-height: 1; }',
                      '.hero-meta .num { font-family: \'Montserrat\'; font-size: 42px; color: var(--accent-secondary); font-weight: 800; line-height: 1; transition: transform 0.3s ease, color 0.3s ease; display: inline-block; cursor: default; }\n.hero-meta .num:hover { transform: scale(1.15) translateY(-4px); color: var(--accent); }')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Counter logic and hover fixed.")
