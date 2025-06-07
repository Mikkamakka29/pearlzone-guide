/** @type {import('tailwindcss').Config} */
module.exports = {
content: [
    "./src/app/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
    // add more folders later if needed
],
theme: {
    extend: {
    colors: {
        primary: "#0B6AFF", // Danube blue
        accent:  "#F8C13B", // thermal-bath gold
    },
    fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui"],
    },
    },
},
plugins: [],
};