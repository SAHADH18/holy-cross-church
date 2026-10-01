/**
 * Holy Cross Forane Church, Manjapra - Main Interactive Script
 * Modern vanilla JS for responsive navigation, hero slider, gallery lightbox, and forms
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Navigation on Scroll
  const header = document.querySelector('.header-main');
  const backToTop = document.querySelector('.back-to-top');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      if (header) header.classList.add('header-scrolled');
      if (backToTop) backToTop.classList.add('visible');
    } else {
      if (header) header.classList.remove('header-scrolled');
      if (backToTop) backToTop.classList.remove('visible');
    }
  });

  if (backToTop) {
    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // 2. Mobile Menu Drawer
  const mobileToggle = document.querySelector('.mobile-nav-toggle');
  const mobileDrawer = document.querySelector('.mobile-drawer');
  const drawerOverlay = document.querySelector('.drawer-overlay');
  const mobileClose = document.querySelector('.mobile-close-btn');

  function openDrawer() {
    if (mobileDrawer) mobileDrawer.classList.add('open');
    if (drawerOverlay) drawerOverlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (mobileDrawer) mobileDrawer.classList.remove('open');
    if (drawerOverlay) drawerOverlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (mobileToggle) mobileToggle.addEventListener('click', openDrawer);
  if (mobileClose) mobileClose.addEventListener('click', closeDrawer);
  if (drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);

  // Mobile Dropdown Accordion
  const mobileDropdownTriggers = document.querySelectorAll('.mobile-nav-item.has-dropdown > .mobile-nav-link');
  mobileDropdownTriggers.forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const parent = trigger.parentElement;
      const menu = parent.querySelector('.mobile-dropdown-menu');
      if (menu) {
        menu.classList.toggle('open');
        const icon = trigger.querySelector('i');
        if (icon) {
          icon.classList.toggle('fa-chevron-up');
          icon.classList.toggle('fa-chevron-down');
        }
      }
    });
  });

  // 3. Homepage Hero Slider
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.slider-dot');
  const prevBtn = document.querySelector('.slider-btn.prev');
  const nextBtn = document.querySelector('.slider-btn.next');
  let currentSlide = 0;
  let slideInterval = null;

  function showSlide(index) {
    if (slides.length === 0) return;
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;

    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
    });

    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });

    currentSlide = index;
  }

  function startSlideShow() {
    if (slides.length > 1) {
      slideInterval = setInterval(() => {
        showSlide(currentSlide + 1);
      }, 5500);
    }
  }

  function resetSlideShow() {
    clearInterval(slideInterval);
    startSlideShow();
  }

  if (slides.length > 0) {
    showSlide(0);
    startSlideShow();

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        showSlide(currentSlide + 1);
        resetSlideShow();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        showSlide(currentSlide - 1);
        resetSlideShow();
      });
    }

    dots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        showSlide(idx);
        resetSlideShow();
      });
    });
  }

  // 4. Gallery Lightbox & Filtering
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.querySelector('.lightbox-modal');
  const lightboxImg = document.querySelector('.lightbox-img');
  const lightboxClose = document.querySelector('.lightbox-close');
  const lightboxPrev = document.querySelector('.lightbox-prev');
  const lightboxNext = document.querySelector('.lightbox-next');
  const filterBtns = document.querySelectorAll('.filter-btn');

  let currentGalleryIndex = 0;
  const visibleGalleryItems = () => Array.from(document.querySelectorAll('.gallery-item:not([style*="display: none"])'));

  function openLightbox(index) {
    const items = visibleGalleryItems();
    if (!items.length || !lightbox || !lightboxImg) return;
    currentGalleryIndex = (index + items.length) % items.length;
    const img = items[currentGalleryIndex].querySelector('img');
    if (img) {
      lightboxImg.src = img.src;
      lightboxImg.alt = img.alt || 'Holy Cross Church Gallery';
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeLightbox() {
    if (lightbox) lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  galleryItems.forEach((item) => {
    item.addEventListener('click', () => {
      const items = visibleGalleryItems();
      const index = items.indexOf(item);
      if (index !== -1) openLightbox(index);
    });
  });

  if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
  if (lightboxNext) {
    lightboxNext.addEventListener('click', (e) => {
      e.stopPropagation();
      openLightbox(currentGalleryIndex + 1);
    });
  }
  if (lightboxPrev) {
    lightboxPrev.addEventListener('click', (e) => {
      e.stopPropagation();
      openLightbox(currentGalleryIndex - 1);
    });
  }

  if (lightbox) {
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (!lightbox || !lightbox.classList.contains('active')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') openLightbox(currentGalleryIndex + 1);
    if (e.key === 'ArrowLeft') openLightbox(currentGalleryIndex - 1);
  });

  // Gallery Filter Tabs
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.getAttribute('data-filter');

      galleryItems.forEach(item => {
        const category = item.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          item.style.display = 'block';
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  // 5. Interactive Forms (Prayer Request & Contact)
  const prayerForms = document.querySelectorAll('form.ajax-form, form#prayer-form, form#contact-form');
  prayerForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const feedback = form.querySelector('.form-feedback') || document.createElement('div');
      feedback.className = 'form-feedback success';
      feedback.innerHTML = '<i class="fa-solid fa-circle-check"></i> Thank you! Your prayer intention / message has been received with blessings. We will pray for your intention in the Holy Mass.';
      
      if (!form.querySelector('.form-feedback')) {
        form.appendChild(feedback);
      } else {
        feedback.style.display = 'block';
      }
      form.reset();

      setTimeout(() => {
        feedback.style.display = 'none';
      }, 7000);
    });
  });

  // 6. Scroll Reveal Animations
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -40px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-up');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.section-title, .quick-card, .profile-card, .news-card, .timing-card, .heritage-panel, .heritage-feathered-image, .heritage-card, .timeline-card, .family-unit-card, .bulletin-card').forEach(el => {
    observer.observe(el);
  });
});
