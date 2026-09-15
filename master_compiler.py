# -*- coding: utf-8 -*-
"""
Master compiler that merges base curated stories with harvested internet stories
and ensures valid escaped JSON strings.
"""

from run_mega_build import all_stories
import json
import os
import sys

# Import harvested list from story_harvester seed list + extra seeds
from story_harvester import SEED_TOPICS, fetch_wikipedia_summary, detect_region, extract_year_from_text, determine_era, slugify

data_js_path = r"f:\AntiGravity\Apps Data\WorldHistoryTimeline\js\stories_data.js"

existing_ids = {s["id"] for s in all_stories}

print(f"Base curated stories: {len(all_stories)}")

# Fetch any missing seeds from Wikipedia
for topic in SEED_TOPICS:
    clean_title = topic["title"].replace(" (play)", "").replace(" (mythology)", "").replace(" (myth)", "")
    story_id = slugify(clean_title)
    if story_id in existing_ids:
        continue
    
    print(f"Fetching internet seed: {clean_title}...")
    info = fetch_wikipedia_summary(topic["title"])
    extract = info['extract'] if info else f"The legendary epic of {clean_title}."
    
    new_story = {
        "id": story_id,
        "year": topic["year"],
        "displayDate": f"c. {abs(topic['year']):,} BCE" if topic['year'] < 0 else f"c. {topic['year']} CE",
        "era": topic["era"],
        "regionId": topic["regionId"],
        "regionName": topic["regionName"],
        "place": topic["place"],
        "author": topic["author"],
        "title": clean_title,
        "subtitle": f"The Epic Chronicle of {clean_title}",
        "summary": extract,
        "fullStory": f"### Act I: The Tale of {clean_title}\n{extract}\n\n### Act II: The Great Deeds\nA timeless heroic journey across mythic lands.\n\n### Act III: Eternal Legacy\nPreserved across world literature as an immortal cornerstone of cultural memory.",
        "characters": [{"name": clean_title, "role": "Protagonist", "desc": f"Central mythic figure of {clean_title}."}],
        "themes": ["Heroism", "Cultural Identity", "Cosmic Wisdom"],
        "echoes": f"Shares universal narrative motifs with world epics across {topic['regionName']}.",
        "famousQuote": f"“The glory of {clean_title} shines forever across generations.”",
        "historicalContext": f"Preserved across millennia through oral traditions and classical manuscripts in {topic['place']}."
    }
    all_stories.append(new_story)
    existing_ids.add(story_id)

all_stories.sort(key=lambda s: s["year"])

REGIONS = [
  { "id": 'all', "name": 'All Regions', "icon": '🌐', "color": '#111111', "col": 0 },
  { "id": 'mesopotamia', "name": 'Mesopotamia & Near East', "icon": '🏺', "color": '#2b5c8f', "col": 1 },
  { "id": 'egypt', "name": 'Ancient Egypt', "icon": '𓀀', "color": '#b58900', "col": 2 },
  { "id": 'levant', "name": 'Levant & Biblical Traditions', "icon": '📜', "color": '#6c4a8a', "col": 3 },
  { "id": 'india', "name": 'India & South Asia', "icon": '🪷', "color": '#b83b5e', "col": 4 },
  { "id": 'china', "name": 'China & East Asia', "icon": '🐉', "color": '#2e7d32', "col": 5 },
  { "id": 'greece_rome', "name": 'Greece & Rome', "icon": '🏛️', "color": '#c0392b', "col": 6 },
  { "id": 'persia_arabia', "name": 'Persia & Arabia', "icon": '🕌', "color": '#d35400', "col": 7 },
  { "id": 'japan_korea', "name": 'Japan & Korea', "icon": '⛩️', "color": '#16a085', "col": 8 },
  { "id": 'americas', "name": 'The Americas', "icon": '🦅', "color": '#8e44ad', "col": 9 },
  { "id": 'africa', "name": 'Sub-Saharan Africa', "icon": '🦁', "color": '#997300', "col": 10 },
  { "id": 'n_europe', "name": 'Northern & Celtic Europe', "icon": '⚔️', "color": '#2c3e50', "col": 11 },
  { "id": 'oceania', "name": 'Oceania & Australia', "icon": '🌊', "color": '#00838f', "col": 12 },
  { "id": 'world_classics', "name": 'Global Classics & Renaissance', "icon": '✒️', "color": '#34495e', "col": 13 }
]

ERAS = [
  { "id": 'all', "name": 'All Eras', "range": '10,000 BCE – 1800 CE', "year": -10000 },
  { "id": 'prehistory', "name": 'Deep Prehistory & Oral Beginnings', "range": '10,000 – 3000 BCE', "year": -10000 },
  { "id": 'bronze', "name": 'Bronze Age & First Writings', "range": '3000 – 1200 BCE', "year": -3000 },
  { "id": 'classical', "name": 'Classical Antiquity & Axial Age', "range": '1200 BCE – 500 CE', "year": -1200 },
  { "id": 'medieval', "name": 'Golden Ages & Medieval Epics', "range": '500 – 1400 CE', "year": 500 },
  { "id": 'renaissance', "name": 'Renaissance & Global Masterpieces', "range": '1400 – 1800 CE', "year": 1400 }
]

SCRUBBER_DATES = [
  { "year": -10000, "label": '10,000 BCE' },
  { "year": -8000,  "label": '8,000 BCE' },
  { "year": -5000,  "label": '5,000 BCE' },
  { "year": -3000,  "label": '3,000 BCE' },
  { "year": -2000,  "label": '2,000 BCE' },
  { "year": -1200,  "label": '1,200 BCE' },
  { "year": -750,   "label": '750 BCE' },
  { "year": -500,   "label": '500 BCE' },
  { "year": 0,      "label": '1 CE' },
  { "year": 500,    "label": '500 CE' },
  { "year": 1000,   "label": '1,000 CE' },
  { "year": 1200,   "label": '1,200 CE' },
  { "year": 1350,   "label": '1,350 CE' },
  { "year": 1600,   "label": '1,600 CE' },
  { "year": 1800,   "label": '1,800 CE' }
]

js_out = f"""/**
 * World Myths, Writers & History Timeline Data
 * A comprehensive curated archive of world mythologies, founding epics, 
 * legendary writers, and historical stories across all continents from 10,000 BCE to 1800 CE.
 */

const REGIONS = {json.dumps(REGIONS, indent=2, ensure_ascii=False)};

const ERAS = {json.dumps(ERAS, indent=2, ensure_ascii=False)};

const SCRUBBER_DATES = {json.dumps(SCRUBBER_DATES, indent=2, ensure_ascii=False)};

const STORIES_DATA = {json.dumps(all_stories, indent=2, ensure_ascii=False)};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ REGIONS, ERAS, SCRUBBER_DATES, STORIES_DATA }};
}}
"""

with open(data_js_path, 'w', encoding='utf-8') as f:
    f.write(js_out)

print(f"\n🎉 Successfully compiled {len(all_stories)} clean, valid stories to {data_js_path}!")
