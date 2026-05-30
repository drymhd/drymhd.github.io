document.addEventListener('DOMContentLoaded', () => {
  // --- THEME SELECTOR ---
  const themeBtn = document.getElementById('theme-toggle');
  const systemThemeDark = window.matchMedia('(prefers-color-scheme: dark)');

  // Retrieve saved theme or default to dark
  const savedTheme = localStorage.getItem('theme') || (systemThemeDark.matches ? 'dark' : 'dark');
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  themeBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
  });

  function updateThemeIcon(theme) {
    if (theme === 'light') {
      themeBtn.innerHTML = `
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m11.314 11.314l.707.707M12 7a5 5 0 100 10 5 5 0 000-10z" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/>
        </svg>
      `;
      themeBtn.setAttribute('aria-label', 'Switch to dark theme');
    } else {
      themeBtn.innerHTML = `
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/>
        </svg>
      `;
      themeBtn.setAttribute('aria-label', 'Switch to light theme');
    }
  }

  // --- MOBILE NAV TOGGLE ---
  const menuToggle = document.getElementById('menu-toggle');
  const navLinks = document.querySelector('.nav-links');

  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const isOpen = navLinks.classList.contains('open');
    menuToggle.innerHTML = isOpen ? '✕' : '☰';
    menuToggle.setAttribute('aria-expanded', isOpen);
  });

  // Close mobile menu when link is clicked
  const navItems = document.querySelectorAll('.nav-links a');
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      if (navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        menuToggle.innerHTML = '☰';
        menuToggle.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // --- INTERSECTION OBSERVER FOR ACTIVE NAV & SCROLL REVEAL FALLBACK ---
  const sections = document.querySelectorAll('section');
  const scrollReveals = document.querySelectorAll('.scroll-reveal');

  const navObserverOptions = {
    root: null,
    rootMargin: '-50% 0px -50% 0px', // trigger when section occupies middle of screen
    threshold: 0
  };

  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navItems.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, navObserverOptions);

  sections.forEach(section => {
    navObserver.observe(section);
  });

  // Intersection Observer Fallback for Scroll Reveal (if CSS animation-timeline is not supported)
  const supportsAnimationTimeline = CSS.supports('animation-timeline', 'view()');

  if (!supportsAnimationTimeline) {
    const revealObserverOptions = {
      root: null,
      rootMargin: '0px 0px -15% 0px',
      threshold: 0.05
    };

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0) scale(1)';
          revealObserver.unobserve(entry.target);
        }
      });
    }, revealObserverOptions);

    scrollReveals.forEach(reveal => {
      // Set initial styles for fallback
      reveal.style.opacity = '0';
      reveal.style.transform = 'translateY(30px) scale(0.98)';
      reveal.style.transition = 'opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
      revealObserver.observe(reveal);
    });
  }
});
