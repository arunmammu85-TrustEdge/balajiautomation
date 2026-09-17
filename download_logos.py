import urllib.request
import os

urls = {
    'allen-bradley.svg': 'https://upload.wikimedia.org/wikipedia/commons/4/4b/Allen-Bradley_logo.svg',
    'schneider.svg': 'https://upload.wikimedia.org/wikipedia/commons/9/9d/Schneider_Electric_2007.svg',
    'mitsubishi.svg': 'https://upload.wikimedia.org/wikipedia/commons/0/0b/Mitsubishi_Electric_logo.svg',
    'delta.svg': 'https://upload.wikimedia.org/wikipedia/commons/b/b8/Delta_Electronics_logo.svg'
}

os.makedirs('assets/images/logos', exist_ok=True)

req_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            with open(f'assets/images/logos/{name}', 'wb') as f:
                f.write(content)
            print(f"Downloaded {name} - Size: {len(content)} bytes")
    except Exception as e:
        print(f"Failed to download {name}: {e}")

