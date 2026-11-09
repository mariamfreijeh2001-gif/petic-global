# Generates the static PETIC GLOBAL site pages (run: python3 tools/build.py)
import os
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = 'PETIC GLOBAL'
PHONE = '+974 4441 1083'; PHONE_RAW = '+97444411083'
EMAIL = 'info@petic-global.com'; SALES = 'sales@petic-global.com'; CEO = 'ceo@petic-global.com'
ADDRESS = '1st Floor, Office 08, Building 382, Street 340, Salwa Road, Zone 55, Doha, Qatar'
TZ_ADDRESS = 'Kisutu Street 2423, Dar es Salaam, Tanzania'
PROFILE = 'assets/docs/PETIC-Global-Company-Profile.pdf'
QUOTE = 'Chase the vision, not the money. The money will end up following you.'

I = {
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'chev': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>',
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>',
 'phone': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 'up': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
 'fb': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.6 1.6-1.6h1.7V4.4c-.3 0-1.3-.1-2.5-.1-2.5 0-4.1 1.5-4.1 4.2v2.3H7.4V14h2.8v8h3.3z"/></svg>',
 'ig': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 'tw': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.7 3h3l-6.6 7.6L22 21h-6.1l-4.8-6.3L5.6 21h-3l7.1-8.1L2 3h6.3l4.3 5.7L17.7 3zm-1.1 16.2h1.7L7.5 4.7H5.7l10.9 14.5z"/></svg>',
 'in': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.9 8.5H3.5V21h3.4V8.5zM5.2 3a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM21 13.3c0-3.6-2-5.1-4.5-5.1-1.8 0-2.9.9-3.4 1.7V8.5H9.8V21h3.4v-6.2c0-1.6.3-3.2 2.3-3.2s2.1 1.9 2.1 3.3V21H21v-7.7z"/></svg>',
 'building': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16M15 9h2a2 2 0 0 1 2 2v10M9 7h2M9 11h2M9 15h2"/></svg>',
 'road': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21L9 3M20 21L15 3M12 5v3M12 11v3M12 17v3"/></svg>',
 'leaf': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c0-9 5-15 16-16-1 11-7 16-16 16z"/><path d="M4 20c4-5 8-8 12-10"/></svg>',
 'flame': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22c4 0 7-3 7-7 0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-3-2-5-3 3-5 6-5 9 0 4 3 7 7 7z"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5l8-3z"/><path d="M9 12l2 2 4-4"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 'users': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4.5-6.2"/></svg>',
 'globe': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>',
 'layers': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5M3 17l9 5 9-5"/></svg>',
 'trophy': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4M6 3h12v6a6 6 0 0 1-12 0V3z"/><path d="M6 5H3v2a3 3 0 0 0 3 3M18 5h3v2a3 3 0 0 1-3 3"/></svg>',
 'cog': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3h0a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8v0a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
 'doc': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>',
 'download': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M4 20h16"/></svg>',
 'target': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg>',
 'eye': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
 'handshake': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 9l4-4 6 2 6-2 4 4-3 7-7 5-7-5-3-7z"/><path d="M8 13l3 3 5-5"/></svg>',
}

NAV = [
 ('index.html', 'Home'),
 ('about.html', 'About Us'),
 ('our-activities.html', 'Our Activities', [
    ('agriculture.html', 'Agriculture'),
    ('roads-construction.html', 'Roads Construction'),
    ('civil-works-and-construction.html', 'Civil Works & Construction'),
    ('oil-and-gas.html', 'Oil & Gas'),
 ]),
 ('contact.html', 'Contact Us'),
]
ACTIVITY_PAGES = {x[0] for x in NAV[2][2]}

