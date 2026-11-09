"""Generate the static PETIC GLOBAL site.

Usage: python3 tools/build.py
Writes the eight HTML pages into the repository root using the shared
header, footer and section templates defined below.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from icons import ICONS as I  # noqa: E402

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE = 'PETIC GLOBAL'
PHONE = '+974&nbsp;4414&nbsp;1888'
PHONE_RAW = '+97444141888'
EMAIL = 'info@petic-global.com'
SALES = 'sales@petic-global.com'
CEO = 'ceo@petic-global.com'
ADDRESS = '1st Floor, Office 08, Building 382, Street 340, Salwa Road, Zone 55, P.O. Box 5090, Doha, Qatar'
TZ_ADDRESS = 'Kisutu Street 2423, Dar es Salaam, Tanzania'
PROFILE = 'PETIC-Global-Company-Profile.pdf'
QUOTE = 'Chase the vision, not the money. The money will end up following you.'


NAV = [
 ('index.html', 'Home'),
 ('about.html', 'About Us'),
 ('our-activities.html', 'Our Activities', [
    ('agriculture.html', 'Agriculture'),
    ('roads-construction.html', 'Roads Construction'),
    ('civil-works-and-construction.html', 'Civil Works &amp; Construction'),
    ('oil-and-gas.html', 'Oil &amp; Gas'),
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
      <a href="contact.html">{I['pin']}Doha, Qatar</a>
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
    <button class="menu-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav"><span></span></button>
  </div>
  <div class="header__progress" aria-hidden="true"></div>
</header>
<nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">
  <ul>{mobile_nav_html(current)}</ul>
  <a class="btn btn--gold" href="{PROFILE}" target="_blank" rel="noopener">{I['download']}Download Company Profile</a>
  <p class="mobile-nav__meta">Call <a href="tel:{PHONE_RAW}">{PHONE}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</nav>
'''

def cta(title='Have a project in mind?', text='You’re welcome to send a message or give us a call. Our team in Doha will get back to you promptly.'):
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
        <a class="brand brand--on-dark" href="index.html"><img src="assets/img/logo.png" alt="{SITE}" width="110" height="45"></a>
        <h4 class="mt-md">About our company</h4>
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
<button class="to-top" type="button" aria-label="Back to top">{I['up']}</button>
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

def page_hero(crumb, h1, lead, img, alt, chip=None, tags=None):
    chip_html = f'<div class="page-hero__chip">{chip[0]}<small>{chip[1]}</small></div>' if chip else ''
    tags_html = '<div class="page-hero__tags reveal" data-delay="2">' + ''.join(f'<span>{t}</span>' for t in tags) + '</div>' if tags else f'<p class="page-hero__quote reveal" data-delay="2">“{QUOTE}”</p>'
    return f'''
<section class="page-hero page-hero--split">
  <img src="assets/img/{img}" alt="" aria-hidden="true">
  <div class="container">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span>{crumb}</span></nav>
      <h1 class="reveal">{h1}</h1>
      <p class="lead reveal" data-delay="1">{lead}</p>
      {tags_html}
    </div>
    <div class="page-hero__img reveal" data-delay="2">
      <img src="assets/img/{img}" alt="{alt}">
      {chip_html}
    </div>
  </div>
</section>
'''

def side_nav(current):
    links = ''.join(f'<a href="{h}"{" class=\"is-active\"" if current == h else ""}>{l}{I["arrow"]}</a>' for h, l in NAV[2][2])
    return f'''
<aside class="sidebar" aria-label="Related information">
  <div class="side-card">
    <h4>Our activities</h4>
    <nav class="side-nav" aria-label="Activity pages">{links}</nav>
  </div>
  <div class="side-card side-card--navy">
    <h4>Talk to our team</h4>
    <p><strong>{PHONE}</strong><br>{EMAIL}</p>
    <p class="text-sm">{ADDRESS}</p>
    <a class="btn btn--gold" href="contact.html">Request a quote{I['arrow']}</a>
  </div>
  <div class="side-card">
    <h4>Company profile</h4>
    <p class="muted text-sm">Download our full corporate profile with capabilities, projects and licences.</p>
    <a class="link-arrow mt-xs" href="{PROFILE}" target="_blank" rel="noopener">Download PDF{I['download']}</a>
  </div>
</aside>
'''

PARTNERS = [('partner-almaha.jpg','Almaha for Industry'),('partner-linex.jpg','LINE-X'),('partner-petro-sharq.jpg','Petro Sharq Group'),('partner-teamone.jpg','TeamOne Shipping &amp; Clearing'),('partner-nature-petroleum.jpg','Nature for Petroleum, Gas and Minerals')]
def partners_marquee():
    logos = ''.join(f'<div class="partner"><img src="assets/img/{f}" alt="{a}" loading="lazy"></div>' for f, a in PARTNERS)
    return f'<div class="marquee reveal" role="group" aria-label="Partner logos"><div class="marquee__track">{logos}{logos}</div></div>'

def service_list(items, icon='check'):
    return '<div class="services">' + ''.join(f'<div class="service"><i>{I[icon]}</i><span>{s}</span></div>' for s in items) + '</div>'

# ---------------------------------------------------------------- HOME
home = f'''
<section class="hero">
  <div class="hero__media"><img src="assets/img/hero-oil-rig.jpg" alt="Oil and gas drilling rig with pipelines at sunset"></div>
  <div class="hero__grid-lines" aria-hidden="true"></div>
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
      <div class="hero__float"><b>77+</b><span>projects delivered worldwide</span></div>
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
  <div class="hero__scroll" aria-hidden="true"><i></i>Scroll</div>
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
      <img src="assets/img/oil-gas-plant-1.jpg" alt="Gas processing facility delivered by the group">
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
      <div class="actions"><a class="btn btn--navy" href="about.html">More about us{I['arrow']}</a></div>
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
        <div class="card__media"><span class="card__num">01</span><img src="assets/img/civil-bridge-beam.jpg" alt="Bridge beam being lifted into place by crane" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['building']}</i><h3>Civil Works &amp; Construction</h3><p>East Trading &amp; Manufacturing Company holds a portfolio of strategic investment in construction equipment and a substantial fleet of mobile plant.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="1" href="roads-construction.html">
        <div class="card__media"><span class="card__num">02</span><img src="assets/img/roads-paving.jpg" alt="Asphalt paving crew laying a new road" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['road']}</i><h3>Roads Construction</h3><p>A hard-earned reputation for the construction quality of asphalt roads and highways, from large highways to small commercial site developments.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="2" href="agriculture.html">
        <div class="card__media"><span class="card__num">03</span><img src="assets/img/agri-harvest-1.jpg" alt="Combine harvester working a wheat field" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['leaf']}</i><h3>Agriculture</h3><p>AgriPro is a leading agriculture company dedicated to transforming arable lands into highly productive and sustainable agricultural ventures.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="3" href="oil-and-gas.html">
        <div class="card__media"><span class="card__num">04</span><img src="assets/img/oil-gas-plant-2.jpg" alt="Oil and gas processing plant" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['flame']}</i><h3>Oil &amp; Gas</h3><p>Our clients include major oil and gas companies, projects and contractors in Yemen, with associations with renowned manufacturers worldwide.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <div class="split__media reveal">
      <img src="assets/img/civil-earthworks.jpg" alt="Earthworks on a desert road project">
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Why choose us</span>
      <h2>The benefit of working with our company.</h2>
      <p class="lead">PETIC GLOBAL holds a portfolio of strategic investment in construction equipment, property and a substantial fleet of mobile plant in Saudi Arabia. This complements the company’s multi-domestic growth strategy, which centres on its operating hubs in Al Khobar, Jubail and Qatar.</p>
      <p>We embrace holistic development and support for employees, with the aim of being a first-choice employer.</p>
      <div class="grid grid--2 grid--tight mt-md">
        {''.join(f'<div class="service"><i>{I["check"]}</i><span>{s}</span></div>' for s in ['Cost estimating','Pre-construction services','Historic restoration','Infrastructure solutions','General contractor','Industrial engineering'])}
      </div>
      <div class="actions"><a class="btn btn--ghost" href="our-activities.html">See more{I['arrow']}</a></div>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="section-head section-head--center reveal">
      <span class="eyebrow">Our services</span>
      <h2>First-class construction and infrastructure.</h2>
      <p class="lead">From architecture to industrial engineering, we take projects from concept through construction, commissioning and long-term operation and maintenance.</p>
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

<section class="quote-band">
  <img src="assets/img/oil-rig-dusk.jpg" alt="" aria-hidden="true" loading="lazy">
  <div class="container reveal">
    <span class="mark" aria-hidden="true">“</span>
    <blockquote>Chase the vision, not the money. <em>The money will end up following you.</em></blockquote>
    <cite>The PETIC GLOBAL philosophy</cite>
  </div>
</section>

<section class="section section--sand">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="reveal"><span class="eyebrow">Where we operate</span><h2>Present across the Gulf and East Africa.</h2></div>
      <p class="lead reveal" data-delay="1">Operating hubs in the Gulf States and East Africa, with manufacturing and supply operations that keep growing.</p>
    </div>
    <div class="presence">
      <div class="place reveal"><b>QATAR</b><h3>Doha</h3><p>Group headquarters on Salwa Road.</p></div>
      <div class="place reveal" data-delay="1"><b>SAUDI ARABIA</b><h3>Al Khobar &amp; Jubail</h3><p>Operating hubs and a substantial fleet of mobile plant.</p></div>
      <div class="place reveal" data-delay="2"><b>TANZANIA</b><h3>Dar es Salaam</h3><p>East Trading &amp; Manufacturing Company: roads, civil works, construction.</p></div>
      <div class="place reveal" data-delay="3"><b>RWANDA</b><h3>Manufacturing</h3><p>Household and pharmaceutical products.</p></div>
      <div class="place reveal" data-delay="4"><b>UGANDA</b><h3>Manufacturing</h3><p>Gas cylinder production.</p></div>
      <div class="place reveal" data-delay="4"><b>YEMEN</b><h3>Oilfield supply</h3><p>Offices, workshops, warehousing and covered storage.</p></div>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Our partners</span><h2>Trusted by industry partners.</h2></div>
    {partners_marquee()}
  </div>
</section>
{cta()}
'''
page('index.html', 'Construction, Agriculture, Oil &amp; Gas', 'PETIC GLOBAL delivers construction, roads, civil works, agriculture and oil & gas services across the Gulf States and East Africa. Chase the vision, not the money.', home)

# ---------------------------------------------------------------- ABOUT
about = page_hero('About us', 'About PETIC GLOBAL.', 'A group established across the Middle East and Africa, providing quality construction projects and engineering services in the sector of oil &amp; gas, infrastructure, manufacturing and agriculture.', 'oil-gas-plant-3.jpg', 'Oil and gas facility at dusk', chip=('77+ projects', 'Private and public sectors worldwide'), tags=['Construction', 'Infrastructure', 'Manufacturing', 'Agriculture', 'Oil &amp; gas']) + f'''
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Who we are</span>
      <h2>Established worldwide, rooted in the Gulf and Africa.</h2>
      <p class="lead">Sheik Salah has been in worldwide business, establishing various companies in the Middle East and Africa, providing quality construction projects and engineering services in the sector of oil &amp; gas.</p>
      <p>At the beginning, the Petic group invested heavily in the Gulf States and Tanzania by building infrastructure and road projects. In its next phase the group moved into manufacturing household and pharmaceutical products in Rwanda, and gas cylinders in Uganda.</p>
      <p>The group is now planning to represent Chinese car manufacturers by creating an assembling workshop in Africa.</p>
      <div class="actions"><a class="btn btn--navy" href="{PROFILE}" target="_blank" rel="noopener">{I['download']}Company profile</a><a class="btn btn--ghost" href="contact.html">Contact us</a></div>
    </div>
    <div class="split__media reveal" data-delay="1">
      <img src="assets/img/oil-pipes-yard.jpg" alt="Steel pipes in the supply yard" class="split__img--tall">
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
      <p>The rapid growth of the group is driven by its bold vision, strong entrepreneurial spirit and devotion to customer satisfaction, delivering excellent quality products and services.</p>
      <ul class="timeline mt-lg">
        <li class="reveal"><span class="tag">Phase one</span><h3>Gulf States &amp; Tanzania</h3><p>Heavy investment in infrastructure and road projects, backed by a substantial fleet of mobile plant in the Gulf States and East Africa.</p></li>
        <li class="reveal" data-delay="1"><span class="tag">Phase two</span><h3>Rwanda &amp; Uganda</h3><p>Manufacturing of household and pharmaceutical products in Rwanda, and gas cylinders in Uganda.</p></li>
        <li class="reveal" data-delay="2"><span class="tag">Next</span><h3>Automotive assembly in Africa</h3><p>Representing Chinese car manufacturers by creating an assembling workshop in Africa.</p></li>
      </ul>
    </div>
    <div class="reveal" data-delay="1">
      <div class="side-card side-card--glass">
        <span class="eyebrow">East Africa</span>
        <h3>East Trading &amp; Manufacturing Company LTD</h3>
        <p class="text-gold">{TZ_ADDRESS}</p>
        <p>East Trading &amp; Manufacturing Company has been set up in Tanzania to provide quality construction services to real estate contractors, construction companies, and the civil engineering and infrastructure industries. The company established a successful track record through commitments to its customers within the operations and construction domain.</p>
        <p>After gaining extensive experience in building services, the company is moving forward to undertake complex and challenging civil engineering and building projects, extending its services from innovative technical concepts and front-end engineering designs to construction management, installation, commissioning and long-term operation and maintenance.</p>
        <p>The company holds a portfolio of strategic investments in the construction sector, owning a substantial fleet of mobile plant in the Gulf States and East Africa. This complements the company’s multi-domestic growth strategy, which focuses its operating hubs in both regions.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--rev">
    <div class="split__media reveal"><img src="assets/img/oil-maintenance-crew.jpg" alt="Maintenance crew servicing plant equipment"></div>
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
      <figure><img src="assets/img/license-incorporation-tanzania.jpg" alt="Certificate of incorporation, Tanzania" loading="lazy" class="gallery__doc"><figcaption>Certificate of Incorporation, Tanzania</figcaption></figure>
      <figure><img src="assets/img/license-registration-1.jpg" alt="Company registration, Rwanda Development Board" loading="lazy" class="gallery__doc"><figcaption>Company registration, Rwanda</figcaption></figure>
      <figure><img src="assets/img/license-registration-2.jpg" alt="Business activities registration, Rwanda Development Board" loading="lazy" class="gallery__doc"><figcaption>Business activities, Rwanda</figcaption></figure>
      <figure><img src="assets/img/license-uma-certificate.jpg" alt="Uganda Manufacturers Association membership certificate" loading="lazy" class="gallery__doc"><figcaption>Uganda Manufacturers Association member</figcaption></figure>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head section-head--center reveal"><span class="eyebrow">Our partners</span><h2>Trusted by global brands.</h2></div>
    {partners_marquee()}
  </div>
</section>
{cta()}
'''
page('about.html', 'About Us', 'Learn about PETIC GLOBAL: our history across the Gulf States, Tanzania, Rwanda and Uganda, our mission, licences and partners.', about)

# ---------------------------------------------------------------- OUR ACTIVITIES
activities = page_hero('Our activities', 'Our activities.', 'Roads, civil works, agriculture and oil &amp; gas: four sectors delivered with dedicated efficiency, technology and a special focus on safety.', 'oil-rig-move.jpg', 'Rig move with heavy transport', chip=('4 sectors', 'One standard of quality and safety'), tags=['Roads', 'Civil works', 'Agriculture', 'Oil &amp; gas']) + f'''
<section class="section">
  <div class="container">
    <div class="grid grid--2 grid--loose">
      <a class="card reveal" href="roads-construction.html">
        <div class="card__media card__media--wide"><img src="assets/img/roads-rollers.jpg" alt="Road rollers compacting asphalt" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['road']}</i><h3>Roads Construction</h3><p>East Trading &amp; Manufacturing Company has worked hard to maintain its reputation in the construction quality of asphalt roads and highways. It has successfully completed a range of large-scale road projects, from large highways to small commercial site developments, approaching every project with dedicated efficiency, technology and a special focus on safety.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="1" href="civil-works-and-construction.html">
        <div class="card__media card__media--wide"><img src="assets/img/civil-tank-construction.jpg" alt="Storage tank construction with crane" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['building']}</i><h3>Civil Works &amp; Construction</h3><p>East Trading &amp; Manufacturing Company holds a portfolio of strategic investment in construction equipment, property and a substantial fleet of mobile construction equipment in Tanzania. This complements the company’s multi-domestic growth strategy, which focuses on its operating hubs in East African countries.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="2" href="agriculture.html">
        <div class="card__media card__media--wide"><img src="assets/img/agri-tractors.jpg" alt="Fleet of tractors in a field" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['leaf']}</i><h3>Agriculture</h3><p>AgriPro is a leading agriculture company dedicated to transforming arable lands into highly productive and sustainable agricultural ventures. With a strong commitment to innovation, technology and environmental responsibility, we provide comprehensive solutions for land development and irrigation systems.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
      </a>
      <a class="card reveal" data-delay="3" href="oil-and-gas.html">
        <div class="card__media card__media--wide"><img src="assets/img/oil-offshore-rig.jpg" alt="Offshore drilling rig" loading="lazy"></div>
        <div class="card__body"><i class="card__icon">{I['flame']}</i><h3>Oil &amp; Gas</h3><p>A well-resourced, full-service oilfield supply company serving the oil &amp; gas industry, with asset integrity, material supply and static equipment rehabilitation services. Our clients include major oil and gas companies, projects and contractors in Yemen.</p><span class="link-arrow">Learn more{I['arrow']}</span></div>
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
agri = page_hero('Agriculture', 'Agriculture: AgriPro.', 'Transforming arable lands into highly productive and sustainable agricultural ventures through land development, irrigation systems, technology and modern heavy machinery.', 'agri-tractors.jpg', 'Fleet of tractors lined up in a field', chip=('Thousands of acres', 'Transformed into productive farmland'), tags=['Land development', 'Irrigation', 'Technology', 'Heavy machinery']) + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Company overview</span>
      <h2 class="reveal">A leading agriculture company.</h2>
      <p class="lead reveal" data-delay="1">AgriPro is a leading agriculture company dedicated to transforming arable lands into highly productive and sustainable agricultural ventures. With a strong commitment to innovation, technology and environmental responsibility, we provide comprehensive solutions for land development, irrigation systems and fertilizer management.</p>
      <p class="reveal" data-delay="1">Our state-of-the-art heavy machinery and expert agronomists ensure that every project we undertake thrives, contributing to global food security and agricultural sustainability.</p>

      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/agri-harvest-1.jpg" alt="Combine harvester unloading grain" loading="lazy">
        <img src="assets/img/agri-combine.jpg" alt="Combine harvester in a wheat field" loading="lazy">
        <img src="assets/img/agri-tractor-field.jpg" alt="Tractor tilling a field" loading="lazy">
      </div>

      <h3 class="reveal">Mission statement</h3>
      <p class="reveal">At AgriPro Innovations, our mission is to revolutionize agriculture by leveraging cutting-edge technology and sustainable practices to develop fertile lands, optimize water usage and maximize crop yields. We are dedicated to enhancing the agricultural sector’s productivity and sustainability.</p>

      <h3 class="reveal">Key services</h3>
      <div class="grid grid--2 grid--tight mt-sm reveal">
        <div class="feature"><i>{I['layers']}</i><h3>Land development</h3><p>Our land development experts assess and prepare agricultural lands, ensuring optimal soil conditions and topography for crop cultivation. We employ advanced land levelling and earthmoving machinery to create fertile and productive fields.</p></div>
        <div class="feature"><i>{I['target']}</i><h3>Irrigation systems</h3><p>We design, install and maintain advanced irrigation systems tailored to each project. Our solutions optimize water usage through precise scheduling and automation, ensuring crops receive the right amount of moisture at the right time.</p></div>
        <div class="feature"><i>{I['eye']}</i><h3>Technology integration</h3><p>We harness agricultural technology to monitor and manage soil health, crop growth and machinery operations. Our integrated approach helps farmers make data-driven decisions for higher yields and resource efficiency.</p></div>
        <div class="feature"><i>{I['cog']}</i><h3>Heavy machinery</h3><p>Our modern fleet includes tractors, ploughs, seeders and harvesters equipped with the latest technology, facilitating efficient farming operations and saving time and resources for our clients.</p></div>
      </div>

      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/agri-irrigation-1.jpg" alt="Centre-pivot irrigation system" loading="lazy">
        <img src="assets/img/agri-irrigation-2.jpg" alt="Irrigation sprinklers over crops" loading="lazy">
        <img src="assets/img/agri-tech.jpg" alt="Farmer using a mobile app in the field" loading="lazy">
      </div>

      <h3 class="reveal">Projects and achievements</h3>
      <p class="reveal">AgriPro Innovations has successfully transformed thousands of acres of land into highly productive and sustainable agricultural ventures. Our projects have not only increased crop yields but have also contributed to the economic development of rural communities.</p>
      <p class="reveal">AgriPro is your trusted partner in agriculture, offering comprehensive solutions for land development, irrigation systems, fertilizer management and technology integration. We are committed to driving agricultural innovation and sustainability for a prosperous future.</p>

      <div class="gallery gallery--3 gallery--spaced reveal">
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
roads = page_hero('Roads construction', 'Roads construction.', 'A reputation built on the construction quality of asphalt roads and highways, from large highways to small commercial site developments.', 'roads-paving.jpg', 'Asphalt paving crew laying a new road', chip=('Multi-million dollar', 'Public and private sector projects'), tags=['Highways', 'Earthwork', 'Drainage', 'Asphalt paving', 'Bridges']) + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Overview</span>
      <h2 class="reveal">All phases of road construction.</h2>
      <p class="lead reveal" data-delay="1">East Trading &amp; Manufacturing Company has worked hard to maintain its reputation in the construction quality of asphalt roads and highways. It has successfully completed a range of large-scale road projects, from large highways to small commercial site developments, approaching every project with dedicated efficiency, technology and a special focus on safety.</p>
      <p class="reveal">The company performs all phases of road construction, including earthwork, utilities, drainage, concrete and asphalt paving, bridge construction, as well as aggregate production.</p>
      <p class="reveal">What makes the company special is not just its versatility: the company has undertaken many public and private sector projects worth multi-million dollars, enabling the group to operate with honesty, integrity and higher standards.</p>

      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/roads-rollers.jpg" alt="Road rollers compacting asphalt" loading="lazy">
        <img src="assets/img/roads-asphalt-fresh.jpg" alt="Freshly laid asphalt road" loading="lazy">
        <img src="assets/img/roads-tipper.jpg" alt="Tipper truck feeding the asphalt paver" loading="lazy">
      </div>

      <h3 class="reveal">Featured services overview</h3>
      <div class="reveal mt-sm">
      {service_list(['Equipment services','Civil construction &amp; general contracting','Electrical, air-conditioning installation and plumbing','Architectural finishing works','Renovation &amp; refurbishment of residential complexes, commercial buildings and industrial facilities','Water supply, sewage, electrical, telecommunications &amp; CATV infrastructure and networks'])}
      </div>

      <h3 class="reveal">Phases we deliver</h3>
      <ul class="reveal">
        <li>Earthwork and aggregate production</li>
        <li>Utilities and drainage</li>
        <li>Concrete and asphalt paving</li>
        <li>Bridge construction</li>
      </ul>
      <a class="btn btn--navy reveal mt-sm" href="contact.html">Discuss a road project{I['arrow']}</a>
    </div>
    {side_nav('roads-construction.html')}
  </div>
</section>
{cta('Planning a highway or site development?', 'From earthworks to final asphalt, our teams deliver roads with efficiency, technology and safety.')}
'''
page('roads-construction.html', 'Roads Construction', 'PETIC GLOBAL roads construction: asphalt roads and highways, earthwork, drainage, paving, bridges and aggregate production.', roads)

# ---------------------------------------------------------------- CIVIL
civil = page_hero('Civil works and construction', 'Civil works &amp; construction.', 'Strategic investment in construction equipment, property and a substantial fleet of mobile plant, supporting projects across East Africa and the Gulf.', 'civil-bridge-beam.jpg', 'Bridge beam being lifted into place by crane', chip=('77+ projects', 'Completed for private and public sectors'), tags=['Design-build', 'Project management', 'Procurement', 'Maintenance']) + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Overview</span>
      <h2 class="reveal">Depth of resources, skilled teams.</h2>
      <p class="lead reveal" data-delay="1">East Trading &amp; Manufacturing Company holds a portfolio of strategic investment in construction equipment, property and a substantial fleet of mobile construction equipment in Tanzania. This complements the company’s multi-domestic growth strategy, which focuses on its operating hubs in East African countries.</p>

      <h3 class="reveal">East Trading</h3>
      <p class="reveal">East Trading’s heavy earthmoving equipment, skilled operatives and expertise in the work and local environment have enabled the company to be involved in many important civil and construction projects in Tanzania. The company strives to provide the best solution to its clients: it has the depth of resources and skilled labour teams to take projects from concept through construction, recognizing suggestions about improvements that lead to success.</p>
      <p class="reveal">East Trading &amp; Manufacturing Company and its main group PETIC GLOBAL have already completed more than 77 projects of various sizes for private and public sectors worldwide. The company and its main group’s operations are well poised to take this commendable journey to its next level.</p>

      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/civil-tank-construction.jpg" alt="Storage tank construction with crane" loading="lazy">
        <img src="assets/img/civil-pipeline.jpg" alt="Pipeline installation across open ground" loading="lazy">
        <img src="assets/img/civil-earthworks.jpg" alt="Earthworks on a desert road project" loading="lazy">
      </div>

      <h3 class="reveal">Our construction capability</h3>
      <p class="reveal">The capability in construction and the range of construction services offered by the group includes:</p>
      <div class="reveal mt-sm">
      {service_list(['Design and construction engineering','Design-build projects','Construction and project management','Procurement of materials and equipment','Manpower supply and personnel services','Facilities maintenance','Concrete repair and waterproofing'])}
      </div>
      <h3 class="reveal">Our equipment fleet</h3>
      <p class="reveal">A substantial fleet of mobile construction equipment and transport vehicles supports our projects, and heavy equipment is also available on a contract or rental basis.</p>
      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/fleet-mixer-truck.jpg" alt="Concrete mixer truck" loading="lazy">
        <img src="assets/img/fleet-loader.jpg" alt="Wheel loader and tipper truck" loading="lazy">
        <img src="assets/img/fleet-tipper-trucks.jpg" alt="Tipper trucks in the yard" loading="lazy">
      </div>
      <a class="btn btn--navy reveal" href="contact.html">Start a project{I['arrow']}</a>
    </div>
    {side_nav('civil-works-and-construction.html')}
  </div>
</section>
{cta('Need a civil works partner?', 'Design-build, project management, procurement and maintenance from one accountable team.')}
'''
page('civil-works-and-construction.html', 'Civil Works and Construction', 'PETIC GLOBAL civil works and construction: design-build, project management, procurement, manpower and facilities maintenance in Tanzania and the Gulf.', civil)

# ---------------------------------------------------------------- OIL & GAS
oil = page_hero('Oil &amp; gas', 'Oil &amp; gas.', 'Asset integrity, material supply and static equipment rehabilitation for the oil &amp; gas industry, serving major companies, projects and contractors.', 'oil-gas-plant-2.jpg', 'Oil and gas processing plant', chip=('API &middot; CSWIP &middot; NACE', 'Certified inspection teams'), tags=['Asset integrity', 'Material supply', 'Equipment rehabilitation']) + f'''
<section class="section">
  <div class="container detail">
    <div class="prose">
      <span class="eyebrow reveal">Asset integrity</span>
      <h2 class="reveal">Safe operation of ageing assets.</h2>
      <p class="lead reveal" data-delay="1">One of the major challenges facing the oil and gas industry today is to ensure the safe operation of their ageing assets. Asset integrity entails making sure an asset can perform its required function effectively and safely.</p>
      <p class="reveal">Our asset integrity partner, Mega, has a well trained and experienced team certified to API (510, 570, 580, 653), CSWIP welding &amp; painting, NACE and ASNT (UT, RT, MT, PT, VT), supported by specialized tools and equipment. Mega is accredited by the Egyptian Accreditation Council (EGAC) under ISO/IEC 17020 as a Type C inspection body in the field of in-service inspection.</p>

      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/oil-maintenance-crew.jpg" alt="Maintenance crew servicing static equipment" loading="lazy">
        <img src="assets/img/oil-gas-plant-1.jpg" alt="Gas processing facility" loading="lazy">
        <img src="assets/img/oil-offshore-rig.jpg" alt="Offshore drilling rig" loading="lazy">
      </div>

      <h3 class="reveal">Material supply services</h3>
      <p class="reveal">PETIC GLOBAL is a well-resourced and full-service oilfield supply company serving the oil &amp; gas industry in the country. Our clients include major oil and gas companies, projects and contractors in Yemen. Our company has associations with renowned manufacturers, major mills and suppliers across the world.</p>
      <p class="reveal">PETIC GLOBAL is an oilfield supplier you can trust for any urgent and important oil &amp; gas project supply. Operations are conducted from purpose-built facilities in Yemen, comprising offices, workshops, warehousing and covered storage areas, from where a wide range of products and services covering a large spectrum of the energy industry are supplied. Products range from materials required for the drilling of wells to equipment required for large downstream projects.</p>
      <p class="reveal">PETIC GLOBAL Stocks and Supplies are committed to client satisfaction in every aspect of our business, guided by our core values of integrity and teamwork.</p>

      <div class="gallery gallery--3 gallery--spaced reveal">
        <img src="assets/img/oil-pipes-yard.jpg" alt="Steel pipes in the supply yard" loading="lazy">
        <img src="assets/img/oil-rig-move.jpg" alt="Rig move with heavy transport" loading="lazy">
        <img src="assets/img/oil-gas-plant-3.jpg" alt="Oil and gas facility at dusk" loading="lazy">
      </div>

      <div class="grid grid--2 grid--tight mt-sm reveal">
        <div class="feature"><i>{I['users']}</i><h3>Team capabilities &amp; qualification</h3><p>Well trained and certified maintenance teams who have gained various maintenance technologies by handling a diversity of process types (oil, gas, LNG and more) with their related operation techniques and safety hazards, inside and outside the oil &amp; gas sector, for railways, the industrial sector and more.</p></div>
        <div class="feature"><i>{I['cog']}</i><h3>Static equipment rehabilitation</h3><p>A significant market share as a unique service provider for boiler and heater revamping, separator fabrication and heat exchangers in oil &amp; gas fields, including water and fire-tube boiler revamping, supported by a specialized workshop complying with the ASME code.</p></div>
      </div>

      <h3 class="reveal">Related services</h3>
      <div class="reveal mt-sm">
      {service_list(['Cost estimating','Pre-construction services','Historic restoration','Infrastructure solutions','General contractor','Industrial engineering'])}
      </div>
      <p class="reveal mt-md"><strong>Call for an appointment</strong></p>
      <a class="btn btn--navy reveal" href="tel:{PHONE_RAW}">{I['phone']}{PHONE}</a>
    </div>
    {side_nav('oil-and-gas.html')}
  </div>
</section>
{cta('Need oilfield supply or inspection?', 'From drilling materials to downstream equipment and in-service inspection, we are ready to support your project.')}
'''
page('oil-and-gas.html', 'Oil &amp; Gas', 'PETIC GLOBAL oil &amp; gas: asset integrity inspection, oilfield material supply and static equipment rehabilitation.', oil)

# ---------------------------------------------------------------- CONTACT
contact = page_hero('Contact us', 'Get in touch.', 'We’d love to hear from you. For general enquiries you can reach the PETIC GLOBAL support team by phone, email or the form below.', 'fleet-tipper-trucks.jpg', 'Company truck fleet', chip=('Doha, Qatar', 'Salwa Road, Zone 55'), tags=['Doha', 'Phone', 'Email', 'Enquiry form']) + f'''
<section class="section">
  <div class="container contact-grid">
    <div>
      <span class="eyebrow reveal">Contact details</span>
      <h2 class="reveal">Send a message.</h2>
      <p class="lead reveal" data-delay="1">Our team in Doha responds to project enquiries, supply requests and partnership proposals.</p>
      <div class="contact-list">
        <div class="contact-item reveal"><i>{I['pin']}</i><div><h3>Headquarters</h3><p>{ADDRESS}</p></div></div>
        <div class="contact-item reveal" data-delay="2"><i>{I['phone']}</i><div><h3>Phone</h3><a href="tel:{PHONE_RAW}">{PHONE}</a></div></div>
        <div class="contact-item reveal" data-delay="3"><i>{I['mail']}</i><div><h3>Email</h3><a href="mailto:{EMAIL}">{EMAIL}</a><a href="mailto:{SALES}">{SALES}</a><a href="mailto:{CEO}">{CEO}</a></div></div>
      </div>
    </div>
    <form class="form reveal" data-contact novalidate>
      <h3 class="form__title">Tell us about your project</h3>
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
page('contact.html', 'Contact Us', 'Contact PETIC GLOBAL in Doha, Qatar. Call +974&nbsp;4414&nbsp;1888 or email info@petic-global.com.', contact)
print('done')
