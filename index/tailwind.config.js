/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'bgi-1': "url('/1.jpg')",
        'bgi-2': "url('/2.jpg')",
        'bgi-3': "url('/3.jpg')",
      }
    },
    plugins: [],
  }
}