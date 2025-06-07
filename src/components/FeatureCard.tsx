/* eslint-disable @next/next/no-img-element */
export default function FeatureCard({ icon, text }:
    { icon: string; text: string }) {
    return (
      <div className="bg-white/80 backdrop-blur p-6 rounded-2xl shadow-sm text-center flex flex-col items-center gap-4">
        <img src={icon} alt="" className="w-10 h-10" />
        <p className="font-semibold">{text}</p>
      </div>
    );
  }
  