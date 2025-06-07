'use client';
import Link from 'next/link';
import { useEffect, useState } from 'react';

export default function Header() {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 30);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

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
        <nav className="hidden sm:flex gap-6 text-sm font-medium">
          <a href="#inside" className="hover:text-primary">Inside</a>
          <a href="#faq" className="hover:text-primary">FAQ</a>
          <a href="#buy" className="hover:text-primary">Buy</a>
        </nav>
      </div>
    </header>
  );
}
