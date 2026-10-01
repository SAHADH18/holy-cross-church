import os
from templates_base import get_shared_header, get_shared_footer

units_list = [
    ("St_xavier's_Unit.html", "സെന്റ് സേവ്യർ കുടുംബ യൂണിറ്റ് (St. Xavier Unit)", "യൂണിറ്റ് - 1"),
    ("Holy_Cross_Unit.html", "ഹോളി ക്രോസ് കുടുംബ യൂണിറ്റ് (Holy Cross Unit)", "യൂണിറ്റ് - 2"),
    ("Assisi_Unit.html", "അസ്സീസി കുടുംബ യൂണിറ്റ് (Assisi Unit)", "യൂണിറ്റ് - 3"),
    ("Don_Bosco_Unit.html", "സെന്റ് ഡോൺ ബോസ്കോ കുടുംബ യൂണിറ്റ് (St. Don Bosco Unit)", "യൂണിറ്റ് - 4"),
    ("St_Theresa_Unit.html", "സെന്റ് തെരേസ കുടുംബ യൂണിറ്റ് (St. Theresa Unit)", "യൂണിറ്റ് - 5"),
    ("St_Rockey_Unit.html", "സെന്റ് റോക്കി കുടുംബ യൂണിറ്റ് (St. Rockey Unit)", "യൂണിറ്റ് - 6"),
    ("Little_flower_Unit.html", "ലിറ്റിൽ ഫ്ലവർ കുടുംബ യൂണിറ്റ് (Little Flower Unit)", "യൂണിറ്റ് - 7"),
    ("St_Joseph_Unit.html", "സെന്റ് ജോസഫ് കുടുംബ യൂണിറ്റ് (St. Joseph Unit)", "യൂണിറ്റ് - 8"),
    ("St_James_Unit.html", "സെന്റ് ജെയിംസ് കുടുംബ യൂണിറ്റ് (St. James Unit)", "യൂണിറ്റ് - 9"),
    ("Holy_Family_Unit.html", "ഹോളി ഫാമിലി കുടുംബ യൂണിറ്റ് (Holy Family Unit)", "യൂണിറ്റ് - 10"),
    ("St_Martin_Unit.html", "സെന്റ് മാർട്ടിൻ കുടുംബ യൂണിറ്റ് (St. Martin Unit)", "യൂണിറ്റ് - 11"),
    ("St_Antony_Unit.html", "സെന്റ് ആന്റണി കുടുംബ യൂണിറ്റ് (St. Antony Unit)", "യൂണിറ്റ് - 12"),
    ("St_Augustine_Unit.html", "സെന്റ് അഗസ്റ്റിൻ കുടുംബ യൂണിറ്റ് (St. Augustine Unit)", "യൂണിറ്റ് - 13"),
    ("St_Mary's_Unit.html", "സെന്റ് മേരീസ് കുടുംബ യൂണിറ്റ് (St. Mary's Unit)", "യൂണിറ്റ് - 14"),
    ("St_Patric_Unit.html", "സെന്റ് പാട്രിക് കുടുംബ യൂണിറ്റ് (St. Patric Unit)", "യൂണിറ്റ് - 15"),
    ("St_ Clare_Unit.html", "സെന്റ് ക്ലെയർ കുടുംബ യൂണിറ്റ് (St. Clare Unit)", "യൂണിറ്റ് - 16"),
    ("St_Alphonsa_Unit.html", "സെന്റ് അൽഫോൻസാ കുടുംബ യൂണിറ്റ് (St. Alphonsa Unit)", "യൂണിറ്റ് - 17"),
    ("St_Kuriakose_Elias_Chavara_Unit.html", "സെന്റ് കുര്യാക്കോസ് ഏലിയാസ് ചാവറ യൂണിറ്റ് (St. Chavara Unit)", "യൂണിറ്റ് - 18"),
    ("St_Vincent_de_Paul _Unit.html", "സെന്റ് വിൻസെന്റ് ഡി പോൾ യൂണിറ്റ് (St. Vincent de Paul Unit)", "യൂണിറ്റ് - 19"),
    ("St_Francis_Unit.html", "സെന്റ് ഫ്രാൻസിസ് കുടുംബ യൂണിറ്റ് (St. Francis Unit)", "യൂണിറ്റ് - 20"),
    ("Sanjo_Unit.html", "സാൻജോ കുടുംബ യൂണിറ്റ് (Sanjo Unit)", "യൂണിറ്റ് - 21"),
    ("St_John_Unit.html", "സെന്റ് ജോൺ കുടുംബ യൂണിറ്റ് (St. John Unit)", "യൂണിറ്റ് - 22"),
    ("Nazreth_Unit.html", "നസ്രത്ത് കുടുംബ യൂണിറ്റ് (Nazreth Unit)", "യൂണിറ്റ് - 23"),
    ("St_Jude_Unit.html", "സെന്റ് ജൂഡ് കുടുംബ യൂണിറ്റ് (St. Jude Unit)", "യൂണിറ്റ് - 24"),
    ("St_Peter_Unit.html", "സെന്റ് പീറ്റർ കുടുംബ യൂണിറ്റ് (St. Peter Unit)", "യൂണിറ്റ് - 25"),
    ("St_Thomas_Unit.html", "സെന്റ് തോമസ് കുടുംബ യൂണിറ്റ് (St. Thomas Unit)", "യൂണിറ്റ് - 26"),
    ("Ave_Maria_Unit.html", "ആവേ മരിയ കുടുംബ യൂണിറ്റ് (Ave Maria Unit)", "യൂണിറ്റ് - 27"),
    ("Vimala_Unit.html", "വിമല കുടുംബ യൂണിറ്റ് (Vimala Unit)", "യൂണിറ്റ് - 28"),
    ("Fathima_Matha_Unit.html", "ഫാത്തിമ മാതാ കുടുംബ യൂണിറ്റ് (Fathima Matha Unit)", "യൂണിറ്റ് - 29"),
    ("St_Mother_Therese_Unit.html", "സെന്റ് മദർ തെരേസ കുടുംബ യൂണിറ്റ് (St. Mother Therese Unit)", "യൂണിറ്റ് - 30"),
    ("St_George_Unit.html", "സെന്റ് ജോർജ് കുടുംബ യൂണിറ്റ് (St. George Unit)", "യൂണിറ്റ് - 31"),
    ("St_Paul_Unit.html", "സെന്റ് പോൾ കുടുംബ യൂണിറ്റ് (St. Paul Unit)", "യൂണിറ്റ് - 32"),
    ("St_Sebastine_Unit.html", "സെന്റ് സെബാസ്റ്റ്യൻ കുടുംബ യൂണിറ്റ് (St. Sebastine Unit)", "യൂണിറ്റ് - 33"),
    ("Mary_Matha_Unit.html", "മേരി മാതാ കുടുംബ യൂണിറ്റ് (Mary Matha Unit)", "യൂണിറ്റ് - 34"),
    ("Secret_Heart_Unit.html", "സേക്രഡ് ഹാർട്ട് കുടുംബ യൂണിറ്റ് (Sacred Heart Unit)", "യൂണിറ്റ് - 35"),
]

