import re
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('original_unit_pages/family_units.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

matches = re.findall(r'<a\s+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.DOTALL)
unit_entries = []
for href, text in matches:
    clean_text = ' '.join(re.sub(r'<[^>]+>', '', text).split()).strip()
    if 'unit' in href.lower() and href != 'family_units.html':
        unit_entries.append((href.strip(), clean_text))

print(f"Total directory entries found: {len(unit_entries)}")
for idx, (href, text) in enumerate(unit_entries, 1):
    print(f"{idx:2}. {text:35} -> {href}")
