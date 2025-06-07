/* eslint-disable @next/next/no-img-element */
import FeatureCard from '@/components/FeatureCard';
import { Clock, MapPinned, UtensilsCrossed } from "lucide-react";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";

export default function Home() {
  return (
    <>
      {/* HERO */}
      <section
        style={{
          backgroundImage: `linear-gradient(to bottom,rgba(0,0,0,.4),rgba(0,0,0,.6)),url(/hero.jpg)`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        }}
        className="h-[90vh] flex flex-col items-center justify-center text-center text-white px-6"
      >
        <h1 className="container text-4xl sm:text-6xl font-extrabold leading-tight drop-shadow-lg mb-6">
          Plan the Perfect <span className="text-primary">Budapest</span> Trip&nbsp;in&nbsp;Minutes
        </h1>
        <p className="container max-w-2xl text-lg sm:text-xl mb-10 opacity-90">
          Skip 30&nbsp;tabs of research. Download an expert-crafted itinerary packed with hidden-gem tips &amp; Google Maps pins.
        </p>
        <a
          id="buy"
          href="https://pearlzone.gumroad.com/l/budapest-itinerary"
          className="gumroad-button inline-block px-8 py-4 rounded-2xl text-lg font-semibold
                     transition-all duration-150 ease-out shadow-lg ring-2 ring-transparent
                     hover:ring-accent/70"
        >
          Download Itinerary (€17)
        </a>
      </section>

      {/* WHAT’S INSIDE */}
      <section id="inside" className="py-20 bg-gray-50">
        <h2 className="text-3xl font-bold text-center mb-14 text-accent">What’s Inside</h2>
        <div className="container grid gap-8 sm:grid-cols-3">
          <FeatureCard icon={Clock}          text="Hour-by-hour schedule" />
          <FeatureCard icon={MapPinned}      text="Google Maps links" />
          <FeatureCard icon={UtensilsCrossed} text="Local foodie picks" />
        </div>
      </section>

      {/* SOCIAL PROOF */}
      <section className="py-20">
        <h2 className="text-3xl font-bold text-center mb-14">Traveller&nbsp;Reviews</h2>
        <div className="container max-w-3xl space-y-8">
          {[
            ['“Worth every euro — saved us a full day of planning.”', '— Anna K.'],
            ['“Loved the hidden cafés! Perfect 3-day flow.”', '— Liam R.'],
            ['“Maps links made navigating Budapest a breeze.”', '— Giulia F.'],
          ].map(([quote, by]) => (
            <figure key={by} className="bg-gray-50 p-6 rounded-2xl shadow">
              <blockquote className="italic mb-2">{quote}</blockquote>
              <figcaption className="text-sm text-gray-500">{by}</figcaption>
            </figure>
          ))}
        </div>
      </section>

      {/* FAQ */}
      <section id="faq" className="py-20 bg-gray-50">
        <h2 className="text-3xl font-bold text-center mb-14">FAQ</h2>
        <Accordion type="single" collapsible className="w-full max-w-3xl mx-auto">
          <AccordionItem value="item-1">
            <AccordionTrigger>How do I get the PDF?</AccordionTrigger>
            <AccordionContent>
              Instant download + email via Gumroad right after payment.
            </AccordionContent>
          </AccordionItem>

          <AccordionItem value="item-2">
            <AccordionTrigger>Does it work offline?</AccordionTrigger>
            <AccordionContent>
              Yes — save it in any PDF reader; all links still open in Google Maps.
            </AccordionContent>
          </AccordionItem>

          <AccordionItem value="item-3">
            <AccordionTrigger>Refunds?</AccordionTrigger>
            <AccordionContent>
              Digital items are non-refundable, but email us within 7 days for any file
              issues and we’ll sort you out.
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      </section>

      {/* FOOTER */}
      <footer className="bg-gray-900 text-gray-300 text-center py-8 text-sm space-x-4">
        © {new Date().getFullYear()} PearlZone.

        <a href="/legal" className="underline text-accent hover:text-white">
          Legal
        </a>

        {/* Free checklist popup */}
        <Dialog>
          <DialogTrigger asChild>
            <button className="underline hover:text-white">
              Free packing checklist
            </button>
          </DialogTrigger>

          <DialogContent className="max-w-sm bg-background text-foreground border-border shadow-lg rounded-xl">
            <h3 className="text-lg font-semibold mb-4">
              Get the Budapest Packing Checklist PDF
            </h3>

            {/* 👉 swap for your real form (ConvertKit, Buttondown, etc.) */}
            <form
              action="https://example.us1.list-manage.com/subscribe/post"
              method="POST"
              className="flex flex-col gap-4"
            >
              <input
                type="email"
                name="EMAIL"
                placeholder="you@example.com"
                required
                className="w-full px-3 py-2 border border-border rounded-md
                text-sm bg-background placeholder:text-muted-foreground
                focus:outline-none focus:ring-2 focus:ring-primary/60"
              />
              <button
                type="submit"
                className="bg-primary text-primary-foreground py-2 rounded-md font-medium hover:bg-primary/90 transition-colors"
              >
                Send me the PDF
              </button>
              <p className="text-xs text-gray-500">
                We’ll email the checklist & occasional Budapest tips. Unsubscribe
                anytime.
              </p>
            </form>
          </DialogContent>
        </Dialog>
      </footer>

      <script async src="https://gumroad.com/js/gumroad.js"></script>
    </>
  );
}
