/* src/components/Header.tsx */
import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-background border-b border-border">
      <div className="container flex items-center py-4">
        {/* Logo (left-aligned) */}
        <Link href="/" className="text-xl font-extrabold">
          <span className="text-foreground">Pearl</span>
          <span className="text-primary">Zone</span>
        </Link>
      </div>
    </header>
  );
}
