import { siteConfig } from '@/lib/site-config'

export const metadata = {
  title: 'Legal',
}

export default function LegalPage() {
  return (
    <main className="bg-[#faf7f2] py-24">
      <div className="container max-w-3xl rounded-[2rem] border border-slate-200 bg-white p-8 shadow-sm sm:p-10">
        <p className="text-sm font-semibold uppercase tracking-[0.18em] text-primary">
          Legal + product terms
        </p>
        <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-950">
          PearlZone legal information
        </h1>
        <div className="mt-8 space-y-8 text-sm leading-7 text-slate-700">
          <section>
            <h2 className="text-lg font-bold text-slate-950">Digital product delivery</h2>
            <p className="mt-2">
              The premium itinerary is intended to be delivered as a digital PDF through Gumroad or another checkout platform you configure. The free packing checklist is a public download intended as a lead magnet or goodwill asset.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Personal-use license</h2>
            <p className="mt-2">
              The PDFs are designed for personal travel planning. If you plan to sell or distribute the premium itinerary commercially, keep your checkout terms, refund policy, and ownership wording aligned with your final business setup.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Planning disclaimer</h2>
            <p className="mt-2">
              Travel information changes. Attraction access rules, prices, temporary closures, and transport flows can shift. The premium guide deliberately includes official visitor links so travelers can verify the small number of details that genuinely need a last check.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Affiliate disclosure</h2>
            <p className="mt-2">
              If you add GetYourGuide, transport, or accommodation affiliate links to the project, disclose them clearly on the relevant page and at checkout where appropriate.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Contact</h2>
            <p className="mt-2">
              For file issues or configuration questions, use{' '}
              <a className="font-semibold text-primary underline" href={`mailto:${siteConfig.contactEmail}`}>
                {siteConfig.contactEmail}
              </a>
              .
            </p>
          </section>
        </div>
      </div>
    </main>
  )
}
