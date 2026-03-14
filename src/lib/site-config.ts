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
      alt: 'Cover of the Budapest premium itinerary PDF',
      label: 'Cover page',
      caption: 'The premium guide opens with a clean overview of the 3-day core route and the 2-day extension.',
      links: [],
    },
    {
      src: '/previews/premium/day-1.png',
      alt: 'Sample day page from the Budapest premium itinerary PDF',
      label: 'Sample day page',
      caption: 'Each day is laid out as a paced route with a morning-to-evening flow, booking priorities, and smart swaps.',
      links: [],
    },
    {
      src: '/previews/premium/links.png',
      alt: 'Essential official links page from the Budapest premium itinerary PDF',
      label: 'Essential links appendix',
      caption: 'The final page collects the official visitor resources worth checking before the trip.',
      links: [
        {
          label: 'BudapestGO',
          url: 'https://bkk.hu/en/tickets-and-passes/budapestgo/',
          description: 'Digital tickets, route planning, and airport bus 100E access.',
        },
        {
          label: 'Parliament visitors',
          url: 'https://www.parlament.hu/web/visitors',
          description: 'Official tour information and ticket guidance.',
        },
        {
          label: 'Széchenyi Bath',
          url: 'https://www.szechenyibath.hu/',
          description: 'Opening hours, ticket types, and visitor details.',
        },
        {
          label: 'Matthias Church',
          url: 'https://matyas-templom.hu/en/',
          description: 'Current church access and ticket information.',
        },
        {
          label: 'Great Synagogue',
          url: 'https://dohany-zsinagoga.hu/',
          description: 'Official visitor information in the Jewish Quarter.',
        },
        {
          label: 'Central Market Hall',
          url: 'https://piaconline.hu/en/central-market-hall/',
          description: 'Opening hours and directions for the market hall.',
        },
        {
          label: 'House of Music Hungary',
          url: 'https://magyarzenehaza.com/en/',
          description: 'Exhibitions, tickets, and current programmes.',
        },
      ],
    },
  ],
  checklistPreviewPages: [
    {
      src: '/previews/checklist/cover.png',
      alt: 'Cover page of the free Budapest packing checklist PDF',
    },
    {
      src: '/previews/checklist/page-2.png',
      alt: 'Packing layout from the free Budapest packing checklist PDF',
    },
  ],
} as const
