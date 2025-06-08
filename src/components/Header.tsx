/* src/components/Header.tsx */
import Link from 'next/link';

export default function Header() {
  return (
    <header className="absolute inset-x-0 top-0 z-50">
      <div className="container flex items-center py-4">
        <Link href="/" className="text-xl font-extrabold">
          <span className="text-white">Pearl</span>
          <span className="text-primary">Zone</span>
        </Link>
      </div>
    </header>
  );
}
