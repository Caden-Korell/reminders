# Reminders

This is a simple web app for creating and viewing reminders. It has a clean interface, dark mode, and updates in real-time without needing to refresh the page.

## What It Does

- Lets you create reminders with a title and a date/time.
- Automatically fetches and displays all reminders.
- Reminders show up instantly after you add them.
- Includes a dark mode toggle just because it looks better at night.

## How It Works

The app sends and receives data from `reminders/api/`. When you submit a new reminder, it sends a POST request. 
It also fetches all existing reminders and updates the page dynamically using JavaScript.

Everything is built into a single HTML file — styling, scripts, layout — all in one place.

## Credit
Brennen - Built backend and database
Harvey - Built html and styled it to look good
Caden - set up api calls for GET and POST requests
