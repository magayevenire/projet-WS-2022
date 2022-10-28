/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  darkMode: "class",
  content: [
    "./*.vue",
    "./pages/**/*.vue",
    "./layouts/*.vue",
    "./components/**/*.vue",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
    fontFamily: {
      inter: ["Inter", ...defaultTheme.fontFamily.sans],
    },
  },
  plugins: [require('flowbite/plugin')],
};
