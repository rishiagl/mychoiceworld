/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'bgi-1': "url('/one.jpg')",
        'bgi-2': "url('/two.jpg')",
        'bgi-3': "url('/three.jpg')",
        'bgi-4': "url('/four.jpg')",
        'bgi-5': "url('/sym.webp')",
        'bgi-6': "url('/bajaj2.webp')",
        'bgh': "url('/bgh.jpg')",
        'logo-lg': "url('/logo/lg.png')",
        'logo-samsung': "url('/logo/samsung.png')",
        'logo-voltas': "url('/logo/voltas.png')",
        'logo-bajaj': "url('/logo/bajaj.png')",
        'logo-symphony': "url('/logo/symphony.png')",
        'logo-symphony': "url('/sym.webp')",
      },

      animation: {
        ["infinite-slider"]: "infiniteSlider 20s linear infinite",
      },
      keyframes: {
        infiniteSlider: {
          "0%": { transform: "translateX(0)" },
          "100%": {
            transform: "translateX(calc(-250px * 5))",
          },
        },
      },
      fontFamily: {
        bungee: ["Bungee Tint", "sans-serif"],
        protest_guerrilla: ["Protest Guerrilla", "sans-serif"],
      },
    },
    plugins: [],
  }
}