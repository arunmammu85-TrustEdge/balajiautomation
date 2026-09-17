import re

# 1. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

# Extract the gallery grid block
match = re.search(r'<div class="gallery-grid">(.*?)</div>', html, flags=re.DOTALL)
if match:
    images_html = match.group(1).strip()
    
    # 1. Convert href to webp
    # Format is: <a href="..."><img src="xyz.webp" ...></a>
    # We want <a href="xyz.webp"><img src="xyz.webp" ...></a>
    
    def replace_href(m):
        full_a_tag = m.group(0)
        src = re.search(r'src="([^"]+)"', full_a_tag).group(1)
        return re.sub(r'href="[^"]+"', f'href="{src}"', full_a_tag)
        
    images_html = re.sub(r'<a.*?</a>', replace_href, images_html)
    
    # 2. Build the new marquee structure
    marquee_html = f"""<div class="marquee-wrapper">
      <div class="marquee-content">
{images_html}
      </div>
      <!-- Duplicate for seamless infinite scroll -->
      <div class="marquee-content" aria-hidden="true">
{images_html}
      </div>
    </div>"""
    
    html = html[:match.start()] + marquee_html + html[match.end():]
    
    with open('index.html', 'w') as f:
        f.write(html)
    print("Gallery HTML updated to marquee.")
else:
    print("gallery-grid not found.")

# 2. Update CSS
with open('assets/css/style.css', 'r') as f:
    css = f.read()

if '.marquee-wrapper' not in css:
    marquee_css = """
/* Gallery Marquee */
.marquee-wrapper {
  display: flex;
  overflow: hidden;
  user-select: none;
  gap: 24px;
  width: 100%;
  padding: 10px 0;
}
.marquee-content {
  flex-shrink: 0;
  display: flex;
  justify-content: space-around;
  gap: 24px;
  min-width: 100%;
  animation: scrollX 60s linear infinite;
}
/* Pause on hover so users can click/view */
.marquee-wrapper:hover .marquee-content {
  animation-play-state: paused;
}
.marquee-content a {
  display: block;
}
.marquee-content img {
  height: 400px; /* Increased size by 100% */
  width: auto;
  max-width: none;
  border-radius: 16px;
  object-fit: cover;
  transition: transform 0.4s ease;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
.marquee-content img:hover {
  transform: scale(1.03);
}

@keyframes scrollX {
  from {
    transform: translateX(0);
  }
  to {
    transform: translateX(calc(-100% - 24px));
  }
}
"""
    css = css.replace('.gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; }', marquee_css)
    # Also clean up old grid img rule
    css = re.sub(r'\.gallery-grid img \{.*?\}', '', css)

    with open('assets/css/style.css', 'w') as f:
        f.write(css)
    print("Gallery CSS updated to marquee.")

