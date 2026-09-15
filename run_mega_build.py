# -*- coding: utf-8 -*-
"""
Appends more legendary world tales to build_mega_dataset.py and runs it.
"""

from build_mega_dataset import stories, make_story
import json, os

extra_stories = [
  make_story(
    "aesop-fables", -600, "c. 600 BCE", "classical", "greece_rome", "Greece & Rome",
    "Thrace & Delphi, Greece", "Aesop (Freed Storyteller & Fabulist)",
    "Aesop's Fables: The Tortoise and the Hare, The Boy Who Cried Wolf", "Animal Wisdom and Moral Truths That Outlasted Empires",
    "Aesop, an enslaved Greek fabulist who won freedom through wit, crafts timeless moral tales showing that steady perseverance overcomes arrogant speed and honesty protects communities.",
    "### Act I: The Tortoise and the Hare\nThe swift Hare mocked the slow Tortoise. Challenged to a race, the overconfident Hare fell asleep under a tree while the steady Tortoise crossed the finish line.\n\n### Act II: The Boy Who Cried Wolf\nA bored shepherd boy repeatedly tricked villagers by shouting 'Wolf!' When a real wolf emerged from the forest, no one believed his cries.",
    [{"name": "The Tortoise & Hare", "role": "Fable Archetypes", "desc": "Proof that slow and steady wins the race."}, {"name": "The Shepherd Boy", "role": "Tragic Liar", "desc": "Learned the cost of broken trust."}],
    ["Moral Integrity", "Perseverance over Hubris", "Practical Wisdom"],
    "Parallels Indian Panchatantra and West African Anansi fables.",
    "“Slow and steady wins the race; no one believes a liar even when he speaks the truth.” — Aesop",
    "Preserved orally and collected by Demetrius of Phalerum around 300 BCE."
  ),
  make_story(
    "princess-kaguya", 900, "c. 900 CE", "medieval", "japan_korea", "Japan & Korea",
    "Bamboo Grove & Mount Fuji, Japan", "Anonymous Heian Court Author",
    "The Tale of the Bamboo Cutter (Princess Kaguya)", "The Shining Maiden in the Stalk, Five Impossible Tasks, and the Smoke of Mount Fuji",
    "An elderly bamboo cutter discovers a glowing miniature maiden inside a stalk of bamboo. Growing into radiant Princess Kaguya, she sets five impossible quests for royal suitors before returning to the Moon.",
    "### Act I: The Shining Stalk\nAn old bamboo cutter slices open a glowing stalk, finding a three-inch baby who grows into the luminous Princess Kaguya.\n\n### Act II: The Five Impossible Quests\nFive noble suitors seek her hand; she asks for the stone bowl of the Buddha, the jeweled branch of Horai, the fire-rat robe, the dragon's neck jewel, and the swallow's cowrie shell. All five fail.\n\n### Act III: The Robe of Feathers\nThe celestial host of the Moon descends on cloud-chariots. Donning a feather robe that erases mortal memories, Kaguya ascends to the heavens, leaving an elixir of immortality that the Emperor burns on the peak of Mount Fuji.",
    [{"name": "Princess Kaguya", "role": "Celestial Moon Maiden", "desc": "Exiled to earth before returning to the Moon."}, {"name": "The Bamboo Cutter (Taketori no Okina)", "role": "Loving Foster Father", "desc": "Raised Kaguya with tenderness."}],
    ["Celestial Purity vs Earthly Sorrow", "Transience of Beauty"],
    "Oldest surviving prose narrative (monogatari) in Japanese literature.",
    "“Mount Fuji's smoke rises forever into the sky, carrying the eternal longing of the Emperor for the Moon Maiden.”",
    "Often described as early proto-science-fiction in world literature."
  ),
  make_story(
    "yoruba-obatala-shango", 1100, "c. 1100 CE", "medieval", "africa", "Sub-Saharan Africa",
    "Ile-Ife & Oyo Kingdom (Nigeria)", "Yoruba Babalawos (Ifá Diviners)",
    "The Yoruba Orishas: Obatala Molds Mankind and Shango's Thunder", "The Sacred Chain from Heaven, the Palm Wine, and the Double-Axe",
    "Supreme God Olodumare sends Obatala down a gold chain to mold the human body from red clay. Later, King Shango rules Oyo with living lightning and thunderstones.",
    "### Act I: The Gold Chain\nObatala descended from heaven on a long gold chain carrying a snail shell of earth, a five-toed hen, and a chameleon to solidify the land at Ile-Ife.\n\n### Act II: Molding Humanity\nObatala sculpted human bodies from clay, but drank palm wine and molded deformed bodies; upon sobering, he vowed to become the eternal protector of disabled persons.\n\n### Act III: Shango the Thunder King\nKing Shango commanded thunder and double-headed axes (Oshe), ruling Oyo with fiery justice.",
    [{"name": "Obatala", "role": "Creator Orisha", "desc": "Molds human forms and protects the disabled."}, {"name": "Shango", "role": "God of Thunder & Lightning", "desc": "Historic third Alaafin (king) of Oyo."}],
    ["Protection of the Vulnerable", "Divine Crafting", "Justice and Storms"],
    "Obatala molding humans parallels Prometheus and Khnum; Shango mirrors Thor and Indra.",
    "“Obatala is the owner of the white cloth and the sculptor of the human face.” — Ifá Corpus",
    "Ile-Ife terracotta and bronze sculptures date from the 11th–14th centuries CE."
  ),
  make_story(
    "chaucer-canterbury", 1387, "c. 1387 – 1400 CE", "medieval", "world_classics", "Global Masterpieces & Renaissance",
    "The Tabard Inn (Southwark) to Canterbury Cathedral", "Geoffrey Chaucer (Father of English Poetry)",
    "The Canterbury Tales: The Knight, the Miller, and the Wife of Bath", "The Pilgrimage to Saint Thomas Becket, Bawdy Humor, and Female Sovereignty",
    "A diverse company of twenty-nine pilgrims journey on horseback to Canterbury Cathedral, competing in a storytelling contest at the Tabard Inn, capturing the vibrant panorama of medieval English life.",
    "### Act I: April Showers and the Tabard Inn\nWhen sweet April rains awaken spring blossoms, pilgrims gather in Southwark, agreeing to tell two tales each on the road.\n\n### Act II: The Chivalric Knight & Bawdy Miller\nThe Knight sings of courtly love and honor, immediately interrupted by the drunken Miller's bawdy comedy of an old carpenter and young clerks.\n\n### Act III: The Wife of Bath's Tale\nThe five-times married Dame Alice argues that what women desire most above all things is sovereignty over their own lives and husbands.",
    [{"name": "Geoffrey Chaucer", "role": "Pilgrim-Narrator", "desc": "Chronicled medieval English society."}, {"name": "The Wife of Bath (Dame Alice)", "role": "Feminist Icon", "desc": "Defended female autonomy and joy."}],
    ["Social Satire", "Female Sovereignty", "Diversity of Human Experience"],
    "Framed storytelling mirrors Boccaccio's Decameron and 1,001 Nights.",
    "“What women desire most is to have sovereignty over their husbands as well as their love.” — Wife of Bath",
    "Established Middle English as a high literary language."
  ),
  make_story(
    "boccaccio-decameron", 1353, "1348 – 1353 CE", "medieval", "world_classics", "Global Masterpieces & Renaissance",
    "Florence & Fiesole Hills, Italy", "Giovanni Boccaccio",
    "The Decameron: One Hundred Tales Escaping the Black Death", "Seven Young Women, Three Men, and Ten Days of Wit and Resilience",
    "Fleeing the terrifying Black Death plague in Florence, ten young aristocrats retreat to a country villa, spending ten days telling one hundred witty, romantic, and satirical stories celebrating human ingenuity.",
    "### Act I: The Plague in Florence\nIn 1348, the horrific Black Death wiped out half of Florence, destroying all social bonds and laws.\n\n### Act II: The Villa Sanctuary\nSeven noblewomen and three men retreat to a countryside garden, electing a king/queen each day to rule over story sessions.\n\n### Act III: The 100 Tales of Human Fortune\nStories of clever merchants outwitting corrupt friars, tragic lovers, and resourceful wives celebrate the triumph of human intellect over blind fortune.",
    [{"name": "Pampinea", "role": "Queen of Day 1", "desc": "Organized the refuge in the hills."}],
    ["Triumph of Wit over Death", "Humanism and Joy", "Framed Narrative"],
    "Direct source for Shakespeare's All's Well That Ends Well and Chaucer.",
    "“Human compassion is a noble virtue in all who have known suffering.” — Boccaccio",
    "The foundational masterpiece of Italian vernacular prose."
  ),
  make_story(
    "goethe-faust", 1808, "1772 – 1808 CE", "renaissance", "world_classics", "Global Masterpieces & Renaissance",
    "Wittenberg & Harz Mountains, Germany", "Johann Wolfgang von Goethe",
    "Faust: The Pact with Mephistopheles and the Eternal Quest", "The Scholar's Disillusionment, the Blood Signature, and Gretchen's Grace",
    "Aging polymath Dr. Heinrich Faust, disillusioned by bookish learning, signs a blood contract with the devil Mephistopheles: if Faust ever says to any fleeting moment, 'Stay, thou art so fair!', his soul belongs to Hell.",
    "### Act I: The Scholar's Study\nFaust has mastered philosophy, law, and medicine, yet finds no living meaning.\n\n### Act II: The Blood Pact\nMephistopheles appears as a black poodle, offering all worldly pleasures. Faust signs in blood, betting that his striving soul will never be satisfied with mere idle comfort.\n\n### Act III: Gretchen and Redemption\nFaust seduces innocent Gretchen, causing tragic ruin. In Part II, Faust devotes his final years to draining coastal marshes to build a free society for millions, saved by divine grace through the Eternal Feminine.",
    [{"name": "Dr. Heinrich Faust", "role": "The Striving Human", "desc": "Archetype of boundless human ambition."}, {"name": "Mephistopheles", "role": "The Spirit of Denial", "desc": "The devil who constantly wills evil yet works the good."}],
    ["The Faustian Bargain", "Boundless Human Striving", "Grace and Redemption"],
    "Transforms the medieval demonic legend into a cosmic meditation on human progress.",
    "“Whoever strives with all his power, him can we redeem!” — Goethe, Faust Part II",
    "Goethe spent sixty years writing Faust, the crowning jewel of German literature."
  )
]

