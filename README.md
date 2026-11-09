# PETIC GLOBAL — company website

Redesigned static website for [petic-global.com](https://petic-global.com). No build tools or
server required: plain HTML, CSS and JavaScript that can be hosted anywhere (GitHub Pages,
Netlify, cPanel, etc.).

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | About us (history, mission, East Africa office, licences, partners) |
| `our-activities.html` | Our activities overview |
| `agriculture.html` | Agriculture (AgriPro) |
| `roads-construction.html` | Roads construction |
| `civil-works-and-construction.html` | Civil works & construction |
| `oil-and-gas.html` | Oil & gas |
| `contact.html` | Contact (form + map) |

## Structure

```
assets/css/style.css   design system + all page styles
assets/js/main.js      menu, sticky header, scroll animations, counters, contact form
assets/img/            images (see "Replacing images" below)
assets/docs/           company profile PDF
tools/build.py         generator that writes the HTML pages
tools/icons.py         inline SVG icons used by the generator
.github/workflows/     GitHub Pages deployment and a build/format/validate check
```

## Replacing images

Drop a new file with the **same name** into `assets/img/` and it appears everywhere it is used.
Recommended sizes are in landscape unless noted.

| File | Used for | Suggested size |
| --- | --- | --- |
| `logo.png` | Header and footer logo (transparent PNG) | 800 × 320 |
| `hero-oil-rig.jpg` | Home hero background | 2400 × 1600 |
| `oil-gas-plant-1/2/3.jpg` | Home specialties, About and Oil & Gas headers, galleries | 1800 × 1200 |
| `oil-rig-dusk.jpg` | Home vision quote background | 2000 × 1200 |
| `oil-rig-move.jpg`, `oil-offshore-rig.jpg`, `oil-maintenance-crew.jpg`, `oil-pipes-yard.jpg` | Our activities and Oil & Gas page | 1200 × 800 |
| `roads-paving.jpg`, `roads-rollers.jpg`, `roads-asphalt-fresh.jpg`, `roads-tipper.jpg` | Roads cards, header and gallery | 1800 × 1200 |
| `civil-bridge-beam.jpg`, `civil-tank-construction.jpg`, `civil-pipeline.jpg`, `civil-earthworks.jpg` | Civil works cards, header and gallery | 1800 × 1200 |
| `fleet-mixer-truck.jpg`, `fleet-loader.jpg`, `fleet-tipper-trucks.jpg` | Equipment fleet gallery, Contact header | 1200 × 800 |
| `agri-*.jpg` | Agriculture page galleries and cards | 1200 × 800 |
| `license-*.jpg` | About page licences (portrait) | 800 × 1100 |
| `partner-*.jpg` | Partner logos | any, ~400 × 120 |

Most project photos were taken from the company profile PDF, so they are limited to about
1200 px wide. Replacing them with the original full-size photos will sharpen the site.

## Editing content

Either edit the HTML files directly, or edit the text in `tools/build.py` and run:

```bash
python3 tools/build.py
```

The script rewrites all eight pages with a consistent header, footer and navigation.
Then format and validate before committing (the CI check does the same):

```bash
npx prettier@3.3.3 --write "*.html" "assets/css/style.css" "assets/js/main.js"
```

```bash
npx html-validate@8.24.2 "*.html"
```

## Hosting on GitHub Pages

The workflow in `.github/workflows/pages.yml` publishes the site on every push.
Enable it once in the repository settings: **Settings → Pages → Build and deployment →
Source: GitHub Actions**. The `CNAME` file sets the custom domain to petic-global.com. For it to resolve, the domain's
DNS must point at GitHub Pages:

| Type | Host | Value |
| --- | --- | --- |
| A | @ | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 |
| CNAME | www | mariamfreijeh2001-gif.github.io |

Then in **Settings → Pages → Custom domain**, confirm `petic-global.com` and tick
**Enforce HTTPS** once the certificate is issued.

## Contact form

The form opens the visitor's email client with the message pre-filled (no server needed).
To send messages through a form service instead, add `data-endpoint="https://..."` to the
`<form>` in `contact.html` (for example a Formspree endpoint).
