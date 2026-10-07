import os
import re
import html
from templates_base import get_shared_header, get_shared_footer

# Complete mapping of 35 Units with their canonical English name, Malayalam name, and unit number
unit_meta = {
    "St_xavier's_Unit.html": {
        "num": 1,
        "en_name": "St. Xavier Unit",
        "ml_name": "സെന്റ് സേവ്യേഴ്സ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 1",
        "img": "images/units/St_xavier.jpg"
    },
    "Holy_Cross_Unit.html": {
        "num": 2,
        "en_name": "Holy Cross Unit",
        "ml_name": "ഹോളി ക്രോസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 2",
        "img": "images/units/Holy_Cross.jpg"
    },
    "Assisi_Unit.html": {
        "num": 3,
        "en_name": "Assisi Unit",
        "ml_name": "അസ്സീസി കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 3",
        "img": "images/units/St_assisi.jpg"
    },
    "Don_Bosco_Unit.html": {
        "num": 4,
        "en_name": "St. Don Bosco Unit",
        "ml_name": "ഡോൺ ബോസ്കോ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 4",
        "img": "images/units/don bosco.jpg"
    },
    "St_Theresa_Unit.html": {
        "num": 5,
        "en_name": "St. Theresa Unit",
        "ml_name": "സെന്റ് തെരേസ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 5",
        "img": "images/units/St_Therese.jpg"
    },
    "St_Rockey_Unit.html": {
        "num": 6,
        "en_name": "St. Rockey Unit",
        "ml_name": "സെന്റ് റോക്കീസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 6",
        "img": "images/units/ST_rockeys.jpg"
    },
    "Little_flower_Unit.html": {
        "num": 7,
        "en_name": "Little Flower Unit",
        "ml_name": "ചെറുപുഷ്പം (ലിറ്റിൽ ഫ്ലവർ) കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 7",
        "img": "images/units/Little_flower.jpg"
    },
    "St_Joseph_Unit.html": {
        "num": 8,
        "en_name": "St. Joseph Unit",
        "ml_name": "സെന്റ് ജോസഫ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 8",
        "img": "images/units/StJoseph.jpg"
    },
    "St_James_Unit.html": {
        "num": 9,
        "en_name": "St. James Unit",
        "ml_name": "സെന്റ് ജെയിംസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 9",
        "img": "images/units/st_james.jpg"
    },
    "Holy_Family_Unit.html": {
        "num": 10,
        "en_name": "Holy Family Unit",
        "ml_name": "തിരുക്കുടുംബം (ഹോളി ഫാമിലി) കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 10",
        "img": "images/units/Holy_Family.jpg"
    },
    "St_Martin_Unit.html": {
        "num": 11,
        "en_name": "St. Martin Unit",
        "ml_name": "സെന്റ് മാർട്ടിൻ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 11",
        "img": "images/units/St_martin.jpg"
    },
    "St_Antony_Unit.html": {
        "num": 12,
        "en_name": "St. Antony Unit",
        "ml_name": "സെന്റ് ആന്റണീസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 12",
        "img": "images/units/St_antony.jpg"
    },
    "St_Augustine_Unit.html": {
        "num": 13,
        "en_name": "St. Augustine Unit",
        "ml_name": "സെന്റ് അഗസ്റ്റിൻസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 13",
        "img": "images/units/St_Augustine.jpg"
    },
    "St_Mary's_Unit.html": {
        "num": 14,
        "en_name": "St. Mary's Unit",
        "ml_name": "സെന്റ് മേരീസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 14",
        "img": "images/units/Mary_Matha_.jpg"
    },
    "St_Patric_Unit.html": {
        "num": 15,
        "en_name": "St. Patric Unit",
        "ml_name": "സെന്റ് പാട്രിക് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 15",
        "img": "images/units/St_Patric.jpg"
    },
    "St_ Clare_Unit.html": {
        "num": 16,
        "en_name": "St. Clare Unit",
        "ml_name": "സെന്റ് ക്ലെയർ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 16",
        "img": "images/units/st_clare.jpg"
    },
    "St_Alphonsa_Unit.html": {
        "num": 17,
        "en_name": "St. Alphonsa Unit",
        "ml_name": "സെന്റ് അൽഫോൻസാ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 17",
        "img": "images/units/st-alphonsa.jpg"
    },
    "St_Kuriakose_Elias_Chavara_Unit.html": {
        "num": 18,
        "en_name": "St. Kuriakose Elias Chavara Unit",
        "ml_name": "സെന്റ് കുര്യാക്കോസ് ഏലിയാസ് ചാവറ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 18",
        "img": "images/units/St_chavarayachan.jpg"
    },
    "St_Vincent_de_Paul _Unit.html": {
        "num": 19,
        "en_name": "St. Vincent de Paul Unit",
        "ml_name": "സെന്റ് വിൻസന്റ് ഡി പോൾ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 19",
        "img": "images/units/St_Vincent_de_Paul.jpg"
    },
    "St_Francis_Unit.html": {
        "num": 20,
        "en_name": "St. Francis Unit",
        "ml_name": "സെന്റ് ഫ്രാൻസിസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 20",
        "img": "images/units/st_francis.jpg"
    },
    "Sanjo_Unit.html": {
        "num": 21,
        "en_name": "Sanjo Unit",
        "ml_name": "സാൻജോ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 21",
        "img": "images/units/Sanjo.jpg"
    },
    "St_John_Unit.html": {
        "num": 22,
        "en_name": "St. John Unit",
        "ml_name": "സെന്റ് ജോൺ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 22",
        "img": "images/units/St_John.jpg"
    },
    "Nazreth_Unit.html": {
        "num": 23,
        "en_name": "Nazreth Unit",
        "ml_name": "നസ്രത്ത് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 23",
        "img": "images/units/Nazareth.jpg"
    },
    "St_Jude_Unit.html": {
        "num": 24,
        "en_name": "St. Jude Unit",
        "ml_name": "സെന്റ് ജൂഡ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 24",
        "img": "images/units/St_Jude.jpg"
    },
    "St_Peter_Unit.html": {
        "num": 25,
        "en_name": "St. Peter Unit",
        "ml_name": "സെന്റ് പീറ്റർ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 25",
        "img": "images/units/St_peter.jpg"
    },
    "St_Thomas_Unit.html": {
        "num": 26,
        "en_name": "St. Thomas Unit",
        "ml_name": "സെന്റ് തോമസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 26",
        "img": "images/units/St.Thomas.jpg"
    },
    "Ave_Maria_Unit.html": {
        "num": 27,
        "en_name": "Ave Maria Unit",
        "ml_name": "ആവേ മരിയ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 27",
        "img": "images/units/Ave Maria.jpg"
    },
    "Vimala_Unit.html": {
        "num": 28,
        "en_name": "Vimala Unit",
        "ml_name": "വിമല കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 28",
        "img": "images/units/St_vimala.jpg"
    },
    "Fathima_Matha_Unit.html": {
        "num": 29,
        "en_name": "Fathima Matha Unit",
        "ml_name": "ഫാത്തിമ മാതാ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 29",
        "img": "images/units/fathima_matha.jpg"
    },
    "St_Mother_Therese_Unit.html": {
        "num": 30,
        "en_name": "St. Mother Therese Unit",
        "ml_name": "സെന്റ് മദർ തെരേസ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 30",
        "img": "images/units/Mother.jpg"
    },
    "St_George_Unit.html": {
        "num": 31,
        "en_name": "St. George Unit",
        "ml_name": "സെന്റ് ജോർജ്ജ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 31",
        "img": "images/units/St_George.jpg"
    },
    "St_Paul_Unit.html": {
        "num": 32,
        "en_name": "St. Paul Unit",
        "ml_name": "സെന്റ് പോൾ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 32",
        "img": "images/units/ST_PAUL.jpg"
    },
    "St_Sebastine_Unit.html": {
        "num": 33,
        "en_name": "St. Sebastine Unit",
        "ml_name": "സെന്റ് സെബാസ്റ്റ്യൻസ് കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 33",
        "img": "images/units/St_sebastine.jpg"
    },
    "Mary_Matha_Unit.html": {
        "num": 34,
        "en_name": "Mary Matha Unit",
        "ml_name": "മേരി മാതാ കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 34",
        "img": "images/units/Mary_Matha_.jpg"
    },
    "Secret_Heart_Unit.html": {
        "num": 35,
        "en_name": "Sacred Heart Unit",
        "ml_name": "തിരുഹൃദയം (സേക്രഡ് ഹാർട്ട്) കുടുംബ യൂണിറ്റ്",
        "ml_num": "യൂണിറ്റ് - 35",
        "img": "images/units/sacred-heart-jesus.jpg"
    }
}

