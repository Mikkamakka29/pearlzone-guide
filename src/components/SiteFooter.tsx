import Link from 'next/link'
import { siteConfig } from '@/lib/site-config'
import { ChecklistDialog } from '@/components/ChecklistDialog'

export function SiteFooter() {
  return (
    <footer className="border-t border-slate-200 bg-slate-950 text-slate-300">
      <div className="container grid gap-8 py-12 md:grid-cols-[1.2fr_.8fr] md:items-end">
        <div>
          <p className="text-xl font-extrabold tracking-tight">
            <span className="text-white">Pearl</span>
            <span className="text-primary">Zone</span>
          </p>
          <p className="mt-4 max-w-xl text-sm leading-6 text-slate-400">
            Budapest planning files built to be clear, calm, and easy to save offline before you fly.
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-4 md:justify-end">
          <ChecklistDialog
            triggerLabel="Free packing checklist"
            className="inline-flex items-center justify-center rounded-full border border-white/15 px-4 py-2 text-sm font-semibold text-white transition hover:bg-white/5"
          />
          <Link href="/legal" className="text-sm font-semibold text-accent transition hover:text-white">
            Legal
          </Link>
          <a href={`mailto:${siteConfig.contactEmail}`} className="text-sm text-slate-400 transition hover:text-white">
            {siteConfig.contactEmail}
          </a>
        </div>
      </div>
    </footer>
  )
}
