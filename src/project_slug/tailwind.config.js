/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./static/styles/**/*.css",
    "./static/scripts/**/*.js",
    // Jinja templates
    "./**/*.html",
    // exclude node_modules/
    "!./node_modules/**",
  ],
  theme: {
    extend: {
      colors: {
        text: "#2d4044",
        primary: "#d5eeea",
        secondary: "#24887b",
        accent: "#2eab9a",
      },
      fontFamily: {
        text: ["Inter", "sans-serif"],
        heading: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
