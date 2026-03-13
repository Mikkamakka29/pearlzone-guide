import {
  CalendarDays,
  CheckCircle2,
  Compass,
  Download,
  MapPinned,
  PlaneLanding,
  Ticket,
  Umbrella,
  UtensilsCrossed,
  Waves,
  type LucideIcon,
} from 'lucide-react'

export type IconCard = {
  title: string
  body: string
  icon: LucideIcon
}

export const heroPills = [
  '3-day core route',
  '2 bonus days',
  'Free packing checklist',
  'Official links appendix',
]

export const premiumBullets: IconCard[] = [
  {
    title: 'Day-by-day route logic',
    body: 'A practical sequence that keeps the city coherent instead of forcing too many big sights into the same block.',
    icon: CalendarDays,
  },
  {
    title: 'Neighborhood-aware planning',
    body: 'Each day stays anchored in one part of the city so you spend more time enjoying Budapest and less time zig-zagging.',
    icon: Compass,
  },
  {
    title: 'Food and café anchors',
    body: 'The guide deliberately creates breaks, not just landmarks. That keeps the trip human-scaled.',
    icon: UtensilsCrossed,
  },
  {
    title: 'Bath + rainy-day backups',
    body: 'You get softer alternatives when the weather changes or energy drops, so the trip still feels designed.',
    icon: Umbrella,
  },
]

export const dayCards = [
  {
    label: 'Day 1',
    title: 'Castle District + Danube',
    body: 'Postcard Budapest done in a calm order: Bastion, church, riverfront, then an evening finish with room for sunset.',
  },
  {
    label: 'Day 2',
    title: 'Parliament + Baths + Quarter',
    body: 'A ceremonial morning, a real thermal block, then dinner and evening energy in the Jewish Quarter.',
  },
  {
    label: 'Day 3',
    title: 'City Park + Andrássy',
    body: 'A more breathable day with park space, architecture, coffee, and a stronger final dinner booking.',
  },
  {
    label: 'Day 4',
    title: 'Szentendre add-on',
    body: 'The optional slower detour: small streets, art-town mood, and an easier pace if you want more margin.',
  },
  {
    label: 'Day 5',
    title: 'Synagogue + food-led finish',
    body: 'A neighborhood-driven closing day focused on atmosphere, cafés, shops, and a softer final night.',
  },
]

export const checklistBullets: IconCard[] = [
  {
    title: 'Before-you-fly checks',
    body: 'Arrival route, offline address, and the bookings that are genuinely worth locking before the rest of the trip.',
    icon: PlaneLanding,
  },
  {
    title: 'Daily bag essentials',
    body: 'The practical items that stop small logistics from eating into your day once you are walking the city.',
    icon: Download,
  },
  {
    title: 'City-use habits',
    body: 'Simple reminders that keep Budapest enjoyable: pacing, under-planning your final evening, and protecting your recovery blocks.',
    icon: CheckCircle2,
  },
]

export const valueProps: IconCard[] = [
  {
    title: 'Actually works offline',
    body: 'Save the PDFs before you fly and keep the route handy even when your connection is patchy.',
    icon: Download,
  },
  {
    title: 'Uses official resources where it matters',
    body: 'The premium guide ends with the links worth checking right before the trip.',
    icon: MapPinned,
  },
  {
    title: 'Made for walking and recovery',
    body: 'The plan intentionally balances big sights with baths, cafés, and lower-pressure transitions.',
    icon: Waves,
  },
  {
    title: 'Pairs with the free checklist',
    body: 'Use the free download to sort the practical details, then use the premium guide to sequence the city.',
    icon: Ticket,
  },
]

export const faqs = [
  {
    q: 'What is free and what is paid?',
    a: 'The Budapest packing checklist is free. The larger 3-day core itinerary with the 2-day extension is the paid PDF.',
  },
  {
    q: 'Does the premium PDF work well on a phone?',
    a: 'Yes. It was laid out to be readable on a phone, easy to save offline, and simple to reference while you are already in the city.',
  },
  {
    q: 'Are prices and opening rules included?',
    a: 'The guide avoids hard-coding details that can change. Instead, it gives you the route logic and the official links worth checking before you go.',
  },
  {
    q: 'Who is this best for?',
    a: 'It is especially good for first-time visitors who want a cleaner 3-day Budapest plan, but it also works for return visitors who want a more structured extension.',
  },
]
