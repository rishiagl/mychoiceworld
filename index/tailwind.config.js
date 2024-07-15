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
      }
    },
    plugins: [],
  }
}