for filename, unit_title, unit_no in units_list:
    if filename in ["Holy_Cross_Unit.html", "Assisi_Unit.html", "Don_Bosco_Unit.html", "St_Theresa_Unit.html"]:
        continue

    body = f"""
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> കുടുംബ കൂട്ടായ്മ</span>
      <h1 class="page-hero-title">{unit_title}</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="family_units.html">Family Units</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>{unit_title}</span>
      </div>
    </div>
  </section>

  <!-- Unit Details Section (Warm Cream #FBF3E5) -->
  <section class="section bg-cream">
    <div class="container">
      <div class="welcome-grid" style="margin-bottom: 50px;">
        <div>
          <div style="border-radius: var(--radius-sm); overflow: hidden; box-shadow: var(--shadow-card); border: 2px solid var(--color-gold);">
            <img src="images/holy_cross_church_manjapra.jpg" alt="{unit_title}" style="width: 100%; height: auto;">
          </div>
        </div>
        <div>
          <div class="section-tag"><i class="fa-solid fa-people-roof text-gold"></i> {unit_no}</div>
          <h2 class="section-title">{unit_title}</h2>
          <div class="gold-divider" style="justify-content: flex-start; margin-left: 0;"><span class="cross-symbol">✝</span></div>
          
          <p style="font-size: 1.08rem; line-height: 1.85; color: var(--color-brown-dark); margin-bottom: 24px;">
            Holy Cross Forane Church Manjapra parish community is structured into active Kudumba Koottayma units to promote Christian brotherhood, weekly prayer gatherings, and pastoral cooperation.
          </p>

          <div class="mass-table-wrapper" style="margin-bottom: 0;">
            <table class="mass-table">
              <tbody>
                <tr>
                  <td style="font-weight: 700; width: 35%; color: var(--color-gold-muted);">Unit Name</td>
                  <td style="font-weight: 600;">{unit_title}</td>
                </tr>
                <tr>
                  <td style="font-weight: 700; color: var(--color-gold-muted);">Unit Number</td>
                  <td style="font-weight: 600;">{unit_no}</td>
                </tr>
                <tr>
                  <td style="font-weight: 700; color: var(--color-gold-muted);">Parish</td>
                  <td style="font-weight: 600;">Holy Cross Forane Church, Manjapra</td>
                </tr>
                <tr>
                  <td style="font-weight: 700; color: var(--color-gold-muted);">Prayer Meetings</td>
                  <td style="font-weight: 600;">Weekly Family Ward Gatherings</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="family_units.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-people-roof"></i></div>
          <h4 class="quick-card-title">All Family Units</h4>
          <p class="quick-card-desc">Back to 35 Family Units directory</p>
        </a>
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Parish mass schedule</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Parish office contact</p>
        </a>
      </div>
    </div>
  </section>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{unit_title} | Holy Cross Forane Church Manjapra</title>
  <meta name="description" content="{unit_title} - Kudumba Koottayma of Holy Cross Forane Church, Manjapra.">
  <link rel="shortcut icon" type="image/png" href="images/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
{get_shared_header("family_units")}
{body}
{get_shared_footer()}
</body>
</html>
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filename}")

print("All family unit pages regenerated with light champagne theme!")
