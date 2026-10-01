import os
import re
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from html.parser import HTMLParser

class DetailedUnitParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h4 = False
        self.in_h5 = False
        self.h4_text = []
        self.h5_text = []
        self.img_src = None
        self.tables = []
        self.current_table = None
        self.current_row = None
        self.current_cell = None
        self.in_cell = False
        self.paragraphs = []
        self.in_p = False
        self.current_p = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'h4':
            self.in_h4 = True
            self.h4_text = []
        elif tag == 'h5':
            self.in_h5 = True
            self.h5_text = []
        elif tag == 'img':
            src = attrs_dict.get('src', '')
            if 'unit' in src.lower() and not self.img_src:
                self.img_src = src
        elif tag == 'table':
            self.current_table = []
        elif tag == 'tr':
            if self.current_table is not None:
                self.current_row = []
        elif tag in ('td', 'th'):
            if self.current_row is not None:
                self.current_cell = []
                self.in_cell = True
        elif tag == 'p':
            self.in_p = True
            self.current_p = []

    def handle_endtag(self, tag):
        if tag == 'h4':
            self.in_h4 = False
        elif tag == 'h5':
            self.in_h5 = False
        elif tag == 'p':
            self.in_p = False
            p_text = ''.join(self.current_p).strip()
            if p_text:
                self.paragraphs.append(p_text)
            self.current_p = []
        elif tag == 'table':
            if self.current_table is not None:
                self.tables.append(self.current_table)
                self.current_table = None
        elif tag == 'tr':
            if self.current_row is not None and self.current_table is not None:
                self.current_table.append(self.current_row)
                self.current_row = None
        elif tag in ('td', 'th'):
            if self.in_cell and self.current_row is not None:
                cell_text = ''.join(self.current_cell).strip()
                self.current_row.append(cell_text)
                self.current_cell = None
                self.in_cell = False

    def handle_data(self, data):
        if self.in_h4:
            self.h4_text.append(data)
        elif self.in_h5:
            self.h5_text.append(data)
        elif self.in_p:
            self.current_p.append(data)
        elif self.in_cell and self.current_cell is not None:
            self.current_cell.append(data)

def inspect_all():
    files = [f for f in os.listdir('original_unit_pages') if f.endswith('.html') and f != 'family_units.html']
    
    # Sort by unit number if possible
    print(f"Total unit files: {len(files)}")
    print("=" * 100)
    
    unit_data_all = {}
    
    for f in sorted(files):
        path = os.path.join('original_unit_pages', f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            html = fp.read()
        
        parser = DetailedUnitParser()
        parser.feed(html)
        
        h4 = ''.join(parser.h4_text).strip()
        h5 = ''.join(parser.h5_text).strip()
        
        # Fallback image search
        img = parser.img_src
        if not img:
            m = re.search(r'<img[^>]+src=["\']([^"\']*units[^"\']*)["\']', html, re.I)
            if m:
                img = m.group(1)
        
        # Normalize image path slashes
        if img:
            img = img.replace('\\', '/')
            if img.startswith('/'):
                img = img[1:]
        
        # Committee
        committee = []
        if len(parser.tables) > 0:
            for row in parser.tables[0]:
                row_text = ' '.join(cell for cell in row if cell).strip()
                if row_text:
                    # Clean up president / secretary format
                    committee.append(row_text)
        
        # Members table
        members = []
        headers = []
        if len(parser.tables) > 1:
            table = parser.tables[1]
            if len(table) > 0:
                headers = table[0]
                for row in table[1:]:
                    if any(cell.strip() for cell in row):
                        members.append(row)
        
        # Check for any 3rd table or extra text
        extra_tables = parser.tables[2:] if len(parser.tables) > 2 else []
        
        print(f"FILE: {f}")
        print(f"  H4 Title: {h4}")
        print(f"  H5 Subtitle: {h5}")
        print(f"  Image: {img}")
        print(f"  Committee ({len(committee)} rows): {committee}")
        print(f"  Members count: {len(members)}, Header: {headers}")
        if len(members) > 0:
            print(f"  Sample Member 1: {members[0]}")
            print(f"  Sample Member Last: {members[-1]}")
        if extra_tables:
            print(f"  EXTRA TABLES ({len(extra_tables)}): {extra_tables}")
        if parser.paragraphs:
            print(f"  Paragraphs: {parser.paragraphs[:3]}")
        print("-" * 80)
        
        unit_data_all[f] = {
            'filename': f,
            'h4': h4,
            'h5': h5,
            'image': img,
            'committee': committee,
            'members_headers': headers,
            'members': members,
            'extra_tables': extra_tables,
            'paragraphs': parser.paragraphs
        }

    return unit_data_all

if __name__ == '__main__':
    inspect_all()
