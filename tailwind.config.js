/** @type {import('tailwindcss').Config} */
module.exports = {
    // Tell Tailwind where to scan for class names
    content: [
      "./src/app/**/*.{js,ts,jsx,tsx}",
      "./src/components/**/*.{js,ts,jsx,tsx}",
      "./src/pages/**/*.{js,ts,jsx,tsx}",
    ],
  
    theme: {
      extend: {
        /* ─── Design-system palette ─────────────────────────────── */
        colors: {
          primary: "#0B6AFF", // Danube blue
          accent:  "#F8C13B", // Thermal-bath gold
        },
        /* ─── Default sans font ─────────────────────────────────── */
        fontFamily: {
          sans: ["Inter", "ui-sans-serif", "system-ui"],
        },
      },
    },
  
    plugins: [],
};
  