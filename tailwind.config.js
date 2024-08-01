/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./*/templates/**/*.html",  // for templates in app directories
    "./**/templates/**/*.html",  // for templates in app subdirectories
    "./static/src/**/*.js",  // for any JavaScript files
    "./*/static/**/*.js",  // for JavaScript in app static directories
  ],
  theme: {
    extend: {
      colors: {
        'custom-purple': '#013A12',
        'custom-dark-green': '#013A12',
        'custom-brown': '#4D1727',
        'custom-orange': '#FF7640',
        'custom-green': '#1DBF73',
        'custom-red': {
          light: '#FFCDD2',
          DEFAULT: '#F44336',
          dark: '#B71C1C',
        },
    },
  },
},
  plugins: [],
}