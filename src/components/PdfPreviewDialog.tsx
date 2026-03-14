/* eslint-disable @next/next/no-img-element */
'use client'

import { Expand, ExternalLink } from 'lucide-react'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog'
import { cn } from '@/lib/utils'

type PreviewLink = {
  label: string
  url: string
  description?: string
}

export function PdfPreviewDialog({
  src,
  alt,
  label,
  caption,
  links,
}: {
  src: string
  alt: string
  label: string
  caption?: string
  links?: readonly PreviewLink[]
}) {
  const hasLinks = Boolean(links?.length)

  return (
    <Dialog>
      <DialogTrigger asChild>
        <button className="group overflow-hidden rounded-[1.4rem] border border-slate-200 bg-white text-left shadow-sm transition hover:-translate-y-1 hover:shadow-xl">
          <div className="relative">
            <img src={src} alt={alt} className="aspect-[4/5] w-full object-cover" />
            <div className="absolute right-4 top-4 rounded-full bg-slate-950/75 p-2 text-white opacity-0 transition group-hover:opacity-100">
              <Expand className="h-4 w-4" />
            </div>
          </div>
          <div className="space-y-1 px-5 py-4">
            <p className="text-sm font-semibold text-slate-900">{label}</p>
            <p className="text-sm text-slate-500">{caption || 'Open the full-page preview'}</p>
          </div>
        </button>
      </DialogTrigger>
      <DialogContent className="max-w-6xl overflow-hidden border border-slate-200 bg-white p-0 shadow-2xl sm:rounded-2xl">
        <DialogHeader className="sr-only">
          <DialogTitle>{label}</DialogTitle>
          <DialogDescription>{caption || alt}</DialogDescription>
        </DialogHeader>
        <div className={cn('grid max-h-[90vh]', hasLinks && 'lg:grid-cols-[minmax(0,1fr)_320px]')}>
          <div className="overflow-auto bg-slate-100 p-3 sm:p-5">
            <div className="flex min-h-full items-center justify-center">
              <img
                src={src}
                alt={alt}
                className="h-auto max-h-[82vh] w-auto max-w-full rounded-xl bg-white shadow-lg object-contain"
              />
            </div>
          </div>
          {hasLinks ? (
            <aside className="overflow-auto border-t border-slate-200 bg-white p-5 lg:border-l lg:border-t-0">
              <p className="text-xs font-semibold uppercase tracking-[0.16em] text-primary">
                Live links
              </p>
              <h3 className="mt-2 text-lg font-bold tracking-tight text-slate-950">
                Open the official resources from this page.
              </h3>
              <p className="mt-2 text-sm leading-6 text-slate-600">
                These are the same official pages referenced in the premium appendix, available here as direct clicks.
              </p>
              <div className="mt-5 grid gap-3">
                {links?.map((link) => (
                  <a
                    key={link.url}
                    href={link.url}
                    target="_blank"
                    rel="noreferrer"
                    className="rounded-2xl border border-slate-200 bg-slate-50 p-4 transition hover:border-primary/30 hover:bg-primary/5"
                  >
                    <div className="flex items-start justify-between gap-3">
                      <div>
                        <p className="font-semibold text-slate-900">{link.label}</p>
                        {link.description ? (
                          <p className="mt-1 text-sm leading-6 text-slate-600">{link.description}</p>
                        ) : null}
                      </div>
                      <ExternalLink className="mt-0.5 h-4 w-4 shrink-0 text-primary" />
                    </div>
                  </a>
                ))}
              </div>
            </aside>
          ) : null}
        </div>
      </DialogContent>
    </Dialog>
  )
}
