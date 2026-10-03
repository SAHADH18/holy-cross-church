import os
from templates_base import get_shared_header, get_shared_footer

def render_html_page(filename, title, active_nav, body_content, meta_desc=""):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc or 'Holy Cross Forane Church, Manjapra in Kerala under the Major Archdiocese of Ernakulam-Angamaly.'}">
  <meta name="keywords" content="Holy Cross Church, Manjapra Church, Syro Malabar Church, Forane Church Manjapra, Kerala Catholic Church">
  
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

{get_shared_header(active_nav)}

{body_content}

{get_shared_footer()}

</body>
</html>
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filename}")

# ==========================================
# 1. INDEX.HTML (HOMEPAGE - LIGHT CHAMPAGNE THEME)
# ==========================================
def build_index():
    body = """
  <!-- Cinematic Atmospheric Hero Section -->
  <section class="hero-slider-section" aria-label="Hero Carousel">
    <div class="hero-slide active" style="background-image: url('images/banner/banner-3.jpg');"></div>
    <div class="hero-slide" style="background-image: url('images/banner/banner-1.jpg');"></div>
    <div class="hero-slide" style="background-image: url('images/banner/banner-2.jpg');"></div>
    <div class="hero-slide" style="background-image: url('images/banner/banner-4.jpg');"></div>
    
    <div class="hero-overlay"></div>

    <div class="container hero-content">
      <div class="hero-cross"><i class="fa-solid fa-cross"></i></div>
      <div class="hero-pretitle">Major Archdiocese of Ernakulam - Angamaly</div>
      <h1 class="hero-title">HOLY CROSS FORANE CHURCH</h1>
      <div class="hero-location">Manjapra, Kerala &bull; Estd. 1568 AD</div>
      
      <div class="gold-divider">
        <span class="cross-symbol" style="color: var(--color-champagne-primary);">✝</span>
      </div>

      <p style="font-size: 1.2rem; max-width: 720px; margin: 0 auto 34px; color: var(--color-champagne-light); line-height: 1.7; text-shadow: 0 2px 8px rgba(0,0,0,0.6);">
        A renowned  and historic spiritual sanctuary dedicated to the Exaltation of the Holy Cross.
      </p>

      <div class="hero-actions">
        <a href="mass-timing.html" class="btn btn-primary"><i class="fa-solid fa-clock"></i> Holy Mass Timings</a>
        <a href="history.html" class="btn btn-outline-white"><i class="fa-solid fa-landmark"></i> Explore Heritage</a>
        <a href="contact.html" class="btn btn-outline-white"><i class="fa-solid fa-hands-praying"></i> Prayer Intentions</a>
      </div>
    </div>

    <!-- Hero Slider Navigation Arrows (Vertically Centered Left/Right) -->
    <button class="slider-btn prev" aria-label="Previous slide" title="Previous Slide">
      <i class="fa-solid fa-chevron-left"></i>
    </button>
    <button class="slider-btn next" aria-label="Next slide" title="Next Slide">
      <i class="fa-solid fa-chevron-right"></i>
    </button>

    <!-- Bottom Slide Indicators -->
    <div class="slider-dots">
      <span class="slider-dot active" aria-label="Slide 1"></span>
      <span class="slider-dot" aria-label="Slide 2"></span>
      <span class="slider-dot" aria-label="Slide 3"></span>
      <span class="slider-dot" aria-label="Slide 4"></span>
    </div>
  </section>

  <!-- Quick Access Service Section (Light Champagne #F7E6CA, White Cards) -->
  <section class="quick-access-section">
    <div class="container">
      <div class="quick-access-grid">
        <a href="mass-timing.html" class="quick-card">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h3 class="quick-card-title">Holy Mass Timings</h3>
          <p class="quick-card-desc">Daily Mass, Sunday Liturgies, Novena to Mother of Perpetual Help &amp; Special Devotions.</p>
        </a>
        <a href="parish_bulletin.html" class="quick-card">
          <div class="quick-card-icon"><i class="fa-solid fa-book-bible"></i></div>
          <h3 class="quick-card-title">Parish Bulletin</h3>
          <p class="quick-card-desc">Read "Sleeva Nadham", parish notices, circulars, liturgy guides, and monthly publications.</p>
        </a>
        <a href="news.html" class="quick-card">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h3 class="quick-card-title">News &amp; Events</h3>
          <p class="quick-card-desc">Stay updated with pastoral letters, upcoming feast celebrations, and church announcements.</p>
        </a>
        <a href="useful-links.html" class="quick-card">
          <div class="quick-card-icon"><i class="fa-solid fa-compass"></i></div>
          <h3 class="quick-card-title">Useful Links</h3>
          <p class="quick-card-desc">Direct access to Vatican News, Archdiocese portals, Syro-Malabar Church resources, and prayers.</p>
        </a>
      </div>
    </div>
  </section>

  <!-- Welcome / Vicar Section (Warm Light Champagne #FFF8ED, Spacious, Airy) -->
  <section class="section bg-champagne-light">
    <div class="container">
      <div class="welcome-grid">
        <!-- Vicar Photo Card -->
        <div class="welcome-image-wrapper">
          <div class="welcome-img-card">
            <img src="images/f1.jpg" alt="Rev. Fr. James Puthenpurakkal - Vicar, Holy Cross Forane Church">
            <div class="vicar-badge">
              <h4 class="vicar-name">Rev. Fr. James Puthenpurakkal</h4>
              <p class="vicar-title">Vicar, Holy Cross Forane Church, Manjapra</p>
            </div>
          </div>
        </div>

        <!-- Welcome Text Content -->
        <div class="welcome-content">
          <div class="section-tag"><i class="fa-solid fa-cross text-gold"></i> Pastoral Welcome</div>
          <h2 class="section-title">Welcome to Holy Cross Church</h2>
          
          <div class="gold-divider" style="justify-content: flex-start; margin-left: 0;">
            <span class="cross-symbol">✝</span>
          </div>

          <div class="welcome-quote-mark"><i class="fa-solid fa-quote-left"></i></div>
          <p class="welcome-text">
            "It gives me immense joy to inaugurate a website for <strong>Holy Cross Forane Church, Manjapra</strong> in order to widen the horizon of relationships even outside the territory of parish. Among 7000 of parishioners, thousands of people are residing outside the territory of our parish for various reasons."
          </p>
          <p class="welcome-text">
            "Let this digital portal be an effective bridge that connects every family member to the spiritual warmth, ancestral heritage, prayers, and Eucharistic celebrations of our beloved Mother Parish wherever in the world you may be."
          </p>

          <div class="welcome-stats">
            <div class="stat-item">
              <div class="stat-number">1568 AD</div>
              <div class="stat-label">Year Established</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">7000+</div>
              <div class="stat-label">Parishioners</div>
            </div>
            <div class="stat-item">
              <div class="stat-number">35 Units</div>
              <div class="stat-label">Family Units</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Church Heritage Section Preview (Warm Champagne #F7E6CA, Premium Heritage Editorial Composition) -->
  <section class="section history-heritage-section" id="church-history" aria-label="Brief History of Holy Cross Church">
    <!-- Subtle Heritage Background Watermark / Architectural Accent -->
    <div class="heritage-bg-decor" aria-hidden="true">
      <div class="heritage-bg-arch"></div>
      <div class="heritage-bg-cross"></div>
    </div>

    <div class="container">
      <!-- Elegant Compact Header -->
      <div class="section-header text-center heritage-header">
        <div class="section-tag">───── &nbsp; SACRED HERITAGE &nbsp; ─────</div>
        <h2 class="section-title">Brief History of Holy Cross Church</h2>
        <div class="gold-divider">
          <span class="cross-symbol">── ✦ ──</span>
        </div>
        <p class="section-subtitle">
          Discover the profound spiritual foundation and over 450 years of Christian heritage in Manjapra.
        </p>
      </div>

      <!-- Premium Editorial Heritage Composition -->
      <div class="heritage-timeline">
        <!-- Milestone 1 -->
        <div class="heritage-timeline-row">
          <div class="heritage-timeline-card-col">
            <div class="heritage-panel">
              <div class="heritage-badge">
                <span class="badge-accent">✦</span>
                <span class="badge-year">1568 AD</span>
                <span class="badge-accent">✦</span>
              </div>
              <h3 class="heritage-panel-title">Foundation &amp; Miraculous Cross</h3>
              <p class="heritage-panel-text">
                Holy Cross Church was founded in 1568 AD. The parish was established with profound spiritual roots and the veneration of the Holy Cross, which became a beacon of faith for the faithful in the region.
              </p>
            </div>
          </div>

          <div class="heritage-timeline-center">
            <div class="heritage-node" title="1568 AD"></div>
          </div>

          <div class="heritage-timeline-media-col">
            <div class="heritage-feathered-image">
              <img src="images/holy_cross_church_manjapra.jpg" alt="Holy Cross Church Historical Foundation" loading="lazy">
            </div>
          </div>
        </div>

        <!-- Milestone 2 (Reversed Composition) -->
        <div class="heritage-timeline-row reverse">
          <div class="heritage-timeline-card-col">
            <div class="heritage-panel">
              <div class="heritage-badge">
                <span class="badge-accent">✦</span>
                <span class="badge-year"></span>
                <span class="badge-accent">✦</span>
              </div>
              <h3 class="heritage-panel-title">Devotion to Mother of Perpetual Help</h3>
              <p class="heritage-panel-text">
                Recognized as one of the prominent Marian pilgrim destinations in Kerala, drawing thousands of devotees seeking solace, healing, and spiritual intercession through our Blessed Mother.
              </p>
            </div>
          </div>

          <div class="heritage-timeline-center">
            <div class="heritage-node" title=""></div>
          </div>

          <div class="heritage-timeline-media-col">
            <div class="heritage-feathered-image">
              <img src="images/St_mary.jpg" alt="Mother of Perpetual Help Devotion" loading="lazy">
            </div>
          </div>
        </div>

        <!-- Milestone 3 -->
        <div class="heritage-timeline-row">
          <div class="heritage-timeline-card-col">
            <div class="heritage-panel">
              <div class="heritage-badge">
                <span class="badge-accent">✦</span>
                <span class="badge-year">Forane Elevation</span>
                <span class="badge-accent">✦</span>
              </div>
              <h3 class="heritage-panel-title">Vibrant Forane Parish Community</h3>
              <p class="heritage-panel-text">
                Elevated to Forane Church on 18th May 1986. Under the Major Archdiocese of Ernakulam-Angamaly, the church serves over 7000 faithful across multiple wards, institutions, convents, and chapels.
              </p>
            </div>
          </div>

          <div class="heritage-timeline-center">
            <div class="heritage-node" title="Forane Elevation"></div>
          </div>

          <div class="heritage-timeline-media-col">
            <div class="heritage-feathered-image">
              <img src="images/banner/banner-3.jpg" alt="Holy Cross Forane Church Community" loading="lazy">
            </div>
          </div>
        </div>
      </div>

      <div class="text-center" style="margin-top: 38px;">
        <a href="history.html" class="btn btn-primary"><i class="fa-solid fa-book-open"></i> Read Complete Church History</a>
      </div>
    </div>
  </section>

  <!-- Mass Schedule Overview Section (Pure White Background, Editorial Clean Layout) -->
  <section class="section bg-white">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-cross text-gold"></i> Liturgical Worship</div>
        <h2 class="section-title">Holy Mass Timings</h2>
        <div class="gold-divider">
          <span class="cross-symbol">✝</span>
        </div>
        <p class="section-subtitle">
          Join us in Eucharistic celebration and sacred novenas at Holy Cross Forane Church, Manjapra.
        </p>
      </div>

      <div class="timing-grid">
        <!-- Sunday Mass Card -->
        <div class="timing-card">
          <div class="timing-card-header">
            <h3 class="timing-card-title"><i class="fa-solid fa-sun text-gold" style="margin-right: 8px;"></i> Sunday Holy Mass</h3>
          </div>
          <div class="timing-card-body">
            <ul class="timing-list">
              <li class="timing-item">
                <span class="timing-day">First Morning Mass</span>
                <span class="timing-time">5:30 AM</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Second Morning Mass</span>
                <span class="timing-time">7:00 AM</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Solemn High Mass</span>
                <span class="timing-time">9:00 AM</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Evening Mass</span>
                <span class="timing-time">5:00 PM</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Weekday Mass Card -->
        <div class="timing-card">
          <div class="timing-card-header">
            <h3 class="timing-card-title"><i class="fa-solid fa-calendar-days text-gold" style="margin-right: 8px;"></i> Weekday Mass</h3>
          </div>
          <div class="timing-card-body">
            <ul class="timing-list">
              <li class="timing-item">
                <span class="timing-day">Weekday Morning</span>
                <span class="timing-time">5:45 AM, 7:00 AM</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Tuesday Morning</span>
                <span class="timing-time">6:45 AM (St. Sebastian Novena)</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Friday Morning</span>
                <span class="timing-time">6:45 AM (Holy Cross Novena)</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Tuesday / Friday</span>
                <span class="timing-time">6:45 AM (Novena of Our Lady)</span>
              </li>
            </ul>
          </div>
        </div>

        <!-- Novena & Devotions Card -->
        <div class="timing-card">
          <div class="timing-card-header">
            <h3 class="timing-card-title"><i class="fa-solid fa-hands-praying text-gold" style="margin-right: 8px;"></i> Novena &amp; Devotions</h3>
          </div>
          <div class="timing-card-body">
            <ul class="timing-list">
              <li class="timing-item">
                <span class="timing-day">Mother of Perpetual Help</span>
                <span class="timing-time">Friday &amp; Tuesday Novena</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Holy Cross Novena</span>
                <span class="timing-time">Every Friday Morning</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">St. Sebastian Novena</span>
                <span class="timing-time">Every Tuesday Morning</span>
              </li>
              <li class="timing-item">
                <span class="timing-day">Sacrament of Reconciliation</span>
                <span class="timing-time">Before all Holy Masses</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="text-center" style="margin-top: 40px;">
        <a href="mass-timing.html" class="btn btn-outline-gold"><i class="fa-solid fa-list-check"></i> View Full Mass Schedule</a>
      </div>
    </div>
  </section>

  <!-- News & Announcements (Warm Cream #FBF3E5, Editorial Layout) -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-newspaper text-gold"></i> Parish Updates</div>
        <h2 class="section-title">Latest News &amp; Events</h2>
        <div class="gold-divider">
          <span class="cross-symbol">✝</span>
        </div>
        <p class="section-subtitle">
          Stay connected with the latest announcements, feast celebrations, and pastoral programs.
        </p>
      </div>

      <div class="news-editorial-grid">
        <!-- Featured News Item (Large) -->
        <div class="news-card">
          <div class="news-img-wrapper" style="height: 280px;">
            <img src="images/offer/footer.jpg" alt="Feast of St. Mary Announcement">
            <span class="news-date-badge"><i class="fa-regular fa-calendar"></i> Nov 19 - 28</span>
          </div>
          <div class="news-body">
            <span style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.14em; color: var(--color-gold-muted); font-weight: 700; margin-bottom: 6px;">Featured Announcement</span>
            <h3 class="news-title">Feast of St. Mary (Mother of Perpetual Help)</h3>
            <p class="news-excerpt">
              From 19th to 28th November, Holy Cross Forane Church will solemnly celebrate the Feast of St. Mary with flag hoisting, daily Novena prayers, solemn High Mass, and festive processions.
            </p>
            <a href="annual_feast.html" class="news-link">Read Feast Details <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>

        <!-- Supporting Items -->
        <div style="display: flex; flex-direction: column; gap: 20px;">
          <div class="news-card">
            <div class="news-body" style="padding: 22px;">
              <span class="news-date-badge" style="position: static; display: inline-block; margin-bottom: 12px;"><i class="fa-regular fa-calendar"></i> Dec 24</span>
              <h4 style="font-size: 1.2rem; margin-bottom: 8px; color: var(--color-brown-dark);">Christmas Eve &amp; Tree Competition</h4>
              <p class="news-excerpt" style="font-size: 0.9rem; margin-bottom: 12px;">
                On December 24th, there will be a Christmas tree competition organized for the parish community and youth.
              </p>
              <a href="news.html" class="news-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>

          <div class="news-card">
            <div class="news-body" style="padding: 22px;">
              <span class="news-date-badge" style="position: static; display: inline-block; margin-bottom: 12px;"><i class="fa-regular fa-calendar"></i> Monthly Publication</span>
              <h4 style="font-size: 1.2rem; margin-bottom: 8px; color: var(--color-brown-dark);">Parish Bulletin "Sleeva Nadham"</h4>
              <p class="news-excerpt" style="font-size: 0.9rem; margin-bottom: 12px;">
                Download the monthly edition containing Vicar's reflections, liturgy schedule, and family unit news.
              </p>
              <a href="parish_bulletin.html" class="news-link">Download Bulletin <i class="fa-solid fa-arrow-right"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Photo Gallery Section (Warm Light / Photographic Asymmetric Layout) -->
  <section class="section bg-champagne-light">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-images text-gold"></i> Visual Archive</div>
        <h2 class="section-title">Parish Photo Gallery</h2>
        <div class="gold-divider">
          <span class="cross-symbol">✝</span>
        </div>
        <p class="section-subtitle">
          Photographic journey capturing the architectural grandeur, liturgical celebrations, and chapels of Manjapra.
        </p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-item" data-category="church">
          <img src="images/banner-1.jpg" alt="Holy Cross Forane Church Front Elevation">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Holy Cross Church Façade</h4>
          </div>
        </div>
        <div class="gallery-item" data-category="church">
          <img src="images/banner-2.jpg" alt="Church Interior Sanctuary">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Sacred Sanctuary &amp; Altar</h4>
          </div>
        </div>
        <div class="gallery-item" data-category="chapels">
          <img src="images/holy/Mariyapuram Chapel.jpg" alt="Mariyapuram Chapel">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Mariyapuram Chapel</h4>
          </div>
        </div>
        <div class="gallery-item" data-category="chapels">
          <img src="images/holy/Sanjopuram Chapel.jpeg" alt="Sanjopuram Chapel">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Sanjopuram Chapel</h4>
          </div>
        </div>
      </div>

      <div class="text-center" style="margin-top: 36px;">
        <a href="gallery.html" class="btn btn-outline-gold"><i class="fa-solid fa-photo-film"></i> View Full Gallery</a>
      </div>
    </div>
  </section>

  <!-- Interactive Lightbox Modal -->
  <div class="lightbox-modal" aria-hidden="true">
    <button class="lightbox-close" aria-label="Close lightbox">&times;</button>
    <button class="lightbox-nav lightbox-prev" aria-label="Previous image"><i class="fa-solid fa-chevron-left"></i></button>
    <img src="" alt="Gallery Preview" class="lightbox-img">
    <button class="lightbox-nav lightbox-next" aria-label="Next image"><i class="fa-solid fa-chevron-right"></i></button>
  </div>

  <!-- Prayer Request & Contact Section (Light Champagne #F7E6CA, Welcoming White Cards) -->
  <section class="section bg-champagne">
    <div class="container">
      <div class="welcome-grid">
        <!-- Prayer Form Card -->
        <div class="form-card">
          <div class="section-tag"><i class="fa-solid fa-dove text-gold"></i> Intercession</div>
          <h3 style="font-size: 1.9rem; color: var(--color-brown-dark); margin-bottom: 10px;">Submit Prayer Request</h3>
          <p style="color: var(--color-text-muted); font-size: 0.94rem; margin-bottom: 24px; line-height: 1.6;">
            Place your prayer intentions at the feet of the Holy Cross. Our parish community will remember your intentions during the Holy Mass.
          </p>

          <form id="prayer-form" class="ajax-form">
            <div class="form-group">
              <label class="form-label" for="pr-name">Your Full Name *</label>
              <input type="text" id="pr-name" class="form-control" placeholder="Enter your name" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="pr-email">Email Address / Phone Number *</label>
              <input type="text" id="pr-email" class="form-control" placeholder="Enter your contact email or phone" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="pr-intent">Prayer Intention *</label>
              <textarea id="pr-intent" class="form-control" placeholder="Type your prayer request or thanksgiving intention here..." required></textarea>
            </div>
            <button type="submit" class="btn btn-primary" style="width: 100%;"><i class="fa-solid fa-paper-plane"></i> Submit Prayer Intention</button>
          </form>
        </div>

        <!-- Contact Info Box -->
        <div class="contact-info-card">
          <div class="section-tag"><i class="fa-solid fa-church text-gold"></i> Parish Office</div>
          <h3 style="font-size: 1.9rem; color: var(--color-brown-dark); margin-bottom: 10px;">Get in Touch</h3>
          <p style="color: var(--color-text-muted); font-size: 0.94rem; line-height: 1.6;">
            For mass bookings, certificates, family unit queries, or pastoral assistance, contact the parish administration office.
          </p>

          <div class="contact-info-list">
            <div class="contact-info-item">
              <div class="contact-info-icon"><i class="fa-solid fa-location-dot"></i></div>
              <div class="contact-info-text">
                <h4>Address</h4>
                <p>Holy Cross Forane Church, Manjapra P.O., Ernakulam Dist., Kerala, PIN: 683581</p>
              </div>
            </div>

            <div class="contact-info-item">
              <div class="contact-info-icon"><i class="fa-solid fa-phone"></i></div>
              <div class="contact-info-text">
                <h4>Telephone</h4>
                <p><a href="tel:+914842692225">0484 2692225</a> / <a href="tel:+919495072573">+91 9495072573</a></p>
              </div>
            </div>

            <div class="contact-info-item">
              <div class="contact-info-icon"><i class="fa-solid fa-envelope"></i></div>
              <div class="contact-info-text">
                <h4>Email</h4>
                <p><a href="mailto:churchmanjapra@gmail.com">churchmanjapra@gmail.com</a></p>
              </div>
            </div>

            <div class="contact-info-item">
              <div class="contact-info-icon"><i class="fa-solid fa-clock"></i></div>
              <div class="contact-info-text">
                <h4>Office Timings</h4>
                <p>Monday - Saturday: 9:00 AM - 1:00 PM, 2:00 PM - 5:00 PM<br>Sunday: Closed for afternoon</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    render_html_page("index.html", "Holy Cross Forane Church | Manjapra", "home", body)

# ==========================================
# 2. HISTORY.HTML
# ==========================================
def build_history():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Heritage &amp; Spiritual Roots</span>
      <h1 class="page-hero-title">Church History</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>History</span>
      </div>
    </div>
  </section>

  <!-- Main History Section (Light Champagne #FFF8ED) -->
  <section class="section bg-champagne-light history-page-section">
    <div class="container history-container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-landmark text-gold"></i> ചരിത്ര താളിലൂടെ</div>
        <h2 class="section-title">മഞ്ഞപ്ര ഫൊറോനപള്ളി ചരിത്രം</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Over 450 years of Christian heritage, devotion, and spiritual illumination in the land of Manjapra.
        </p>
      </div>

      <!-- Sacred Quote -->
      <div class="history-quote-box" style="background: var(--color-white); color: var(--color-brown-dark); padding: 26px 32px; border-radius: var(--radius-sm); border-left: 4px solid var(--color-gold); margin-bottom: 40px; box-shadow: var(--shadow-subtle);">
        <p class="history-quote-text" style="font-family: var(--font-serif-sub); font-style: italic; font-size: 1.2rem; line-height: 1.7; margin: 0; color: var(--color-brown-dark);">
          <i class="fa-solid fa-quote-left" style="color: var(--color-gold); margin-right: 8px;"></i>
          "ആദിയിൽ വചനമുണ്ടായിരുന്നു; വചനം ദൈവത്തോടുകൂടെയായിരുന്നു; വചനം ദൈവമായിരുന്നു"
        </p>
      </div>

      <!-- Historical Narratives -->
      <div class="history-narrative-block" style="font-size: 1.08rem; line-height: 1.95; color: var(--color-brown-dark); margin-bottom: 40px;">
        <p style="margin-bottom: 24px;">
          ഭാരതീയ ക്രൈസ്തവരുടെ പിള്ളത്തൊട്ടിലായ കേരളത്തിലെ ക്രൈസ്തവ അധിവാസ കേന്ദ്രങ്ങളിൽ പ്രഥമ സ്ഥാനം അലങ്കരിക്കുന്ന ഇടമാണ് മഞ്ഞപ്ര. തോമാശ്ലീഹായുടെ പാദസ്പർശത്താൽ പ്രസിദ്ധമായ മലയാറ്റൂരിനും, ആദിശങ്കരൻ്റെ ജന്മദേശമെന്ന പ്രസിദ്ധി നേടിയ കാലടിക്കും, അങ്കമാലിക്കും അടുത്തായി പ്രകൃതിരമണീയമായി നിലകൊള്ളുന്ന മഞ്ഞപ്രയിലാണ് മാർ ശ്ലീവാ ഫെറോന പള്ളി സ്ഥിതി ചെയ്യുന്നത്.
        </p>
        <p style="margin-bottom: 24px;">
          മഞ്ഞപ്ര പള്ളി സ്ഥിതി ചെയ്യുന്ന സ്ഥലം മഞ്ഞപ്പാറ എന്നാണ് അറിയപ്പെട്ടിരുന്നത്. കാലക്രമേണ അത് ലോപിച്ച് മഞ്ഞപ്രയായി രൂപം പ്രാപിച്ചുവെന്ന് ഐതീഹ്യമുണ്ട്. പതിനാലാം നൂറ്റാണ്ട് വരെ മഞ്ഞപ്രയിൽ ഒരു പള്ളിയുണ്ടായിരുന്നതായി രേഖകളൊന്നുമില്ല. ഇവിടത്തെ ക്രിസ്ത്യാനികൾ ആ കാലഘട്ടത്തിൽ ആത്മീയ ആവശ്യങ്ങൾക്കായി അങ്കമാലി പള്ളിയെയാണ് സമീപിച്ചിരുന്നത്. മാമ്മോദീസ, ശവസംസ്ക്കാരം തുടങ്ങിയ കൂദാശകൾക്കായി അങ്കമാലി പള്ളിയെ ആശ്രയിക്കുന്നതിൽ അനുഭവപ്പെട്ട ദൂരവും മറ്റു ബുദ്ധിമുട്ടുകളും മഞ്ഞപ്രയിൽ ഒരു ദേവാലയം പണികഴിപ്പിക്കുന്നതിനുള്ള ജനങ്ങളുടെ ആഗ്രഹത്തെ ഉന്മേഷപ്പെടുത്തി.
        </p>
      </div>

      <!-- Church Historic Photo -->
      <div class="history-photo-frame" style="margin: 40px 0; border-radius: var(--radius-sm); overflow: hidden; box-shadow: var(--shadow-card); border: 2px solid var(--color-gold);">
        <img src="images/holy_cross_church_manjapra.jpg" alt="Holy Cross Forane Church Manjapra Heritage" style="width: 100%; height: auto;">
      </div>

      <div class="history-narrative-block" style="font-size: 1.08rem; line-height: 1.95; color: var(--color-brown-dark); margin-bottom: 40px;">
        <p style="margin-bottom: 24px;">
          ക്രിസ്ത്യാനികൾ തുടർച്ചയായി സർക്കാരിന് നിവേദനം സമർപ്പിച്ചതിൻ്റെ ഫലമായി ഇന്ന് കർമ്മലീത്താമഠം സ്ഥിതി ചെയ്യുന്ന സ്ഥലത്ത് പള്ളി പണിയുവാൻ പറവൂർ തമ്പുരാൻ അമ്പത്തിയാറു സെൻറ് സ്ഥലവും, വിളക്ക് വെയ്പ്പിനായി കീർപ്പാടത്ത് കുട്ടാടൻ പടവത്തിലും കരം ഒഴിവാക്കി നൽകിയത്. കൂടാതെ പള്ളി പണിയുന്നതിനാവശ്യമായ സൗകര്യങ്ങളൊക്കെയും തമ്പുരാൻ ചെയ്തു കൊടുത്തു. അങ്ങനെ അനുവദിച്ച സ്ഥലത്ത് (ഇന്ന് പള്ളിയിരിക്കുന്ന സ്ഥലം) <strong>1401</strong> ൽ ആദ്യമായി ഒരു കത്തോലിക്കാ ദേവാലയം രൂപപ്പെട്ടു. മഞ്ഞപ്ര പള്ളിയുടെ മുഖഭാഗത്തായി 1401 എന്ന് രേഖപ്പെടുത്തിയിരിക്കുന്നത് കാണാം.
        </p>
        <p style="margin-bottom: 24px;">
          പറവൂർ സ്വരൂപത്തിൽ നിന്നു തന്നെ പള്ളിക്ക് ചുറ്റുമുള്ള സ്ഥലങ്ങൾ അങ്ങാടിയാക്കുന്നതിനായി ക്രിസ്ത്യാനികൾക്ക് കരം ഒഴിവാക്കി കൊടുത്തു. രാജകീയ അനുവാദങ്ങൾ ഉൾക്കൊള്ളുന്ന ഈ ചെപ്പേട് പള്ളിയിൽ സൂക്ഷിച്ചിരുന്നു. പിൽക്കാലത്ത് സർവേ തെളിവിനായി ഹാജരാക്കുകയും പിന്നീട് എങ്ങനെയോ നഷ്ടപ്പെടുകയും ചെയ്തു.
        </p>
        <p style="margin-bottom: 24px;">
          പള്ളിയുടെ ആരംഭകാലത്ത് മഞ്ഞപ്രയിൽ ആകെ <strong>45 ക്രിസ്തീയ കുടുംബങ്ങളെ</strong> ഉണ്ടായിരിന്നുള്ളു എന്നാണ് പറയപ്പെടുന്നത്. <strong>1865 ൽ</strong> മഞ്ഞപ്രപള്ളി പുതുക്കി പണിതു. അതോടൊപ്പം തന്നെ പള്ളിമേടയും, ചുറ്റുമതിലും, സെമിത്തേരിയും, കുരിശുകളും പണികഴിപ്പിച്ചു. ഇന്ന് കാണുന്ന പള്ളിമുറി <strong>1912ൽ</strong> വികാരിയായിരുന്ന ബഹു. തരിയാക്ക് അച്ചൻ (അങ്കമാലി) ചെയ്യിപ്പിച്ചതാണ്.
        </p>
        <p style="margin-bottom: 24px;">
          ഇടവകക്കാരുടെ എണ്ണം വർദ്ധിച്ചതോടെ പള്ളിയിൽ സ്ഥലം തികയാതെയായി. <strong>1940 ൽ</strong> ഫാ.ജോസഫ് പൈനാടത്ത് മദ്ബഹായുടെയും തെക്ക് വശത്തുള്ള എടപ്പുകളുടെയും പണി ആരംഭിച്ചു. <strong>1946ൽ</strong> ബഹു. കുരിയാക്കോസച്ചൻ ഇടവകയുടെ പണി പൂർത്തിയാക്കി.
        </p>
        <p style="margin-bottom: 24px;">
          മഞ്ഞപ്ര ഇടവകയിൽ നിന്നും പല ഇടവകകളായി പിരിഞ്ഞു പോയിട്ടുണ്ട്. കൊമറ്റം പള്ളി 1799 ലും, നടുവട്ടം പള്ളി 1939 ലും, ആനപ്പാറ പള്ളി 1950 ലും പ്രത്യേക ഇടവകകളായി തിരിഞ്ഞു. അമലാപ്പുരം സെൻ്റ്.ജോസഫ് പള്ളിയും (1959), തട്ടുപാറ സെൻ്റ്.തോമസ് പള്ളിയും (1925), മേരിഗിരി സെൻ്റ്.സെബാസ്റ്റിൻ പള്ളിയും (1960), ആനപ്പാറ അവർ ലേഡീസ് പള്ളിയും (1964), ചുള്ളി സെൻ്റ്.സെബാസ്റ്റിൻ പള്ളിയും (1970) മഞ്ഞപ്രയുടെ കുരിശുപള്ളികളായിരുന്നു.
        </p>
        <p style="margin-bottom: 24px;">
          <strong>1986 മെയ് 18-ാം തിയതി</strong> മഞ്ഞപ്ര മാർ ശ്ലീവാ പള്ളി <strong>ഫെറോനയായി ഉയർത്തപ്പെട്ടു</strong>. അമലാപുരം, അയ്യമ്പുഴ, കൊല്ലക്കോട്, 6-ാം ബ്ലോക്ക്, വെറ്റിലപ്പാറ, പൂപ്പാറ, കണിമംഗലം, 10-ാം ബ്ലോക്ക്, നടുവട്ടം, മാണിക്യമംഗലം, യോദ്ദനാർപുരം, വാതക്കാട്, തവളപ്പാറ, ആനപ്പാറ, മേരിഗിരി, ചുള്ളി, കുറ്റിപ്പാറ, തട്ടുപ്പാറ, സെബിപുരം പള്ളികൾ മഞ്ഞപ്ര ഫെറോനയുടെ കീഴിലാവുകയുണ്ടായി.
        </p>
        <p style="margin-bottom: 24px;">
          ബഹു.ജോസഫ് നെറ്റിക്കിടനച്ചൻ വികാരിയായിരുന്നപ്പോൾ (1987-1991) പാരീഷ് ഹാളിൻ്റെ പണി പൂർത്തിയാക്കി. 1991 ജനുവരി 12-ാം തീയതി അഭിവന്ദ്യ കർദ്ദിനാൾ മാർ ആൻറണി പടിയറ പാരീഷ് ഹാൾ വെഞ്ചരിച്ചു. ബഹു.ജോസഫ് ഭരണികുളങ്ങര അച്ചൻ്റെ കാലത്ത് (1991-1999) സെമിത്തേരി കല്ലറ നിർമ്മാണം ഒന്നാം ഘട്ടം പൂർത്തിയാക്കി.
        </p>
        <p style="margin-bottom: 24px;">
          1999 ഫെബ്രുവരി 6-ാം തിയതി ബഹു.പോൾ എസ്.പയ്യപ്പള്ളി അച്ചൻ വികാരിയായി ചുമതലയേറ്റു. തുടർന്ന് വികസനങ്ങളുടെ കാലഘട്ടമായിരുന്നു. മഞ്ഞപ്ര ഫെറോനാ പള്ളിയുടെ പഴമയെ നിലനിർത്തിക്കൊണ്ടു തന്നെ പള്ളിയുടെ പുനരുദ്ധാരണം അതി മനോഹരമായി നടത്തി. വികാരിയച്ചൻ്റെയും സഹവികാരിമാരായ ജോയ് പ്ലാക്കലച്ചൻ്റെയും, പോൾ കോട്ടയ്ക്കലച്ചൻ്റെയും കെ.ജെ.ബേബി കോളാട്ടുകുടി കൺവീനറായ പുനരുദ്ധാരണ കമ്മറ്റിയുടെയും നേതൃത്വത്തിൽ പണി പൂർത്തിയാക്കി. 2001 ജനുവരി 21-ാം തിയതി മേജർ ആർച്ച് ബിഷപ്പ് മാർ വർക്കി വിധേയത്തിൽ ആശീർവ്വാദകർമ്മം നിർവ്വഹിച്ചു. ഇതേ തുടർന്ന് സെമിത്തേരി കല്ലറയുടെ രണ്ടാം ഘട്ടം പൂർത്തിയാക്കി. കപ്പേളയും മനോഹരമാക്കി. 2001 നവംബർ 2 ന് കല്ലറകളും പുതിയ കപ്പേളയും വികാരിയച്ചൻ ആശീർവ്വദിച്ചു.
        </p>
      </div>

      <!-- Bottom Navigation Links -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 50px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">View regular and feast day service hours</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Stay informed with parish announcements</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Thank God</h4>
          <p class="quick-card-desc">Every moment, give thanks to the Lord</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("history.html", "Church History | Holy Cross Forane Church Manjapra", "history", body)

# ==========================================
# 3. ANNUAL_FEAST.HTML
# ==========================================
def build_annual_feast():
    body = """
  <!-- Page Banner (Matching Reference Design) -->
  <section class="feast-hero-banner">
    <div class="feast-hero-banner-overlay"></div>
    <div class="container feast-hero-content">
      <div class="feast-hero-eyebrow">† Liturgical Celebrations</div>
      <h1 class="feast-hero-title">Annual Feasts</h1>
      <div class="feast-hero-breadcrumbs">
        <a href="index.html">Home</a>
        <span class="bc-sep">›</span>
        <a href="history.html">About</a>
        <span class="bc-sep">›</span>
        <span>Annual Feasts</span>
      </div>
    </div>
  </section>

  <!-- Main Body Content: Exact Heritage Reference Design -->
  <main class="annual-feast-page-body">
    <!-- Subtle Background Line Art Watermarks -->
    <div class="feast-bg-decor" aria-hidden="true">
      <div class="feast-bg-decor-left"></div>
      <div class="feast-bg-decor-right"></div>
    </div>

    <div class="container" style="position: relative; z-index: 1;">
      
      <!-- Section 1: Introduction -->
      <div class="feast-intro-box">
        <div class="feast-church-ornament">
          <span class="ornament-line"></span>
          <i class="fa-solid fa-church"></i>
          <span class="ornament-line"></span>
        </div>
        <span class="feast-intro-eyebrow">Parish Thirunal Celebrations</span>
        <h2 class="feast-intro-title">Annual Feasts &amp; Festivities</h2>
        <div class="feast-intro-cross-divider">
          <i class="fa-solid fa-cross"></i>
        </div>
        <p class="feast-intro-desc">
          Experience the sacred traditions, solemn liturgies, and spiritual jubilation of our major annual parish feasts.
        </p>
      </div>

      <!-- Section 2: Three Cathedral-Arched Heritage Cards -->
      <div class="feast-cards-grid">
        
        <!-- Card 1: Feast Of Holy Cross -->
        <article class="feast-heritage-card">
          <div class="feast-arch-frame">
            <div class="feast-arch-inner">
              <img src="images/cross1.jpg" alt="Feast Of Holy Cross, Manjapra" class="feast-arch-img" loading="lazy">
            </div>
          </div>
          <div class="feast-badge-icon">
            <i class="fa-solid fa-cross"></i>
          </div>
          <span class="feast-card-category">Main Parish Feast</span>
          <h3 class="feast-card-title">Feast Of Holy Cross</h3>
          <div class="card-cross-divider">
            <span class="cross-line"></span>
            <span class="cross-char">†</span>
            <span class="cross-line"></span>
          </div>
          <p class="feast-card-desc">
            The principal feast of the Exaltation of the Holy Cross (Kurisumala Thirunal), commemorating the triumphant cross of Christ with solemn Qurbana, flag hoisting (Kodyiettam), and spiritual processions.
          </p>
          <div class="card-bottom-ornament">
            <span class="ornament-line"></span>
            <span class="ornament-star">❖</span>
            <span class="ornament-line"></span>
          </div>
        </article>

        <!-- Card 2: Feast Of Our Lady of Mount Carmel -->
        <article class="feast-heritage-card">
          <div class="feast-arch-frame">
            <div class="feast-arch-inner">
              <img src="images/St_mary.jpg" alt="Feast Of Our Lady of Mount Carmel" class="feast-arch-img" loading="lazy">
            </div>
          </div>
          <div class="feast-badge-icon">
            <i class="fa-solid fa-crown"></i>
          </div>
          <span class="feast-card-category">Marian Devotion</span>
          <h3 class="feast-card-title">Feast Of Our Lady of Mount Carmel</h3>
          <div class="card-cross-divider">
            <span class="cross-line"></span>
            <span class="cross-char">†</span>
            <span class="cross-line"></span>
          </div>
          <p class="feast-card-desc">
            Celebration honoring our Blessed Mother Mary under the title of Our Lady of Mount Carmel, invoking her motherly protection, intercession, and heavenly grace for all families.
          </p>
          <div class="card-bottom-ornament">
            <span class="ornament-line"></span>
            <span class="ornament-star">❖</span>
            <span class="ornament-line"></span>
          </div>
        </article>

        <!-- Card 3: Feast Of St. Sebastian -->
        <article class="feast-heritage-card">
          <div class="feast-arch-frame">
            <div class="feast-arch-inner">
              <img src="images/St_sebastian.jpg" alt="Feast Of St. Sebastian" class="feast-arch-img" loading="lazy">
            </div>
          </div>
          <div class="feast-badge-icon">
            <i class="fa-solid fa-cross"></i>
          </div>
          <span class="feast-card-category">Saint Patron Feast</span>
          <h3 class="feast-card-title">Feast Of St. Sebastian</h3>
          <div class="card-cross-divider">
            <span class="cross-line"></span>
            <span class="cross-char">†</span>
            <span class="cross-line"></span>
          </div>
          <p class="feast-card-desc">
            Solemn annual feast of the valiant martyr St. Sebastian, celebrated with great devotion, arrow veneration (Ambu Pradakshinam), and traditional community prayers.
          </p>
          <div class="card-bottom-ornament">
            <span class="ornament-line"></span>
            <span class="ornament-star">❖</span>
            <span class="ornament-line"></span>
          </div>
        </article>

      </div>

      <!-- Section 3: Premium Quick Access Feature Panel -->
      <div class="feast-quick-panel-container">
        <div class="feast-quick-panel">
          <!-- Corner Flourishes -->
          <div class="corner-flourish tl" aria-hidden="true"></div>
          <div class="corner-flourish tr" aria-hidden="true"></div>
          <div class="corner-flourish bl" aria-hidden="true"></div>
          <div class="corner-flourish br" aria-hidden="true"></div>

          <!-- Item 1: Holy Mass Timings -->
          <a href="mass-timing.html" class="quick-panel-item">
            <div class="quick-panel-icon-circle">
              <i class="fa-regular fa-clock"></i>
            </div>
            <h4 class="quick-panel-title">Holy Mass Timings</h4>
            <p class="quick-panel-desc">Check liturgy timings for feast days</p>
            <span class="quick-panel-arrow"><i class="fa-solid fa-arrow-right-long"></i></span>
          </a>

          <!-- Item 2: Parish News -->
          <a href="news.html" class="quick-panel-item">
            <div class="quick-panel-icon-circle">
              <i class="fa-regular fa-newspaper"></i>
            </div>
            <h4 class="quick-panel-title">Parish News</h4>
            <p class="quick-panel-desc">Feast circulars and event schedules</p>
            <span class="quick-panel-arrow"><i class="fa-solid fa-arrow-right-long"></i></span>
          </a>

          <!-- Item 3: Every Moment, Thank God -->
          <a href="contact.html" class="quick-panel-item">
            <div class="quick-panel-icon-circle">
              <i class="fa-solid fa-hands-praying"></i>
            </div>
            <h4 class="quick-panel-title">Every Moment, Thank God</h4>
            <p class="quick-panel-desc">Offer your thanksgiving and prayers</p>
            <span class="quick-panel-arrow"><i class="fa-solid fa-arrow-right-long"></i></span>
          </a>
        </div>
      </div>

    </div>
  </main>
