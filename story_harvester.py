# -*- coding: utf-8 -*-
"""
Advanced Story Harvester & Autonomous Web Crawler
Cross-platform: Works on Windows, macOS, and Linux (GitHub Actions).
Extracts world mythologies, folklore, founding epics, and classical literature from Wikipedia,
and merges them cleanly into stories_data.js.
"""

import urllib.request
import urllib.parse
import json
import re
import os
import sys
import argparse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

USER_AGENT = 'WorldTimelineHarvester/2.0 (https://github.com/Ranabdullah/AntiGravity; contact: info@antigravity.org)'

# Relative cross-platform path to stories_data.js
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_JS_PATH = os.path.join(SCRIPT_DIR, 'js', 'stories_data.js')

SEED_TOPICS = [
    # Greece & Rome
    {"title": "Heracles", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -800, "place": "Thebes & Mycenae", "author": "Archaic Greek Myth"},
    {"title": "Jason and the Argonauts", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -750, "place": "Iolcos & Colchis", "author": "Apollonius of Rhodes"},
    {"title": "Perseus", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -800, "place": "Argos", "author": "Archaic Greek Myth"},
    {"title": "Theseus and the Minotaur", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -750, "place": "Knossos Labyrinth, Crete", "author": "Plutarch & Classical Lore"},
    {"title": "Cupid and Psyche", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": 160, "place": "Roman Empire", "author": "Apuleius"},
    {"title": "Oedipus Rex", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -429, "place": "Thebes, Greece", "author": "Sophocles"},
    {"title": "Medea (play)", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -431, "place": "Corinth, Greece", "author": "Euripides"},
    {"title": "Prometheus", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -700, "place": "Mount Caucasus", "author": "Hesiod & Aeschylus"},
    {"title": "Pandora's box", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -700, "place": "Ancient Greece", "author": "Hesiod"},
    {"title": "Daedalus", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -750, "place": "Crete", "author": "Ovid"},
    {"title": "Bellerophon", "regionId": "greece_rome", "regionName": "Greece & Rome", "era": "classical", "year": -750, "place": "Corinth & Lycia", "author": "Homer"},

    # Mesopotamia
    {"title": "Adapa", "regionId": "mesopotamia", "regionName": "Mesopotamia & Near East", "era": "bronze", "year": -1400, "place": "Eridu, Sumer", "author": "Mesopotamian Scribes"},
    {"title": "Etana", "regionId": "mesopotamia", "regionName": "Mesopotamia & Near East", "era": "bronze", "year": -2000, "place": "Kish, Sumer", "author": "Sumerian King List"},
    {"title": "Lugalbanda", "regionId": "mesopotamia", "regionName": "Mesopotamia & Near East", "era": "bronze", "year": -2100, "place": "Uruk, Sumer", "author": "Sumerian Epic Cycle"},
    {"title": "Enmerkar and the Lord of Aratta", "regionId": "mesopotamia", "regionName": "Mesopotamia & Near East", "era": "bronze", "year": -2100, "place": "Uruk, Sumer", "author": "Sumerian Scribes"},
    {"title": "Anzû", "regionId": "mesopotamia", "regionName": "Mesopotamia & Near East", "era": "bronze", "year": -1800, "place": "Zagros Mountains, Sumer", "author": "Akkadian Myth"},

    # Egypt
    {"title": "Tale of the Two Brothers", "regionId": "egypt", "regionName": "Ancient Egypt", "era": "bronze", "year": -1200, "place": "Thebes, Egypt", "author": "Papyrus D'Orbiney"},
    {"title": "The Eloquent Peasant", "regionId": "egypt", "regionName": "Ancient Egypt", "era": "bronze", "year": -1850, "place": "Wadi Natrun, Egypt", "author": "Middle Kingdom Scribe"},
    {"title": "Tale of the Doomed Prince", "regionId": "egypt", "regionName": "Ancient Egypt", "era": "bronze", "year": -1300, "place": "Mitanni & Egypt", "author": "Papyrus Harris 500"},
    {"title": "Setne Khamwas and Si-Osire", "regionId": "egypt", "regionName": "Ancient Egypt", "era": "classical", "year": -300, "place": "Memphis, Egypt", "author": "Demotic Egyptian Scribe"},

    # India
    {"title": "Samudra Manthana", "regionId": "india", "regionName": "India & South Asia", "era": "classical", "year": -1000, "place": "Ocean of Milk", "author": "Vishnu Purana"},
    {"title": "Nala and Damayanti", "regionId": "india", "regionName": "India & South Asia", "era": "classical", "year": -400, "place": "Vidarbha, India", "author": "Vyasa"},
    {"title": "Savitri and Satyavan", "regionId": "india", "regionName": "India & South Asia", "era": "classical", "year": -400, "place": "Madra, India", "author": "Vyasa"},
    {"title": "Jataka tales", "regionId": "india", "regionName": "India & South Asia", "era": "classical", "year": -300, "place": "Magadha, India", "author": "Buddhist Tradition"},
    {"title": "Baital Pachisi", "regionId": "india", "regionName": "India & South Asia", "era": "medieval", "year": 1050, "place": "Ujjain, India", "author": "Somadeva (Kathasaritsagara)"},
    {"title": "Hitopadesha", "regionId": "india", "regionName": "India & South Asia", "era": "medieval", "year": 1100, "place": "Pataliputra, India", "author": "Narayana Pandit"},

    # China
    {"title": "Yu the Great", "regionId": "china", "regionName": "China & East Asia", "era": "bronze", "year": -2070, "place": "Yellow River, China", "author": "Shanhaijing"},
    {"title": "Legend of the White Snake", "regionId": "china", "regionName": "China & East Asia", "era": "medieval", "year": 1100, "place": "Hangzhou, China", "author": "Song Dynasty Lore"},
    {"title": "Butterfly Lovers", "regionId": "china", "regionName": "China & East Asia", "era": "classical", "year": 350, "place": "Zhejiang, China", "author": "Jin Dynasty Lore"},
    {"title": "Water Margin", "regionId": "china", "regionName": "China & East Asia", "era": "medieval", "year": 1368, "place": "Mount Liang, China", "author": "Shi Nai'an"},
    {"title": "Dream of the Red Chamber", "regionId": "china", "regionName": "China & East Asia", "era": "renaissance", "year": 1791, "place": "Beijing, Qing Dynasty", "author": "Cao Xueqin"},
    {"title": "Investiture of the Gods", "regionId": "china", "regionName": "China & East Asia", "era": "renaissance", "year": 1570, "place": "Shang & Zhou China", "author": "Xu Zhonglin"},

    # Japan & Korea
    {"title": "Urashima Tarō", "regionId": "japan_korea", "regionName": "Japan & Korea", "era": "medieval", "year": 720, "place": "Ryūgū-jō, Japan", "author": "Nihon Shoki"},
    {"title": "Momotarō", "regionId": "japan_korea", "regionName": "Japan & Korea", "era": "medieval", "year": 1300, "place": "Onigashima, Japan", "author": "Japanese Lore"},
    {"title": "The Tale of the Heike", "regionId": "japan_korea", "regionName": "Japan & Korea", "era": "medieval", "year": 1240, "place": "Kyoto, Japan", "author": "Biwa Hōshi Bards"},
    {"title": "Chunhyangjeon", "regionId": "japan_korea", "regionName": "Japan & Korea", "era": "renaissance", "year": 1650, "place": "Namwon, Korea", "author": "Pansori Tradition"},
    {"title": "Hong Gildong jeon", "regionId": "japan_korea", "regionName": "Japan & Korea", "era": "renaissance", "year": 1612, "place": "Joseon Korea", "author": "Heo Gyun"},
    {"title": "Tale of the Bamboo Cutter", "regionId": "japan_korea", "regionName": "Japan & Korea", "era": "medieval", "year": 900, "place": "Mount Fuji, Japan", "author": "Heian Anonymous"},

    # Americas
    {"title": "White Buffalo Calf Woman", "regionId": "americas", "regionName": "The Americas", "era": "medieval", "year": 1100, "place": "Great Plains (Lakota)", "author": "Lakota Oral Tradition"},
    {"title": "Sedna (mythology)", "regionId": "americas", "regionName": "The Americas", "era": "prehistory", "year": -3000, "place": "Arctic Ocean", "author": "Inuit Tradition"},
    {"title": "Nanabozho", "regionId": "americas", "regionName": "The Americas", "era": "classical", "year": 100, "place": "Great Lakes (Ojibwe)", "author": "Anishinaabe Elders"},
    {"title": "Manco Cápac", "regionId": "americas", "regionName": "The Americas", "era": "medieval", "year": 1200, "place": "Lake Titicaca & Cuzco", "author": "Inca Royal Lore"},
    {"title": "Coyote (mythology)", "regionId": "americas", "regionName": "The Americas", "era": "prehistory", "year": -5000, "place": "North America", "author": "Indigenous Oral Custodians"},
    {"title": "Twin Holy Boys", "regionId": "americas", "regionName": "The Americas", "era": "prehistory", "year": -2000, "place": "Southwestern US (Navajo)", "author": "Diné Bahaneʼ"},

    # Africa
    {"title": "Mwindo epic", "regionId": "africa", "regionName": "Sub-Saharan Africa", "era": "medieval", "year": 1100, "place": "Congo Basin", "author": "Nyanga Bards"},
    {"title": "Epic of Sundiata", "regionId": "africa", "regionName": "Sub-Saharan Africa", "era": "medieval", "year": 1235, "place": "Mali Empire", "author": "Djeli Mamadou Kouyaté"},
    {"title": "Kebra Nagast", "regionId": "africa", "regionName": "Sub-Saharan Africa", "era": "medieval", "year": 1320, "place": "Aksum & Lalibela, Ethiopia", "author": "Ethiopian Orthodox Scribes"},
    {"title": "Dausi", "regionId": "africa", "regionName": "Sub-Saharan Africa", "era": "medieval", "year": 1150, "place": "Ghana Empire", "author": "Soninke Griots"},

    # Northern & Celtic Europe
    {"title": "Children of Lir", "regionId": "n_europe", "regionName": "Northern & Celtic Europe", "era": "medieval", "year": 800, "place": "Sea of Moyle, Ireland", "author": "Irish Monastic Lore"},
    {"title": "Mabinogion", "regionId": "n_europe", "regionName": "Northern & Celtic Europe", "era": "medieval", "year": 1100, "place": "Wales", "author": "Welsh Bards"},
    {"title": "Nibelungenlied", "regionId": "n_europe", "regionName": "Northern & Celtic Europe", "era": "medieval", "year": 1200, "place": "Worms, Germany", "author": "Middle High German Master"},
    {"title": "Kalevala", "regionId": "n_europe", "regionName": "Northern & Celtic Europe", "era": "medieval", "year": 1000, "place": "Karelia & Finland", "author": "Finnish Runic Bards"},
    {"title": "Völsunga saga", "regionId": "n_europe", "regionName": "Northern & Celtic Europe", "era": "medieval", "year": 1250, "place": "Scandinavia & Iceland", "author": "Icelandic Scribe"},
    {"title": "Cú Chulainn", "regionId": "n_europe", "regionName": "Northern & Celtic Europe", "era": "classical", "year": 100, "place": "Ulster, Ireland", "author": "Ulster Cycle"},

    # World Classics
    {"title": "Macbeth", "regionId": "world_classics", "regionName": "Global Classics & Renaissance", "era": "renaissance", "year": 1606, "place": "Scotland", "author": "William Shakespeare"},
    {"title": "Doctor Faustus (play)", "regionId": "world_classics", "regionName": "Global Classics & Renaissance", "era": "renaissance", "year": 1592, "place": "Wittenberg", "author": "Christopher Marlowe"},
    {"title": "Gargantua and Pantagruel", "regionId": "world_classics", "regionName": "Global Classics & Renaissance", "era": "renaissance", "year": 1532, "place": "France", "author": "François Rabelais"},
    {"title": "Orlando Furioso", "regionId": "world_classics", "regionName": "Global Classics & Renaissance", "era": "renaissance", "year": 1532, "place": "Ferrara, Italy", "author": "Ludovico Ariosto"},
    {"title": "The Decameron", "regionId": "world_classics", "regionName": "Global Classics & Renaissance", "era": "medieval", "year": 1353, "place": "Florence, Italy", "author": "Giovanni Boccaccio"}
]

REGION_KEYWORDS = {
    'mesopotamia': ['mesopotamia', 'sumer', 'babylon', 'akkad', 'assyria', 'uruk', 'cuneiform', 'tigris', 'euphrates'],
    'egypt': ['egypt', 'pharaoh', 'nile', 'pyramid', 'thebes', 'osiris', 'isis', 'horus', 'hieroglyph'],
    'levant': ['israel', 'canaan', 'judah', 'jerusalem', 'hebrew', 'bible', 'torah', 'exodus', 'arabian nights', 'baghdad'],
    'india': ['india', 'vedic', 'sanskrit', 'hindu', 'mahabharata', 'ramayana', 'buddha', 'ganga', 'purana', 'kalidasa'],
    'china': ['china', 'chinese', 'han dynasty', 'tang dynasty', 'ming dynasty', 'daoism', 'confucius', 'yellow river', 'yangtze'],
    'greece_rome': ['greece', 'greek', 'athens', 'sparta', 'rome', 'roman', 'homer', 'virgil', 'zeus', 'olympus', 'latin'],
    'persia_arabia': ['persia', 'persian', 'iran', 'zoroastrian', 'shahnameh', 'ferdowsi', 'rumi', 'nizami', 'shiraz'],
    'japan_korea': ['japan', 'japanese', 'shinto', 'kyoto', 'heian', 'korea', 'korean', 'samguk', 'joseon', 'gojoseon'],
    'americas': ['maya', 'aztec', 'inca', 'mesoamerica', 'andes', 'lakota', 'cherokee', 'haida', 'ojibwe', 'navajo', 'popol vuh'],
    'africa': ['mali', 'yoruba', 'ghana empire', 'songhai', 'ethiopia', 'aksum', 'zulu', 'bantu', 'ashanti', 'anansi', 'griot'],
    'n_europe': ['norse', 'viking', 'odin', 'thor', 'celtic', 'ireland', 'irish', 'welsh', 'arthur', 'beowulf', 'finland', 'kalevala'],
    'oceania': ['aboriginal', 'dreamtime', 'australia', 'polynesia', 'maori', 'new zealand', 'hawaii', 'maui', 'pele'],
    'world_classics': ['renaissance', 'shakespeare', 'dante', 'cervantes', 'milton', 'goethe', 'chaucer', 'boccaccio']
}

def detect_region(text):
    text_lower = text.lower()
    scores = {region: 0 for region in REGION_KEYWORDS}
    for region, keywords in REGION_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                scores[region] += 1
    best_region = max(scores, key=scores.get)
    if scores[best_region] > 0:
        return best_region
    return 'world_classics'

def extract_year_from_text(text):
    match_bce = re.search(r'(\d+)\s*(?:BCE|BC)', text, re.IGNORECASE)
    if match_bce:
        return -int(match_bce.group(1))
    match_cent_bce = re.search(r'(\d+)(?:st|nd|rd|th)\s*century\s*(?:BCE|BC)', text, re.IGNORECASE)
    if match_cent_bce:
        return -(int(match_cent_bce.group(1)) * 100 - 50)
    match_cent_ce = re.search(r'(\d+)(?:st|nd|rd|th)\s*century\s*(?:CE|AD)?', text, re.IGNORECASE)
    if match_cent_ce:
        return int(match_cent_ce.group(1)) * 100 - 50
    match_yr = re.search(r'\b(1[0-8]\d{2}|[5-9]\d{2})\b', text)
    if match_yr:
        return int(match_yr.group(1))
    return 500

def fetch_wikipedia_summary(title):
    encoded_title = urllib.parse.quote(title.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_title}"
    headers = {'User-Agent': USER_AGENT}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return {
                    'title': data.get('title', title),
                    'extract': data.get('extract', ''),
                    'description': data.get('description', '')
                }
    except Exception:
        pass
    return None

def search_wikipedia(query, limit=10):
    encoded_query = urllib.parse.quote(query)
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={encoded_query}&limit={limit}&namespace=0&format=json"
    headers = {'User-Agent': USER_AGENT}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                if len(data) >= 2:
                    return data[1]
    except Exception as e:
        print(f"Error searching Wikipedia: {e}")
    return []

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def determine_era(year):
    if year < -3000:
        return 'prehistory'
    elif year < -1200:
        return 'bronze'
    elif year < 500:
        return 'classical'
    elif year < 1400:
        return 'medieval'
    else:
        return 'renaissance'

DEFAULT_REGIONS = [
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

DEFAULT_ERAS = [
  { "id": 'all', "name": 'All Eras', "range": '10,000 BCE – 1800 CE', "year": -10000 },
  { "id": 'prehistory', "name": 'Deep Prehistory & Oral Beginnings', "range": '10,000 – 3000 BCE', "year": -10000 },
  { "id": 'bronze', "name": 'Bronze Age & First Writings', "range": '3000 – 1200 BCE', "year": -3000 },
  { "id": 'classical', "name": 'Classical Antiquity & Axial Age', "range": '1200 BCE – 500 CE', "year": -1200 },
  { "id": 'medieval', "name": 'Golden Ages & Medieval Epics', "range": '500 – 1400 CE', "year": 500 },
  { "id": 'renaissance', "name": 'Renaissance & Global Masterpieces', "range": '1400 – 1800 CE', "year": 1400 }
]

DEFAULT_SCRUBBER_DATES = [
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

def load_existing_dataset():
    if not os.path.exists(DATA_JS_PATH):
        return DEFAULT_REGIONS, DEFAULT_ERAS, DEFAULT_SCRUBBER_DATES, []
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const STORIES_DATA = (\[.*?\]);', content, re.DOTALL)
    stories = []
    if match:
        try:
            stories = json.loads(match.group(1))
        except Exception as e:
            print(f"Error parsing STORIES_DATA: {e}")
    return DEFAULT_REGIONS, DEFAULT_ERAS, DEFAULT_SCRUBBER_DATES, stories

def save_dataset(regions, eras, scrubber_dates, stories):
    stories.sort(key=lambda s: s["year"])

    js_out = f"""/**
 * World Myths, Writers & History Timeline Data
 * A comprehensive curated archive of world mythologies, founding epics, 
 * legendary writers, and historical stories across all continents from 10,000 BCE to 1800 CE.
 */

const REGIONS = {json.dumps(regions, indent=2, ensure_ascii=False)};

const ERAS = {json.dumps(eras, indent=2, ensure_ascii=False)};

const SCRUBBER_DATES = {json.dumps(scrubber_dates, indent=2, ensure_ascii=False)};

const STORIES_DATA = {json.dumps(stories, indent=2, ensure_ascii=False)};

if (typeof module !== 'undefined' && module.exports) {{
  module.exports = {{ REGIONS, ERAS, SCRUBBER_DATES, STORIES_DATA }};
}}
"""
    with open(DATA_JS_PATH, 'w', encoding='utf-8') as f:
        f.write(js_out)

def harvest_topics(topic_titles):
    regions, eras, scrubber_dates, stories = load_existing_dataset()
    existing_ids = {s["id"] for s in stories}
    added_count = 0

    for title in topic_titles:
        clean_title = title.replace(" (play)", "").replace(" (mythology)", "").replace(" (myth)", "")
        story_id = slugify(clean_title)
        if story_id in existing_ids:
            continue

        print(f"  → Mining: {clean_title}...")
        info = fetch_wikipedia_summary(title)
        if not info or not info['extract']:
            continue

        extract = info['extract']
        description = info['description']
        full_text = f"{clean_title} {description} {extract}"

        region_id = detect_region(full_text)
        year = extract_year_from_text(full_text)
        era = determine_era(year)
        
        region_names = {
            'mesopotamia': 'Mesopotamia & Near East',
            'egypt': 'Ancient Egypt',
            'levant': 'Levant & Biblical Traditions',
            'india': 'India & South Asia',
            'china': 'China & East Asia',
            'greece_rome': 'Greece & Rome',
            'persia_arabia': 'Persia & Arabia',
            'japan_korea': 'Japan & Korea',
            'americas': 'The Americas',
            'africa': 'Sub-Saharan Africa',
            'n_europe': 'Northern & Celtic Europe',
            'oceania': 'Oceania & Australia',
            'world_classics': 'Global Classics & Renaissance'
        }

        display_date = f"{abs(year):,} BCE" if year < 0 else f"{year} CE"

        new_story = {
            "id": story_id,
            "year": year,
            "displayDate": f"c. {display_date}",
            "era": era,
            "regionId": region_id,
            "regionName": region_names.get(region_id, 'World Heritage'),
            "place": description or f"{region_names.get(region_id, 'World')} Region",
            "author": f"Classical {region_names.get(region_id, '')} Tradition",
            "title": clean_title,
            "subtitle": description or f"The Epic of {clean_title}",
            "summary": extract,
            "fullStory": f"### Act I: The Awakening of {clean_title}\n{extract}\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
            "characters": [
                {"name": clean_title, "role": "Protagonist", "desc": description or "Central mythic figure."}
            ],
            "themes": ["Mythology", "Cultural Heritage", "Timeless Wisdom"],
            "echoes": f"Shares foundational archetypes with epic literature across {region_names.get(region_id, 'the world')}.",
            "famousQuote": f"“The memory of {clean_title} endures throughout the ages.”",
            "historicalContext": f"Preserved across millennia through oral traditions and classical manuscripts."
        }

        stories.append(new_story)
        existing_ids.add(story_id)
        added_count += 1

    save_dataset(regions, eras, scrubber_dates, stories)
    print(f"\n✨ Harvest Complete! Added {added_count} new stories. Total collection: {len(stories)} stories.")

def main():
    parser = argparse.ArgumentParser(description="Autonomous World Stories Harvester")
    parser.add_argument("--query", "-q", help="Search and harvest stories by keyword (e.g. 'Babylonian myth')")
    parser.add_argument("--titles", "-t", nargs="+", help="Direct list of Wikipedia titles to harvest")
    args = parser.parse_args()

    if args.query:
        print(f"🔍 Searching Wikipedia for '{args.query}'...")
        results = search_wikipedia(args.query, limit=15)
        print(f"Found {len(results)} potential topics: {results}")
        harvest_topics(results)
    elif args.titles:
        harvest_topics(args.titles)
    else:
        # Rotating auto-expansion list
        seed_titles = [t["title"] for t in SEED_TOPICS]
        harvest_topics(seed_titles)

if __name__ == '__main__':
    main()
