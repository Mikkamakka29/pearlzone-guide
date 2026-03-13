export const siteConfig = {
  name: 'PearlZone',
  domain: 'pearlzone.hu',
  siteUrl: 'https://pearlzone.hu',
  gumroadUrl:
    process.env.NEXT_PUBLIC_GUMROAD_URL ||
    'https://pearlzone.gumroad.com/l/budapest-itinerary',
  contactEmail:
    process.env.NEXT_PUBLIC_CONTACT_EMAIL || 'hello@pearlzone.hu',
  freeChecklistUrl: '/downloads/budapest-packing-checklist.pdf',
  premiumPreviewPages: [
    {
      src: '/previews/premium/cover.png',
      alt: 'Cover preview of the premium Budapest itinerary PDF',
      label: 'Premium cover',
    },
    {
      src: '/previews/premium/day-1.png',
      alt: 'Day 1 sample page from the premium Budapest itinerary PDF',
      label: 'Sample day page',
    },
    {
      src: '/previews/premium/links.png',
      alt: 'Official links appendix sample page from the premium Budapest itinerary PDF',
      label: 'Official links page',
    },
  ],
  checklistPreviewPages: [
    {
      src: '/previews/checklist/cover.png',
      alt: 'Cover page of the free Budapest packing checklist PDF',
    },
    {
      src: '/previews/checklist/page-2.png',
      alt: 'Second page of the free Budapest packing checklist PDF',
    },
  ],
} as const
