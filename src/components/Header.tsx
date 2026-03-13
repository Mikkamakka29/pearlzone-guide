import Link from 'next/link'

export default function Header() {
  return (
    <header className="absolute inset-x-0 top-0 z-40">
      <div className="container flex items-center py-5">
        <Link href="/" className="text-xl font-extrabold tracking-tight">
          <span className="text-white">Pearl</span>
          <span className="text-primary">Zone</span>
        </Link>
      </div>
    </header>
  )
}
