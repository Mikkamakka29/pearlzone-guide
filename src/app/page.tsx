/* eslint-disable @next/next/no-img-element */
export default function Home() {
  return (
    <main>
      {/* HERO */}
      <section className="h-[90vh] flex flex-col items-center justify-center text-center px-6">
        <h1 className="text-4xl sm:text-6xl font-bold leading-tight mb-4">
          Plan the Perfect <span className="text-primary">Budapest</span> Trip&nbsp;in&nbsp;Minutes
        </h1>
        <p className="max-w-2xl text-lg sm:text-xl mb-8">
          Skip 30&nbsp;tabs of research. Download an expert-crafted 3- or 5-day itinerary with hidden-gem tips &amp; Google&nbsp;Maps pins.
        </p>
        <a
          className="gumroad-button inline-block bg-primary text-white px-6 py-3 rounded-2xl text-lg font-semibold shadow hover:shadow-lg transition"
          href="https://pearlzone.gumroad.com/l/budapest-itinerary"
          target="_blank"
          rel="noopener"
        >
          Download Itinerary (€17)
        </a>
      </section>

      {/* WHAT’S INSIDE */}
      <section className="bg-gray-50 py-16 px-6">
        <h2 className="text-3xl font-bold text-center mb-10">What’s Inside</h2>
        <div className="max-w-5xl mx-auto grid sm:grid-cols-3 gap-8">
          {[
            'Hour-by-hour schedule',
            'Google Maps links',
            'Local foodie picks',
          ].map((item) => (
            <div
              key={item}
              className="bg-white p-6 rounded-2xl shadow flex items-center justify-center text-center font-semibold"
            >
              {item}
            </div>
          ))}
        </div>
      </section>

      {/* FAQ */}
      <section className="py-16 px-6">
        <h2 className="text-3xl font-bold text-center mb-10">FAQ</h2>
        <div className="max-w-3xl mx-auto space-y-6">
          <details className="bg-gray-50 p-4 rounded-xl">
            <summary className="cursor-pointer font-semibold">
              How do I get the PDF?
            </summary>
            <p className="mt-2">Instant download &amp; email via Gumroad after payment.</p>
          </details>
          <details className="bg-gray-50 p-4 rounded-xl">
            <summary className="cursor-pointer font-semibold">
              Does it work offline?
            </summary>
            <p className="mt-2">Yes—save it in Books/Kindle or any PDF reader.</p>
          </details>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-gray-900 text-gray-300 text-center py-8 text-sm">
        © {new Date().getFullYear()} PearlZone.{' '}
        <a href="/legal" className="underline">
          Legal
        </a>
      </footer>

      <script async src="https://gumroad.com/js/gumroad.js"></script>
    </main>
  );
}