def parse_original_file(filename):
    path = os.path.join('original_unit_pages', filename)
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Extract all tables
    table_pattern = re.compile(r'<table[^>]*>(.*?)</table>', re.DOTALL | re.IGNORECASE)
    raw_tables = table_pattern.findall(content)

    committee_rows = []
    member_rows = []

    if len(raw_tables) > 0:
        # Table 1: Executive Committee
        tr_matches = re.findall(r'<tr[^>]*>(.*?)</tr>', raw_tables[0], re.DOTALL | re.IGNORECASE)
        for tr in tr_matches:
            # Extract cell text
            td_texts = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL | re.IGNORECASE)
            full_row_str = ' '.join(re.sub(r'<[^>]+>', '', t) for t in td_texts)
            clean_str = ' '.join(full_row_str.split()).replace('&nbsp;', ' ').strip()
            
            # Parse Role : Name
            if ':' in clean_str:
                parts = clean_str.split(':', 1)
                role = parts[0].strip()
                name = parts[1].strip()
                if role:
                    committee_rows.append((role, name))
            elif clean_str:
                committee_rows.append(('Office Bearer', clean_str))

    if len(raw_tables) > 1:
        # Table 2: Members
        tr_matches = re.findall(r'<tr[^>]*>(.*?)</tr>', raw_tables[1], re.DOTALL | re.IGNORECASE)
        for tr in tr_matches:
            td_texts = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL | re.IGNORECASE)
            clean_cells = [' '.join(re.sub(r'<[^>]+>', '', t).split()).replace('&nbsp;', '').strip() for t in td_texts]
            
            # Check if this is a header row
            if clean_cells and any('{Ia' in c or 't]cv' in c or 'ho«pt]cv' in c or 't^m¬' in c or 'ക്രമ' in c or 'പേര്' in c for c in clean_cells):
                continue
            
            if len(clean_cells) >= 2:
                slno = clean_cells[0]
                name = clean_cells[1]
                phone = clean_cells[2] if len(clean_cells) > 2 else ''
                # Clean phone
                phone_clean = phone.replace(' ', '').replace('-', '')
                if slno or name or phone:
                    member_rows.append({
                        'slno': slno,
                        'name': name,
                        'phone': phone
                    })

    return {
        'committee': committee_rows,
        'members': member_rows
    }

