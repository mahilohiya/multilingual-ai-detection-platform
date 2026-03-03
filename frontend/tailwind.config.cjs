/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#050816",
        surface: "#0b1020",
        accent: "#a855f7",
        accentSoft: "#4c1d95",
        human: "#22c55e",
        ai: "#f97373"
      }
    }
  },
  plugins: []
};

