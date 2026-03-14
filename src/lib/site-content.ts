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
  '3 core days',
  '2 add-on days',
  'Free packing checklist',
  'Official links appendix',
]

export const premiumBullets: IconCard[] = [
  {
    title: 'Smarter sequencing',
    body: 'The guide keeps each day geographically coherent so you spend less time zig-zagging across the city.',
    icon: CalendarDays,
  },
  {
    title: 'Reserve-first guidance',
    body: 'You get quick notes on what is worth booking early and what can stay flexible until you land.',
    icon: Compass,
  },
  {
    title: 'Food and coffee anchors',
    body: 'The days include natural breaks for lunch, coffee, and a calmer reset between headline sights.',
    icon: UtensilsCrossed,
  },
  {
    title: 'Rainy-day and low-energy swaps',
    body: 'The route still works when the weather changes or when you want to slow the trip down a little.',
    icon: Umbrella,
  },
]

export const dayCards = [
  {
    label: 'Day 1',
    title: 'Castle District + Danube',
    body: 'A strong first-impression day built around the Bastion, church interiors, river views, and an elegant evening finish.',
  },
  {
    label: 'Day 2',
    title: 'Parliament + baths + Quarter',
    body: 'The ceremonial city core in the morning, thermal recovery in the afternoon, and the Jewish Quarter once the pace lifts again.',
  },
  {
    label: 'Day 3',
    title: 'City Park + Andrássy',
    body: 'A more breathable day of architecture, park space, cafés, and a final dinner that feels earned rather than rushed.',
  },
  {
    label: 'Day 4',
    title: 'Szentendre add-on',
    body: 'A slower art-town day if you want one well-paced escape from the centre without losing the feel of the trip.',
  },
  {
    label: 'Day 5',
    title: 'Synagogue + food-led finish',
    body: 'A softer closing day shaped around the Jewish Quarter, good food, design shops, and a final golden-hour walk.',
  },
]

export const checklistBullets: IconCard[] = [
  {
    title: 'What to save offline',
    body: 'Addresses, confirmations, transport tools, and the small details that are annoying to look for after you land.',
    icon: PlaneLanding,
  },
  {
    title: 'What to pack for walking and baths',
    body: 'A simple carry system for long city days, weather swings, and a thermal-bath session that still feels easy.',
    icon: Download,
  },
  {
    title: 'What to sort before the flight home',
    body: 'A short reset list so the final evening stays pleasant and the departure morning stays calm.',
    icon: CheckCircle2,
  },
]

export const valueProps: IconCard[] = [
  {
    title: 'Built for walking days',
    body: 'The route is designed around how Budapest actually feels on foot, not around collecting the longest list of stops.',
    icon: Waves,
  },
  {
    title: 'Easy to save offline',
    body: 'Both PDFs are laid out to be readable on a phone and useful once you are already out in the city.',
    icon: Download,
  },
  {
    title: 'Current official links included',
    body: 'The premium guide ends with the official visitor pages worth checking right before the trip.',
    icon: MapPinned,
  },
  {
    title: 'Works for 3 days or 5',
    body: 'Use the 3-day core alone or add the extra two days when you want more breathing room in the schedule.',
    icon: Ticket,
  },
]

export const faqs = [
  {
    q: 'What is free and what is paid?',
    a: 'The Budapest packing checklist is free. The larger 3-day premium itinerary with the 2-day extension is the paid PDF.',
  },
  {
    q: 'Is the premium guide easy to use on a phone?',
    a: 'Yes. It is laid out to be readable on a phone, easy to save offline, and simple to reference while you are already in the city.',
  },
  {
    q: 'Does the premium file include current official links?',
    a: 'Yes. The final appendix collects the official visitor pages worth checking for transport, baths, Parliament, church access, and a few other practical details.',
  },
  {
    q: 'Who is this best for?',
    a: 'It is especially useful for first-time visitors who want a confident Budapest plan without over-scheduling every hour of the trip.',
  },
]
