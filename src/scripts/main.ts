/**
 * Petic International site behaviour.
 * Sticky header shadow and scroll progress, back-to-top, mobile menu,
 * reveal-on-scroll animations, animated counters and the contact form.
 */

function setupHeader(): void {
  const header = document.querySelector<HTMLElement>('.header');
  const progress = document.querySelector<HTMLElement>('.header__progress');
  const toTop = document.querySelector<HTMLButtonElement>('.to-top');

  const onScroll = (): void => {
    const y = window.scrollY;
    header?.classList.toggle('is-scrolled', y > 10);
    toTop?.classList.toggle('is-visible', y > 600);
    if (progress) {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = `${max > 0 ? Math.min(y / max, 1) * 100 : 0}%`;
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  toTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

function setupMobileMenu(): void {
  const toggle = document.querySelector<HTMLButtonElement>('.menu-toggle');
  if (!toggle) return;

  const setOpen = (open: boolean): void => {
    document.body.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
  };

  toggle.addEventListener('click', () => setOpen(!document.body.classList.contains('menu-open')));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') setOpen(false);
  });
}

function setupReveal(): void {
  const items = document.querySelectorAll<HTMLElement>('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach((el) => el.classList.add('is-in'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      }
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' },
  );
  items.forEach((el) => io.observe(el));
}

function setupCounters(): void {
  const counters = document.querySelectorAll<HTMLElement>('[data-count]');
  if (!counters.length || !('IntersectionObserver' in window)) return;

  const animate = (el: HTMLElement): void => {
    const target = parseInt(el.dataset.count ?? '0', 10);
    const suffix = el.dataset.suffix ?? '';
    const duration = 1400;
    let start: number | null = null;
    const tick = (ts: number): void => {
      start ??= ts;
      const p = Math.min((ts - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      el.textContent = `${Math.round(target * eased)}${suffix}`;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        animate(entry.target as HTMLElement);
        io.unobserve(entry.target);
      }
    },
    { threshold: 0.6 },
  );
  counters.forEach((el) => io.observe(el));
}

/**
 * Contact form. Without a `data-endpoint`, it opens the visitor's mail client with the
 * message pre-filled. With one (for example a Formspree URL) it posts the form there.
 */
function setupContactForm(): void {
  const form = document.querySelector<HTMLFormElement>('.form[data-contact]');
  const status = form?.querySelector<HTMLElement>('.form__status');
  if (!form || !status) return;

  const show = (message: string): void => {
    status.textContent = message;
    status.classList.add('is-visible');
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const field = (name: string): string => String(data.get(name) ?? '');
    const endpoint = form.dataset.endpoint;

    if (endpoint) {
      fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then((r) => {
          if (!r.ok) throw new Error(`Form service responded ${r.status}`);
          show('Thank you. Your message has been sent and our team will reply shortly.');
          form.reset();
        })
        .catch(() =>
          show('Sorry, the message could not be sent. Please email info@petic-global.com directly.'),
        );
      return;
    }

    const subject = encodeURIComponent(`[Website enquiry] ${field('subject') || 'General enquiry'}`);
    const body = encodeURIComponent(
      `Name: ${field('name')}\nEmail: ${field('email')}\nPhone: ${field('phone') || '-'}\n` +
        `Sector: ${field('sector') || '-'}\n\n${field('message')}`,
    );
    window.location.href = `mailto:info@petic-global.com?subject=${subject}&body=${body}`;
    show(
      'Your email client should now open with the message pre-filled. If it does not, write to info@petic-global.com.',
    );
  });
}

setupHeader();
setupMobileMenu();
setupReveal();
setupCounters();
setupContactForm();