def nav_html(current):
    items = []
    for entry in NAV:
        href, label = entry[0], entry[1]
        subs = entry[2] if len(entry) > 2 else None
        active = (current == href) or (subs and current in ACTIVITY_PAGES)
        cls = ' class="is-active"' if active else ''
        if subs:
            sub = ''.join(f'<li><a href="{h}"{" class=\"is-active\"" if current == h else ""}>{l}</a></li>' for h, l in subs)
            items.append(f'<li class="has-sub"><a href="{href}"{cls}>{label}{I["chev"]}</a><ul class="sub">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
    return ''.join(items)

def mobile_nav_html(current):
    items = []
    for entry in NAV:
        href, label = entry[0], entry[1]
        subs = entry[2] if len(entry) > 2 else None
        cls = ' class="is-active"' if current == href else ''
        items.append(f'<li><a href="{href}"{cls}>{label}</a></li>')
        if subs:
            items.append('<li><ul class="mobile-sub">' + ''.join(f'<li><a href="{h}"{" class=\"is-active\"" if current == h else ""}>{l}</a></li>' for h, l in subs) + '</ul></li>')
    return ''.join(items)

def header(current):
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar">
  <div class="container">
    <div class="topbar__contacts">
      <a href="tel:{PHONE_RAW}">{I['phone']}{PHONE}</a>
      <a href="mailto:{EMAIL}">{I['mail']}{EMAIL}</a>
      <a href="contact.html">{I['pin']}Doha, Qatar &middot; Dar es Salaam, Tanzania</a>
    </div>
    <div class="topbar__social">
      <a href="#" aria-label="Facebook">{I['fb']}</a>
      <a href="#" aria-label="Instagram">{I['ig']}</a>
      <a href="#" aria-label="X (Twitter)">{I['tw']}</a>
      <a href="#" aria-label="LinkedIn">{I['in']}</a>
    </div>
  </div>
</div>
<header class="header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="{SITE} home">
      <img src="assets/img/logo.png" alt="{SITE}" width="124" height="50">
    </a>
    <nav aria-label="Primary"><ul class="nav">{nav_html(current)}</ul></nav>
    <a class="btn btn--gold btn--sm header__cta" href="{PROFILE}" target="_blank" rel="noopener">{I['download']}Download Profile</a>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span></span></button>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  <ul>{mobile_nav_html(current)}</ul>
  <a class="btn btn--gold" href="{PROFILE}" target="_blank" rel="noopener">{I['download']}Download Company Profile</a>
  <p class="mobile-nav__meta">Call <a href="tel:{PHONE_RAW}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</nav>
'''

def cta(title='Have a project in mind?', text='You’re welcome to send a message or give us a call. Our team in Doha and Dar es Salaam will get back to you promptly.'):
    return f'''
<section class="cta">
  <div class="container">
    <div class="reveal">
      <span class="eyebrow">Let’s work together</span>
      <h2>{title}</h2>
      <p>{text}</p>
    </div>
    <div class="cta__actions reveal" data-delay="1">
      <a class="btn btn--gold" href="contact.html">Send a message{I['arrow']}</a>
      <a class="btn btn--ghost-light" href="tel:{PHONE_RAW}">{I['phone']}{PHONE}</a>
    </div>
  </div>
</section>
'''

FOOTER = f'''
<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div>
        <a class="brand" href="index.html" style="background:#fff;padding:8px 12px;border-radius:12px;display:inline-flex"><img src="assets/img/logo.png" alt="{SITE}" width="110" height="45"></a>
        <h4 style="margin-top:22px">About our company</h4>
        <p>The Petic group invested heavily in the Gulf States and Tanzania, building infrastructure and road projects. In its next phase the group moved into manufacturing household and pharmaceutical products in Rwanda, and gas cylinders in Uganda.</p>
        <div class="footer__social">
          <a href="#" aria-label="Facebook">{I['fb']}</a><a href="#" aria-label="Instagram">{I['ig']}</a><a href="#" aria-label="X (Twitter)">{I['tw']}</a><a href="#" aria-label="LinkedIn">{I['in']}</a>
        </div>
      </div>
      <div>
        <h4>Useful links</h4>
        <div class="footer__links">
          <a href="index.html">Home</a><a href="about.html">About us</a><a href="our-activities.html">Our activities</a><a href="contact.html">Contact us</a><a href="{PROFILE}" target="_blank" rel="noopener">Company profile (PDF)</a>
        </div>
      </div>
      <div>
        <h4>Our activities</h4>
        <div class="footer__links">
          <a href="agriculture.html">Agriculture</a><a href="roads-construction.html">Roads construction</a><a href="civil-works-and-construction.html">Civil works &amp; construction</a><a href="oil-and-gas.html">Oil &amp; gas</a>
        </div>
      </div>
      <div>
        <h4>Contact us</h4>
        <ul class="footer__contact">
          <li>{I['pin']}<span>{ADDRESS}</span></li>
          <li>{I['phone']}<a href="tel:{PHONE_RAW}">{PHONE}</a></li>
          <li>{I['mail']}<span><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="mailto:{SALES}">{SALES}</a><br><a href="mailto:{CEO}">{CEO}</a></span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; <span data-year>2025</span> {SITE}. All rights reserved.</span>
      <span>Construction &middot; Infrastructure &middot; Agriculture &middot; Oil &amp; Gas</span>
    </div>
  </div>
</footer>
<button class="to-top" aria-label="Back to top">{I['up']}</button>
<script src="assets/js/main.js"></script>
'''

def page(filename, title, description, body, current=None):
    current = current or filename
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {SITE}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#002e42">
<meta property="og:title" content="{title} | {SITE}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/hero-oil-rig.jpg">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="assets/img/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    with open(os.path.join(OUT, filename), 'w') as f:
        f.write(html)
    print('wrote', filename)

def page_hero(crumb, h1, lead, img, alt):
    return f'''
<section class="page-hero">
  <img src="assets/img/{img}" alt="{alt}">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>{crumb}</span></nav>
    <h1 class="reveal">{h1}</h1>
    <p class="lead reveal" data-delay="1">{lead}</p>
    <p class="page-hero__quote reveal" data-delay="2">“{QUOTE}”</p>
  </div>
</section>
'''

def side_nav(current):
    links = ''.join(f'<a href="{h}"{" class=\"is-active\"" if current == h else ""}>{l}{I["arrow"]}</a>' for h, l in NAV[2][2])
    return f'''
<aside class="sidebar">
  <div class="side-card">
    <h4>Our activities</h4>
    <nav class="side-nav">{links}</nav>
  </div>
  <div class="side-card side-card--navy">
    <h4>Talk to our team</h4>
    <p><strong>{PHONE}</strong><br>{EMAIL}</p>
    <p style="font-size:.9rem">{ADDRESS}</p>
    <a class="btn btn--gold" href="contact.html">Request a quote{I['arrow']}</a>
  </div>
  <div class="side-card">
    <h4>Company profile</h4>
    <p class="muted" style="font-size:.95rem">Download our full corporate profile with capabilities, projects and licences.</p>
    <a class="link-arrow" href="{PROFILE}" target="_blank" rel="noopener" style="margin-top:10px">Download PDF{I['download']}</a>
  </div>
</aside>
'''

def service_list(items, icon='check'):
    return '<div class="services">' + ''.join(f'<div class="service"><i>{I[icon]}</i><span>{s}</span></div>' for s in items) + '</div>'

# ---------------------------------------------------------------- HOME
home = f'''
<section class="hero">
  <div class="hero__media"><img src="assets/img/hero-oil-rig.jpg" alt="Oil and gas drilling rig with pipelines at sunset"></div>
  <div class="container hero__grid">
    <div>
      <span class="hero__tag reveal"><b>Since 2002</b> Gulf States &middot; East Africa</span>
      <h1 class="reveal" data-delay="1">Building <em>your dreams</em> across the Gulf and Africa.</h1>
      <p class="lead reveal" data-delay="2">Only if you plan with a good degree of foresight can serious mistakes be avoided. Foresight is a given at PETIC GLOBAL: construction, infrastructure, agriculture and oil &amp; gas services delivered with one simple promise, <strong>can do</strong>.</p>
      <div class="hero__actions reveal" data-delay="3">
        <a class="btn btn--gold" href="our-activities.html">Explore our activities{I['arrow']}</a>
        <a class="btn btn--ghost-light" href="about.html">About the group</a>
      </div>
      <p class="hero__quote reveal" data-delay="4">“{QUOTE}”</p>
    </div>
    <div class="hero__panel reveal" data-delay="2">
      <div class="hero__card">
        <h3>What we do</h3>
        <div class="hero__list">
          <a href="civil-works-and-construction.html"><span><i>{I['building']}</i>Civil Works &amp; Construction</span>{I['arrow']}</a>
          <a href="roads-construction.html"><span><i>{I['road']}</i>Roads Construction</span>{I['arrow']}</a>
          <a href="agriculture.html"><span><i>{I['leaf']}</i>Agriculture</span>{I['arrow']}</a>
          <a href="oil-and-gas.html"><span><i>{I['flame']}</i>Oil &amp; Gas</span>{I['arrow']}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="stats" aria-label="Key figures">
  <div class="container">
    <div class="stat reveal"><i>{I['trophy']}</i><div><b><span data-count="77" data-suffix="+">77+</span></b><span>Projects completed worldwide</span></div></div>
    <div class="stat reveal" data-delay="1"><i>{I['globe']}</i><div><b><span data-count="6">6</span></b><span>Countries of operation</span></div></div>
    <div class="stat reveal" data-delay="2"><i>{I['layers']}</i><div><b><span data-count="4">4</span></b><span>Business sectors</span></div></div>
    <div class="stat reveal" data-delay="3"><i>{I['pin']}</i><div><b><span data-count="3">3</span></b><span>Operating hubs: Al Khobar, Jubail, Qatar</span></div></div>
  </div>
</section>

<section class="section" id="about">
  <div class="container split">
    <div class="split__media reveal">
      <img src="assets/img/steel-frame-worker.jpg" alt="Engineer working on a steel structure">
      <div class="split__badge"><b>Can do!</b><span>The PETIC GLOBAL philosophy, fulfilled over and over.</span></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Our specialties</span>
      <h2>Reliability, from feasibility to hand-over.</h2>
      <p class="lead">East Trading &amp; its main group PETIC GLOBAL International’s project and construction management services include early involvement during the feasibility and design development stages, securing value engineering alternatives and full scrutiny of constructability issues.</p>
      <p>Planning and coordination of construction activities and designs are delivered in time to secure uninterrupted construction activities. We continually strive to improve our performance and to complete projects within the scheduled time, while maintaining standards of quality and safety during execution.</p>
      <ul class="checks">
        <li>{I['check']}<span>Early involvement during feasibility and design development</span></li>
        <li>{I['check']}<span>Value engineering alternatives and constructability review</span></li>
        <li>{I['check']}<span>Quality management and excellent safety practices applied daily</span></li>
        <li>{I['check']}<span>Customer-oriented synergy arising from our partnerships</span></li>
      </ul>
      <div style="margin-top:28px"><a class="btn btn--navy" href="about.html">More about us{I['arrow']}</a></div>
    </div>
  </div>
</section>

<section class="section section--soft" id="activities">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="reveal"><span class="eyebrow">What we do</span><h2>Our activities.</h2></div>
      <p class="lead reveal" data-delay="1">Four sectors, one standard: quality, safety and delivery on time across the Gulf States and East Africa.</p>
    </div>
    <div class="grid grid--4">
      <a class="card reveal" href="civil-works-and-construction.html">
        <div class="card__media"><img src="assets/img/construction-worker.jpg" alt="Construction worker on site" loading="lazy"><i class="card__icon">{I['building']}</i></div>
        <div class="card__body"><h3>Civil Works &amp; Construction</h3><p>East Trading &amp; Manufacturing Company holds a portfolio of strategic investment in construction equipment and a substantial fleet of mobile plant.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="1" href="roads-construction.html">
        <div class="card__media"><img src="assets/img/road-asphalt.jpg" alt="Asphalt paving machinery on a new road" loading="lazy"><i class="card__icon">{I['road']}</i></div>
        <div class="card__body"><h3>Roads Construction</h3><p>A hard-earned reputation for the construction quality of asphalt roads and highways, from large highways to small commercial site developments.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="2" href="agriculture.html">
        <div class="card__media"><img src="assets/img/agri-harvest-1.jpg" alt="Combine harvester working a wheat field" loading="lazy"><i class="card__icon">{I['leaf']}</i></div>
        <div class="card__body"><h3>Agriculture</h3><p>AgriPro is a leading agriculture company dedicated to transforming arable lands into highly productive and sustainable agricultural ventures.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="3" href="oil-and-gas.html">
        <div class="card__media"><img src="assets/img/refinery-plant.jpg" alt="Oil and gas processing plant" loading="lazy"><i class="card__icon">{I['flame']}</i></div>
        <div class="card__body"><h3>Oil &amp; Gas</h3><p>Our clients include major oil and gas companies, projects and contractors in Yemen, with associations with renowned manufacturers worldwide.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <div class="split__media reveal">
      <img src="assets/img/industrial-worker.jpg" alt="Worker inspecting industrial equipment">
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Why choose us</span>
      <h2>The benefit of working with our company.</h2>
      <p class="lead">PETIC GLOBAL holds a portfolio of strategic investment in construction equipment, property and a substantial fleet of mobile plant in Saudi Arabia. This complements the company’s multi-domestic growth strategy, which centres on its operating hubs in Al Khobar, Jubail and Qatar.</p>
      <p>We embrace holistic development and support for employees, with the aim of being a first-choice employer.</p>
      <div class="grid grid--2" style="margin-top:26px;gap:14px">
        {''.join(f'<div class="service"><i>{I["check"]}</i><span>{s}</span></div>' for s in ['Cost estimating','Pre-construction services','Historic restoration','Infrastructure solutions','General contractor','Industrial engineering'])}
      </div>
      <div style="margin-top:28px"><a class="btn btn--ghost" href="our-activities.html">See more{I['arrow']}</a></div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Our services</span>
      <h2>First-class construction and infrastructure.</h2>
      <p class="lead" style="color:#b9cad3">From architecture to industrial engineering, we take projects from concept through construction, commissioning and long-term operation and maintenance.</p>
    </div>
    <div class="grid grid--3">
      <div class="feature reveal"><i>{I['building']}</i><h3>Construction</h3><p>Infrastructure solutions and first-class construction, delivered by skilled teams and a modern fleet of equipment.</p></div>
      <div class="feature reveal" data-delay="1"><i>{I['layers']}</i><h3>Architecture</h3><p>Industrial engineering and construction, from innovative technical concepts to front-end engineering designs.</p></div>
      <div class="feature reveal" data-delay="2"><i>{I['cog']}</i><h3>Industrial engineering</h3><p>Oil rigs or refineries, power stations or steel mills, piping, mechanical and construction, whatever the project.</p></div>
      <div class="feature reveal"><i>{I['eye']}</i><h3>Interior design</h3><p>Architectural finishing works, renovation and refurbishment of residential complexes, commercial buildings and industrial facilities.</p></div>
      <div class="feature reveal" data-delay="1"><i>{I['road']}</i><h3>Infrastructure</h3><p>Roads, bridges, drainage, water supply, sewage, electrical, telecommunications and CATV networks.</p></div>
      <div class="feature reveal" data-delay="2"><i>{I['globe']}</i><h3>Skyscrapers &amp; city landmarks</h3><p>Design-build projects and construction management for landmark developments in the Gulf and East Africa.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="reveal"><span class="eyebrow">Reliability</span><h2>Systematically achieving the optimum.</h2></div>
      <p class="lead reveal" data-delay="1">It is not without reason that PETIC GLOBAL is one of the companies able to document their competence in black and white for the benefit of our customers.</p>
    </div>
    <div class="pillars">
      <div class="pillar reveal"><h3>Our strategy</h3><p>Our strategies, structure and systems are focused on creating constant customer satisfaction by delivering services, solutions and products that are qualitative and cost effective.</p></div>
      <div class="pillar reveal" data-delay="1"><h3>Our promise</h3><p>The PETIC GLOBAL philosophy can be put into one simple formula: can do! That promise remains the highest factor guiding our actions in future.</p></div>
      <div class="pillar reveal" data-delay="2"><h3>Our standard</h3><p>A high quality standard that makes the group a successful enterprise, brought to life daily through quality management and excellent safety practices.</p></div>
    </div>
  </div>
</section>

<section class="section section--navy section--tight">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">How we work</span><h2>From plan to hand-over.</h2></div>
    <div class="steps">
      <div class="step reveal"><h3>Offering construction plans</h3><p>Early involvement during feasibility and design development, securing value engineering alternatives.</p></div>
      <div class="step reveal" data-delay="1"><h3>Project assignment</h3><p>Planning and coordination of construction activities and designs, delivered in time to keep work uninterrupted.</p></div>
      <div class="step reveal" data-delay="2"><h3>Building the project</h3><p>Execution within the scheduled time while maintaining our standards of quality and safety.</p></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Testimonials</span><h2>Building the future cities.</h2></div>
    <div class="grid grid--3">
      <div class="quote reveal"><h3>Unique and influential solutions</h3><p>Urban design draws together the many strands of place-making, environmental stewardship, social equity and economic viability into the creation of places with distinct beauty and identity.</p></div>
      <div class="quote reveal" data-delay="1"><h3>Building the idea of future</h3><p>As the complexity of buildings increases, the field of architecture has become multi-disciplinary, combining technological expertise with discipline.</p></div>
      <div class="quote reveal" data-delay="2"><h3>Engineering and design combined</h3><p>A unique combination of engineering and design, creating places with distinct beauty and identity for the communities we serve.</p></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Our partners</span><h2>Trusted by industry partners.</h2></div>
    <div class="partners reveal">
      <div class="partner"><img src="assets/img/partner-almaha.jpg" alt="Almaha for Industry" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-linex.jpg" alt="LINE-X" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-petro-sharq.jpg" alt="Petro Sharq Group" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-teamone.jpg" alt="TeamOne Shipping &amp; Clearing" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-nature-petroleum.jpg" alt="Nature for Petroleum, Gas and Minerals" loading="lazy"></div>
    </div>
  </div>
</section>
{cta()}
'''
page('index.html', 'Construction, Infrastructure, Agriculture & Oil and Gas', 'PETIC GLOBAL delivers construction, roads, civil works, agriculture and oil & gas services across the Gulf States and East Africa. Chase the vision, not the money.', home)

# ---------------------------------------------------------------- ABOUT
about = page_hero('About us', 'About PETIC GLOBAL.', 'A group established across the Middle East and Africa, providing quality construction projects and engineering services in the sector of oil &amp; gas, infrastructure, manufacturing and agriculture.', 'site-engineer.jpg', 'Site engineer overseeing construction works') + f'''
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>Established worldwide, rooted in the Gulf and Africa.</h2>
      <p class="lead">Sheik Salah has been in worldwide business, establishing various companies in the Middle East and Africa, providing quality construction projects and engineering services in the sector of oil &amp; gas.</p>
      <p>At the beginning, the Petic group invested heavily in the Gulf States and Tanzania by building infrastructure and road projects. In its next phase the group moved into manufacturing household and pharmaceutical products in Rwanda, and gas cylinders in Uganda.</p>
      <p>The group is now planning to represent Chinese car manufacturers by creating an assembling workshop in Africa.</p>
      <div style="margin-top:26px;display:flex;gap:14px;flex-wrap:wrap"><a class="btn btn--navy" href="{PROFILE}" target="_blank" rel="noopener">{I['download']}Company profile</a><a class="btn btn--ghost" href="contact.html">Contact us</a></div>
    </div>
    <div class="split__media reveal" data-delay="1">
      <img src="assets/img/gas-plant-portrait.jpg" alt="Gas processing plant" style="aspect-ratio:4/5">
      <div class="split__badge"><b>77+</b><span>projects of various sizes completed for private and public sectors worldwide.</span></div>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="grid grid--3">
      <div class="feature reveal"><i>{I['trophy']}</i><h3>Projects</h3><p>The PETIC GLOBAL philosophy can be put into one simple formula: can do! That is a promise we have been fulfilling over and over, and it will remain the highest factor guiding our actions in future. We continually strive to improve our performance.</p></div>
      <div class="feature reveal" data-delay="1"><i>{I['target']}</i><h3>Mission</h3><p>Oil rigs or refineries, power stations or steel mills, piping, mechanical, construction: whatever the project, we can develop our involvement in those areas which allow our clients to take a back seat. Why? Because they know that everything which is or could be important is in good hands.</p></div>
      <div class="feature reveal" data-delay="2"><i>{I['eye']}</i><h3>Think</h3><p>Only if you plan with a good degree of foresight can serious mistakes be avoided. Foresight is a given at PETIC GLOBAL.</p></div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Our journey</span>
      <h2>From infrastructure to manufacturing.</h2>
      <p style="color:#b9cad3">The rapid growth of the group is driven by its bold vision, strong entrepreneurial spirit and devotion to customer satisfaction, delivering excellent quality products and services.</p>
      <ul class="timeline" style="margin-top:30px">
        <li class="reveal"><span class="tag">Phase one</span><h3>Gulf States &amp; Tanzania</h3><p>Heavy investment in infrastructure and road projects, backed by a substantial fleet of mobile plant in the Gulf States and East Africa.</p></li>
        <li class="reveal" data-delay="1"><span class="tag">Phase two</span><h3>Rwanda &amp; Uganda</h3><p>Manufacturing of household and pharmaceutical products in Rwanda, and gas cylinders in Uganda.</p></li>
        <li class="reveal" data-delay="2"><span class="tag">Next</span><h3>Automotive assembly in Africa</h3><p>Representing Chinese car manufacturers by creating an assembling workshop in Africa.</p></li>
      </ul>
    </div>
    <div class="reveal" data-delay="1">
      <div class="side-card" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);color:#c8d6dd">
        <span class="eyebrow">East Africa</span>
        <h3 style="color:#fff">East Trading &amp; Manufacturing Company LTD</h3>
        <p style="color:var(--gold);font-weight:600">{TZ_ADDRESS}</p>
        <p>East Trading &amp; Manufacturing Company has been set up in Tanzania to provide quality construction services to real estate contractors, construction companies, and the civil engineering and infrastructure industries. The company established a successful track record through commitments to its customers within the operations and construction domain.</p>
        <p>After gaining extensive experience in building services, the company is moving forward to undertake complex and challenging civil engineering and building projects, extending its services from innovative technical concepts and front-end engineering designs to construction management, installation, commissioning and long-term operation and maintenance.</p>
        <p>The company holds a portfolio of strategic investments in the construction sector, owning a substantial fleet of mobile plant in the Gulf States and East Africa. This complements the company’s multi-domestic growth strategy, which focuses its operating hubs in both regions.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <div class="split__media reveal"><img src="assets/img/rebar-crew.jpg" alt="Construction crew preparing reinforcement steel"></div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Our mission</span>
      <h2>Contributing to the development of the Gulf States and East Africa.</h2>
      <p class="lead">Our mission is to participate in and contribute to the development and enrichment of services in the Gulf States and East Africa region, offering communities solutions in the construction sector and providing high quality engineering services.</p>
      <p>The company is fully committed to looking after the interests of its customers, employees, shareholders and communities. The group conducts its business ethically and profitably as a responsible corporate citizen. To accomplish our mission, we continually:</p>
      <ul class="checks">
        <li>{I['check']}<span>Enhance our competence with powerful, qualified engineering minds, enabling good communication at all levels to improve the operating environment.</span></li>
        <li>{I['check']}<span>Expand our presence in existing markets through fair pricing, respecting deadlines, quality products and good-value solutions, using advanced and creative technological approaches with continuous improvement of our operating systems.</span></li>
        <li>{I['check']}<span>Energize our employees by continuously promoting a culture that recognizes performance and valuable contributions, and celebrates successes.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Our licences</span><h2>Registered, certified and accountable.</h2><p class="lead">Certificates of incorporation, registrations and memberships held by the group’s companies in East Africa.</p></div>
    <div class="gallery reveal">
      <img src="assets/img/license-incorporation-tanzania.jpg" alt="Certificate of incorporation, Tanzania" loading="lazy" style="aspect-ratio:3/4;object-fit:contain;background:#fff">
      <img src="assets/img/license-registration-1.jpg" alt="Company registration document" loading="lazy" style="aspect-ratio:3/4;object-fit:contain;background:#fff">
      <img src="assets/img/license-registration-2.jpg" alt="Company registration document" loading="lazy" style="aspect-ratio:3/4;object-fit:contain;background:#fff">
      <img src="assets/img/license-uma-certificate.jpg" alt="Uganda Manufacturers Association membership certificate" loading="lazy" style="aspect-ratio:3/4;object-fit:contain;background:#fff">
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Our partners</span><h2>Trusted by global brands.</h2></div>
    <div class="partners reveal">
      <div class="partner"><img src="assets/img/partner-almaha.jpg" alt="Almaha for Industry" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-linex.jpg" alt="LINE-X" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-petro-sharq.jpg" alt="Petro Sharq Group" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-teamone.jpg" alt="TeamOne Shipping &amp; Clearing" loading="lazy"></div>
      <div class="partner"><img src="assets/img/partner-nature-petroleum.jpg" alt="Nature for Petroleum, Gas and Minerals" loading="lazy"></div>
    </div>
  </div>