def generate_unit_html(filename, meta, parsed_data):
    unit_num = meta['num']
    en_name = meta['en_name']
    ml_name = meta['ml_name']
    ml_num = meta['ml_num']
    img_path = meta['img']

    full_display_title = f"{ml_name} ({en_name})"
    page_title = f"{en_name} | Holy Cross Forane Church Manjapra"
    
    committee_rows = parsed_data['committee'] if parsed_data else []
    member_rows = parsed_data['members'] if parsed_data else []
    total_unit_members = len(member_rows)

    # Build Executive Committee HTML
    committee_html = ""
    if committee_rows:
        committee_html = f"""        <div class="unit-committee-box">
          <div class="unit-committee-header">
            <span class="section-tag" style="margin-bottom: 0;"><i class="fa-solid fa-users-gear text-gold"></i> ഭരണസമിതി</span>
            <span class="unit-committee-pill">{ml_num}</span>
          </div>
          <h3 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--color-brown-dark); margin-bottom: 12px;">Unit Executive Committee</h3>
          <div class="gold-divider" style="justify-content: flex-start; margin-left: 0; margin-bottom: 16px;"><span class="cross-symbol">✝</span></div>
          
          <table class="committee-table">
            <tbody>
"""
        for role, name in committee_rows:
            committee_html += f"""              <tr>
                <td class="committee-role">{html.escape(role)}</td>
                <td class="committee-name">{html.escape(name) if name else '<span style="color: var(--color-text-muted); font-style: italic;">—</span>'}</td>
              </tr>
"""
        committee_html += """            </tbody>
          </table>
        </div>"""
    else:
        committee_html = f"""        <div class="unit-committee-box">
          <div class="section-tag"><i class="fa-solid fa-people-roof text-gold"></i> <span class="unit-num-nobr">{ml_num}</span></div>
          <h3 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--color-brown-dark); margin-bottom: 12px;">{full_display_title}</h3>
          <div class="gold-divider" style="justify-content: flex-start; margin-left: 0; margin-bottom: 16px;"><span class="cross-symbol">✝</span></div>
          <p style="color: var(--color-brown-dark); line-height: 1.8; font-size: 1.05rem;">
            Holy Cross Forane Church Manjapra parish community ward unit active in regular prayer gatherings, spiritual communion, and pastoral support.
          </p>
        </div>"""

    # Active page identifier
    active_slug = "family_units"

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <meta name="description" content="{full_display_title} - {ml_num} Kudumba Koottayma of Holy Cross Forane Church, Manjapra.">
  <link rel="shortcut icon" type="image/png" href="images/favicon.png">
  <link rel="icon" type="image/png" href="images/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

