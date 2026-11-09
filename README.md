# PETIC GLOBAL — company website

Corporate website for [petic-global.com](https://petic-global.com), built with
[Astro](https://astro.build) and TypeScript. The build produces a fully static site (plain HTML,
CSS, a small script and optimised images) that is deployed to GitHub Pages.

## Getting started

Requires Node.js 22 or newer.

```bash
npm install
```

```bash
npm run dev
```

Opens a live-reloading development server at http://localhost:4321.

| Command                | What it does                                              |
| ---------------------- | --------------------------------------------------------- |
| `npm run dev`          | Start the development server                              |
| `npm run build`        | Build the production site into `dist/`                    |
| `npm run preview`      | Serve the built site locally                              |
| `npm run check`        | Type-check all `.astro` and `.ts` files                   |
| `npm run format`       | Format the source with Prettier                           |
| `npm run format:check` | Verify formatting (used by CI)                            |

## Project structure

```
public/                      files copied as-is: CNAME, robots.txt, favicon, company profile PDF
src/
  assets/img/                photos; imported by name and optimised at build time
  components/                reusable UI (Header, Footer, PageHero, ActivityCard, Gallery, …)
  data/site.ts               company details, navigation, partners, shared lists
  layouts/Base.astro         <head> metadata, header, footer and scripts for every page
  lib/images.ts              helper that resolves an image by file name
  pages/                     one .astro file per page; the file name is the URL
  scripts/main.ts            menu, sticky header, scroll animations, counters, contact form
  styles/global.css          design tokens and all component styles
.github/workflows/           CI check and GitHub Pages deployment
```

## Editing content

- **Company details** (phone, emails, address, social links, profile file name) live in
  `src/data/site.ts` and flow into every page.
- **Page text** lives in the matching file under `src/pages/`. Shared blocks such as the header,
  footer and call-to-action band are components under `src/components/`.
- **Photos** go in `src/assets/img/` and are referenced by file name, for example
  `img('roads-paving.jpg')`. Astro converts them to WebP in several sizes at build time, so
  drop in the largest version you have. Logos and the favicon live in `public/img/`.
- **Company profile PDF** is `public/Petic-International-Business-Profile.pdf`. Replace the file
  with the same name to update the download. Keep it under 100 MB (GitHub's limit); 10 MB or
  less gives visitors a quick download. The current file was compressed from 32 MB to 8.5 MB
  with Ghostscript at 170 dpi with no visible loss.

## Contact form

The form opens the visitor's email client with the message pre-filled, so it needs no server.
To send messages through a form service instead, add `data-endpoint="https://..."` to the
`<form>` in `src/pages/contact.astro` (for example a Formspree endpoint).

## Hosting on GitHub Pages

Pushes to `main` run `.github/workflows/pages.yml`, which builds the site and publishes it.
Enable it once in the repository settings: **Settings → Pages → Build and deployment →
Source: GitHub Actions**.

`public/CNAME` sets the custom domain to petic-global.com. For it to resolve, the domain's DNS
must point at GitHub Pages:

| Type  | Host | Value                                                                  |
| ----- | ---- | ---------------------------------------------------------------------- |
| A     | @    | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153     |
| CNAME | www  | mariamfreijeh2001-gif.github.io                                        |

Then in **Settings → Pages → Custom domain**, confirm `petic-global.com` and tick
**Enforce HTTPS** once the certificate is issued.
