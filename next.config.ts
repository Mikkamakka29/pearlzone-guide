import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  // Tell Next to do a static HTML export → writes to /out
  output: 'export',
  // (Optional) if you plan to use <Image>, disable optimisation for static export:
  images: { unoptimized: true },
}

export default nextConfig