{get_shared_header(active_slug)}

  <!-- Page Banner (Cross Landscape Banner) -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Family Unit &bull; <span class="unit-num-nobr">Unit - {unit_num}</span></span>
      <h1 class="page-hero-title">{en_name}</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="family_units.html">Family Units</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>{en_name}</span>
      </div>
    </div>
  </section>

  <!-- Unit Details Main Section -->
  <section class="section bg-cream unit-detail-section" style="padding-top: 50px; padding-bottom: 70px;">
    <div class="container unit-detail-container">
      
      <!-- Back Link & Header info -->
      <div class="unit-top-actions" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 30px; flex-wrap: wrap; gap: 14px;">
        <a href="family_units.html" class="btn btn-outline-gold btn-sm">
          <i class="fa-solid fa-arrow-left"></i> Back to Family Units Directory
        </a>
        <div style="font-size: 0.95rem; color: var(--color-brown-dark); font-weight: 600;">
          <i class="fa-solid fa-church text-gold"></i> Holy Cross Forane Church, Manjapra
        </div>
      </div>

      <!-- Unit Intro Grid: Left Image, Right Committee -->
      <div class="unit-intro-grid">
        <div class="unit-image-card">
          <div class="unit-image-wrapper">
            <img src="{img_path}" alt="{full_display_title}" onerror="this.src='images/holy_cross_church_manjapra.jpg'">
          </div>
          <div class="unit-card-info">
            <h4 class="unit-card-name">{en_name}</h4>
            <span class="unit-card-subtitle"><span class="unit-num-nobr">{ml_num}</span> &bull; {ml_name}</span>
            <div class="unit-stats-grid">
              <div class="unit-stat-item">
                <span class="unit-stat-label">Family</span>
                <span class="unit-stat-value">{unit_num}</span>
              </div>
              <div class="unit-stat-item">
                <span class="unit-stat-label">Total Unit Members</span>
                <span class="unit-stat-value">{total_unit_members}</span>
              </div>
            </div>
          </div>
        </div>

{committee_html}
      </div>

      <!-- Quick Access Cards -->
      <div class="unit-quick-nav" style="margin-top: 60px;">
        <div class="section-header text-center" style="margin-bottom: 28px;">
          <div class="section-tag"><i class="fa-solid fa-star text-gold"></i> വേഗത്തിലുള്ള ലിങ്കുകൾ</div>
          <h3 style="font-family: var(--font-serif); font-size: 2rem; color: var(--color-brown-dark);">Quick Navigation</h3>
          <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        </div>

        <div class="quick-access-grid">
          <a href="family_units.html" class="quick-card" style="margin: 0;">
            <div class="quick-card-icon"><i class="fa-solid fa-people-roof"></i></div>
            <h4 class="quick-card-title">All 35 Family Units</h4>
            <p class="quick-card-desc">Browse complete parish directory</p>
          </a>
          <a href="mass-timing.html" class="quick-card" style="margin: 0;">
            <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
            <h4 class="quick-card-title">Holy Mass Timings</h4>
            <p class="quick-card-desc">Daily &amp; Sunday liturgical schedule</p>
          </a>
          <a href="contact.html" class="quick-card" style="margin: 0;">
            <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
            <h4 class="quick-card-title">Every Moment, Thank God</h4>
            <p class="quick-card-desc">Parish office contact &amp; prayers</p>
          </a>
        </div>
      </div>

    </div>
  </section>

{get_shared_footer()}
</body>
</html>
"""
    return page_html

def main():
    generated_count = 0
    for filename, meta in unit_meta.items():
        parsed = parse_original_file(filename)
        html_code = generate_unit_html(filename, meta, parsed)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_code)
        
        member_count = len(parsed['members']) if parsed else 0
        comm_count = len(parsed['committee']) if parsed else 0
        print(f"Generated {filename:36} -> Unit {meta['num']:2}: {meta['en_name']:30} ({comm_count} comm, {member_count} members)")
        generated_count += 1

    print(f"\nSuccessfully generated all {generated_count} Family Unit pages with exact original data and champagne heritage design!")

if __name__ == '__main__':
    main()
