import urllib.request
import json

filename = 'File:DeltaPSU_logo.svg'
name = 'delta.svg'

req_headers = {'User-Agent': 'Mozilla/5.0 (Bot for automation project)'}
try:
    api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={filename}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers=req_headers)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        pages = data['query']['pages']
        page = list(pages.values())[0]
        if 'imageinfo' in page:
            image_url = page['imageinfo'][0]['url']
            print(f"Found URL for {name}: {image_url}")
            
            img_req = urllib.request.Request(image_url, headers=req_headers)
            with urllib.request.urlopen(img_req) as img_resp:
                content = img_resp.read()
                with open(f'assets/images/logos/{name}', 'wb') as f:
                    f.write(content)
                print(f"Successfully downloaded {name} ({len(content)} bytes)")
        else:
            print(f"Could not find image info for {filename}")
except Exception as e:
    print(f"Error fetching {name}: {e}")