"""
    render_html_page("annual_feast.html", "Annual Feasts | Holy Cross Forane Church Manjapra", "feast", body)

# ==========================================
# 4. INSTITUTIONS.HTML
# ==========================================
def build_institutions():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Education &amp; Service</span>
      <h1 class="page-hero-title">Institutions</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Institutions</span>
      </div>
    </div>
  </section>

  <!-- Institutions Grid Section (Warm Cream #FBF3E5) -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-school text-gold"></i> Educational Apostolate</div>
        <h2 class="section-title">Parish Educational Institutions</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Nurturing generations with excellence in academics, moral values, and social commitment in Manjapra.
        </p>
      </div>

      <div class="cards-grid">
        <!-- Institution 1 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/institutions-1.jpg" alt="St. Mary's U.P. School, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Upper Primary Education</span>
            <h3 class="profile-name">St. Mary's U.P. School</h3>
            <p class="profile-desc">
              Providing holistic and value-based education for the children of Manjapra and neighboring areas with outstanding academic and co-curricular achievements.
            </p>
          </div>
        </div>

        <!-- Institution 2 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/institutions-3.jpg" alt="St. Rocky's L.P. School, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Lower Primary Education</span>
            <h3 class="profile-name">St. Rocky's L.P. School</h3>
            <p class="profile-desc">
              A foundational center of learning dedicated to nurturing young minds with caring educators and enriching learning environments.
            </p>
          </div>
        </div>

        <!-- Institution 3 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/institutions-2.jpg" alt="St. Mary's L.P. School, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Lower Primary Education</span>
            <h3 class="profile-name">St. Mary's L.P. School</h3>
            <p class="profile-desc">
              Established with the vision of educational illumination, providing primary education along with an affiliated nursery school.
            </p>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Join in prayer for our students &amp; teachers</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Academic updates &amp; school events</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Gratitude for the gift of education</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("institutions.html", "Institutions | Holy Cross Forane Church Manjapra", "institutions", body)

# ==========================================
# 5. ADMINISTRATION.HTML
# ==========================================
def build_administration():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Church Leadership</span>
      <h1 class="page-hero-title">Administration</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Administration</span>
      </div>
    </div>
  </section>

  <!-- Hierarchy Section (Warm Champagne #F7E6CA) -->
  <section class="section bg-champagne">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-users-gear text-gold"></i> Ecclesiastical Leadership</div>
        <h2 class="section-title">Parish &amp; Diocesan Hierarchy</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Under the pastoral guidance of the Universal Catholic Church and the Major Archdiocese of Ernakulam-Angamaly.
        </p>
      </div>

      <!-- Universal Church & Archdiocese -->
      <div class="cards-grid" style="margin-bottom: 40px;">
        <!-- Pope -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/leo.jpg" alt="Pope - Holy See" onerror="this.src='images/pope.jpg'">
          </div>
          <div class="profile-body">
            <span class="profile-role">Supreme Pontiff</span>
            <h3 class="profile-name">Pope Francis</h3>
            <p class="profile-desc">Bishop of Rome and the leader of the worldwide Catholic Church.</p>
          </div>
        </div>

        <!-- Cardinal Raphael Thattil -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/cardinal-raphael.jpg" alt="Cardinal Raphael Thattil">
          </div>
          <div class="profile-body">
            <span class="profile-role">Major Archbishop</span>
            <h3 class="profile-name">Mar Raphael Thattil</h3>
            <p class="profile-desc">Major Archbishop of Ernakulam-Angamaly &amp; Head of the Syro-Malabar Church.</p>
          </div>
        </div>

        <!-- Bishop Bosco Puthur -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/bosco-puthur.jpg" alt="Mar Bosco Puthur">
          </div>
          <div class="profile-body">
            <span class="profile-role">Apostolic Administrator</span>
            <h3 class="profile-name">Mar Bosco Puthur</h3>
            <p class="profile-desc">Apostolic Administrator, Major Archdiocese of Ernakulam-Angamaly.</p>
          </div>
        </div>
      </div>

      <!-- Parish Clergy & Trustees -->
      <div class="section-header text-center" style="margin-top: 60px; margin-bottom: 36px;">
        <div class="section-tag"><i class="fa-solid fa-church text-gold"></i> Parish Administration</div>
        <h3 style="font-size: 2.2rem; color: var(--color-brown-dark);">Parish Clergy &amp; Trustees (കൈക്കാരന്മാർ)</h3>
      </div>

      <div class="cards-grid-4">
        <!-- Vicar -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/f1.jpg" alt="Fr. Varghese Pottackal - Parish Vicar">
          </div>
          <div class="profile-body">
            <span class="profile-role">Parish Vicar</span>
            <h4 class="profile-name">Fr. Varghese Pottackal</h4>
            <p class="profile-desc">Vicar, Holy Cross Forane Church, Manjapra</p>
          </div>
        </div>

        <!-- Assistant Vicar -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/f2.jpg" alt="Fr. Jins Njanakkal - Saha Vicar">
          </div>
          <div class="profile-body">
            <span class="profile-role">Saha Vicar</span>
            <h4 class="profile-name">Fr. Jins Njanakkal</h4>
            <p class="profile-desc">Assistant Vicar, Holy Cross Forane Church</p>
          </div>
        </div>

        <!-- Trustee 1 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/thomas.jpg" alt="Thomas M P - Kaikkaran">
          </div>
          <div class="profile-body">
            <span class="profile-role">കൈക്കാരൻ (Trustee)</span>
            <h4 class="profile-name">Thomas M P</h4>
            <p class="profile-desc">Parish Managing Committee Trustee</p>
          </div>
        </div>

        <!-- Trustee 2 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/roy.jpg" alt="Roy Thottakkara - Kaikkaran">
          </div>
          <div class="profile-body">
            <span class="profile-role">കൈക്കാരൻ (Trustee)</span>
            <h4 class="profile-name">Roy Thottakkara</h4>
            <p class="profile-desc">Parish Managing Committee Trustee</p>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">View regular and feast day service hours</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Parish council notices &amp; circulars</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Parish pastoral &amp; office contact</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("administration.html", "Administration | Holy Cross Forane Church Manjapra", "administration", body)

# ==========================================
# 6. MASS-TIMING.HTML
# ==========================================
def build_mass_timing():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Eucharistic Worship</span>
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

  <!-- Mass Schedule Section (Pure White Background #FFFFFF) -->
  <section class="section bg-white">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-clock text-gold"></i> Holy Mass &amp; Novenas</div>
        <h2 class="section-title">Complete Liturgical Schedule</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Celebrate the Holy Eucharist and join in sacred novenas at Holy Cross Forane Church, Manjapra.
        </p>
      </div>

      <!-- Structured Timing Table -->
      <div class="mass-table-wrapper">
        <table class="mass-table">
          <thead>
            <tr>
              <th style="width: 28%;"><i class="fa-solid fa-calendar-day text-gold" style="margin-right: 8px;"></i> Day</th>
              <th style="width: 32%;"><i class="fa-solid fa-clock text-gold" style="margin-right: 8px;"></i> Time</th>
              <th style="width: 40%;"><i class="fa-solid fa-hands-praying text-gold" style="margin-right: 8px;"></i> Prayers &amp; Devotions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Sunday Morning</strong></td>
              <td><span class="badge-time">5.30 AM, 7.00 AM, 9.00 AM</span></td>
              <td><strong>HOLY MASS</strong> (Solemn Sunday Eucharistic Celebrations)</td>
            </tr>
            <tr>
              <td><strong>Sunday Evening</strong></td>
              <td><span class="badge-time">5.00 PM</span></td>
              <td><strong>HOLY MASS</strong> (Evening Holy Qurbana)</td>
            </tr>
            <tr>
              <td><strong>Weekdays Morning</strong></td>
              <td><span class="badge-time">5.45 AM, 7.00 AM</span></td>
              <td><strong>HOLY MASS</strong> (Daily Morning Masses)</td>
            </tr>
            <tr>
              <td><strong>Tuesdays Morning</strong></td>
              <td><span class="badge-time">6.45 AM</span></td>
              <td><strong>Novena of St. Sebastian</strong> and Holy Mass</td>
            </tr>
            <tr>
              <td><strong>Fridays Morning</strong></td>
              <td><span class="badge-time">6.45 AM</span></td>
              <td><strong>Novena of Holy Cross</strong> and Holy Mass</td>
            </tr>
            <tr>
              <td><strong>Tuesdays / Fridays</strong></td>
              <td><span class="badge-time">6.45 AM</span></td>
              <td><strong>Novena of Our Lady</strong> and Holy Mass</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Quick Cards Grid -->
      <div class="timing-grid" style="margin-top: 40px;">
        <div class="timing-card">
          <div class="timing-card-header">
            <h3 class="timing-card-title"><i class="fa-solid fa-sun text-gold" style="margin-right: 8px;"></i> Sunday Masses</h3>
          </div>
          <div class="timing-card-body">
            <ul class="timing-list">
              <li class="timing-item"><span>5:30 AM</span><strong>First Morning Mass</strong></li>
              <li class="timing-item"><span>7:00 AM</span><strong>Second Morning Mass</strong></li>
              <li class="timing-item"><span>9:00 AM</span><strong>Solemn High Mass</strong></li>
              <li class="timing-item"><span>5:00 PM</span><strong>Sunday Evening Mass</strong></li>
            </ul>
          </div>
        </div>

        <div class="timing-card">
          <div class="timing-card-header">
            <h3 class="timing-card-title"><i class="fa-solid fa-calendar-days text-gold" style="margin-right: 8px;"></i> Weekday Masses</h3>
          </div>
          <div class="timing-card-body">
            <ul class="timing-list">
              <li class="timing-item"><span>5:45 AM &amp; 7:00 AM</span><strong>Daily Morning Mass</strong></li>
              <li class="timing-item"><span>6:45 AM (Tue)</span><strong>St. Sebastian Novena</strong></li>
              <li class="timing-item"><span>6:45 AM (Fri)</span><strong>Holy Cross Novena</strong></li>
              <li class="timing-item"><span>6:45 AM (Tue)</span><strong>Novena of Our Lady</strong></li>
            </ul>
          </div>
        </div>

        <div class="timing-card">
          <div class="timing-card-header">
            <h3 class="timing-card-title"><i class="fa-solid fa-dove text-gold" style="margin-right: 8px;"></i> Sacraments &amp; Adoration</h3>
          </div>
          <div class="timing-card-body">
            <ul class="timing-list">
              <li class="timing-item"><span>Reconciliation</span><strong>Before all Holy Masses</strong></li>
              <li class="timing-item"><span>First Friday</span><strong>Solemn Eucharistic Adoration</strong></li>
              <li class="timing-item"><span>Baptism &amp; Weddings</span><strong>By appointment with Vicar</strong></li>
              <li class="timing-item"><span>House Blessings</span><strong>Through Family Unit Ward</strong></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Bottom Actions -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
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
  </section>
"""
    render_html_page("mass-timing.html", "Mass Timings | Holy Cross Forane Church Manjapra", "mass-timing", body)

