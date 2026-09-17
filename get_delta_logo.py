import urllib.request
import re

req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
req = urllib.request.Request("https://www.deltaww.com/en-US/index", headers=req_headers)

try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        # Look for img tag with logo in src
        match = re.search(r'<img[^>]+src="([^"]*logo[^"]*\.svg|[^"]*logo[^"]*\.png)"', html, re.I)
        if match:
            logo_url = match.group(1)
            if not logo_url.startswith('http'):
                logo_url = 'https://www.deltaww.com' + logo_url
            print(f"Found logo: {logo_url}")
            
            img_req = urllib.request.Request(logo_url, headers=req_headers)
            with urllib.request.urlopen(img_req) as img_resp:
                content = img_resp.read()
                ext = 'svg' if 'svg' in logo_url else 'png'
                with open(f'assets/images/logos/delta.{ext}', 'wb') as f:
                    f.write(content)
                print(f"Downloaded delta.{ext}!")
        else:
            print("Logo not found in HTML.")
except Exception as e:
    print(f"Error: {e}")
