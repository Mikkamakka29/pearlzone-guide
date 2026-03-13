'use client'

import { Expand } from 'lucide-react'
import {
  Dialog,
  DialogContent,
  DialogTrigger,
} from '@/components/ui/dialog'

export function PdfPreviewDialog({
  src,
  alt,
  label,
}: {
  src: string
  alt: string
  label: string
}) {
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
          <div className="flex items-center justify-between px-5 py-4">
            <div>
              <p className="text-sm font-semibold text-slate-900">{label}</p>
              <p className="text-sm text-slate-500">Click to enlarge</p>
            </div>
          </div>
        </button>
      </DialogTrigger>
      <DialogContent className="max-w-5xl overflow-hidden border border-slate-200 bg-white p-0 shadow-2xl sm:rounded-2xl">
        <img src={src} alt={alt} className="h-auto w-full object-contain" />
      </DialogContent>
    </Dialog>
  )
}
