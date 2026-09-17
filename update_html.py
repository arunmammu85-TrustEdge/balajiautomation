import re

with open('index.html', 'r') as f:
    content = f.read()

new_head_content = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #09090b;
    --bg-panel: rgba(24, 24, 27, 0.6);
    --bg-panel-hover: rgba(39, 39, 42, 0.8);
    --line: rgba(255, 255, 255, 0.1);
    --line-bright: rgba(255, 255, 255, 0.2);
    --text: #f4f4f5;
    --text-dim: #a1a1aa;
    --text-faint: #71717a;
    --accent: #f97316;
    --accent-glow: rgba(249, 115, 22, 0.3);
    --accent-gradient: linear-gradient(135deg, #f97316, #e11d48);
    --teal: #2dd4bf;
    --radius: 12px;
  }
  
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0;
    background-color: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    overflow-x: hidden;
  }
  h1, h2, h3, h4 {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    margin: 0;
    line-height: 1.2;
  }
  a { color: inherit; text-decoration: none; }
  img { max-width: 100%; display: block; }
  .mono { font-family: 'Inter', monospace; }
  .wrap { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
  ::selection { background: var(--accent); color: #fff; }

  /* Dynamic Background */
  .grid-bg {
    position: relative;
  }
  .grid-bg::before {
    content: '';
    position: fixed;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: 
      radial-gradient(circle at 50% 50%, rgba(249, 115, 22, 0.05), transparent 40%),
      radial-gradient(circle at 80% 20%, rgba(225, 29, 72, 0.05), transparent 30%);
    z-index: -1;
    pointer-events: none;
  }

  /* Header */
  header {
    position: sticky; top: 0; z-index: 50;
    background: rgba(9, 9, 11, 0.7);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--line);
    transition: all 0.3s ease;
  }
  .headbar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 16px 0;
  }
  .brand { display: flex; align-items: center; gap: 16px; transition: transform 0.2s; }
  .brand:hover { transform: scale(1.02); }
  .brand img { height: 48px; width: auto; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.3)); }
  .brand-text { display: flex; flex-direction: column; }
  .brand-text .name { font-family: 'Outfit'; font-weight: 800; font-size: 18px; letter-spacing: 0.03em; background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .brand-text .tag { font-size: 11px; color: var(--text-faint); letter-spacing: 0.1em; font-weight: 500; text-transform: uppercase; margin-top: 2px;}
  
  nav ul { list-style: none; display: flex; gap: 8px; margin: 0; padding: 0; }
  nav a {
    display: block; padding: 8px 16px; font-size: 14px; color: var(--text-dim);
    font-weight: 500; border-radius: 20px; transition: all 0.2s ease;
  }
  nav a:hover { color: var(--text); background: rgba(255,255,255,0.05); }
  nav a.active { color: #fff; background: var(--accent-gradient); box-shadow: 0 4px 12px var(--accent-glow); }
  .nav-toggle { display: none; background: transparent; border: 1px solid var(--line); color: var(--text); padding: 8px 12px; border-radius: var(--radius); font-family: 'Outfit'; font-weight: 600; cursor: pointer; }

  @media (max-width: 860px) {
    nav { position: absolute; top: 100%; left: 0; right: 0; background: rgba(9, 9, 11, 0.95); backdrop-filter: blur(10px); display: none; border-bottom: 1px solid var(--line); }
    nav.open { display: block; animation: slideDown 0.3s ease forwards; }
    nav ul { flex-direction: column; padding: 16px 24px; gap: 8px; }
    nav a { padding: 12px; border-radius: 8px; }
    .nav-toggle { display: block; }
  }
  @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }

  /* Page Sections */
  .page { display: none; }
  .page.active { display: block; animation: fadeUp 0.5s cubic-bezier(0.16, 1, 0.3, 1); }
  @keyframes fadeUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

  section { padding: 80px 0; }
  section.tight { padding: 48px 0; }

  .eyebrow {
    font-size: 13px; font-weight: 600; color: var(--accent);
    letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;
    display: flex; align-items: center; gap: 12px;
  }
  .eyebrow::before { content: ""; width: 32px; height: 2px; background: var(--accent-gradient); display: inline-block; border-radius: 2px;}

  /* Hero */
  .hero { padding: 120px 0 80px; position: relative; }
  .hero::after { content:''; position:absolute; bottom:0; left:0; right:0; height:1px; background: linear-gradient(90deg, transparent, var(--line-bright), transparent); }
  .hero h1 { font-size: clamp(40px, 6vw, 72px); max-width: 900px; color: #fff; letter-spacing: -0.02em; }
  .hero h1 .hl { background: var(--accent-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
  .hero p.lead { margin-top: 24px; max-width: 650px; color: var(--text-dim); font-size: 18px; font-weight: 400; }
  
  .hero-actions { margin-top: 40px; display: flex; gap: 16px; flex-wrap: wrap; }
  .btn {
    font-family: 'Outfit'; font-size: 15px; font-weight: 600; padding: 14px 28px;
    border-radius: 30px; display: inline-flex; align-items: center; gap: 8px;
    transition: all 0.3s ease; cursor: pointer; border: none;
  }
  .btn-primary { background: var(--accent-gradient); color: #fff; box-shadow: 0 8px 24px var(--accent-glow); }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 12px 32px var(--accent-glow); filter: brightness(1.1); }
  .btn-ghost { background: transparent; color: var(--text); border: 1px solid var(--line-bright); }
  .btn-ghost:hover { border-color: #fff; background: rgba(255,255,255,0.05); transform: translateY(-2px); }

  .hero-meta {
    margin-top: 80px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px;
    padding-top: 40px; border-top: 1px solid var(--line);
  }
  .hero-meta div { display: flex; flex-direction: column; }
  .hero-meta .num { font-family: 'Outfit'; font-size: 36px; color: #fff; font-weight: 800; line-height: 1; }
  .hero-meta .lbl { font-size: 14px; color: var(--text-faint); margin-top: 8px; font-weight: 500; }
  @media (max-width: 768px) { .hero-meta { grid-template-columns: repeat(2, 1fr); gap: 32px; } }

  /* Section Headings */
  .sec-head { max-width: 700px; margin-bottom: 48px; }
  .sec-head h2 { font-size: clamp(32px, 4vw, 48px); color: #fff; letter-spacing: -0.01em; }
  .sec-head p { color: var(--text-dim); margin-top: 16px; font-size: 16px; }

  /* Cards */
  .card-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
  .card {
    background: var(--bg-panel); border: 1px solid var(--line); padding: 32px;
    border-radius: var(--radius); transition: all 0.3s ease; backdrop-filter: blur(10px);
  }
  .card:hover { transform: translateY(-4px); border-color: var(--line-bright); background: var(--bg-panel-hover); box-shadow: 0 12px 40px rgba(0,0,0,0.2); }
  .card h3 { font-size: 20px; color: #fff; margin-bottom: 12px; }
  .card p, .card li { color: var(--text-dim); font-size: 15px; }
  .card ul { margin: 0; padding-left: 20px; }
  .card li { margin-bottom: 8px; }
  @media (max-width: 860px) { .card-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 600px) { .card-grid { grid-template-columns: 1fr; } }

  /* Chip Strip */
  .strip { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px; }
  .chip {
    font-size: 14px; font-weight: 500; color: var(--text); background: rgba(255,255,255,0.03);
    border: 1px solid var(--line); padding: 8px 16px; border-radius: 20px;
    transition: all 0.2s ease;
  }
  .chip:hover { border-color: var(--accent); color: #fff; background: rgba(249, 115, 22, 0.1); }

  /* About */
  .split { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
  @media (max-width: 860px) { .split { grid-template-columns: 1fr; gap: 40px; } }
  .split p { color: var(--text-dim); font-size: 16px; margin-top: 16px; }
  .split img { border-radius: var(--radius); border: 1px solid var(--line); box-shadow: 0 20px 40px rgba(0,0,0,0.3); transition: transform 0.3s; }
  .split img:hover { transform: scale(1.02); }

  .why-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; margin-top: 40px; }
  @media (max-width: 768px) { .why-grid { grid-template-columns: 1fr; } }
  .why-item { background: var(--bg-panel); border: 1px solid var(--line); padding: 32px; border-radius: var(--radius); transition: all 0.3s; }
  .why-item:hover { border-color: var(--line-bright); background: var(--bg-panel-hover); }
  .why-item .tagnum { color: var(--accent); font-size: 13px; font-weight: 600; letter-spacing: 0.05em; }
  .why-item h3 { margin-top: 12px; font-size: 20px; color: #fff; }
  .why-item p, .why-item li { color: var(--text-dim); font-size: 15px; margin-top: 12px; }
  .why-item ul { padding-left: 20px; margin: 12px 0 0; }
  .why-item li { margin-bottom: 8px; }

  /* Products */
  .product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; }
  .p-item { background: var(--bg-panel); border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; transition: all 0.3s; }
  .p-item:hover { transform: translateY(-4px); border-color: var(--line-bright); box-shadow: 0 12px 30px rgba(0,0,0,0.4); }
  .p-item img { width: 100%; height: 200px; object-fit: cover; border-bottom: 1px solid var(--line); transition: transform 0.5s; }
  .p-item:hover img { transform: scale(1.05); }
  .p-item .cap { padding: 16px 20px; font-size: 15px; color: #fff; font-weight: 500; position: relative; z-index: 2; background: var(--bg-panel); }

  /* Table Tabs */
  .tabs { display: flex; gap: 12px; margin: 40px 0 24px; flex-wrap: wrap; background: rgba(0,0,0,0.2); padding: 6px; border-radius: 30px; display: inline-flex; border: 1px solid var(--line); }
  .tab-btn {
    font-size: 14px; font-weight: 600; padding: 10px 24px; background: transparent;
    border: none; border-radius: 20px; color: var(--text-dim); cursor: pointer; transition: all 0.2s;
  }
  .tab-btn:hover { color: #fff; }
  .tab-btn.on { color: #fff; background: var(--accent-gradient); box-shadow: 0 4px 12px var(--accent-glow); }
  .tab-panel { display: none; animation: fadeIn 0.4s ease; }
  .tab-panel.on { display: block; }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

  .tech-table { width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 16px; border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; }
  .tech-table th {
    text-align: left; font-size: 13px; color: var(--text-faint); background: rgba(255,255,255,0.02);
    text-transform: uppercase; letter-spacing: 0.05em; padding: 16px 24px; border-bottom: 1px solid var(--line);
  }
  .tech-table td { padding: 16px 24px; border-bottom: 1px solid var(--line); font-size: 15px; color: var(--text-dim); vertical-align: top; background: var(--bg-panel); transition: background 0.2s; }
  .tech-table td.brand { color: #fff; font-weight: 600; font-family: 'Outfit'; font-size: 16px; }
  .tech-table tr:last-child td { border-bottom: none; }
  .tech-table tr:hover td { background: var(--bg-panel-hover); color: var(--text); }

  /* Services */
  .service-row {
    display: grid; grid-template-columns: 280px 1fr; gap: 40px;
    padding: 40px; border: 1px solid var(--line); border-radius: var(--radius); margin-bottom: 24px;
    background: var(--bg-panel); transition: all 0.3s;
  }
  .service-row:hover { border-color: var(--line-bright); background: var(--bg-panel-hover); transform: translateY(-2px); }
  @media (max-width: 768px) { .service-row { grid-template-columns: 1fr; gap: 24px; padding: 24px; } }
  .service-row img { border-radius: 8px; width: 100%; height: 180px; object-fit: cover; }
  .service-row h3 { font-size: 22px; color: #fff; margin-bottom: 16px; }
  .service-row ul { margin: 0; padding-left: 20px; color: var(--text-dim); font-size: 15px; }
  .service-row li { margin-bottom: 8px; }
  .service-row li ul { margin-top: 8px; }

  .value-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 24px; }
  @media (max-width: 900px) { .value-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 600px) { .value-grid { grid-template-columns: 1fr; } }
  .value-item { background: var(--bg-panel); border: 1px solid var(--line); padding: 32px; border-radius: var(--radius); transition: all 0.3s; }
  .value-item:hover { transform: translateY(-4px); border-color: var(--line-bright); }
  .value-item .mark { display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 50%; background: rgba(45, 212, 191, 0.1); color: var(--teal); font-size: 18px; font-weight: bold; margin-bottom: 16px; }
  .value-item h4 { font-size: 18px; color: #fff; }
  .value-item ul { margin: 12px 0 0; padding-left: 20px; color: var(--text-dim); font-size: 14px; }
  .value-item li { margin-bottom: 6px; }

  /* Gallery */
  .gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; }
  .gallery-grid a { display: block; border-radius: var(--radius); overflow: hidden; aspect-ratio: 1; position: relative; }
  .gallery-grid a::after { content: ''; position: absolute; inset: 0; border: 1px solid var(--line); border-radius: var(--radius); pointer-events: none; transition: border-color 0.3s; }
  .gallery-grid img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s ease, filter 0.3s; filter: brightness(0.8); }
  .gallery-grid a:hover img { transform: scale(1.1); filter: brightness(1.1); }
  .gallery-grid a:hover::after { border-color: var(--line-bright); }

  /* Contact */
  .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 24px; }
  @media (max-width: 768px) { .contact-grid { grid-template-columns: 1fr; } }
  .contact-cell { background: var(--bg-panel); border: 1px solid var(--line); padding: 40px; border-radius: var(--radius); transition: all 0.3s; }
  .contact-cell:hover { border-color: var(--line-bright); background: var(--bg-panel-hover); }
  .contact-cell .lbl { font-size: 13px; color: var(--text-faint); text-transform: uppercase; letter-spacing: 0.1em; font-weight: 600; margin-bottom: 12px; }
  .contact-cell .val { font-size: 18px; color: #fff; font-weight: 500; }
  .contact-cell .val a { transition: color 0.2s; }
  .contact-cell .val a:hover { color: var(--accent); }
  
  .social-row { display: flex; gap: 12px; margin-top: 16px; }
  .social-row a {
    width: 44px; height: 44px; border: 1px solid var(--line); border-radius: 50%;
    display: flex; align-items: center; justify-content: center; font-size: 16px; color: var(--text);
    background: rgba(255,255,255,0.02); transition: all 0.3s ease;
  }
  .social-row a:hover { border-color: var(--accent); color: #fff; background: var(--accent); box-shadow: 0 4px 12px var(--accent-glow); transform: translateY(-2px); }

  /* Footer & CTA */
  .cta-band {
    border: 1px solid var(--line); background: var(--bg-panel); border-radius: var(--radius);
    padding: 48px; display: flex; justify-content: space-between; align-items: center; gap: 32px; flex-wrap: wrap;
    margin-top: 80px; position: relative; overflow: hidden;
  }
  .cta-band::before {
    content: ''; position: absolute; top: -50%; right: -10%; width: 50%; height: 200%;
    background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%); z-index: 0; pointer-events: none;
  }
  .cta-band > * { position: relative; z-index: 1; }
  .cta-band h3 { color: #fff; font-size: 28px; max-width: 500px; }
  .cta-band p { color: var(--text-dim); font-size: 16px; margin-top: 12px; }

  footer { border-top: 1px solid var(--line); padding: 40px 0; margin-top: 40px; }
  .foot-row { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 24px; }
  footer p { color: var(--text-faint); font-size: 14px; margin: 0; }
  footer .foot-links { display: flex; gap: 24px; }
  footer .foot-links a { color: var(--text-dim); font-size: 14px; font-weight: 500; transition: color 0.2s; }
  footer .foot-links a:hover { color: #fff; }
</style>"""

# Replace fonts and CSS
content = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?</style>', new_head_content, content, flags=re.DOTALL)

# Replace logo
content = re.sub(r'<img src="https://balajiautomation\.com/wp-content/uploads/2022/08/BALAJI-AUTOMATION-4-1\.png" alt="Balaji Automation logo">', r'<img src="logo_cropped.png" alt="Balaji Automation logo">', content)

with open('index.html', 'w') as f:
    f.write(content)

print("Updated index.html successfully.")
