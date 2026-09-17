with open('assets/css/style.css', 'r') as f:
    css = f.read()

# 1. Reduce logo height by ~15%
css = css.replace('.brand img { background: transparent; border-radius: 0; padding: 0; height: 50px; transition: height 0.3s ease; }', 
                  '.brand img { background: transparent; border-radius: 0; padding: 0; height: 42px; transition: height 0.3s ease; }')

# 2. Reduce shrink state logo height
css = css.replace('header.shrink .brand img {\n  height: 38px;\n}', 
                  'header.shrink .brand img {\n  height: 32px;\n}')

# 3. Reduce header padding slightly to make it less thick
css = css.replace('.headbar {\n  display: flex; align-items: center; justify-content: space-between;\n  padding: 16px 0;\n  transition: padding 0.3s ease;\n}', 
                  '.headbar {\n  display: flex; align-items: center; justify-content: space-between;\n  padding: 12px 0;\n  transition: padding 0.3s ease;\n}')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Header logo and padding reduced.")
