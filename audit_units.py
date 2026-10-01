import os
import re
import sys
from html.parser import HTMLParser

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

class SimpleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.current_tag = None
        self.text_chunks = []
        self.h4_text = None
        self.h5_text = None
        self.img_src = None
        self.in_h4 = False
        self.in_h5 = False
        self.tables = []
        self.current_table = None
        self.current_row = None
        self.current_cell = None
        self.in_cell = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'h4':
            self.in_h4 = True
            self.current_h4 = []
        elif tag == 'h5':
            self.in_h5 = True
            self.current_h5 = []
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

    def handle_endtag(self, tag):
        if tag == 'h4':
            self.in_h4 = False
            if self.h4_text is None and hasattr(self, 'current_h4'):
                self.h4_text = ''.join(self.current_h4).strip()
        elif tag == 'h5':
            self.in_h5 = False
            if self.h5_text is None and hasattr(self, 'current_h5'):
                self.h5_text = ''.join(self.current_h5).strip()
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
            self.current_h4.append(data)
        elif self.in_h5:
            self.current_h5.append(data)
        elif self.in_cell and self.current_cell is not None:
            self.current_cell.append(data)

def audit_all():
    files = [f for f in os.listdir('original_unit_pages') if f.endswith('.html') and f != 'family_units.html']
    print(f"Auditing {len(files)} unit files:")
    print("=" * 110)
    
    results = []
    for f in sorted(files):
        path = os.path.join('original_unit_pages', f)
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            html = fp.read()
        
        parser = SimpleHTMLParser()
        parser.feed(html)
        
        # fallback img search
        if not parser.img_src:
            m = re.search(r'<img[^>]+src=["\']([^"\']*units[^"\']*)["\']', html, re.I)
            if m:
                parser.img_src = m.group(1)
        
        # committee and members
        comm_count = len(parser.tables[0]) if len(parser.tables) > 0 else 0
        memb_count = max(0, len(parser.tables[1]) - 1) if len(parser.tables) > 1 else 0
        
        print(f"{f:36} | {parser.h5_text or 'N/A':12} | {parser.h4_text or 'N/A':30} | Img: {parser.img_src or 'None':30} | Comm: {comm_count:2} rows | Memb: {memb_count:3} rows")
        results.append({
            'file': f,
            'h5': parser.h5_text,
            'h4': parser.h4_text,
            'img': parser.img_src,
            'tables': parser.tables
        })
    return results

if __name__ == '__main__':
    audit_all()
