/* src/components/Header.tsx */
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useState } from 'react';
import { Menu } from 'lucide-react';
import {
  Sheet,
  SheetContent,
  SheetTrigger,
} from '@/components/ui/sheet';

const nav = [
  { href: '#inside', label: 'Inside' },
  { href: '#faq',    label: 'FAQ'   },
  { href: '#buy',    label: 'Buy'   },
];

export default function Header() {
  const [scrolled, setScrolled] = useState(false);
  const pathname   = usePathname();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    onScroll();
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  /* ------------- NAV LINK SHARED STYLES ------------- */
  const linkBase =
    'relative after:absolute after:bottom-0 after:left-0 after:h-0.5 ' +
    'after:w-0 after:bg-primary after:transition-all hover:after:w-full';

  return (
    <header
      className={`
        fixed inset-x-0 top-0 z-50 transition-colors
        ${scrolled
          ? 'bg-white/70 dark:bg-gray-900/80 backdrop-blur-md shadow-sm'
          : 'bg-transparent'}
      `}
    >
      <div className="container flex items-center justify-between py-3">
        {/* Logo */}
        <Link href="/" className="text-xl font-extrabold">
          Pearl<span className="text-primary">Zone</span>
        </Link>

        {/* Desktop nav */}
        <nav className="hidden sm:flex gap-8 text-sm font-medium">
          {nav.map(({ href, label }) => (
            <a
              key={href}
              href={href}
              className={`${linkBase} after:duration-300 ${
                pathname === href ? 'text-primary after:w-full' : 'text-foreground'
              }`}
            >
              {label}
            </a>
          ))}
        </nav>

        {/* Mobile nav */}
        <div className="sm:hidden">
          <Sheet>
            <SheetTrigger aria-label="Open menu">
              <Menu className="w-6 h-6" />
            </SheetTrigger>

            <SheetContent
              side="left"
              className="w-64 bg-background/95 backdrop-blur border-r border-border p-6"
            >
              <nav className="flex flex-col gap-6 mt-10 font-medium text-lg">
                {nav.map(({ href, label }) => (
                  <a
                    key={href}
                    href={href}
                    className="hover:text-primary transition-colors"
                  >
                    {label}
                  </a>
                ))}
              </nav>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  );
}
