import '@/app/globals.css';
import type { Metadata } from 'next';
import Header from '@/components/Header';

export const metadata: Metadata = {
  title: 'PearlZone – Budapest Itinerary',
  description: 'Plan the perfect Budapest trip in minutes.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen font-sans text-gray-900 antialiased bg-white">
        <Header />
        <main className="pt-16">{children}</main>
        <div className="fixed bottom-0 inset-x-0 z-40 flex sm:hidden justify-center p-4 bg-white/90 backdrop-blur border-t border-border">
          <a
            href="#buy"
            className="bg-primary text-white py-3 px-6 rounded-full font-semibold shadow-lg"
          >
            Get Itinerary (€17)
          </a>
        </div>
      </body>
    </html>
  );
}
