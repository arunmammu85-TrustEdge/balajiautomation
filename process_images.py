import re
import os
import urllib.request
from PIL import Image
from io import BytesIO

with open('index.html', 'r') as f:
    html = f.read()

# Find all image src URLs
urls = re.findall(r'<img[^>]+src=\"([^\"]+)\"', html)

# Keep track of replacements
replacements = {}

print(f"Found {len(urls)} image URLs.")

for i, url in enumerate(set(urls)):
    if url.startswith('data:'): continue
    
    # Generate a unique local filename
    # e.g. "SCADA.2.jpg" -> "SCADA.2.webp"
    basename = url.split('/')[-1]
    name_without_ext = os.path.splitext(basename)[0]
    
    # Some names might clash (e.g. 1.png and 1.jpg). We prepend a prefix if needed, or just use an index
    safe_name = f"img_{i}_{name_without_ext}.webp"
    local_path = os.path.join('assets/images', safe_name)
    
    try:
        if url.startswith('http'):
            print(f"Downloading {url}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                img_data = response.read()
            img = Image.open(BytesIO(img_data))
        else:
            print(f"Opening local file {url}...")
            img = Image.open(url)
            
        # Convert to RGB if needed to save as WebP
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGBA')
            
        img.save(local_path, 'WEBP', quality=85)
        replacements[url] = local_path
        print(f"Saved {local_path}")
    except Exception as e:
        print(f"Failed to process {url}: {e}")

# Replace in HTML
for old_url, new_url in replacements.items():
    html = html.replace(f'src="{old_url}"', f'src="{new_url}"')

with open('index.html', 'w') as f:
    f.write(html)

print("HTML updated successfully.")