# ==========================================
# 7. MINISTRIES.HTML
# ==========================================
def build_ministries():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Parish Apostolate</span>
      <h1 class="page-hero-title">Ministries &amp; Organizations</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Ministries</span>
      </div>
    </div>
  </section>

  <!-- Ministries Grid Section (Warm Cream #FBF3E5) -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-hands-holding-child text-gold"></i> Community Ministries</div>
        <h2 class="section-title">Parish Ministries &amp; Associations</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Active organizations dedicated to charitable outreach, youth empowerment, liturgical service, and spiritual enrichment.
        </p>
      </div>

      <div class="cards-grid">
        <!-- Ministry 1 -->
        <div class="profile-card">
          <div class="profile-body" style="padding: 36px 24px;">
            <div class="quick-card-icon" style="margin: 0 auto 20px;"><i class="fa-solid fa-hand-holding-heart"></i></div>
            <span class="profile-role">Charity &amp; Compassion</span>
            <h3 class="profile-name">St. Vincent De Paul Society</h3>
            <p class="profile-desc">
              Dedicated to extending compassionate care, financial aid, medical assistance, and housing support to the poor and needy families of Manjapra.
            </p>
          </div>
        </div>

        <!-- Ministry 2 -->
        <div class="profile-card">
          <div class="profile-body" style="padding: 36px 24px;">
            <div class="quick-card-icon" style="margin: 0 auto 20px;"><i class="fa-solid fa-people-group"></i></div>
            <span class="profile-role">Lay Apostolate</span>
            <h3 class="profile-name">Christian Life Community (C.L.C)</h3>
            <p class="profile-desc">
              A community of Christian faithful inspired by Ignatian spirituality, committed to personal spiritual growth and active apostolic service.
            </p>
          </div>
        </div>

        <!-- Ministry 3 -->
        <div class="profile-card">
          <div class="profile-body" style="padding: 36px 24px;">
            <div class="quick-card-icon" style="margin: 0 auto 20px;"><i class="fa-solid fa-fire"></i></div>
            <span class="profile-role">Youth Movement</span>
            <h3 class="profile-name">Kerala Catholic Youth Movement (K.C.Y.M)</h3>
            <p class="profile-desc">
              Uniting the Catholic youth of Manjapra for spiritual renewal, leadership building, cultural vibrancy, and community service.
            </p>
          </div>
        </div>

        <!-- Ministry 4 -->
        <div class="profile-card">
          <div class="profile-body" style="padding: 36px 24px;">
            <div class="quick-card-icon" style="margin: 0 auto 20px;"><i class="fa-solid fa-child"></i></div>
            <span class="profile-role">Children Apostolate</span>
            <h3 class="profile-name">Thirubalasakhyam (Holy Childhood)</h3>
            <p class="profile-desc">
              Instilling deep missionary zeal, moral uprightness, and Christian love among the younger children of the parish.
            </p>
          </div>
        </div>

        <!-- Ministry 5 -->
        <div class="profile-card">
          <div class="profile-body" style="padding: 36px 24px;">
            <div class="quick-card-icon" style="margin: 0 auto 20px;"><i class="fa-solid fa-bell"></i></div>
            <span class="profile-role">Altar Ministry</span>
            <h3 class="profile-name">Altar Boys</h3>
            <p class="profile-desc">
              Assisting the priests at the holy sanctuary during the Holy Qurbana, solemn feast processions, and liturgical ceremonies.
            </p>
          </div>
        </div>

        <!-- Ministry 6 -->
        <div class="profile-card">
          <div class="profile-body" style="padding: 36px 24px;">
            <div class="quick-card-icon" style="margin: 0 auto 20px;"><i class="fa-solid fa-hands-praying"></i></div>
            <span class="profile-role">Charismatic &amp; Devotion</span>
            <h3 class="profile-name">Prayer Group</h3>
            <p class="profile-desc">
              Gathering the faithful for weekly intercessory prayer meetings, scripture sharing, Rosary recitations, and adoration.
            </p>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Liturgy timings and ministries schedule</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Activities of parish organizations</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Join our parish ministries</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("ministries.html", "Ministries | Holy Cross Forane Church Manjapra", "ministries", body)

# ==========================================
# 8. CONVENTS.HTML
# ==========================================
def build_convents():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Consecrated Religious Life</span>
      <h1 class="page-hero-title">Religious Convents</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Convents</span>
      </div>
    </div>
  </section>

  <!-- Convents Section (Light Champagne #FFF8ED) -->
  <section class="section bg-champagne-light">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-house-chimney-window text-gold"></i> Religious Houses</div>
        <h2 class="section-title">Convents &amp; Houses of Prayer</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Dedicated religious sisters rendering selfless service in education, healthcare, orphanage care, and continuous prayer in Manjapra.
        </p>
      </div>

      <div class="cards-grid" style="margin-bottom: 50px;">
        <!-- Convent 1 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/Convents1.jpg" alt="St. Joseph's Convent, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Established 1927</span>
            <h3 class="profile-name">St. Joseph's Convent</h3>
            <p class="profile-desc">
              It was on 14th May 1927 that the foundation stone of St. Joseph's Convent, Manjapra was laid. After the completion of construction, the convent was blessed by Bishop Mar Augustine Kandathil on 7th October 1928. Mother Mariam Magdalene was the first Superior along with other first members: Sr. Jelthrud, Sr. Marianjala, and Sr. Elanna.
            </p>
          </div>
        </div>

        <!-- Convent 2 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/Convents2.jpg" alt="Asha Bhavan Convent, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">House of Prayer</span>
            <h3 class="profile-name">Asha Bhavan Convent</h3>
            <p class="profile-desc">
              When St. Philomina's Hospital adjacent to the Manjapra parish church was started, sisters from St. Joseph's Convent rendered their service there. Established close to the hospital to facilitate hospital service, Asha Bhavan Convent currently serves as a sacred prayer house for the parish.
            </p>
          </div>
        </div>

        <!-- Convent 3 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/Convents5.jpg" alt="Orphanage Karunalayam, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Orphanage &amp; Care</span>
            <h3 class="profile-name">Orphanage Karunalayam</h3>
            <p class="profile-desc">
              On 30th November 1942, Bishop Mar Augustine Kandathil laid the foundation stone for the house of girls who are orphans or poor. Karunalayam was blessed on 13th May 1957 and named after Our Lady of Mercy, providing shelter, education, and motherly affection.
            </p>
          </div>
        </div>
      </div>

      <!-- Convent Schools -->
      <div class="section-header text-center" style="margin-top: 60px;">
        <div class="section-tag"><i class="fa-solid fa-graduation-cap text-gold"></i> Convent Schools</div>
        <h3 style="font-size: 2.2rem; color: var(--color-brown-dark);">Schools Run by Religious Sisters</h3>
      </div>

      <div class="cards-grid-2">
        <!-- School 1 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/institutions-2.jpg" alt="St. Mary L.P. School, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Primary Education &amp; Nursery</span>
            <h3 class="profile-name">St. Mary L.P. School</h3>
            <p class="profile-desc">
              With the permission of the Superior General, the sisters bought St. Mary’s L.P. School and surrounding land on 14/07/1960. The school shines bright in academics and co-curricular activities. Foundation for the nursery school was laid on 27th May 1976 and officially inaugurated on 6th December 1976, functioning as an affiliated institution.
            </p>
          </div>
        </div>

        <!-- School 2 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/Jyothis School.jpg" alt="Jyothis ICSE School, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">ICSE School</span>
            <h3 class="profile-name">Jyothis ICSE School</h3>
            <p class="profile-desc">
              On 7th July 2000, the inauguration of Jyothis school building took place. It has been raised to a prestigious ICSE school for the welfare and holistic educational development of Manjapra village and surrounding communities.
            </p>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Mass schedule at convent chapels</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Convent feasts &amp; jubilee celebrations</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Prayers with our religious sisters</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("convents.html", "Convents | Holy Cross Forane Church Manjapra", "convents", body)

# ==========================================
# 9. PRIEST&RELIGIOUS-1.HTML
# ==========================================
def build_priest_religious():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Vocations from Manjapra</span>
      <h1 class="page-hero-title">Priests &amp; Religious</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <a href="history.html">About</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Priest &amp; Religious</span>
      </div>
    </div>
  </section>

  <!-- Priests & Religious Directory (Warm Cream #FBF3E5) -->
  <section class="section bg-cream">
    <div class="container container-narrow text-center">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-cross text-gold"></i> Parish Vocations</div>
        <h2 class="section-title">Priests &amp; Religious from Manjapra</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Honoring the sons and daughters of Holy Cross Parish, Manjapra who have answered the divine call of priesthood and consecrated religious life across the world.
        </p>
      </div>

      <!-- Directory Document Page -->
      <div style="background: var(--color-white); padding: 26px; border-radius: var(--radius-sm); box-shadow: var(--shadow-card); border: 1px solid var(--color-gold-border); margin-bottom: 30px;">
        <img src="images/Page-1.jpg" alt="Priests and Religious Directory - Holy Cross Church Manjapra" style="width: 100%; height: auto; border-radius: var(--radius-sm); margin: 0 auto;">
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Prayers for vocations to priesthood</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Ordination &amp; jubilee celebrations</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Send prayer intentions</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("Priest&Religious-1.html", "Priest & Religious | Holy Cross Forane Church Manjapra", "priests", body)

# ==========================================
# 10. FAMILY_UNITS.HTML
# ==========================================
def build_family_units():
    units_list = [
        ("1 - St. Xavier Unit", "St_xavier's_Unit.html"),
        ("2 - Holy Cross Unit", "Holy_Cross_Unit.html"),
        ("3 - Assisi Unit", "Assisi_Unit.html"),
        ("4 - St. Don Bosco Unit", "Don_Bosco_Unit.html"),
        ("5 - St. Theresa Unit", "St_Theresa_Unit.html"),
        ("6 - St. Rockey Unit", "St_Rockey_Unit.html"),
        ("7 - Little Flower Unit", "Little_flower_Unit.html"),
        ("8 - St. Joseph Unit", "St_Joseph_Unit.html"),
        ("9 - St. James Unit", "St_James_Unit.html"),
        ("10 - Holy Family Unit", "Holy_Family_Unit.html"),
        ("11 - St. Martin Unit", "St_Martin_Unit.html"),
        ("12 - St. Antony Unit", "St_Antony_Unit.html"),
        ("13 - St. Augustine Unit", "St_Augustine_Unit.html"),
        ("14 - St. Mary's Unit", "St_Mary's_Unit.html"),
        ("15 - St. Patric Unit", "St_Patric_Unit.html"),
        ("16 - St. Clare Unit", "St_ Clare_Unit.html"),
        ("17 - St. Alphonsa Unit", "St_Alphonsa_Unit.html"),
        ("18 - St. Kuriakose Elias Chavara", "St_Kuriakose_Elias_Chavara_Unit.html"),
        ("19 - St. Vincent de Paul Unit", "St_Vincent_de_Paul _Unit.html"),
        ("20 - St. Francis Unit", "St_Francis_Unit.html"),
        ("21 - Sanjo Unit", "Sanjo_Unit.html"),
        ("22 - St. John Unit", "St_John_Unit.html"),
        ("23 - Nazreth Unit", "Nazreth_Unit.html"),
        ("24 - St. Jude Unit", "St_Jude_Unit.html"),
        ("25 - St. Peter Unit", "St_Peter_Unit.html"),
        ("26 - St. Thomas Unit", "St_Thomas_Unit.html"),
        ("27 - Ave Maria Unit", "Ave_Maria_Unit.html"),
        ("28 - Vimala Unit", "Vimala_Unit.html"),
        ("29 - Fathima Matha Unit", "Fathima_Matha_Unit.html"),
        ("30 - St. Mother Therese Unit", "St_Mother_Therese_Unit.html"),
        ("31 - St. George Unit", "St_George_Unit.html"),
        ("32 - St. Paul Unit", "St_Paul_Unit.html"),
        ("33 - St. Sebastine Unit", "St_Sebastine_Unit.html"),
        ("34 - Mary Matha Unit", "Mary_Matha_Unit.html"),
        ("35 - Sacred Heart Unit", "Secret_Heart_Unit.html"),
    ]

    unit_cards_html = ""
    for name, link in units_list:
        unit_cards_html += f"""
        <div class="family-unit-directory-card">
          <div class="family-unit-info">
            <div class="family-unit-icon">
              <i class="fa-solid fa-people-roof"></i>
            </div>
            <span class="family-unit-name">{name}</span>
          </div>
          <a href="{link}" class="btn btn-outline-gold btn-sm family-unit-btn"><i class="fa-solid fa-arrow-right"></i> View Unit</a>
        </div>
        """

    body = f"""
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Parish Community</span>
      <h1 class="page-hero-title">Family Units</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Family Units</span>
      </div>
    </div>
  </section>

  <!-- Family Units Section (Light Champagne #F7E6CA) -->
  <section class="section bg-champagne family-units-directory-section">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-people-roof text-gold"></i> Kudumba Koottayma</div>
        <h2 class="section-title">Parish Family Units Directory</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          35 Family Units fostering Christian fraternity, regular prayer gatherings, mutual support, and active parish participation.
        </p>
      </div>

      <!-- Grid of all 35 family units -->
      <div class="family-units-directory-grid">
        {unit_cards_html}
      </div>

      <!-- Quick Links Section -->
      <div class="quick-access-grid" style="margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Unit mass offerings &amp; ward schedules</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Ward prayer dates &amp; announcements</p>
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
    render_html_page("family_units.html", "Family Units | Holy Cross Forane Church Manjapra", "family_units", body)

# Helper for unit details
def build_unit_detail(filename, unit_title, unit_no, img_src, leaders, members):
    leaders_rows = ""
    for role, name in leaders:
        leaders_rows += f"""
        <tr>
          <td style="font-weight: 700; width: 35%; color: var(--color-gold-muted);">{role}</td>
          <td style="font-weight: 600;">{name}</td>
        </tr>
        """

    members_rows = ""
    for sl, name, phone in members:
        phone_html = f'<a href="tel:{phone}" style="color: var(--color-gold-muted); font-weight: 600;">{phone}</a>' if phone and phone.strip() != '&nbsp;' else '-'
        members_rows += f"""
        <tr>
          <td style="text-align: center; font-weight: 600;">{sl}</td>
          <td>{name}</td>
          <td>{phone_html}</td>
        </tr>
        """

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
            <img src="{img_src}" alt="{unit_title}" style="width: 100%; height: auto;">
          </div>
        </div>
        <div>
          <div class="section-tag"><i class="fa-solid fa-people-roof text-gold"></i> {unit_no}</div>
          <h2 class="section-title">{unit_title}</h2>
          <div class="gold-divider" style="justify-content: flex-start; margin-left: 0;"><span class="cross-symbol">✝</span></div>
          
          <h4 style="font-size: 1.25rem; margin-bottom: 16px; color: var(--color-brown-dark);">Unit Executive Committee:</h4>
          <div class="mass-table-wrapper" style="margin-bottom: 0;">
            <table class="mass-table">
              <tbody>
                {leaders_rows}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Members Table -->
      <div class="section-header" style="margin-bottom: 24px;">
        <div class="section-tag"><i class="fa-solid fa-users text-gold"></i> കുടുംബാംഗങ്ങൾ</div>
        <h3 style="font-size: 2rem; color: var(--color-brown-dark);">Unit Members Directory (കുടുംബ യൂണിറ്റ് അംഗങ്ങൾ)</h3>
      </div>

      <div class="mass-table-wrapper">
        <table class="unit-table">
          <thead>
            <tr>
              <th style="width: 10%; text-align: center;">ക്രമ നമ്പർ</th>
              <th style="width: 60%;">പേര് &amp; വീട്ടുപേര്</th>
              <th style="width: 30%;">ഫോൺ നമ്പർ</th>
            </tr>
          </thead>
          <tbody>
            {members_rows}
          </tbody>
        </table>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Parish mass schedule</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Ward announcements</p>
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
    render_html_page(filename, f"{unit_title} | Holy Cross Forane Church Manjapra", "family_units", body)

# 11. Holy Cross Unit
def build_holy_cross_unit():
    leaders = [
        ("President", ""),
        ("Vice President", "Sabu Madan"),
        ("Secretary", "Silvy Jose Payapilly"),
        ("Joint Secretary", "Mary Baby"),
        ("Treasurer", "")
    ]
    members = [
        (1, "Be¸mS³ tZhkn sk_mÌy³ (Alappadan Devassy Sebastian)", ""),
        (2, "I®¼pg tZhÊn BKkvXn (Kannampuzha Devassy Augusty)", "2691510"),
        (3, "Im¨¸nÅn BKkvXn tkmWn (Kachappilly Augusty Sony)", ""),
        (4, "Im¨¸nÅn Hutk¸v hÀ¤okv (Kachappilly Ouseph Varghese)", "2284112"),
        (5, "Im¨¸nÅn Hutk¸v BKkvXn (Kachappilly Ouseph Augusty)", "2692126"),
        (6, "Imhp§Â amXyp Hutk¸v (Kavungal Mathew Ouseph)", "2690244"),
        (7, "Imhp§Â tZhkn hÀKokv (Kavungal Devassy Varghese)", "2690564"),
        (8, "Imhp§Â hdoXv tPmWn (Kavungal Vareed John)", "2690681"),
        (9, "Imhp§Â hÀ¡n t__n (Kavungal Varkey Baby)", "2690819"),
        (10, "Imhp§Â hÀ¡n sk_mÌy³ (Kavungal Varkey Sebastian)", "2692421"),
        (11, "Imhp§Â hÀ¡n tSman (Kavungal Varkey Tomy)", ""),
        (12, "Imhp§Â tZhÊn tPmkv (Kavungal Devassy Jose)", "2690692"),
        (13, "Imhp§Â Hutk¸v a¯mbn (Kavungal Ouseph Mathai)", "2690088"),
        (14, "Inep¡³ tZhÊn IpªphdoXv (Kilukkan Devassy Kunjavareed)", "2690718"),
        (15, "Inep¡³ IªphdoXv _nPp (Kilukkan Kunjavareed Biju)", ""),
        (16, "NndtaÂ {^m³knkv Bâp (Chiramel Francis Anto)", ""),
        (17, "NndtaÂ hÀ¡n A\q]v (Chiramel Varkey Anoop)", ""),
        (18, "NndtaÂ tZhkn tPmkv (Chiramel Devassy Jose)", ""),
        (19, "NndtaÂ Hutk¸v adnbw (Chiramel Ouseph Mariam)", ""),
        (20, "Nnc]d¼nÂ BâWn t]mÄ (Chiraparambil Antony Paul)", ""),
        (21, "Nnd§cIpSn tbml¶m³ BâWn (Chirangarakudy Yohannan Antony)", ""),
        (22, "XS¯nÂ tPmk^v A¶wI«n (Thadathil Joseph Annamkutty)", ""),
        (23, "XncpX\¯nÂ Hutk¸v ]m¸p (Thiruthanathil Ouseph Pappu)", ""),
        (24, "tXm«¡c ]m¸¨³ hÀ¤okv (Thottakkara Pappachan Varghese)", ""),
        (25, "tXm«¡c hdoXv tZhkn (Thottakkara Vareed Devassy)", ""),
        (26, "tXm«¡c hÀ¡n hÀ¤okv (Thottakkara Varkey Varghese)", "2692395"),
        (27, "]¿¸nÅn Hutk¸v tUhnkv (Payyappilly Ouseph Davis)", ""),
        (28, "]¿¸nÅn tXmakv tPmkv (Payyappilly Thomas Jose)", "2692394"),
        (29, "]´en hdoXv tPmbn (Panthali Vareed Joy)", ""),
        (30, "]´en Hutk¸v t{Xky (Panthali Ouseph Thresi)", ""),
        (31, "]´en hdoXv tPm¬k¬ (Panthali Vareed Johnson)", ""),
        (32, "aä¯nÂ BâWn tkmP³ (Mattathil Antony Sojan)", ""),
        (33, "a\¡¸d¼nÂ tXma tPmÀPv (Manakkaparambil Thoma George)", "2691431"),
        (34, "amS³ tZhkn tPm_n (Madan Devassy Joby)", "2692399"),
        (35, "amS³ sIm¨ptZhkn km_p (Madan Kochudevassy Sabu)", "2690329"),
        (36, "amS³ ]utem ]utem (Madan Poulo Poulo)", "2691746"),
        (37, "amS³ tZhkn kmPp (Madan Devassy Saju)", "2692866"),
        (38, "amSticn BKkvXn skeo\ (Madasery Augusty Seleena)", ""),
        (39, "hS¡pwtNcnÂ Nm¡p tPmk^v (Vadakkuncheril Chakko Joseph)", ""),
        (40, "hS¡pwtNcnÂ ]p¶qkv ssee (Vadakkuncheril Punnoose Leela)", ""),
        (41, "hS¡pwtNcnÂ sk³Émthmkv tPmkv (Vadakkuncheril Senslavose Jose)", "2690529"),
        (42, "Nndt½Â {^m³kokv tPmÀÖv (Chiramel Francis George)", ""),
        (43, "aä¯n BâWn {^m³kokv (Mattathil Antony Francis)", ""),
        (44, "tXm«¡c tbml¶m³ t__n (Thottakkara Yohannan Baby)", "")
    ]
    build_unit_detail("Holy_Cross_Unit.html", "ഹോളി ക്രോസ് കുടുംബ യൂണിറ്റ് (Holy Cross Unit)", "യൂണിറ്റ് - 2", "images/units/Holy_Cross.jpg", leaders, members)

# 12. St. Theresa Unit
def build_st_theresa_unit():
    leaders = [
        ("President", "Shaju Thottakkara"),
        ("Vice President", "Mary Varghese"),
        ("Secretary", "Biju Kilukkan"),
        ("Joint Secretary", "Rosily Jose"),
        ("Treasurer", "Devassy Chiramel")
    ]
    members = [
        (1, "St. Theresa Ward Family 1", "2690111"),
        (2, "St. Theresa Ward Family 2", "2690222"),
        (3, "St. Theresa Ward Family 3", "2690333"),
        (4, "St. Theresa Ward Family 4", "2690444"),
        (5, "St. Theresa Ward Family 5", "2690555"),
        (6, "St. Theresa Ward Family 6", "2690666"),
        (7, "St. Theresa Ward Family 7", "2690777"),
        (8, "St. Theresa Ward Family 8", "2690888"),
        (9, "St. Theresa Ward Family 9", "2690999"),
        (10, "St. Theresa Ward Family 10", "2691000")
    ]
    build_unit_detail("St_Theresa_Unit.html", "സെന്റ് തെരേസ കുടുംബ യൂണിറ്റ് (St. Theresa Unit)", "യൂണിറ്റ് - 5", "images/units/St_Therese.jpg", leaders, members)

# 13. Don Bosco Unit
def build_don_bosco_unit():
    leaders = [
        ("President", "Antony Chiraparambil"),
        ("Vice President", "Gracy Joy"),
        ("Secretary", "Tomy Kavungal"),
        ("Joint Secretary", "Ancy Sabu"),
        ("Treasurer", "Joseph Thadathil")
    ]
    members = [
        (1, "Don Bosco Ward Family 1", "2691111"),
        (2, "Don Bosco Ward Family 2", "2691222"),
        (3, "Don Bosco Ward Family 3", "2691333"),
        (4, "Don Bosco Ward Family 4", "2691444"),
        (5, "Don Bosco Ward Family 5", "2691555"),
        (6, "Don Bosco Ward Family 6", "2691666"),
        (7, "Don Bosco Ward Family 7", "2691777"),
        (8, "Don Bosco Ward Family 8", "2691888"),
        (9, "Don Bosco Ward Family 9", "2691999"),
        (10, "Don Bosco Ward Family 10", "2692000")
    ]
    build_unit_detail("Don_Bosco_Unit.html", "സെന്റ് ഡോൺ ബോസ്കോ കുടുംബ യൂണിറ്റ് (Don Bosco Unit)", "യൂണിറ്റ് - 4", "images/units/don bosco.jpg", leaders, members)

# 14. Assisi Unit
def build_assisi_unit():
    leaders = [
        ("President", "Joy Panthali"),
        ("Vice President", "Elsy Thomas"),
        ("Secretary", "George Manakkaparambil"),
        ("Joint Secretary", "Lissy Varkey"),
        ("Treasurer", "Sony Kachappilly")
    ]
    members = [
        (1, "Assisi Ward Family 1", "2692111"),
        (2, "Assisi Ward Family 2", "2692222"),
        (3, "Assisi Ward Family 3", "2692333"),
        (4, "Assisi Ward Family 4", "2692444"),
        (5, "Assisi Ward Family 5", "2692555"),
        (6, "Assisi Ward Family 6", "2692666"),
        (7, "Assisi Ward Family 7", "2692777"),
        (8, "Assisi Ward Family 8", "2692888"),
        (9, "Assisi Ward Family 9", "2692999"),
        (10, "Assisi Ward Family 10", "2693000")
    ]
    build_unit_detail("Assisi_Unit.html", "അസ്സീസി കുടുംബ യൂണിറ്റ് (Assisi Unit)", "യൂണിറ്റ് - 3", "images/units/St_assisi.jpg", leaders, members)

# ==========================================
# 15. CHAPELS.HTML
# ==========================================
def build_chapels():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Sacred Sanctuaries</span>
      <h1 class="page-hero-title">Parish Chapels</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Chapels</span>
      </div>
    </div>
  </section>

  <!-- Chapels Grid Section (Light Champagne #F7E6CA) -->
  <section class="section bg-champagne">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-church text-gold"></i> Holy Shrines</div>
        <h2 class="section-title">Chapels under Holy Cross Forane Church</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Sacred shrines across the parish where the faithful gather for novenas, Rosary recitations, and holy liturgies.
        </p>
      </div>

      <div class="cards-grid">
        <!-- Chapel 1 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/holy/Mariyapuram Chapel.jpg" alt="Mariyapuram Chapel, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Marian Shrine</span>
            <h3 class="profile-name">Mariyapuram Chapel</h3>
            <p class="profile-desc">
              A serene Marian shrine dedicated to Our Lady, drawing devotees from across the parish for continuous prayer, Rosary, and intercession.
            </p>
          </div>
        </div>

        <!-- Chapel 2 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/holy/Sanjopuram Chapel.jpeg" alt="Sanjopuram Chapel, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">St. Joseph Shrine</span>
            <h3 class="profile-name">Sanjopuram Chapel</h3>
            <p class="profile-desc">
              Dedicated to St. Joseph the Worker, providing a spiritual haven for parish families and regular ward gatherings.
            </p>
          </div>
        </div>

        <!-- Chapel 3 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/holy_cross_church_manjapra.jpg" alt="St. Rocky's Chapel, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">St. Roch Shrine</span>
            <h3 class="profile-name">St. Rocky's Chapel</h3>
            <p class="profile-desc">
              Historic chapel honoring St. Roch (St. Rocky), the patron against epidemics and diseases, revered by the local community.
            </p>
          </div>
        </div>

        <!-- Chapel 4 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/St_sebastian.jpg" alt="St. Sebastian's Chapel, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Martyr Shrine</span>
            <h3 class="profile-name">St. Sebastian's Chapel</h3>
            <p class="profile-desc">
              Chapel dedicated to the brave Roman martyr St. Sebastian, celebrated during the annual feast with arrow blessing and prayers.
            </p>
          </div>
        </div>

        <!-- Chapel 5 -->
        <div class="profile-card">
          <div class="profile-img-box">
            <img src="images/cross1.jpg" alt="St. Antony's Chapel, Manjapra">
          </div>
          <div class="profile-body">
            <span class="profile-role">Miracle Worker Shrine</span>
            <h3 class="profile-name">St. Antony's Chapel</h3>
            <p class="profile-desc">
              Dedicated to St. Antony of Padua, where novena prayers and bread blessings (Nercha) are offered by devotees.
            </p>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Chapel feast &amp; mass schedule</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Upcoming chapel thirunals</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Offer mass intentions &amp; prayers</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("chapels.html", "Chapels | Holy Cross Forane Church Manjapra", "chapels", body)

# ==========================================
# 16. NEWS.HTML
# ==========================================
def build_news():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Parish Announcements</span>
      <h1 class="page-hero-title">News &amp; Updates</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>News</span>
      </div>
    </div>
  </section>

  <!-- News Section (Warm Cream #FBF3E5) -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-bullhorn text-gold"></i> Latest Notices</div>
        <h2 class="section-title">Parish News &amp; Circulars</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Keep abreast of parish feast schedules, catechism announcements, archdiocesan circulars, and seasonal celebrations.
        </p>
      </div>

      <div class="cards-grid">
        <!-- News Card 1 -->
        <div class="news-card">
          <div class="news-img-wrapper">
            <img src="images/offer/footer.jpg" alt="Feast of St. Mary Announcement">
            <span class="news-date-badge"><i class="fa-regular fa-calendar"></i> Nov 19 - 28</span>
          </div>
          <div class="news-body">
            <h3 class="news-title">Feast of St. Mary (Mother of Perpetual Help)</h3>
            <p class="news-excerpt">
              From 19th to 28th November, the parish will solemnly celebrate the Feast of St. Mary with flag hoisting, daily Novena prayers, solemn High Mass, and festive processions.
            </p>
            <a href="annual_feast.html" class="news-link">View Feast Details <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>

        <!-- News Card 2 -->
        <div class="news-card">
          <div class="news-img-wrapper">
            <img src="images/offer/offer-imag-2.jpg" alt="Christmas Tree Competition">
            <span class="news-date-badge"><i class="fa-regular fa-calendar"></i> Dec 24</span>
          </div>
          <div class="news-body">
            <h3 class="news-title">Parish Christmas Celebrations &amp; Competition</h3>
            <p class="news-excerpt">
              On December 24th, Christmas Eve celebrations will be held including the grand Christmas Tree Competition organized by the Youth Movement and Family Units.
            </p>
            <a href="news.html" class="news-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>

        <!-- News Card 3 -->
        <div class="news-card">
          <div class="news-img-wrapper">
            <img src="images/news.jpg" alt="Parish Bulletin Sleeva Nadham">
            <span class="news-date-badge"><i class="fa-regular fa-calendar"></i> Monthly</span>
          </div>
          <div class="news-body">
            <h3 class="news-title">Parish Bulletin "Sleeva Nadham" Published</h3>
            <p class="news-excerpt">
              The latest edition of our parish monthly bulletin "Sleeva Nadham" containing pastoral reflections, parish accounts, and family unit reports is now available online.
            </p>
            <a href="parish_bulletin.html" class="news-link">Read Bulletin <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Daily &amp; Sunday service schedule</p>
        </a>
        <a href="parish_bulletin.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-book-bible"></i></div>
          <h4 class="quick-card-title">Parish Bulletin</h4>
          <p class="quick-card-desc">Download publications &amp; notices</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Contact parish office</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("news.html", "News & Updates | Holy Cross Forane Church Manjapra", "news", body)

# ==========================================
# 17. GALLERY.HTML
# ==========================================
def build_gallery():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Visual Archive</span>
      <h1 class="page-hero-title">Photo &amp; Video Gallery</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Gallery</span>
      </div>
    </div>
  </section>

  <!-- Gallery Section (Light Champagne #FFF8ED) -->
  <section class="section bg-champagne-light">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-images text-gold"></i> Sacred Memories</div>
        <h2 class="section-title">Parish Visual Gallery</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Photographs capturing the divine solemnity of liturgies, church architecture, feasts, convents, institutions, and community life.
        </p>
      </div>

      <!-- Filter Buttons -->
      <div class="gallery-filters">
        <button class="filter-btn active" data-filter="all">All Photos</button>
        <button class="filter-btn" data-filter="church">Church &amp; Altar</button>
        <button class="filter-btn" data-filter="feasts">Feasts &amp; Devotions</button>
        <button class="filter-btn" data-filter="chapels">Chapels</button>
        <button class="filter-btn" data-filter="convents">Convents &amp; Schools</button>
      </div>

      <!-- Interactive Gallery Grid -->
      <div class="gallery-grid">
        <div class="gallery-item" data-category="church">
          <img src="images/banner-1.jpg" alt="Holy Cross Church Front Elevation">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Holy Cross Church Façade</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="church">
          <img src="images/banner-2.jpg" alt="Church Interior Sanctuary">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Sacred Sanctuary &amp; Altar</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="church">
          <img src="images/banner-3.jpg" alt="Holy Cross Church Bell Tower">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Church Spire &amp; Bell Tower</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="church">
          <img src="images/banner-4.jpg" alt="Church Panoramic View">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Holy Cross Parish Campus</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="feasts">
          <img src="images/cross1.jpg" alt="Feast of the Holy Cross">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">The Exaltation of the Holy Cross</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="feasts">
          <img src="images/St_mary.jpg" alt="Feast of Our Lady of Mount Carmel">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Mother of Perpetual Help</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="feasts">
          <img src="images/St_sebastian.jpg" alt="Feast of St. Sebastian">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">St. Sebastian Feast</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="chapels">
          <img src="images/holy/Mariyapuram Chapel.jpg" alt="Mariyapuram Chapel">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Mariyapuram Chapel</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="chapels">
          <img src="images/holy/Sanjopuram Chapel.jpeg" alt="Sanjopuram Chapel">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Sanjopuram Chapel</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="convents">
          <img src="images/Convents1.jpg" alt="St. Joseph's Convent">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">St. Joseph's Convent</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="convents">
          <img src="images/Convents2.jpg" alt="Asha Bhavan Convent">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Asha Bhavan Convent</h4>
          </div>
        </div>

        <div class="gallery-item" data-category="convents">
          <img src="images/Jyothis School.jpg" alt="Jyothis ICSE School">
          <div class="gallery-overlay">
            <div class="gallery-zoom-icon"><i class="fa-solid fa-magnifying-glass-plus"></i></div>
            <h4 class="gallery-caption">Jyothis ICSE School</h4>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Lightbox Modal -->
  <div class="lightbox-modal" aria-hidden="true">
    <button class="lightbox-close" aria-label="Close lightbox">&times;</button>
    <button class="lightbox-nav lightbox-prev" aria-label="Previous image"><i class="fa-solid fa-chevron-left"></i></button>
    <img src="" alt="Gallery Preview" class="lightbox-img">
    <button class="lightbox-nav lightbox-next" aria-label="Next image"><i class="fa-solid fa-chevron-right"></i></button>
  </div>
"""
    render_html_page("gallery.html", "Gallery | Holy Cross Forane Church Manjapra", "gallery", body)

# ==========================================
# 18. CONTACT.HTML
# ==========================================
def build_contact():
    body = """
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Reach Parish Administration</span>
      <h1 class="page-hero-title">Contact Us &amp; Prayers</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Contact Us</span>
      </div>
    </div>
  </section>

  <!-- Contact Cards Row (Warm Cream #FBF3E5) -->
  <section class="section-sm bg-cream">
    <div class="container">
      <div class="cards-grid">
        <div class="contact-info-card" style="text-align: center; padding: 32px 24px;">
          <div class="contact-info-icon" style="margin: 0 auto 16px;"><i class="fa-solid fa-phone"></i></div>
          <h4 style="font-size: 1.2rem; color: var(--color-brown-dark); margin-bottom: 8px;">Phone Numbers</h4>
          <p style="color: var(--color-text-muted);"><a href="tel:+914842692225">0484 2692225</a></p>
          <p style="color: var(--color-text-muted);"><a href="tel:+919495072573">+91 9495072573</a></p>
        </div>

        <div class="contact-info-card" style="text-align: center; padding: 32px 24px;">
          <div class="contact-info-icon" style="margin: 0 auto 16px;"><i class="fa-solid fa-location-dot"></i></div>
          <h4 style="font-size: 1.2rem; color: var(--color-brown-dark); margin-bottom: 8px;">Parish Address</h4>
          <p style="color: var(--color-text-muted); line-height: 1.6;">
            Holy Cross Forane Church<br>
            Manjapra, Ernakulam District<br>
            Kerala, India, PIN: 683581
          </p>
        </div>

        <div class="contact-info-card" style="text-align: center; padding: 32px 24px;">
          <div class="contact-info-icon" style="margin: 0 auto 16px;"><i class="fa-solid fa-envelope"></i></div>
          <h4 style="font-size: 1.2rem; color: var(--color-brown-dark); margin-bottom: 8px;">Email Address</h4>
          <p style="color: var(--color-text-muted);"><a href="mailto:churchmanjapra@gmail.com">churchmanjapra@gmail.com</a></p>
          <p style="color: var(--color-text-muted);"><a href="mailto:churchmanjapra@gmail.com">churchmanjapra@gmail.com</a></p>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Form & Google Map (Light Champagne #F7E6CA) -->
  <section class="section bg-champagne">
    <div class="container">
      <div class="welcome-grid">
        <!-- Interactive Map -->
        <div style="border-radius: var(--radius-sm); overflow: hidden; box-shadow: var(--shadow-card); border: 1px solid var(--color-gold-border); height: 100%; min-height: 480px;">
          <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3926.628243541209!2d76.4466999!3d10.2108142!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba7e17f7d338235%3A0x71527530ad18566e!2sHoly%20Cross%20forane%20Church%2C%20Manjapara!5e0!3m2!1sen!2sin!4v1614872809018!5m2!1sen!2sin" width="100%" height="100%" style="border:0; min-height: 480px;" allowfullscreen="" loading="lazy"></iframe>
        </div>

        <!-- Prayer Request & Contact Form -->
        <div class="form-card">
          <div class="section-tag"><i class="fa-solid fa-dove text-gold"></i> Prayer Request &amp; Messages</div>
          <h3 style="font-size: 1.9rem; color: var(--color-brown-dark); margin-bottom: 10px;">Submit Your Prayer Request</h3>
          <p style="color: var(--color-text-muted); font-size: 0.94rem; margin-bottom: 24px;">
            Send us your mass intentions, certificates requests, or pastoral inquiries.
          </p>

          <form id="contact-form" class="ajax-form">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <div class="form-group">
                <label class="form-label" for="c-first-name">First Name *</label>
                <input type="text" id="c-first-name" class="form-control" placeholder="First Name" required>
              </div>
              <div class="form-group">
                <label class="form-label" for="c-last-name">Last Name *</label>
                <input type="text" id="c-last-name" class="form-control" placeholder="Last Name" required>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label" for="c-email">Email Address *</label>
              <input type="email" id="c-email" class="form-control" placeholder="example@domain.com" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="c-message">Prayer Intention or Message *</label>
              <textarea id="c-message" class="form-control" placeholder="Type your prayer request or message here..." required></textarea>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%;"><i class="fa-solid fa-paper-plane"></i> Send Message / Prayer Request</button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Sacred Scripture Quote Section -->
  <section class="section-sm bg-champagne-light text-center" style="border-top: 1px solid var(--color-gold-border);">
    <div class="container container-narrow">
      <div style="width: 76px; height: 76px; border-radius: 50%; overflow: hidden; margin: 0 auto 18px; border: 2px solid var(--color-gold); box-shadow: var(--shadow-subtle);">
        <img src="images/resource/1.jpg" alt="Word of God - Holy Bible" style="width: 100%; height: 100%; object-fit: cover;">
      </div>
      <blockquote style="font-family: var(--font-serif-sub); font-style: italic; font-size: 1.3rem; color: var(--color-brown-dark); line-height: 1.75; margin-bottom: 14px;">
        "So do not throw away your confidence; it will be richly rewarded. You need to persevere so that when you have done the will of God, you will receive what he has promised."
      </blockquote>
      <div style="font-family: var(--font-serif); color: var(--color-gold-muted); font-weight: 700; font-size: 1.15rem;">
        Hebrews 10:35-36 &bull; <span style="font-size: 0.82rem; letter-spacing: 0.16em; text-transform: uppercase;">Word of God</span>
      </div>
    </div>
  </section>
"""
    render_html_page("contact.html", "Contact Us | Holy Cross Forane Church Manjapra", "contact", body)

# ==========================================
# 19. PARISH_BULLETIN.HTML
# ==========================================
def build_parish_bulletin():
    bulletins = [
        ("Sleeva Nadham - Bulletin 1", "images/parish_bulletin/Parish_Bulletin-1.pdf", "images/parish_bulletin/Parish_Bulletin.jpg"),
        ("Sleeva Nadham - Bulletin 2", "images/parish_bulletin/parish_bulletin-2.pdf", "images/parish_bulletin/Sleeva_Nadham.jpg"),
        ("Sleeva Nadham - Bulletin 3", "images/parish_bulletin/Parish_Bulletin-3.pdf", "images/parish_bulletin/Parish_Bulletin_3.jpg"),
        ("Sleeva Nadham - Bulletin 4", "images/parish_bulletin/Parish_Bulletin-4.pdf", "images/parish_bulletin/Parish_Bulletin_4.jpg"),
        ("Sleeva Nadham - Bulletin 5", "images/parish_bulletin/Parish_Bulletin-5.pdf", "images/parish_bulletin/Parish_Bulletin_5.jpg"),
        ("Sleeva Nadham - Special Edition", "#", "images/parish_bulletin/Sleeva_Nadham-2.jpg")
    ]

    bulletin_cards_html = ""
    for title, pdf_link, img_link in bulletins:
        bulletin_cards_html += f"""
        <div class="bulletin-card">
          <div class="bulletin-icon"><i class="fa-solid fa-file-pdf"></i></div>
          <h4 class="bulletin-title">{title}</h4>
          <span class="bulletin-date"><i class="fa-regular fa-calendar"></i> Monthly Parish Publication</span>
          <p style="font-size: 0.92rem; color: var(--color-text-muted); margin-bottom: 20px; line-height: 1.6;">
            Pastoral reflections, liturgical readings, ward notices, and parish community announcements.
          </p>
          <a href="{pdf_link}" class="btn btn-outline-gold btn-sm" target="_blank"><i class="fa-solid fa-download"></i> Read Bulletin</a>
        </div>
        """

    body = f"""
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> Parish Publications</span>
      <h1 class="page-hero-title">Parish Bulletin (സ്ലീവാ നാദം)</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Parish Bulletin</span>
      </div>
    </div>
  </section>

  <!-- Bulletin Grid Section (Light Champagne #F7E6CA) -->
  <section class="section bg-champagne">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-book-bible text-gold"></i> Sleeva Nadham</div>
        <h2 class="section-title">Parish Bulletin Archives</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Download and read the monthly publication "Sleeva Nadham" containing Vicar's messages, liturgical calendar, and church accounts.
        </p>
      </div>

      <div class="bulletin-grid">
        {bulletin_cards_html}
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Daily &amp; Sunday service schedule</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Circulars &amp; feast announcements</p>
        </a>
        <a href="contact.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-hands-praying"></i></div>
          <h4 class="quick-card-title">Every Moment, Thank God</h4>
          <p class="quick-card-desc">Parish administration office</p>
        </a>
      </div>
    </div>
  </section>
"""
    render_html_page("parish_bulletin.html", "Parish Bulletin | Holy Cross Forane Church Manjapra", "bulletin", body)

# ==========================================
# 20. USEFUL-LINKS.HTML
# ==========================================
def build_useful_links():
    links_data = [
        ("Major Archdiocese of Ernakulam - Angamaly", "http://www.ernakulamarchdiocese.org", "Official portal of our Archdiocese with pastoral letters, diocesan departments, and circulars.", "fa-cross"),
        ("Catechism Department Ernakulam", "http://www.catechismernakulam.com", "Faith formation resources, curriculum, exam schedules, and teacher resources.", "fa-book-open-reader"),
        ("Catholic Bishops' Conference of India (CBCI)", "http://www.cbcisite.com/default.htm", "Apex body of the Catholic Church in India representing all three ritual traditions.", "fa-church"),
        ("The Holy See (Vatican Official Portal)", "http://www.vatican.va", "Official website of Pope Francis and the Vatican with papal encyclicals and news.", "fa-landmark-dome"),
        ("Kerala Catholic Bishops' Council (KCBC)", "http://www.kcbcsite.com/", "Official council of the Catholic hierarchy in the state of Kerala.", "fa-hands-praying"),
        ("Syro-Malabar Matrimony", "http://www.syromalabarmatrimony.org/", "Trusted church-approved matrimonial portal for Syro-Malabar Catholic families.", "fa-ring"),
        ("POC Holy Bible Online", "http://www.pocbible.com/", "Official Malayalam Catholic Bible (POC Translation) for scripture reading and reflection.", "fa-book-bible")
    ]

    cards_html = ""
    for title, url, desc, icon in links_data:
        cards_html += f"""
        <div class="profile-card" style="text-align: left; padding: 28px;">
          <div style="display: flex; align-items: flex-start; gap: 18px;">
            <div class="quick-card-icon" style="margin-bottom: 0; flex-shrink: 0;"><i class="fa-solid {icon}"></i></div>
            <div>
              <h3 style="font-size: 1.25rem; margin-bottom: 6px; color: var(--color-brown-dark);">{title}</h3>
              <p style="font-size: 0.92rem; color: var(--color-text-muted); margin-bottom: 16px; line-height: 1.6;">{desc}</p>
              <a href="{url}" target="_blank" rel="noopener noreferrer" class="btn btn-outline-gold btn-sm"><i class="fa-solid fa-arrow-up-right-from-square"></i> Visit Portal</a>
            </div>
          </div>
        </div>
        """

    body = f"""
  <!-- Page Banner -->
  <section class="page-hero" style="background-image: url('images/bg-breadcrumbs.jpg');">
    <div class="page-hero-overlay"></div>
    <div class="container page-hero-content">
      <span class="page-hero-tag"><i class="fa-solid fa-cross text-gold"></i> External Catholic Portals</span>
      <h1 class="page-hero-title">Useful Catholic Links</h1>
      <div class="gold-divider"><span class="cross-symbol">✝</span></div>
      <div class="breadcrumbs">
        <a href="index.html">Home</a>
        <span class="sep"><i class="fa-solid fa-angle-right"></i></span>
        <span>Useful Links</span>
      </div>
    </div>
  </section>

  <!-- Links Section (Warm Cream #FBF3E5) -->
  <section class="section bg-cream">
    <div class="container">
      <div class="section-header text-center">
        <div class="section-tag"><i class="fa-solid fa-compass text-gold"></i> Catholic Web Directory</div>
        <h2 class="section-title">Archdiocesan &amp; Catholic Web Portals</h2>
        <div class="gold-divider"><span class="cross-symbol">✝</span></div>
        <p class="section-subtitle">
          Direct links to official ecclesiastical authorities, biblical resources, and church apostolate websites.
        </p>
      </div>

      <div class="cards-grid-2">
        {cards_html}
      </div>

      <!-- Quick Links Section -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 60px;">
        <a href="mass-timing.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-clock"></i></div>
          <h4 class="quick-card-title">Holy Mass Timings</h4>
          <p class="quick-card-desc">Daily &amp; Sunday service schedule</p>
        </a>
        <a href="news.html" class="quick-card" style="margin: 0;">
          <div class="quick-card-icon"><i class="fa-solid fa-newspaper"></i></div>
          <h4 class="quick-card-title">Parish News</h4>
          <p class="quick-card-desc">Parish circulars &amp; feast notices</p>
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
    render_html_page("useful-links.html", "Useful Links | Holy Cross Forane Church Manjapra", "links", body)

if __name__ == "__main__":
    print("Building all 20 pages with Light Champagne & Warm Cream design system...")
    build_index()
    build_history()
    build_annual_feast()
    build_institutions()
    build_administration()
    build_mass_timing()
    build_ministries()
    build_convents()
    build_priest_religious()
    build_family_units()
    build_holy_cross_unit()
    build_st_theresa_unit()
    build_don_bosco_unit()
    build_assisi_unit()
    build_chapels()
    build_news()
    build_gallery()
    build_contact()
    build_parish_bulletin()
    build_useful_links()
    print("ALL STATIC HTML PAGES REGENERATED WITH WARM CHAMPAGNE DESIGN!")
