import type { MetadataRoute } from 'next'
import { siteConfig } from '@/lib/site-config'

export const dynamic = 'force-static'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: siteConfig.siteUrl,
      lastModified: '2026-03-13',
      changeFrequency: 'weekly',
      priority: 1,
    },
    {
      url: `${siteConfig.siteUrl}/legal`,
      lastModified: '2026-03-13',
      changeFrequency: 'monthly',
      priority: 0.5,
    },
  ]
}
