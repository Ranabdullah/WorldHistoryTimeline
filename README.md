# World Myths, Writers & History — Chronological Multi-Track Timeline

An interactive, high-contrast, top-to-bottom chronological timeline connecting global mythologies, founding epics, and legendary writers from **10,000 BCE to 1800 CE**.

## ✨ Key Highlights

- **1920x1080 High-Density & Mobile Responsive**:
  - High-contrast editorial aesthetic (**Solid Black History Spine on Pure White Background**).
  - Parallel regional columns with continuous **vertical dotted lines from top to bottom**.
  - Optimized for 1080p full-screen viewing and seamless mobile touch navigation.
- **Independent Box Zooming & Density Controls**:
  - **Box Size Slider (`0.65x` to `1.5x`)**: Zoom in and out of the cards without altering the timeline scale.
  - **3 Density Modes**: `Compact` (high-density badges), `Regular` (editorial cards), and `Detailed` (expanded summaries).
- **Google Photos Style Date Scrubber**:
  - Fixed on the right edge of the screen.
  - 1-click jump to any epoch (`10,000 BCE`, `5,000 BCE`, `3,000 BCE`, `1,200 BCE`, `1 CE`, `1,000 CE`, `1,400 CE`, `1,800 CE`).
  - Real-time year tooltip tracking your scroll position.
- **Middle-Mouse & Drag Panning**:
  - Hold the middle mouse button (or drag empty space) to pan freely in any direction.
- **In-Window Expandable Story Reader**:
  - Multi-act chapter breakdown, character dossiers, comparative mythology echoes, ancient quotes, and **AI Voice Narration (Text-to-Speech)**.

---

## 🌐 Automated Web Story Harvester (`story_harvester.py`)

The application includes an automated web crawler and miner program that queries open web APIs (Wikipedia / Wikimedia REST API) for ancient authors, mythologies, folklore, and epics across every continent, formats them, and merges them into `stories_data.js`.

### How to Run the Harvester:

```bash
cd "Apps Data/WorldHistoryTimeline"
python story_harvester.py
```

- Fetches summaries, historical dates, cultural regions, and characters.
- Deduplicates against existing entries.
- Automatically updates `js/stories_data.js` with new stories!

---

## 🚀 Running Locally

```bash
# Using Python:
python -m http.server 8080 -d "Apps Data/WorldHistoryTimeline"

# Or using Node.js:
npx serve "Apps Data/WorldHistoryTimeline"
```
Navigate to `http://localhost:8080`.

---

## 🐙 Pushing to GitHub

```bash
git add "Apps Data/WorldHistoryTimeline"
git commit -m "Update timeline with 1080p compact layout and automated story harvester"
git push origin main
```

---

## ⚡ Cloudflare Pages / Workers Deployment

- **Automated Git Deploy**: In Cloudflare Dashboard, connect `Ranabdullah/AntiGravity` and set **Build output directory** to `Apps Data/WorldHistoryTimeline`.
- **Wrangler Deploy**:
  ```bash
  npx wrangler deploy
  ```
