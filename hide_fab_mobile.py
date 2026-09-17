with open('assets/css/style.css', 'a') as f:
    f.write("\n@media (max-width: 768px) {\n  .fab-top { display: none !important; }\n}\n")

print("Scroll to top button hidden on mobile.")
