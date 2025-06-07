import '@/app/globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'PearlZone – Budapest Itinerary',
  description: 'Plan the perfect Budapest trip in minutes.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen font-sans text-gray-900 antialiased bg-white">
        {children}
      </body>
    </html>
  );
}
