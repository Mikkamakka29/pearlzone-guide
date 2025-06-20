/* eslint-disable @next/next/no-img-element */
import { Clock, MapPinned, UtensilsCrossed } from "lucide-react";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import { Star } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { ShieldCheck } from "lucide-react";

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
          className="gumroad-button inline-block px-8 py-4 rounded-2xl text-lg font-semibold transition-all duration-150 ease-out shadow-lg ring-2 ring-transparent hover:ring-accent/70">
          Download Itinerary (€17)
        </a>
        <div className="mt-4 flex items-center gap-2">
          {Array.from({ length: 5 }).map((_, i) => (
            <Star key={i} className="w-5 h-5 text-accent fill-accent" />
          ))}
          <span className="text-sm opacity-90">4.9/5 • 126 travelers</span>
        </div>
      </section>

      {/* WHY PEARLZONE */}
      <section className="py-24 bg-background scroll-mt-24">
        <h2 className="text-3xl font-bold text-center mb-16">Why PearlZone?</h2>

        <div className="container grid gap-10 sm:grid-cols-3">
          <Badge className="flex items-start gap-4 p-6 bg-white/90 dark:bg-card shadow border border-border">
            <Clock className="w-6 h-6 text-primary mt-1" />
            <div>
              <p className="font-semibold">Save 10 h of planning</p>
              <p className="text-sm text-muted-foreground">Skip research rabbit-holes</p>
            </div>
          </Badge>

          <Badge className="flex items-start gap-4 p-6 bg-white/90 dark:bg-card shadow border border-border">
            <MapPinned className="w-6 h-6 text-primary mt-1" />
            <div>
              <p className="font-semibold">Seamless Google Maps</p>
              <p className="text-sm text-muted-foreground">Tap-to-navigate pins</p>
            </div>
          </Badge>

          <Badge className="flex items-start gap-4 p-6 bg-white/90 dark:bg-card shadow border border-border">
            <UtensilsCrossed className="w-6 h-6 text-primary mt-1" />
            <div>
              <p className="font-semibold">Local foodie secrets</p>
              <p className="text-sm text-muted-foreground">Eat beyond goulash</p>
            </div>
          </Badge>
        </div>
      </section>

      {/* SOCIAL PROOF */}
      <section className="py-20 scroll-mt-24">
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

      {/* 7-Day Risk-free Guarantee */}
      <section className="py-20 scroll-mt-24">
      <Alert
        className="container mx-auto max-w-4xl        /* limit width to 1024 px */
                  flex items-center gap-4
                  p-6 bg-accent/10 border border-accent/30 rounded-2xl">
        <ShieldCheck className="w-7 h-7 text-accent shrink-0 self-start" />  {/* icon top-aligns */}     

        <div className="space-y-1">
          <AlertTitle className="font-semibold leading-none">
            7-Day&nbsp;Guarantee
          </AlertTitle>
          <AlertDescription className="leading-snug">
            Not happy? Email us within a week and we’ll refund you — no questions asked.
          </AlertDescription>
        </div>
      </Alert>
      </section>

      {/* FAQ */}
      <section id="faq" className="py-20 bg-gray-50 scroll-mt-24">
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

          <DialogContent className="max-w-sm bg-white dark:bg-card text-foreground border border-border shadow-xl rounded-xl space-y-5">
            <h3 className="text-lg font-semibold">Get the Budapest Packing Checklist PDF</h3>

            <form
              action="#"
              method="POST"
              className="flex flex-col gap-4"
            >
              <input
                type="email"
                required
                placeholder="you@example.com"
                className="w-full px-3 py-2 rounded-md text-sm
                          bg-background border border-border
                          placeholder:text-muted-foreground
                          focus:outline-none focus:ring-2 focus:ring-primary/60"
              />

              {/* accent-gold button */}
              <button
                type="submit"
                className="bg-accent text-accent-foreground py-2 rounded-md font-medium
                          shadow transition-colors
                          hover:bg-[hsl(var(--accent)/.85)] focus:ring-2 focus:ring-accent/60"
              >
                Send me the PDF
              </button>

              <p className="text-xs text-muted-foreground">
                We’ll email the checklist & occasional Budapest tips. Unsubscribe anytime.
              </p>
            </form>
          </DialogContent>
        </Dialog>
      </footer>

      <script async src="https://gumroad.com/js/gumroad.js"></script>
    </>
  );
}