all_stories = stories + extra_stories
all_stories.sort(key=lambda s: s["year"])

print(f"Total mega dataset stories count: {len(all_stories)}")

# Overwrite js/stories_data.js
js_content = """/**
 * World Myths, Writers & History Timeline Data
 * A comprehensive curated archive of world mythologies, founding epics, 
 * legendary writers, and historical stories across all continents from 10,000 BCE to 1800 CE.
 */

const REGIONS = [
  { id: 'all', name: 'All Regions', icon: '🌐', color: '#111111', col: 0 },
  { id: 'mesopotamia', name: 'Mesopotamia & Near East', icon: '🏺', color: '#2b5c8f', col: 1 },
  { id: 'egypt', name: 'Ancient Egypt', icon: '𓀀', color: '#b58900', col: 2 },
  { id: 'levant', name: 'Levant & Biblical Traditions', icon: '📜', color: '#6c4a8a', col: 3 },
  { id: 'india', name: 'India & South Asia', icon: '🪷', color: '#b83b5e', col: 4 },
  { id: 'china', name: 'China & East Asia', icon: '🐉', color: '#2e7d32', col: 5 },
  { id: 'greece_rome', name: 'Greece & Rome', icon: '🏛️', color: '#c0392b', col: 6 },
  { id: 'persia_arabia', name: 'Persia & Arabia', icon: '🕌', color: '#d35400', col: 7 },
  { id: 'japan_korea', name: 'Japan & Korea', icon: '⛩️', color: '#16a085', col: 8 },
  { id: 'americas', name: 'The Americas', icon: '🦅', color: '#8e44ad', col: 9 },
  { id: 'africa', name: 'Sub-Saharan Africa', icon: '🦁', color: '#997300', col: 10 },
  { id: 'n_europe', name: 'Northern & Celtic Europe', icon: '⚔️', color: '#2c3e50', col: 11 },
  { id: 'oceania', name: 'Oceania & Australia', icon: '🌊', color: '#00838f', col: 12 },
  { id: 'world_classics', name: 'Global Classics & Renaissance', icon: '✒️', color: '#34495e', col: 13 }
];

const ERAS = [
  { id: 'all', name: 'All Eras', range: '10,000 BCE – 1800 CE', year: -10000 },
  { id: 'prehistory', name: 'Deep Prehistory & Oral Beginnings', range: '10,000 – 3000 BCE', year: -10000 },
  { id: 'bronze', name: 'Bronze Age & First Writings', range: '3000 – 1200 BCE', year: -3000 },
  { id: 'classical', name: 'Classical Antiquity & Axial Age', range: '1200 BCE – 500 CE', year: -1200 },
  { id: 'medieval', name: 'Golden Ages & Medieval Epics', range: '500 – 1400 CE', year: 500 },
  { id: 'renaissance', name: 'Renaissance & Global Masterpieces', range: '1400 – 1800 CE', year: 1400 }
];

const SCRUBBER_DATES = [
  { year: -10000, label: '10,000 BCE' },
  { year: -8000,  label: '8,000 BCE' },
  { year: -5000,  label: '5,000 BCE' },
  { year: -3000,  label: '3,000 BCE' },
  { year: -2000,  label: '2,000 BCE' },
  { year: -1200,  label: '1,200 BCE' },
  { year: -750,   label: '750 BCE' },
  { year: -500,   label: '500 BCE' },
  { year: 0,      label: '1 CE' },
  { year: 500,    label: '500 CE' },
  { year: 1000,   label: '1,000 CE' },
  { year: 1200,   label: '1,200 CE' },
  { year: 1350,   label: '1,350 CE' },
  { year: 1600,   label: '1,600 CE' },
  { year: 1800,   label: '1,800 CE' }
];

const STORIES_DATA = """ + json.dumps(all_stories, indent=2, ensure_ascii=False) + """;

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { REGIONS, ERAS, SCRUBBER_DATES, STORIES_DATA };
}
"""

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js', 'stories_data.js')
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("stories_data.js successfully regenerated with mega dataset!")
