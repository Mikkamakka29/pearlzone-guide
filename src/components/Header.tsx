'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';
import { Menu } from 'lucide-react';

export default function Header() {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 30);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  /* ——— NAV LINKS (reuse once) ——— */
  const NavLinks = () => (
    <>
      <a href="#inside" className="hover:text-primary">Inside</a>
      <a href="#faq"    className="hover:text-primary">FAQ</a>
      <a href="#buy"    className="hover:text-primary">Buy</a>
    </>
  );

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition
        ${scrolled ? 'bg-white/80 backdrop-blur border-b border-gray-200' : 'bg-transparent'}
      `}
    >
      <div className="container flex items-center justify-between py-3">
        <Link href="/" className="text-xl font-bold">
          Pearl<span className="text-primary">Zone</span>
        </Link>

        {/* Desktop Nav */}
        <nav className="hidden sm:flex gap-6 text-sm font-medium">
          <NavLinks />
        </nav>

        {/* Mobile Menu */}
        <div className="sm:hidden">
          <Sheet>
            <SheetTrigger asChild>
              <button aria-label="Open menu">
                <Menu className="w-6 h-6" />
              </button>
            </SheetTrigger>
            <SheetContent side="left" className="flex flex-col gap-6 pt-20 text-lg font-semibold">
              <NavLinks />
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  );
}