</section>
{cta()}
'''
page('about.html', 'About Us', 'Learn about PETIC GLOBAL: our history across the Gulf States, Tanzania, Rwanda and Uganda, our mission, licences and partners.', about)

# ---------------------------------------------------------------- OUR ACTIVITIES
activities = page_hero('Our activities', 'Our activities.', 'Roads, civil works, agriculture and oil &amp; gas: four sectors delivered with dedicated efficiency, technology and a special focus on safety.', 'construction-worker.jpg', 'Construction worker on a building site') + f'''
<section class="section">
  <div class="container">
    <div class="grid grid--2" style="gap:32px">
      <a class="card reveal" href="roads-construction.html">
        <div class="card__media" style="aspect-ratio:16/10"><img src="assets/img/road-asphalt.jpg" alt="Asphalt paving" loading="lazy"><i class="card__icon">{I['road']}</i></div>
        <div class="card__body"><h3>Roads Construction</h3><p>East Trading &amp; Manufacturing Company has worked hard to maintain its reputation in the construction quality of asphalt roads and highways. It has successfully completed a range of large-scale road projects, from large highways to small commercial site developments, approaching every project with dedicated efficiency, technology and a special focus on safety.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="1" href="civil-works-and-construction.html">
        <div class="card__media" style="aspect-ratio:16/10"><img src="assets/img/site-engineer.jpg" alt="Site engineer on a construction site" loading="lazy"><i class="card__icon">{I['building']}</i></div>
        <div class="card__body"><h3>Civil Works &amp; Construction</h3><p>East Trading &amp; Manufacturing Company holds a portfolio of strategic investment in construction equipment, property and a substantial fleet of mobile construction equipment in Tanzania. This complements the company’s multi-domestic growth strategy, which focuses on its operating hubs in East African countries.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="2" href="agriculture.html">
        <div class="card__media" style="aspect-ratio:16/10"><img src="assets/img/agri-tractors.jpg" alt="Fleet of tractors in a field" loading="lazy"><i class="card__icon">{I['leaf']}</i></div>
        <div class="card__body"><h3>Agriculture</h3><p>AgriPro is a leading agriculture company dedicated to transforming arable lands into highly productive and sustainable agricultural ventures. With a strong commitment to innovation, technology and environmental responsibility, we provide comprehensive solutions for land development and irrigation systems.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="3" href="oil-and-gas.html">
        <div class="card__media" style="aspect-ratio:16/10"><img src="assets/img/hero-oil-rig.jpg" alt="Oil drilling rig" loading="lazy"><i class="card__icon">{I['flame']}</i></div>
        <div class="card__body"><h3>Oil &amp; Gas</h3><p>A well-resourced, full-service oilfield supply company serving the oil &amp; gas industry, with asset integrity, material supply and static equipment rehabilitation services. Our clients include major oil and gas companies, projects and contractors in Yemen.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section--navy section--tight">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Capabilities</span><h2>One group, end-to-end delivery.</h2></div>
    <div class="grid grid--3">
      <div class="feature reveal"><i>{I['doc']}</i><h3>Design &amp; engineering</h3><p>Design and construction engineering, design-build projects, front-end engineering designs.</p></div>
      <div class="feature reveal" data-delay="1"><i>{I['cog']}</i><h3>Construction &amp; management</h3><p>Construction and project management, procurement of materials and equipment, manpower supply.</p></div>
      <div class="feature reveal" data-delay="2"><i>{I['shield']}</i><h3>Operation &amp; maintenance</h3><p>Facilities maintenance, concrete repair and waterproofing, long-term operation and maintenance.</p></div>
    </div>
  </div>
