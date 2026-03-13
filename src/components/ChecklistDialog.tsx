'use client'

import { Download } from 'lucide-react'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
import { siteConfig } from '@/lib/site-config'
import { checklistBullets } from '@/lib/site-content'

export function ChecklistDialog({
  triggerLabel = 'Get the free checklist',
  className = '',
}: {
  triggerLabel?: string
  className?: string
}) {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <button
          className={className || 'inline-flex items-center justify-center rounded-full border border-white/30 bg-white/10 px-5 py-3 text-sm font-semibold text-white backdrop-blur transition hover:bg-white/15'}
        >
          {triggerLabel}
        </button>
      </DialogTrigger>
      <DialogContent className="max-w-4xl overflow-hidden border border-border bg-white p-0 text-foreground dark:bg-card sm:rounded-2xl">
        <div className="grid gap-0 md:grid-cols-[1.08fr_.92fr]">
          <div className="bg-slate-50 p-6 md:p-8">
            <DialogHeader className="space-y-3 text-left">
              <DialogTitle className="text-2xl text-slate-900">
                Free Budapest packing checklist
              </DialogTitle>
              <DialogDescription className="text-base text-slate-600">
                A genuinely useful 2-page companion PDF visitors can download instantly.
              </DialogDescription>
            </DialogHeader>

            <div className="mt-6 grid gap-4">
              {checklistBullets.map(({ title, body, icon: Icon }) => (
                <div
                  key={title}
                  className="rounded-2xl border border-slate-200 bg-white p-4 shadow-sm"
                >
                  <div className="flex items-start gap-3">
                    <div className="rounded-xl bg-primary/10 p-2 text-primary">
                      <Icon className="h-5 w-5" />
                    </div>
                    <div>
                      <p className="font-semibold text-slate-900">{title}</p>
                      <p className="mt-1 text-sm leading-6 text-slate-600">{body}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            <div className="mt-6 flex flex-wrap gap-3">
              <a
                href={siteConfig.freeChecklistUrl}
                download
                className="inline-flex items-center gap-2 rounded-full bg-primary px-5 py-3 text-sm font-semibold text-white transition hover:bg-primary/90"
              >
                <Download className="h-4 w-4" />
                Download checklist PDF
              </a>
              <a
                href={siteConfig.freeChecklistUrl}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-2 rounded-full border border-slate-300 px-5 py-3 text-sm font-semibold text-slate-900 transition hover:bg-slate-100"
              >
                Open in new tab
              </a>
            </div>
          </div>

          <div className="grid gap-0 bg-white md:grid-rows-2">
            {siteConfig.checklistPreviewPages.map((page) => (
              <div key={page.src} className="border-b border-slate-200 last:border-b-0">
                <img
                  src={page.src}
                  alt={page.alt}
                  className="h-full w-full object-cover"
                />
              </div>
            ))}
          </div>
        </div>
      </DialogContent>
    </Dialog>
  )
}
