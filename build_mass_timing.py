from templates_base import get_shared_header, get_shared_footer

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Holy Mass Timings | Holy Cross Forane Church Manjapra</title>
  <meta name="description" content="Holy Mass Timings and Novena prayer schedule at Holy Cross Forane Church, Manjapra.">
  <meta name="keywords" content="Holy Mass Timings, Manjapra Church Mass, Novena Timings, Holy Cross Church, Syro Malabar Church">
  
  <!-- Favicon -->
  <link rel="shortcut icon" type="image/png" href="images/favicon.png">
  <link rel="icon" type="image/png" href="images/favicon.png">

  <!-- Google Fonts: Cormorant Garamond, Playfair Display, Plus Jakarta Sans, Noto Sans Malayalam -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Noto+Sans+Malayalam:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

{get_shared_header("mass-timing")}

  <!-- Page Banner (Cross Landscape Banner) -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> വിശുദ്ധ കുർബാന സമയങ്ങൾ</span>
      <h1 class="page-hero-title">Holy Mass Timings</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Mass Timings</span>
      </div>
    </div>
  </section>

  <!-- Main Section: Original 6-Row Mass Timings Table -->
  <section class="section bg-cream" style="padding-top: 55px; padding-bottom: 60px;">
    <div class="container">
      
      <div class="section-header text-center" style="margin-bottom: 36px;">
        <div class="section-tag"><i class="fa-solid fa-clock text-gold"></i> വിശുദ്ധ കുർബാന &bull; നൊവേന</div>
        <h2 class="section-title">Holy Mass Timings</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      </div>

      <!-- Original 6-Row Table Card -->
      <div class="mass-schedule-container">
        <div class="mass-schedule-card">
          <div class="mass-schedule-table-wrap">
            <table class="mass-schedule-table">
              <thead>
                <tr>
                  <th style="width: 28%;"><i class="fa-solid fa-calendar-day text-gold" style="margin-right: 8px;"></i> Day</th>
                  <th style="width: 34%;"><i class="fa-solid fa-clock text-gold" style="margin-right: 8px;"></i> Time</th>
                  <th style="width: 38%;"><i class="fa-solid fa-hands-praying text-gold" style="margin-right: 8px;"></i> Prayers</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="timing-day-cell">Sunday Morning</td>
                  <td class="timing-time-cell"><span class="timing-time-pill">5.30 AM, 7.00 AM, 9.00 AM</span></td>
                  <td class="timing-prayers-cell"><strong>HOLY MASS</strong></td>
                </tr>
                <tr>
                  <td class="timing-day-cell">Sunday Evening</td>
                  <td class="timing-time-cell"><span class="timing-time-pill">5.00 PM</span></td>
                  <td class="timing-prayers-cell"><strong>HOLY MASS</strong></td>
                </tr>
                <tr>
                  <td class="timing-day-cell">Weekdays Morning</td>
                  <td class="timing-time-cell"><span class="timing-time-pill">5.45 AM, 7.00 AM</span></td>
                  <td class="timing-prayers-cell"><strong>HOLY MASS</strong></td>
                </tr>
                <tr>
                  <td class="timing-day-cell">Tuesdays Morning</td>
                  <td class="timing-time-cell"><span class="timing-time-pill">6.45 AM</span></td>
                  <td class="timing-prayers-cell">Novena of St.Sebastian and Holy Mass</td>
                </tr>
                <tr>
                  <td class="timing-day-cell">Fridays Morning</td>
                  <td class="timing-time-cell"><span class="timing-time-pill">6.45 AM</span></td>
                  <td class="timing-prayers-cell">Novena of Holy Cross and Holy mass</td>
                </tr>
                <tr>
                  <td class="timing-day-cell">Tuesdays Morning</td>
                  <td class="timing-time-cell"><span class="timing-time-pill">6.45 AM</span></td>
                  <td class="timing-prayers-cell">Novena of Our Lady and Holy Mass</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Quick Access Section -->
      <div style="margin-top: 50px;">
        <div class="section-header text-center" style="margin-bottom: 26px;">
          <div class="section-tag"><i class="fa-solid fa-star text-gold"></i> വേഗത്തിലുള്ള ലിങ്കുകൾ</div>
          <h3 style="font-family: var(--font-serif); font-size: 1.85rem; color: var(--color-brown-dark);">Quick Navigation</h3>
          <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        </div>

        <div class="quick-access-grid">
          <a href="mass-timing.html" class="quick-card" style="margin: 0;">
            <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
            <h4 class="quick-card-title">Holy Mass Timings</h4>
            <p class="quick-card-desc">Daily &amp; Sunday service schedule</p>
          </a>
          <a href="news.html" class="quick-card" style="margin: 0;">
            <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
            <h4 class="quick-card-title">Parish News</h4>
            <p class="quick-card-desc">Feast and liturgy announcements</p>
          </a>
          <a href="contact.html" class="quick-card" style="margin: 0;">
            <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
            <h4 class="quick-card-title">Every Moment, Thank God</h4>
            <p class="quick-card-desc">Book mass intentions and prayers</p>
          </a>
        </div>
      </div>

    </div>
  </section>

{get_shared_footer()}

</body>
</html>
"""

with open("mass-timing.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully regenerated mass-timing.html with exact original content and champagne heritage design!")
