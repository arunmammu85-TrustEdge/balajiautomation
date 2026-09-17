with open('assets/css/style.css', 'r') as f:
    css = f.read()

old_block = """#technologies .wrap {
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 48px;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.1);
  border: 1px solid rgba(255,255,255,0.8);
}"""

# In case there are subtle whitespace differences, we can just replace it with empty string
css = css.replace(old_block, "")

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Removed wrapper background.")