</section>
{cta()}
'''
page('our-activities.html', 'Our Activities', 'Explore PETIC GLOBAL’s activities: roads construction, civil works and construction, agriculture, and oil & gas services.', activities)

# ---------------------------------------------------------------- AGRICULTURE
agri = page_hero('Agriculture', 'Agriculture: AgriPro.', 'Transforming arable lands into highly productive and sustainable agricultural ventures through land development, irrigation systems, technology and modern heavy machinery.', 'agri-tractors.jpg', 'Fleet of tractors lined up in a field') + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Company overview</span>
      <h2 class="reveal">A leading agriculture company.</h2>
      <p class="lead reveal" data-delay="1">AgriPro is a leading agriculture company dedicated to transforming arable lands into highly productive and sustainable agricultural ventures. With a strong commitment to innovation, technology and environmental responsibility, we provide comprehensive solutions for land development, irrigation systems and fertilizer management.</p>
      <p class="reveal" data-delay="1">Our state-of-the-art heavy machinery and expert agronomists ensure that every project we undertake thrives, contributing to global food security and agricultural sustainability.</p>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/agri-harvest-1.jpg" alt="Combine harvester unloading grain" loading="lazy">
        <img src="assets/img/agri-combine.jpg" alt="Combine harvester in a wheat field" loading="lazy">
        <img src="assets/img/agri-tractor-field.jpg" alt="Tractor tilling a field" loading="lazy">
      </div>

      <h3 class="reveal">Mission statement</h3>
      <p class="reveal">At AgriPro Innovations, our mission is to revolutionize agriculture by leveraging cutting-edge technology and sustainable practices to develop fertile lands, optimize water usage and maximize crop yields. We are dedicated to enhancing the agricultural sector’s productivity and sustainability.</p>

      <h3 class="reveal">Key services</h3>
      <div class="grid grid--2 reveal" style="gap:16px;margin-top:18px">
        <div class="feature"><i>{I['layers']}</i><h3>Land development</h3><p>Our land development experts assess and prepare agricultural lands, ensuring optimal soil conditions and topography for crop cultivation. We employ advanced land levelling and earthmoving machinery to create fertile and productive fields.</p></div>
        <div class="feature"><i>{I['target']}</i><h3>Irrigation systems</h3><p>We design, install and maintain advanced irrigation systems tailored to each project. Our solutions optimize water usage through precise scheduling and automation, ensuring crops receive the right amount of moisture at the right time.</p></div>
        <div class="feature"><i>{I['eye']}</i><h3>Technology integration</h3><p>We harness agricultural technology to monitor and manage soil health, crop growth and machinery operations. Our integrated approach helps farmers make data-driven decisions for higher yields and resource efficiency.</p></div>
        <div class="feature"><i>{I['cog']}</i><h3>Heavy machinery</h3><p>Our modern fleet includes tractors, ploughs, seeders and harvesters equipped with the latest technology, facilitating efficient farming operations and saving time and resources for our clients.</p></div>
      </div>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/agri-irrigation-1.jpg" alt="Centre-pivot irrigation system" loading="lazy">
        <img src="assets/img/agri-irrigation-2.jpg" alt="Irrigation sprinklers over crops" loading="lazy">
        <img src="assets/img/agri-tech.jpg" alt="Farmer using a mobile app in the field" loading="lazy">
      </div>

      <h3 class="reveal">Projects and achievements</h3>
      <p class="reveal">AgriPro Innovations has successfully transformed thousands of acres of land into highly productive and sustainable agricultural ventures. Our projects have not only increased crop yields but have also contributed to the economic development of rural communities.</p>
      <p class="reveal">AgriPro is your trusted partner in agriculture, offering comprehensive solutions for land development, irrigation systems, fertilizer management and technology integration. We are committed to driving agricultural innovation and sustainability for a prosperous future.</p>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/agri-planter.jpg" alt="Tractor with a precision planter" loading="lazy">
        <img src="assets/img/agri-soil.jpg" alt="Seedling with soil nutrient symbols" loading="lazy">
        <img src="assets/img/agri-handshake.jpg" alt="Handshake in front of farm machinery" loading="lazy">
      </div>
      <a class="btn btn--navy reveal" href="contact.html">Contact us{I['arrow']}</a>
    </div>
    {side_nav('agriculture.html')}
  </div>
</section>
{cta('Ready to develop your land?', 'Talk to our agronomists about land development, irrigation and machinery for your project.')}
'''
page('agriculture.html', 'Agriculture', 'AgriPro by PETIC GLOBAL: land development, irrigation systems, technology integration and heavy machinery for sustainable agriculture.', agri)

