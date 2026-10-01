import urllib.request
import urllib.parse
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Cookie': 'humans_21909=1'
}

missing_files = ["St_xavier's_Unit.html", "St_Mary's_Unit.html"]

for filename in missing_files:
    url = 'http://holycrosschurchmanjapra.com/' + urllib.parse.quote(filename)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(os.path.join('original_unit_pages', filename), 'wb') as f:
                f.write(data)
            print('Successfully fetched', filename, 'len:', len(data))
            page_str = data.decode('utf-8', errors='ignore')
            img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', page_str, re.I)
            for img in img_srcs:
                if 'unit' in img.lower() or 'images/' in img.lower():
                    img_clean = img.strip().replace('\\', '/')
                    img_url = 'http://holycrosschurchmanjapra.com/' + urllib.parse.quote(img_clean)
                    try:
                        os.makedirs(os.path.dirname(img_clean), exist_ok=True)
                        img_req = urllib.request.Request(img_url, headers=headers)
                        with urllib.request.urlopen(img_req) as i_resp:
                            with open(img_clean, 'wb') as img_f:
                                img_f.write(i_resp.read())
                        print('  Downloaded img:', img_clean)
                    except Exception as ie:
                        print('  Failed img:', img_clean, ie)
    except Exception as e:
        print('Failed', filename, e)
