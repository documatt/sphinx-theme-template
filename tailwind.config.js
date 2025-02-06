/** @type {import('tailwindcss').Config} */
module.exports = {
  // Paths are relative to project root, not tailwind.config.js file
  content: [
    "./src/project_slug/static/styles/**/*.css",
    "./src/project_slug/static/scripts/**/*.js",
    // Jinja templates
    "./src/project_slug/**/*.html",
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