# ---------------------------------------------------------------- ROADS
roads = page_hero('Roads construction', 'Roads construction.', 'A reputation built on the construction quality of asphalt roads and highways, from large highways to small commercial site developments.', 'road-asphalt.jpg', 'Asphalt paving machinery on a new road') + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Overview</span>
      <h2 class="reveal">All phases of road construction.</h2>
      <p class="lead reveal" data-delay="1">East Trading &amp; Manufacturing Company has worked hard to maintain its reputation in the construction quality of asphalt roads and highways. It has successfully completed a range of large-scale road projects, from large highways to small commercial site developments, approaching every project with dedicated efficiency, technology and a special focus on safety.</p>
      <p class="reveal">The company performs all phases of road construction, including earthwork, utilities, drainage, concrete and asphalt paving, bridge construction, as well as aggregate production.</p>
      <p class="reveal">What makes the company special is not just its versatility: the company has undertaken many public and private sector projects worth multi-million dollars, enabling the group to operate with honesty, integrity and higher standards.</p>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/road-asphalt.jpg" alt="Road roller compacting asphalt" loading="lazy">
        <img src="assets/img/site-engineer.jpg" alt="Engineer supervising site works" loading="lazy">
        <img src="assets/img/rebar-crew.jpg" alt="Crew preparing reinforcement" loading="lazy">
      </div>

      <h3 class="reveal">Featured services overview</h3>
      <div class="reveal" style="margin-top:18px">
      {service_list(['Equipment services','Civil construction &amp; general contracting','Electrical, air-conditioning installation and plumbing','Architectural finishing works','Renovation &amp; refurbishment of residential complexes, commercial buildings and industrial facilities','Water supply, sewage, electrical, telecommunications &amp; CATV infrastructure and networks'])}
      </div>

      <h3 class="reveal">Phases we deliver</h3>
      <ul class="reveal">
        <li>Earthwork and aggregate production</li>
        <li>Utilities and drainage</li>
        <li>Concrete and asphalt paving</li>
        <li>Bridge construction</li>
      </ul>
      <a class="btn btn--navy reveal" href="contact.html" style="margin-top:12px">Discuss a road project{I['arrow']}</a>
    </div>
    {side_nav('roads-construction.html')}
  </div>
