with open('assets/css/style.css', 'a') as f:
    f.write("\n/* Hero Ghost Button Override */\n")
    f.write(".hero .btn-ghost { color: #ffffff !important; border-color: rgba(255,255,255,0.4) !important; }\n")
    f.write(".hero .btn-ghost:hover { border-color: #ffffff !important; color: #ffffff !important; background: rgba(255,255,255,0.1) !important; }\n")

print("Ghost button fixed.")
