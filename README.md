# YouTube Trending Tracker

This Python script fetches trending YouTube videos in the **Gaming** category (category ID `20`) and stores them in a local SQLite database. It’s useful for analyzing what’s hot on YouTube without needing to hit the API every time.

---

## Features

- Pulls up to **200 trending Gaming videos** from the U.S.
- Collects data like:
  - Video title
  - Channel name
  - View count
  - Publish date
  - Video URL
- Saves everything into a local SQLite database (`ytTrends.db`)

---

## Setup

### 1. Get a YouTube API Key

Go to the [Google Cloud Console](https://console.cloud.google.com/) and enable the **YouTube Data API v3** for your project. Generate an API key.

### 2. Add your API key

You can hardcode the key (not recommended), or use an environment variable for safety.