</section>
{cta('Planning a highway or site development?', 'From earthworks to final asphalt, our teams deliver roads with efficiency, technology and safety.')}
'''
page('roads-construction.html', 'Roads Construction', 'PETIC GLOBAL roads construction: asphalt roads and highways, earthwork, drainage, paving, bridges and aggregate production.', roads)

# ---------------------------------------------------------------- CIVIL
civil = page_hero('Civil works and construction', 'Civil works &amp; construction.', 'Strategic investment in construction equipment, property and a substantial fleet of mobile plant, supporting projects across East Africa and the Gulf.', 'steel-frame-worker.jpg', 'Worker on a steel structure') + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Overview</span>
      <h2 class="reveal">Depth of resources, skilled teams.</h2>
      <p class="lead reveal" data-delay="1">East Trading &amp; Manufacturing Company holds a portfolio of strategic investment in construction equipment, property and a substantial fleet of mobile construction equipment in Tanzania. This complements the company’s multi-domestic growth strategy, which focuses on its operating hubs in East African countries.</p>

      <h3 class="reveal">East Trading</h3>
      <p class="reveal">East Trading’s heavy earthmoving equipment, skilled operatives and expertise in the work and local environment have enabled the company to be involved in many important civil and construction projects in Tanzania. The company strives to provide the best solution to its clients: it has the depth of resources and skilled labour teams to take projects from concept through construction, recognizing suggestions about improvements that lead to success.</p>
      <p class="reveal">East Trading &amp; Manufacturing Company and its main group PETIC GLOBAL have already completed more than 77 projects of various sizes for private and public sectors worldwide. The company and its main group’s operations are well poised to take this commendable journey to its next level.</p>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/engineers-warehouse.jpg" alt="Engineers inspecting an industrial building" loading="lazy">
        <img src="assets/img/construction-worker.jpg" alt="Construction worker with power tools" loading="lazy">
        <img src="assets/img/rebar-crew.jpg" alt="Crew preparing reinforcement steel" loading="lazy">
      </div>

      <h3 class="reveal">Our construction capability</h3>
      <p class="reveal">The capability in construction and the range of construction services offered by the group includes:</p>
      <div class="reveal" style="margin-top:18px">
      {service_list(['Design and construction engineering','Design-build projects','Construction and project management','Procurement of materials and equipment','Manpower supply and personnel services','Facilities maintenance','Concrete repair and waterproofing'])}
      </div>
      <a class="btn btn--navy reveal" href="contact.html" style="margin-top:28px">Start a project{I['arrow']}</a>
    </div>
    {side_nav('civil-works-and-construction.html')}
  </div>
</section>
{cta('Need a civil works partner?', 'Design-build, project management, procurement and maintenance from one accountable team.')}
'''
page('civil-works-and-construction.html', 'Civil Works and Construction', 'PETIC GLOBAL civil works and construction: design-build, project management, procurement, manpower and facilities maintenance in Tanzania and the Gulf.', civil)

