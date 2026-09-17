with open('assets/css/style.css', 'r') as f:
    css = f.read()

old_card = """.card {
  background: transparent; border: none; padding: 32px;
  border-radius: var(--radius); transition: all 0.3s ease;
  box-shadow: none;
}
.card:hover { transform: translateY(-6px); }"""

new_card = """.card {
  background: #ffffff; 
  border: 1px solid var(--line-bright);
  border-top: 4px solid var(--accent);
  padding: 32px;
  border-radius: 12px; 
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
}
.card:hover { 
  transform: translateY(-6px); 
  box-shadow: 0 12px 30px rgba(0,0,0,0.08); 
  border-color: var(--accent); 
}"""

css = css.replace(old_card, new_card)

with open('assets/css/style.css', 'w') as f:
    f.write(css)

print("Cards styled.")
