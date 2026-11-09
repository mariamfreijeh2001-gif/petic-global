import type { ImageMetadata } from 'astro';

/** Every image under src/assets/img, keyed by path relative to that folder (e.g. 'products/flanges.png'). */
const modules = import.meta.glob<ImageMetadata>('/src/assets/img/**/*.{jpg,png}', {
  eager: true,
  import: 'default',
});

const byName = new Map<string, ImageMetadata>();
for (const [path, image] of Object.entries(modules)) {
  byName.set(path.replace('/src/assets/img/', ''), image);
}

/** Returns the imported image for a file name in src/assets/img, or throws at build time if missing. */
export function img(name: string): ImageMetadata {
  const image = byName.get(name);
  if (!image) throw new Error(`Unknown image: ${name}`);
  return image;
}
