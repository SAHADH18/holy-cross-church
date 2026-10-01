import urllib.request
import urllib.parse
import re
import os
import time

os.makedirs('original_unit_pages', exist_ok=True)
os.makedirs('images/units', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Cookie': 'humans_21909=1'
}

def fetch_url(url):
    # Quote the URL path properly
    parsed = urllib.parse.urlsplit(url)
    path = urllib.parse.quote(parsed.path)
    safe_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, parsed.fragment))
    req = urllib.request.Request(safe_url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()

# 1. Fetch original family_units.html
print("Fetching original family_units.html...")
content = fetch_url('http://holycrosschurchmanjapra.com/family_units.html')
html = content.decode('utf-8', errors='ignore')
with open('original_unit_pages/family_units.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Extract all unit links from original family_units.html
raw_links = re.findall(r'href=["\']([^"\']*Unit[^"\']*\.html)["\']', html, re.I)
unit_links = []
for l in raw_links:
    clean_l = l.strip()
    if clean_l and clean_l not in unit_links:
        unit_links.append(clean_l)

print(f"Discovered {len(unit_links)} unit links from family_units.html:")
for idx, l in enumerate(unit_links, 1):
    print(f"  {idx}. {l}")

# 2. Fetch each original unit HTML
for idx, filename in enumerate(unit_links, 1):
    target_path = os.path.join('original_unit_pages', filename)
    url = f'http://holycrosschurchmanjapra.com/{filename}'
    print(f"Fetching [{idx}/{len(unit_links)}] {filename} ...")
    try:
        data = fetch_url(url)
        with open(target_path, 'wb') as f:
            f.write(data)
        
        # Check for images referenced in this unit page
        page_str = data.decode('utf-8', errors='ignore')
        img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', page_str, re.I)
        for img in img_srcs:
            if 'unit' in img.lower() or 'images/' in img.lower():
                img_clean = img.strip().replace('\\', '/')
                local_img_path = img_clean
                if local_img_path.startswith('/'):
                    local_img_path = local_img_path[1:]
                # Download if missing
                if not os.path.exists(local_img_path):
                    img_url = f'http://holycrosschurchmanjapra.com/{img_clean}'
                    print(f"  Downloading image {img_url} -> {local_img_path}")
                    try:
                        os.makedirs(os.path.dirname(local_img_path), exist_ok=True)
                        img_data = fetch_url(img_url)
                        with open(local_img_path, 'wb') as img_f:
                            img_f.write(img_data)
                    except Exception as e:
                        print(f"    Failed image {img_clean}: {e}")
    except Exception as e:
        print(f"  Failed unit {filename}: {e}")
    time.sleep(0.2)

print("Finished fetching all original unit pages!")
