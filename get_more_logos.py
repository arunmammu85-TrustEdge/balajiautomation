import urllib.request
import json
import os
import time

files = {
    'omron.svg': 'File:Omron_Logo.svg',
    'fuji.svg': 'File:Fuji_Electric_logo.svg',
    'lg.svg': 'File:LG_logo_(2015).svg',
    'delta.svg': 'File:Delta_Electronics_logo.svg'
}

req_headers = {'User-Agent': 'Mozilla/5.0 (Bot for automation project; contact@example.com)'}

for name, filename in files.items():
    try:
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={filename}&prop=imageinfo&iiprop=url&format=json"
        req = urllib.request.Request(api_url, headers=req_headers)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            pages = data['query']['pages']
            page = list(pages.values())[0]
            if 'imageinfo' in page:
                image_url = page['imageinfo'][0]['url']
                img_req = urllib.request.Request(image_url, headers=req_headers)
                with urllib.request.urlopen(img_req) as img_resp:
                    content = img_resp.read()
                    with open(f'assets/images/logos/{name}', 'wb') as f:
                        f.write(content)
                print(f"Downloaded {name}!")
            else:
                print(f"Not found: {filename}")
    except Exception as e:
        print(f"Error {name}: {e}")
    time.sleep(1)
