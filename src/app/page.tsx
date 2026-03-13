/* eslint-disable @next/next/no-img-element */
import { ArrowRight, CheckCircle2, Download } from 'lucide-react'
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion'
import { Card, CardContent } from '@/components/ui/card'
import { ChecklistDialog } from '@/components/ChecklistDialog'
import { PdfPreviewDialog } from '@/components/PdfPreviewDialog'
import { SectionHeading } from '@/components/SectionHeading'
import { dayCards, faqs, heroPills, premiumBullets, valueProps } from '@/lib/site-content'
import { siteConfig } from '@/lib/site-config'

export default function Home() {
  return (
    <>
      <section className="relative isolate overflow-hidden bg-slate-950">
        <img
          src="/hero.jpg"
          alt="Golden-hour aerial view of Budapest"
          className="absolute inset-0 h-full w-full object-cover opacity-80"
        />
        <div className="absolute inset-0 bg-[linear-gradient(180deg,rgba(7,17,40,0.45)_0%,rgba(7,17,40,0.72)_50%,rgba(7,17,40,0.88)_100%)]" />
        <div className="absolute inset-x-0 bottom-0 h-28 bg-[linear-gradient(180deg,rgba(7,17,40,0)_0%,rgba(247,243,237,1)_100%)]" />

        <div className="container relative z-10 flex min-h-[88svh] items-center pt-28 pb-20">
          <div className="max-w-3xl text-white">
            <div className="mb-6 flex flex-wrap gap-2">
              {heroPills.map((pill) => (
                <span
                  key={pill}
                  className="rounded-full border border-white/20 bg-white/10 px-3 py-1.5 text-xs font-semibold uppercase tracking-[0.15em] text-white/90 backdrop-blur"
                >
                  {pill}
                </span>
              ))}
            </div>

            <h1 className="max-w-3xl text-4xl font-extrabold tracking-tight sm:text-5xl lg:text-6xl">
              Plan Budapest in minutes, not in 30 browser tabs.
            </h1>
            <p className="mt-6 max-w-2xl text-base leading-7 text-white/85 sm:text-xl sm:leading-8">
              Get a premium 3-day core itinerary with a clean 2-day extension, plus a genuinely useful free packing checklist you can download instantly.
            </p>

            <div className="mt-8 flex flex-wrap gap-3">
              <a
                href={siteConfig.gumroadUrl}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-2 rounded-full bg-primary px-5 py-3 text-sm font-semibold text-white shadow-2xl shadow-primary/20 transition hover:bg-primary/90"
              >
                Buy the premium itinerary
                <ArrowRight className="h-4 w-4" />
              </a>
              <ChecklistDialog />
            </div>

            <div className="mt-8 flex flex-wrap gap-5 text-sm text-white/80">
              <span className="inline-flex items-center gap-2">
                <CheckCircle2 className="h-4 w-4 text-accent" />
                Designed to be saved offline before you fly
              </span>
              <span className="inline-flex items-center gap-2">
                <Download className="h-4 w-4 text-accent" />
                Free packing checklist available right now
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-[#faf7f2] py-20">
        <div className="container grid gap-8 lg:grid-cols-[1.15fr_0.85fr]">
          <Card className="overflow-hidden rounded-[2rem] border-slate-200 bg-white shadow-sm">
            <CardContent className="p-8 sm:p-10">
              <SectionHeading
                eyebrow="Premium offer"
                title="What the premium PDF actually helps you do"
                body="It is built to remove sequencing decisions, protect your energy, and keep the city feeling elegant instead of over-packed."
              />
              <div className="mt-8 grid gap-4 sm:grid-cols-2">
                {premiumBullets.map(({ title, body, icon: Icon }) => (
                  <div key={title} className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
                    <div className="mb-4 inline-flex rounded-xl bg-primary/10 p-2 text-primary">
                      <Icon className="h-5 w-5" />
                    </div>
                    <p className="font-semibold text-slate-900">{title}</p>
                    <p className="mt-2 text-sm leading-6 text-slate-600">{body}</p>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card className="overflow-hidden rounded-[2rem] border-slate-200 bg-slate-950 text-white shadow-sm">
            <CardContent className="p-8 sm:p-10">
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-accent">
                Free download
              </p>
              <h2 className="mt-3 text-3xl font-bold tracking-tight">
                Start with the practical companion file.
              </h2>
              <p className="mt-4 text-base leading-7 text-white/80">
                Download a short, practical companion PDF that handles the packing and prep side of the trip before you buy anything.
              </p>

              <div className="mt-6 rounded-3xl border border-white/10 bg-white/5 p-3">
                <img
                  src={siteConfig.checklistPreviewPages[0].src}
                  alt={siteConfig.checklistPreviewPages[0].alt}
                  className="aspect-[4/5] w-full rounded-[1.2rem] object-cover"
                />
              </div>

              <div className="mt-6 flex flex-wrap gap-3">
                <ChecklistDialog
                  triggerLabel="Preview + download"
                  className="inline-flex items-center justify-center rounded-full bg-accent px-5 py-3 text-sm font-semibold text-accent-foreground transition hover:bg-accent/90"
                />
                <a
                  href={siteConfig.freeChecklistUrl}
                  download
                  className="inline-flex items-center gap-2 rounded-full border border-white/15 px-5 py-3 text-sm font-semibold text-white transition hover:bg-white/5"
                >
                  <Download className="h-4 w-4" />
                  Direct PDF download
                </a>
              </div>
            </CardContent>
          </Card>
        </div>
      </section>

      <section className="bg-white py-20">
        <div className="container">
          <SectionHeading
            eyebrow="Preview gallery"
            title="Preview the premium PDF before you buy"
            body="The preview pages show the tone, structure, and readability of the premium guide so you know exactly what kind of trip planning help you are getting."
          />
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            {siteConfig.premiumPreviewPages.map((page) => (
              <PdfPreviewDialog
                key={page.src}
                src={page.src}
                alt={page.alt}
                label={page.label}
              />
            ))}
          </div>
        </div>
      </section>

      <section className="bg-[#faf7f2] py-20">
        <div className="container">
          <SectionHeading
            eyebrow="Route architecture"
            title="The guide is organised around cleaner days, not more attractions"
            body="This is what makes the PDF feel worth paying for: the city is sequenced in a way that reduces friction and keeps energy where it matters."
          />
          <div className="mt-10 grid gap-6 lg:grid-cols-5">
            {dayCards.map((day) => (
              <div
                key={day.label}
                className="rounded-[1.6rem] border border-slate-200 bg-white p-6 shadow-sm"
              >
                <p className="text-sm font-semibold uppercase tracking-[0.16em] text-primary">
                  {day.label}
                </p>
                <h3 className="mt-3 text-xl font-bold tracking-tight text-slate-900">
                  {day.title}
                </h3>
                <p className="mt-3 text-sm leading-6 text-slate-600">{day.body}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-white py-20">
        <div className="container">
          <SectionHeading
            eyebrow="Project value"
            title="Why this guide lands better than generic travel posts"
            body="It is designed to reduce decision fatigue, not impress you with the longest possible list of things to do."
          />
          <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
            {valueProps.map(({ title, body, icon: Icon }) => (
              <Card key={title} className="rounded-[1.5rem] border-slate-200 bg-slate-50 shadow-none">
                <CardContent className="p-6">
                  <div className="inline-flex rounded-xl bg-primary/10 p-2 text-primary">
                    <Icon className="h-5 w-5" />
                  </div>
                  <h3 className="mt-4 text-lg font-bold tracking-tight text-slate-900">
                    {title}
                  </h3>
                  <p className="mt-2 text-sm leading-6 text-slate-600">{body}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      <section className="bg-[#faf7f2] py-20">
        <div className="container grid gap-8 rounded-[2rem] border border-slate-200 bg-white p-8 shadow-sm lg:grid-cols-[1fr_auto] lg:items-center lg:p-10">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.18em] text-primary">
              Ready to plan
            </p>
            <h2 className="mt-3 text-3xl font-bold tracking-tight text-slate-950">
              Use the free checklist first, then grab the full premium itinerary when you are ready to lock the route.
            </h2>
            <p className="mt-4 max-w-3xl text-base leading-7 text-slate-600">
              The premium PDF is built for visitors who want Budapest to feel clean, paced, and easy to follow on the ground - not like a race between disconnected highlights.
            </p>
          </div>
          <div className="flex flex-wrap gap-3 lg:justify-end">
            <ChecklistDialog
              triggerLabel="See the free checklist"
              className="inline-flex items-center justify-center rounded-full border border-slate-300 px-5 py-3 text-sm font-semibold text-slate-900 transition hover:bg-slate-50"
            />
            <a
              href={siteConfig.gumroadUrl}
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center gap-2 rounded-full bg-primary px-6 py-4 text-sm font-semibold text-white shadow-lg transition hover:bg-primary/90"
            >
              Buy the premium PDF
              <ArrowRight className="h-4 w-4" />
            </a>
          </div>
        </div>
      </section>

      <section className="bg-white py-20">
        <div className="container grid gap-12 lg:grid-cols-[0.78fr_1.22fr]">
          <SectionHeading
            eyebrow="FAQ"
            title="Frequently asked before buying"
            body="The goal is to answer the practical questions quickly so the page stays calm and conversion-friendly."
          />
          <Accordion type="single" collapsible className="w-full rounded-[1.6rem] border border-slate-200 bg-slate-50 px-6">
            {faqs.map((item, index) => (
              <AccordionItem key={item.q} value={`item-${index}`}>
                <AccordionTrigger className="text-base font-semibold text-slate-900 hover:no-underline">
                  {item.q}
                </AccordionTrigger>
                <AccordionContent className="pb-5 text-sm leading-7 text-slate-600">
                  {item.a}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>
    </>
  )
}
