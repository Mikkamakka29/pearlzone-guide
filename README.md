# PearlZone

A conversion-focused static Next.js landing page for a Budapest itinerary product.

## What is included

- A polished landing page for `pearlzone.hu`
- A **free** direct-download PDF at `public/downloads/budapest-packing-checklist.pdf`
- A **premium** PDF product file at `product-files/budapest-premium-itinerary.pdf`
- Preview images generated from the premium and free PDFs in `public/previews/`
- A Python generator script at `scripts/generate_pdfs.py`

## Configure before deploy

Create a `.env.local` file if you want to override the defaults:

```bash
NEXT_PUBLIC_GUMROAD_URL=https://pearlzone.gumroad.com/l/your-product
NEXT_PUBLIC_CONTACT_EMAIL=hello@pearlzone.hu
```

If you skip this, the site uses the fallback values from `src/lib/site-config.ts`.

## Run locally

```bash
npm install
npm run dev
```

## Production build

```bash
npm run build
```

This project uses static export via Next.js and is suitable for Cloudflare Pages.

## Regenerate the PDFs

```bash
python scripts/generate_pdfs.py
```

After regeneration, render preview images again if you change the PDF layout.

## Suggested launch workflow

1. Upload `product-files/budapest-premium-itinerary.pdf` to Gumroad.
2. Set your Gumroad URL in `.env.local`.
3. Deploy the site.
4. Keep the free checklist live as a direct download.
5. Use the premium preview gallery on the landing page to support conversion.
