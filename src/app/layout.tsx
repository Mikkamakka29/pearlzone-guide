import '@/app/globals.css'
import type { Metadata } from 'next'
import Header from '@/components/Header'
import { SiteFooter } from '@/components/SiteFooter'
import { siteConfig } from '@/lib/site-config'

export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.siteUrl),
  title: {
    default: 'PearlZone | Budapest itinerary PDF + free packing checklist',
    template: `%s | ${siteConfig.name}`,
  },
  description:
    'Carefully paced Budapest itinerary PDFs with a free packing checklist and a premium 3-to-5-day city guide.',
  openGraph: {
    title: 'PearlZone | Budapest itinerary PDF + free packing checklist',
    description:
      'Carefully paced Budapest itinerary PDFs with a free packing checklist and a premium 3-to-5-day city guide.',
    url: siteConfig.siteUrl,
    siteName: siteConfig.name,
    images: [
      {
        url: '/hero.jpg',
        width: 1456,
        height: 816,
        alt: 'Golden-hour Budapest skyline used as the PearlZone hero image',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'PearlZone | Budapest itinerary PDF + free packing checklist',
    description:
      'Carefully paced Budapest itinerary PDFs with a free packing checklist and a premium 3-to-5-day city guide.',
    images: ['/hero.jpg'],
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-background font-sans text-foreground antialiased">
        <Header />
        <main>{children}</main>
        <SiteFooter />
        <div className="fixed inset-x-0 bottom-0 z-30 border-t border-slate-200 bg-white/95 p-3 backdrop-blur sm:hidden">
          <a
            href={siteConfig.gumroadUrl}
            target="_blank"
            rel="noreferrer"
            className="flex items-center justify-center rounded-full bg-primary px-5 py-3 text-sm font-semibold text-white shadow-lg"
          >
            Get the premium itinerary
          </a>
        </div>
      </body>
    </html>
  )
}
