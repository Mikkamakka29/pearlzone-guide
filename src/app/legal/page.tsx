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
            <h2 className="text-lg font-bold text-slate-950">Digital delivery</h2>
            <p className="mt-2">
              The Budapest premium itinerary and the Budapest packing checklist are digital PDF products delivered by download. If you have trouble accessing a file, please get in touch and we will help.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Personal-use license</h2>
            <p className="mt-2">
              These files are intended for personal travel planning. They may not be redistributed, resold, or published publicly without written permission.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Planning disclaimer</h2>
            <p className="mt-2">
              Travel information changes. Opening hours, ticketing rules, temporary closures, transport details, and visitor access can shift. Please verify any time-sensitive detail through the official resources linked in the guide before you go.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Refunds</h2>
            <p className="mt-2">
              Because the premium itinerary is a digital product, purchases are generally final. If you received the wrong file or your download is defective, contact us and we will make it right.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Affiliate disclosure</h2>
            <p className="mt-2">
              Some outbound links may be affiliate links. If you book through them, PearlZone may earn a commission at no extra cost to you.
            </p>
          </section>

          <section>
            <h2 className="text-lg font-bold text-slate-950">Contact</h2>
            <p className="mt-2">
              For file issues, delivery questions, or general support, email{' '}
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
