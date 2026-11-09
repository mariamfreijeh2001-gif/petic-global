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
tools/build.py         generator that writes the HTML pages (optional)
```

## Replacing images

Drop a new file with the **same name** into `assets/img/` and it appears everywhere it is used.
Recommended sizes are in landscape unless noted.

| File | Used for | Suggested size |
| --- | --- | --- |
| `logo.png` | Header and footer logo (transparent PNG) | 800 × 320 |
| `hero-oil-rig.jpg` | Home hero background, activity cards | 2400 × 1600 |
| `steel-frame-worker.jpg` | Home "Our specialties", civil works hero | 1800 × 1200 |
| `industrial-worker.jpg` | Home "Why choose us" | 1600 × 1200 |
| `construction-worker.jpg` | Civil works card, Our activities hero | 1800 × 1200 |
| `road-asphalt.jpg` | Roads card, roads hero | 1800 × 1200 |
| `site-engineer.jpg` | About hero, Our activities card | 2400 × 1400 |
| `engineers-warehouse.jpg` | Contact hero, civil works gallery | 1600 × 1200 |
| `rebar-crew.jpg` | About mission, galleries | 1600 × 1100 |
| `refinery-plant.jpg` | Oil & gas hero and card | 2400 × 1600 |
| `gas-plant-portrait.jpg` | About page (portrait) | 1000 × 1375 |
| `steel-pipes.jpg` | Oil & gas gallery | 1200 × 800 |
| `agri-*.jpg` | Agriculture page galleries and cards | 1200 × 800 |
| `license-*.jpg` | About page licences (portrait) | 800 × 1100 |
| `partner-*.jpg` | Partner logos | any, ~400 × 120 |

## Editing content

Either edit the HTML files directly, or edit the text in `tools/build.py` and run:

```bash
python3 tools/build.py
```

The script rewrites all eight pages with a consistent header, footer and navigation.

## Contact form

The form opens the visitor's email client with the message pre-filled (no server needed).
To send messages through a form service instead, add `data-endpoint="https://..."` to the
`<form>` in `contact.html` (for example a Formspree endpoint).
