// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://petic-global.com',
  integrations: [sitemap()],
  build: { format: 'directory' },
  trailingSlash: 'ignore',
});
