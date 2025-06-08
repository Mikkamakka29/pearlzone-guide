/* src/components/Header.tsx */
'use client';

import Link from 'next/link';
import { useEffect, useState } from 'react';

export default function Header() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 20);
    onScroll();
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition-colors
        ${scrolled
          ? 'bg-white/70 dark:bg-gray-900/80 backdrop-blur-md shadow-sm'
          : 'bg-transparent'}
      `}
    >
      <div className="container flex items-center justify-center py-3">
        {/* Logo */}
        <Link
          href="/"
          className="text-xl font-extrabold flex gap-1 items-baseline"
        >
          <span
            className={`transition-colors ${
              scrolled ? 'text-foreground' : 'text-white'
            }`}
          >
            Pearl
          </span>
          <span className="text-primary">Zone</span>
        </Link>
      </div>
    </header>
  );
}
