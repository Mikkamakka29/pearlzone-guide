import Link from 'next/link'

export default function NotFound() {
  return (
    <main className="grid min-h-[70vh] place-items-center bg-[#faf7f2] px-6 py-24">
      <div className="max-w-xl text-center">
        <p className="text-sm font-semibold uppercase tracking-[0.18em] text-primary">404</p>
        <h1 className="mt-4 text-4xl font-bold tracking-tight text-slate-950">
          This page wandered off the route.
        </h1>
        <p className="mt-4 text-base leading-7 text-slate-600">
          Head back to the main landing page to preview the Budapest itinerary setup.
        </p>
        <Link
          href="/"
          className="mt-8 inline-flex rounded-full bg-primary px-5 py-3 text-sm font-semibold text-white transition hover:bg-primary/90"
        >
          Back to PearlZone
        </Link>
      </div>
    </main>
  )
}
