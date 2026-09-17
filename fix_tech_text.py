with open('assets/css/style.css', 'a') as f:
    f.write("\n/* Technologies Header and Tabs Visibility Fix */\n")
    f.write("#technologies > .wrap > div:first-child {\n")
    f.write("  background: rgba(255, 255, 255, 0.9);\n")
    f.write("  backdrop-filter: blur(12px);\n")
    f.write("  -webkit-backdrop-filter: blur(12px);\n")
    f.write("  padding: 32px;\n")
    f.write("  border-radius: 16px;\n")
    f.write("  box-shadow: 0 10px 40px rgba(0,0,0,0.08);\n")
    f.write("  border: 1px solid rgba(255,255,255,0.8);\n")
    f.write("}\n")
    f.write("#technologies > .wrap > div:first-child h2 {\n")
    f.write("  color: #0f172a !important;\n")
    f.write("}\n")
    f.write("#technologies > .wrap > div:first-child p.lead {\n")
    f.write("  color: #334155 !important;\n")
    f.write("  font-weight: 500;\n")
    f.write("}\n")
    
    # Tabs visibility fix
    f.write("#technologies .tabs {\n")
    f.write("  background: rgba(255, 255, 255, 0.9);\n")
    f.write("  backdrop-filter: blur(12px);\n")
    f.write("  padding: 12px 24px;\n")
    f.write("  border-radius: 100px;\n")
    f.write("  display: inline-flex;\n")
    f.write("  box-shadow: 0 10px 40px rgba(0,0,0,0.08);\n")
    f.write("  border: 1px solid rgba(255,255,255,0.8);\n")
    f.write("  margin: 0 auto 32px auto;\n")
    f.write("}\n")
    
    # We must center the tabs container, because it is display: inline-flex
    # The parent (.wrap) is not text-align: center by default, we'll wrap tabs or just flex the parent.
    f.write("#technologies .tabs-container {\n")
    f.write("  text-align: center;\n")
    f.write("}\n")

print("Tech text fixed.")