# ---------------------------------------------------------------- OIL & GAS
oil = page_hero('Oil &amp; gas', 'Oil &amp; gas.', 'Asset integrity, material supply and static equipment rehabilitation for the oil &amp; gas industry, serving major companies, projects and contractors.', 'refinery-plant.jpg', 'Oil and gas processing plant') + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Asset integrity</span>
      <h2 class="reveal">Safe operation of ageing assets.</h2>
      <p class="lead reveal" data-delay="1">One of the major challenges facing the oil and gas industry today is to ensure the safe operation of their ageing assets. Asset integrity entails making sure an asset can perform its required function effectively and safely.</p>
      <p class="reveal">Our asset integrity partner, Mega, has a well trained and experienced team certified to API (510, 570, 580, 653), CSWIP welding &amp; painting, NACE and ASNT (UT, RT, MT, PT, VT), supported by specialized tools and equipment. Mega is accredited by the Egyptian Accreditation Council (EGAC) under ISO/IEC 17020 as a Type C inspection body in the field of in-service inspection.</p>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/construction-worker.jpg" alt="Technician at work" loading="lazy">
        <img src="assets/img/industrial-worker.jpg" alt="Inspector checking equipment" loading="lazy">
        <img src="assets/img/steel-frame-worker.jpg" alt="Worker on steel framework" loading="lazy">
      </div>

      <h3 class="reveal">Material supply services</h3>
      <p class="reveal">PETIC GLOBAL is a well-resourced and full-service oilfield supply company serving the oil &amp; gas industry in the country. Our clients include major oil and gas companies, projects and contractors in Yemen. Our company has associations with renowned manufacturers, major mills and suppliers across the world.</p>
      <p class="reveal">PETIC GLOBAL is an oilfield supplier you can trust for any urgent and important oil &amp; gas project supply. Operations are conducted from purpose-built facilities in Yemen, comprising offices, workshops, warehousing and covered storage areas, from where a wide range of products and services covering a large spectrum of the energy industry are supplied. Products range from materials required for the drilling of wells to equipment required for large downstream projects.</p>
      <p class="reveal">PETIC GLOBAL Stocks and Supplies are committed to client satisfaction in every aspect of our business, guided by our core values of integrity and teamwork.</p>

      <div class="gallery gallery--3 reveal" style="margin:32px 0">
        <img src="assets/img/steel-pipes.jpg" alt="Stacked steel pipes" loading="lazy">
        <img src="assets/img/hero-oil-rig.jpg" alt="Drilling rig and pipelines" loading="lazy">
        <img src="assets/img/refinery-plant.jpg" alt="Refinery plant" loading="lazy">
      </div>

      <div class="grid grid--2 reveal" style="gap:16px;margin-top:18px">
        <div class="feature"><i>{I['users']}</i><h3>Team capabilities &amp; qualification</h3><p>Well trained and certified maintenance teams who have gained various maintenance technologies by handling a diversity of process types (oil, gas, LNG and more) with their related operation techniques and safety hazards, inside and outside the oil &amp; gas sector, for railways, the industrial sector and more.</p></div>
        <div class="feature"><i>{I['cog']}</i><h3>Static equipment rehabilitation</h3><p>A significant market share as a unique service provider for boiler and heater revamping, separator fabrication and heat exchangers in oil &amp; gas fields, including water and fire-tube boiler revamping, supported by a specialized workshop complying with the ASME code.</p></div>
      </div>

      <h3 class="reveal">Related services</h3>
      <div class="reveal" style="margin-top:18px">
      {service_list(['Cost estimating','Pre-construction services','Historic restoration','Infrastructure solutions','General contractor','Industrial engineering'])}
      </div>
      <a class="btn btn--navy reveal" href="tel:{PHONE_RAW}" style="margin-top:28px">{I['phone']}Call for appointment: {PHONE}</a>
    </div>
    {side_nav('oil-and-gas.html')}
  </div>
