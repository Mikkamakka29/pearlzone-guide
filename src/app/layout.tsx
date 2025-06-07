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
      </body>
    </html>
  );
}
