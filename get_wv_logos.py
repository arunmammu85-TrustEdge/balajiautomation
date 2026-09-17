import urllib.request

urls = {
    'delta.svg': 'https://cdn.worldvectorlogo.com/logos/delta-electronics-1.svg',
    'omron.svg': 'https://cdn.worldvectorlogo.com/logos/omron-1.svg',
    'fuji.svg': 'https://cdn.worldvectorlogo.com/logos/fuji-electric-logo-1.svg',
    'lg.svg': 'https://cdn.worldvectorlogo.com/logos/lg-electronics.svg'
}

req_headers = {'User-Agent': 'Mozilla/5.0'}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            with open(f'assets/images/logos/{name}', 'wb') as f:
                f.write(content)
            print(f"Downloaded {name}")
    except Exception as e:
        print(f"Failed {name}: {e}")

