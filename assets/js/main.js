/* PETIC GLOBAL — site scripts (no dependencies) */
(function () {
  'use strict';

  // Sticky header shadow
  var header = document.querySelector('.header');
  var toTop = document.querySelector('.to-top');
  var progress = document.querySelector('.header__progress');
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (progress) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = (max > 0 ? Math.min(y / max, 1) * 100 : 0) + '%';
    }
    if (header) header.classList.toggle('is-scrolled', y > 10);
    if (toTop) toTop.classList.toggle('is-visible', y > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Back to top
  if (toTop)
    toTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('menu-open')) {
        document.body.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.classList.add('is-in');
            io.unobserve(en.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' },
    );
    items.forEach(function (el) {
      io.observe(el);
    });
  } else {
    items.forEach(function (el) {
      el.classList.add('is-in');
    });
  }

  // Count-up stats
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (en) {
          if (!en.isIntersecting) return;
          var el = en.target,
            target = parseInt(el.getAttribute('data-count'), 10),
            suffix = el.getAttribute('data-suffix') || '';
          var start = null,
            dur = 1400;
          function tick(ts) {
            if (!start) start = ts;
            var p = Math.min((ts - start) / dur, 1),
              eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased) + suffix;
            if (p < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
          cio.unobserve(el);
        });
      },
      { threshold: 0.6 },
    );
    counters.forEach(function (el) {
      cio.observe(el);
    });
  }

  // Contact form: opens the visitor's mail client with a pre-filled message.
  // Replace with a form service (e.g. Formspree) by setting data-endpoint on the <form>.
  var form = document.querySelector('.form[data-contact]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = new FormData(form);
      var status = form.querySelector('.form__status');
      var endpoint = form.getAttribute('data-endpoint');
      if (endpoint) {
        fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (r) {
            if (!r.ok) throw new Error();
            status.textContent = 'Thank you. Your message has been sent and our team will reply shortly.';
            status.classList.add('is-visible');
            form.reset();
          })
          .catch(function () {
            status.textContent = 'Sorry, the message could not be sent. Please email info@petic-global.com directly.';
            status.classList.add('is-visible');
          });
        return;
      }
      var subject = encodeURIComponent('[Website enquiry] ' + (data.get('subject') || 'General enquiry'));
      var body = encodeURIComponent(
        'Name: ' +
          data.get('name') +
          '\nEmail: ' +
          data.get('email') +
          '\nPhone: ' +
          (data.get('phone') || '-') +
          '\nSector: ' +
          (data.get('sector') || '-') +
          '\n\n' +
          data.get('message'),
      );
      window.location.href = 'mailto:info@petic-global.com?subject=' + subject + '&body=' + body;
      status.textContent =
        'Your email client should now open with the message pre-filled. If it does not, write to info@petic-global.com.';
      status.classList.add('is-visible');
    });
  }

  // Footer year
  var year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();
