document.addEventListener('DOMContentLoaded', () => {
  // Page Loader
  const loader = document.getElementById('page-loader');
  if (loader) {
    window.addEventListener('load', () => {
      loader.style.opacity = '0';
      setTimeout(() => loader.remove(), 1200);
    });
  }

  
  // Set dynamic years of expertise based on 1990
  const expCounter = document.getElementById('exp-counter');
  if (expCounter) {
    const currentYear = new Date().getFullYear();
    const yearsOfExp = currentYear - 1990;
    expCounter.setAttribute('data-target', yearsOfExp);
  }

  
  // Header Shrink
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      if(header) header.classList.add('shrink');
    } else {
      if(header) header.classList.remove('shrink');
    }
  });

  // Dynamic Fade-Up Elements
  document.querySelectorAll('section, .card, .why-item, .p-item, .value-item, .contact-cell, .hero').forEach(el => {
    el.classList.add('fade-up');
  });

  const fadeObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        obs.unobserve(entry.target); // Only animate once
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -50px 0px' });
  
  document.querySelectorAll('.fade-up').forEach(el => fadeObserver.observe(el));

  // Set current year in footer
  const yearEl = document.getElementById('year');
  if(yearEl) yearEl.textContent = new Date().getFullYear();

  
  // Navigation & Scrollspy
  const sections = document.querySelectorAll('#home, #about, #products, #services, #gallery, #contact');
  const navLinks = document.querySelectorAll('nav a');

  window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (window.scrollY >= (sectionTop - 200)) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(a => {
      a.classList.remove('active');
      if (a.getAttribute('href') === '#' + current) {
        a.classList.add('active');
      }
    });
  });

  // Smooth scroll click
  navLinks.forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = a.getAttribute('href').replace('#', '');
      const target = document.getElementById(targetId);
      if(target) {
        window.scrollTo({
          top: target.offsetTop - 80, // offset for fixed header
          behavior: 'smooth'
        });
      }
      const navMenu = document.getElementById('navMenu');
      if(navMenu) navMenu.classList.remove('open');
    });
  });


  const navToggle = document.getElementById('navToggle');
  if(navToggle) {
    navToggle.addEventListener('click', ()=>{
      document.getElementById('navMenu').classList.toggle('open');
    });
  }

  // Product Tech Tabs
  document.querySelectorAll('.tab-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('on'));
      document.querySelectorAll('.tab-panel').forEach(p=>p.classList.remove('on'));
      btn.classList.add('on');
      const panel = document.getElementById('tab-'+btn.dataset.tab);
      if(panel) panel.classList.add('on');
    });
  });

  // Scroll Progress and Scroll-to-Top FAB
  const progressBar = document.getElementById('scroll-progress');
  const fabTop = document.getElementById('fab-top');

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    
    if (progressBar && scrollHeight > 0) {
      const progress = (scrollTop / scrollHeight) * 100;
      progressBar.style.width = progress + '%';
    }

    if (fabTop) {
      if (scrollTop > 300) {
        fabTop.classList.add('show');
      } else {
        fabTop.classList.remove('show');
      }
    }
  });

  if (fabTop) {
    fabTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  
  
  // Animated Number Counters using requestAnimationFrame
  const counters = document.querySelectorAll('.num[data-target]');
  const duration = 2000; // 2 seconds

  function animateCounter(counter) {
    if (counter.dataset.animId) {
      cancelAnimationFrame(parseInt(counter.dataset.animId));
    }
    const target = +counter.getAttribute('data-target');
    const suffix = counter.getAttribute('data-suffix') || '';
    let startTimestamp = null;
    
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      // easeOutExpo
      const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      
      const current = Math.floor(easeProgress * target);
      counter.innerText = current + suffix;
      
      if (progress < 1) {
        counter.dataset.animId = window.requestAnimationFrame(step);
      }
    };
    counter.dataset.animId = window.requestAnimationFrame(step);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const counter = entry.target;
      if (entry.isIntersecting) {
        animateCounter(counter);
      } else {
        // Reset when out of view so it runs again
        if (counter.dataset.animId) cancelAnimationFrame(parseInt(counter.dataset.animId));
        counter.innerText = '0' + (counter.getAttribute('data-suffix') || '');
      }
    });
  }, { threshold: 0.1 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });

  // ─── Re-run counters on hero-meta mouseover ──────────────────────────────
  const heroMeta = document.querySelector('.hero-meta');
  if (heroMeta) {
    heroMeta.addEventListener('mouseenter', () => {
      heroMeta.querySelectorAll('.num[data-target]').forEach(counter => {
        animateCounter(counter);
      });
    });
  }

  // ─── Re-run word animation on hero h1 mouseover ──────────────────────────
  const heroH1 = document.querySelector('.hero-text-box h1');
  if (heroH1) {
    heroH1.addEventListener('mouseenter', () => {
      const words = heroH1.querySelectorAll('.w');
      words.forEach(w => {
        w.style.animation = 'none';
        w.offsetHeight; // force reflow
        w.style.animation = '';
      });
    });
  }

  // ─── Hero Slider with Dots ───────────────────────────────────────────────
  const slides = document.querySelectorAll('.hero-slide');
  const dots   = document.querySelectorAll('.hero-dot');
  let current  = 0;
  let timer    = null;

  function goTo(index) {
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = (index + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
  }

  function startAuto() {
    clearInterval(timer);
    timer = setInterval(() => goTo(current + 1), 6000);
  }

  // Dot click
  dots.forEach(dot => {
    dot.addEventListener('click', () => {
      goTo(+dot.dataset.index);
      startAuto(); // restart timer
    });
  });

  // Init
  goTo(0);
  startAuto();

});
