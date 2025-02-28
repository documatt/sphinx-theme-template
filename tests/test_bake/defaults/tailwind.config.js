/** @type {import('tailwindcss').Config} */
module.exports = {
  // Paths are relative to project root, not tailwind.config.js file
  content: [
    "./src/sphinx_minimal_theme/static/styles/**/*.css",
    "./src/sphinx_minimal_theme/static/scripts/**/*.js",
    // Jinja templates
    "./src/sphinx_minimal_theme/**/*.html",
    // exclude node_modules/
    "!./node_modules/**",
  ],
  theme: {
    extend: {
      colors: {
        text: "#2d4044",
        background: "#FAF8FC",
        primary: "#0072F5",
        secondary: "#0C7CBA",
        accent: "#0C7CBA",
      },
      fontFamily: {
        text: ["Inter", "sans-serif"],
        heading: ["Work Sans", "sans-serif"],
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
