/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  darkMode: "class",
  content: ["./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
    fontFamily: {
      inter: ["Inter", ...defaultTheme.fontFamily.sans],
    },
  },
  plugins: [],
};