</section>
{cta('Need oilfield supply or inspection?', 'From drilling materials to downstream equipment and in-service inspection, we are ready to support your project.')}
'''
page('oil-and-gas.html', 'Oil & Gas', 'PETIC GLOBAL oil & gas: asset integrity inspection, oilfield material supply and static equipment rehabilitation.', oil)

# ---------------------------------------------------------------- CONTACT
contact = page_hero('Contact us', 'Get in touch.', 'We’d love to hear from you. For general enquiries you can reach the PETIC GLOBAL support team by phone, email or the form below.', 'engineers-warehouse.jpg', 'Engineers reviewing plans') + f'''
<section class="section">
  <div class="container contact-grid">
    <div>
      <span class="eyebrow reveal">Contact details</span>
      <h2 class="reveal">Send a message.</h2>
      <p class="lead reveal" data-delay="1">Our teams in Doha and Dar es Salaam respond to project enquiries, supply requests and partnership proposals.</p>
      <div class="contact-list">
        <div class="contact-item reveal"><i>{I['pin']}</i><div><h3>Headquarters</h3><p>{ADDRESS}</p></div></div>
        <div class="contact-item reveal" data-delay="1"><i>{I['pin']}</i><div><h3>East Africa office</h3><p>East Trading &amp; Manufacturing Company LTD<br>{TZ_ADDRESS}</p></div></div>
        <div class="contact-item reveal" data-delay="2"><i>{I['phone']}</i><div><h3>Phone</h3><a href="tel:{PHONE_RAW}">{PHONE}</a></div></div>
        <div class="contact-item reveal" data-delay="3"><i>{I['mail']}</i><div><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a><a href="mailto:{SALES}">{SALES}</a><a href="mailto:{CEO}">{CEO}</a></div></div>
      </div>
    </div>
    <form class="form reveal" data-contact novalidate>
      <h3 style="margin-bottom:20px">Tell us about your project</h3>
      <div class="form__row">
        <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" required placeholder="Your name"></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required placeholder="you@company.com"></div>
      </div>
      <div class="form__row">
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" placeholder="+974 ..."></div>
        <div class="field"><label for="f-sector">Sector</label><select id="f-sector" name="sector"><option value="">Select a sector</option><option>Civil works &amp; construction</option><option>Roads construction</option><option>Agriculture</option><option>Oil &amp; gas</option><option>Other</option></select></div>
      </div>
      <div class="field"><label for="f-subject">Subject</label><input id="f-subject" name="subject" type="text" placeholder="How can we help?"></div>
      <div class="field"><label for="f-message">Message</label><textarea id="f-message" name="message" required placeholder="Describe your project or enquiry"></textarea></div>
      <button class="btn btn--gold" type="submit">Send message{I['arrow']}</button>
      <p class="form__note">We will reply to the email address you provide. Your details are never shared.</p>
      <div class="form__status" role="status" aria-live="polite"></div>
    </form>
  </div>
</section>

<section class="section section--soft section--tight">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Find us</span><h2>Salwa Road, Doha.</h2></div>
    <div class="map reveal"><iframe title="Map of PETIC GLOBAL headquarters on Salwa Road, Doha" src="https://www.google.com/maps?q=Salwa+Road,+Zone+55,+Doha,+Qatar&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  </div>
</section>
'''
page('contact.html', 'Contact Us', 'Contact PETIC GLOBAL in Doha, Qatar or Dar es Salaam, Tanzania. Call +974 4441 1083 or email info@petic-global.com.', contact)
print('done')
