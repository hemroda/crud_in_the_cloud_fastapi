/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html', // Adjust to your HTML template folder
        './**/*.html',          // If you have standalone HTML files
        './static/src/**/*.css', // If you use Tailwind in raw CSS files
        './static/js/*.js',            // For JavaScript files
        './**/*.py',            // If Tailwind classes are in Python templates
      ],
  theme: {
    extend: {},
  },
  plugins: [],
}

