# Social Media Analytics Infographic

A single, self-contained infographic page that visualizes the **MASTER**,
**BRAND**, and **DEMOGRAPHICS** views of the `analytics_long_v7` spreadsheet.

There is no server, no build step required to view it, and no dependencies to
install — just open **`index.html`** in any browser.

## What it shows

The MASTER ("Raw Data") tab is the single source of truth (long format:
`brand, platform, period, scope, metric, value`). Everything else is computed
from it live in the browser, so the three spreadsheet views are all covered:

- **KPIs** — followers, reach, engagements, engagement rate, likes, video views.
- **Reach & engagement over time** — monthly impressions and engagements.
- **Reach by platform** — share of reach across X, Instagram, LinkedIn, etc.
- **Follower growth** — total followers over time.
- **Brand comparison** (mirrors the **Brand** tab) — every brand × platform with
  reach, likes, comments, shares, reposts, engagement rate, and followers.
  `reach = impressions + views`; `engagement rate = (likes+comments+shares) / reach`.
- **Demographics** (mirrors the **Demographics** tab) — gender, age, and top
  locations as a follower-weighted blend.
- **Raw data** (the **Master** tab) — every underlying fact, searchable.

Filters at the top (brand, platform, date range) update every chart at once.
**Save / Print** exports the current view to PDF from the browser.

## How to share it

Pick whichever is easiest:

1. **Send the file** — email or message `index.html`. It works offline once
   loaded (it only pulls the Chart.js library from a CDN).
2. **Host it for a link** — enable **GitHub Pages** for this repo
   (Settings → Pages → Branch: your branch, folder: `/root`). The page is then
   live at `https://<user>.github.io/<repo>/`.
3. **Open locally** — double-click `index.html`.

## Refreshing the data

1. In Google Sheets, open the spreadsheet and **File → Download → CSV**
   (this exports the first tab, "Raw Data" / MASTER).
2. Replace `data/master.csv` with the new export.
3. Run the build to regenerate the page:

   ```bash
   python3 build.py
   ```

That re-embeds the data into `index.html`. No other tooling needed (standard
library Python only).

## Files

| File             | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| `index.html`     | The shareable infographic (data embedded).           |
| `template.html`  | Page template; `build.py` injects the data into it.  |
| `build.py`       | Reads `data/master.csv` → writes `index.html`.       |
| `data/master.csv`| Snapshot of the MASTER tab (long-format source data).|
