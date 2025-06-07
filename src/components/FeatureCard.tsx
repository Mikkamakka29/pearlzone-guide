import { Card, CardContent } from "@/components/ui/card";
import type { LucideIcon } from "lucide-react";

interface FeatureProps {
  icon: LucideIcon;
  text: string;
}

export default function FeatureCard({ icon: Icon, text }: FeatureProps) {
  return (
    <Card className="shadow-sm">
      <CardContent className="p-6 flex flex-col items-center gap-4">
        <Icon className="w-8 h-8 text-primary" strokeWidth={1.8} />
        <p className="font-semibold text-center">{text}</p>
      </CardContent>
    </Card>
  );
}
