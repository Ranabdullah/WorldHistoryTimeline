/**
 * World Myths, Writers & History Timeline Data
 * A comprehensive curated archive of world mythologies, founding epics, 
 * legendary writers, and historical stories across all continents from 10,000 BCE to 1800 CE.
 */

const REGIONS = [
  {
    "id": "all",
    "name": "All Regions",
    "icon": "🌐",
    "color": "#111111",
    "col": 0
  },
  {
    "id": "mesopotamia",
    "name": "Mesopotamia & Near East",
    "icon": "🏺",
    "color": "#2b5c8f",
    "col": 1
  },
  {
    "id": "egypt",
    "name": "Ancient Egypt",
    "icon": "𓀀",
    "color": "#b58900",
    "col": 2
  },
  {
    "id": "levant",
    "name": "Levant & Biblical Traditions",
    "icon": "📜",
    "color": "#6c4a8a",
    "col": 3
  },
  {
    "id": "india",
    "name": "India & South Asia",
    "icon": "🪷",
    "color": "#b83b5e",
    "col": 4
  },
  {
    "id": "china",
    "name": "China & East Asia",
    "icon": "🐉",
    "color": "#2e7d32",
    "col": 5
  },
  {
    "id": "greece_rome",
    "name": "Greece & Rome",
    "icon": "🏛️",
    "color": "#c0392b",
    "col": 6
  },
  {
    "id": "persia_arabia",
    "name": "Persia & Arabia",
    "icon": "🕌",
    "color": "#d35400",
    "col": 7
  },
  {
    "id": "japan_korea",
    "name": "Japan & Korea",
    "icon": "⛩️",
    "color": "#16a085",
    "col": 8
  },
  {
    "id": "americas",
    "name": "The Americas",
    "icon": "🦅",
    "color": "#8e44ad",
    "col": 9
  },
  {
    "id": "africa",
    "name": "Sub-Saharan Africa",
    "icon": "🦁",
    "color": "#997300",
    "col": 10
  },
  {
    "id": "n_europe",
    "name": "Northern & Celtic Europe",
    "icon": "⚔️",
    "color": "#2c3e50",
    "col": 11
  },
  {
    "id": "oceania",
    "name": "Oceania & Australia",
    "icon": "🌊",
    "color": "#00838f",
    "col": 12
  },
  {
    "id": "world_classics",
    "name": "Global Classics & Renaissance",
    "icon": "✒️",
    "color": "#34495e",
    "col": 13
  }
];

const ERAS = [
  {
    "id": "all",
    "name": "All Eras",
    "range": "10,000 BCE – 1800 CE",
    "year": -10000
  },
  {
    "id": "prehistory",
    "name": "Deep Prehistory & Oral Beginnings",
    "range": "10,000 – 3000 BCE",
    "year": -10000
  },
  {
    "id": "bronze",
    "name": "Bronze Age & First Writings",
    "range": "3000 – 1200 BCE",
    "year": -3000
  },
  {
    "id": "classical",
    "name": "Classical Antiquity & Axial Age",
    "range": "1200 BCE – 500 CE",
    "year": -1200
  },
  {
    "id": "medieval",
    "name": "Golden Ages & Medieval Epics",
    "range": "500 – 1400 CE",
    "year": 500
  },
  {
    "id": "renaissance",
    "name": "Renaissance & Global Masterpieces",
    "range": "1400 – 1800 CE",
    "year": 1400
  }
];

const SCRUBBER_DATES = [
  {
    "year": -10000,
    "label": "10,000 BCE"
  },
  {
    "year": -8000,
    "label": "8,000 BCE"
  },
  {
    "year": -5000,
    "label": "5,000 BCE"
  },
  {
    "year": -3000,
    "label": "3,000 BCE"
  },
  {
    "year": -2000,
    "label": "2,000 BCE"
  },
  {
    "year": -1200,
    "label": "1,200 BCE"
  },
  {
    "year": -750,
    "label": "750 BCE"
  },
  {
    "year": -500,
    "label": "500 BCE"
  },
  {
    "year": 0,
    "label": "1 CE"
  },
  {
    "year": 500,
    "label": "500 CE"
  },
  {
    "year": 1000,
    "label": "1,000 CE"
  },
  {
    "year": 1200,
    "label": "1,200 CE"
  },
  {
    "year": 1350,
    "label": "1,350 CE"
  },
  {
    "year": 1600,
    "label": "1,600 CE"
  },
  {
    "year": 1800,
    "label": "1,800 CE"
  }
];

const STORIES_DATA = [
  {
    "id": "rainbow-serpent",
    "year": -10000,
    "displayDate": "c. 10,000+ BCE (65,000 Year Living Oral Tradition)",
    "era": "prehistory",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Arnhem Land & Australian Red Centre",
    "author": "Aboriginal Songline Custodians & Elders",
    "title": "The Dreaming and the Great Rainbow Serpent (Almudj / Wagyl)",
    "subtitle": "The Creation of Earth's Watercourses and Living Songlines",
    "summary": "In the primordial Dreamtime (Tjukurpa), the giant Rainbow Serpent slithers across a barren earth, carving out gorges, rivers, and waterholes, establishing the sacred ancestral laws (Songlines).",
    "fullStory": "### Act I: The Awakening from Deep Earth\nIn the Dreamtime (Tjukurpa), the Rainbow Serpent stirred beneath the arid Australian crust, erupting upward to release the first life-giving rains.\n\n### Act II: Sculpting the Gorges\nHer massive undulating body carved deep riverbeds like the Katherine and Ord rivers, leaving sacred waterholes (billabongs) behind.\n\n### Act III: The Sacred Law\nShe gave clans their languages, totem laws, and unwritten Songlines. Those who disrespect Country face her tempestuous wrath.\n\n### Epilogue: Everywhen\nThe Dreaming is not in the past; it is an eternal present living in the land today.",
    "characters": [
      {
        "name": "Almudj (Rainbow Serpent)",
        "role": "Creator & Water Guardian",
        "desc": "Ancestral serpent whose movement shaped rivers."
      },
      {
        "name": "Ancestral Elders",
        "role": "Songline Keepers",
        "desc": "Preserve unwritten maps of Country."
      }
    ],
    "themes": [
      "Living Country",
      "Sacred Stewardship",
      "Everywhen"
    ],
    "echoes": "Parallels Jörmungandr in Norse and Quetzalcoatl in Mesoamerica.",
    "famousQuote": "“The land is our mother; we belong to the land.” — Yolngu Songline Teaching",
    "historicalContext": "Rock art depicting Rainbow Serpents in Arnhem Land is dated over 10,000 years old."
  },
  {
    "id": "tiddalik-frog",
    "year": -8000,
    "displayDate": "c. 8000 BCE",
    "era": "prehistory",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Wollombi Valley, Eastern Australia",
    "author": "Kulin & Gunai Nations Oral Tradition",
    "title": "Tiddalik the Giant Frog: The Great Drought and the Burst of Life",
    "subtitle": "The Monster of Thirst Who Swallowed Every River",
    "summary": "Tiddalik the giant frog awakens with an insatiable thirst, drinking every river and lake dry until the animal council makes him laugh, releasing a torrential flood that revives the earth.",
    "fullStory": "### Act I: The Thirst of Tiddalik\nTiddalik drank until rivers shrank to mud and billabongs turned to dust. The animals faced extinction.\n\n### Act II: The Animal Council\nWombat, Kangaroo, and Kookaburra gathered to make Tiddalik laugh so water would pour from his mouth. Dances and jokes failed.\n\n### Act III: The Eel's Dance\nNabunum the Eel tied himself in knots and spun like a top. Tiddalik cracked a smile, then burst into roaring laughter—releasing a deluge that revived every forest.",
    "characters": [
      {
        "name": "Tiddalik",
        "role": "Giant Frog of Thirst",
        "desc": "Swallowed all freshwater on the continent."
      },
      {
        "name": "Nabunum the Eel",
        "role": "Comedic Savior",
        "desc": "Made Tiddalik laugh with contortionist dances."
      }
    ],
    "themes": [
      "Resource Conservation",
      "Community Cooperation",
      "Humor as Power"
    ],
    "echoes": "Parallels the Vedic myth of Indra piercing Vritra to release cosmic waters.",
    "famousQuote": "“Take only what you need from the waterhole, lest Tiddalik return.” — Gunai Proverb",
    "historicalContext": "Echoes megafauna memories of giant Pleistocene amphibians in prehistoric Australia."
  },
  {
    "id": "pangu-nuwa",
    "year": -5000,
    "displayDate": "c. 5000 – 2700 BCE",
    "era": "prehistory",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Yellow River & Mount Buzhou",
    "author": "Traditional Lore (Recorded by Xu Zheng)",
    "title": "Pangu and Nüwa: The Cosmic Egg and the Pillars of Heaven",
    "subtitle": "Separation of Yin-Yang, Clay Humanity, and Molten Sky Stones",
    "summary": "Pangu cleaves Yin and Yang apart with an axe, transforming his dying body into mountains and rivers. Later, serpent-goddess Nüwa molds humans from yellow mud and repairs the broken sky.",
    "fullStory": "### Act I: The Cosmic Egg\nPangu sleeps inside an egg of chaos, striking it to separate clear Heaven from murky Earth.\n\n### Act II: The Great Sacrifice\nHis breath became the wind, left eye the Sun, right eye the Moon, and blood the Yangtze and Yellow rivers.\n\n### Act III: Nüwa's Clay Children\nNüwa molded figures from yellow silt along the Yellow River.\n\n### Act IV: The Broken Sky\nWhen Gonggong smashed Mount Buzhou, Nüwa melted five-colored stones to patch the heavens.",
    "characters": [
      {
        "name": "Pangu",
        "role": "Creator Giant",
        "desc": "Separated Heaven and Earth."
      },
      {
        "name": "Nüwa",
        "role": "Mother Goddess",
        "desc": "Molded humanity and repaired the sky."
      }
    ],
    "themes": [
      "Yin-Yang Harmony",
      "Self-Sacrifice",
      "Restoration"
    ],
    "echoes": "Pangu's body mirrors Norse Ymir and Vedic Purusha; Nüwa mirrors Prometheus.",
    "famousQuote": "“Pangu stood between heaven and earth, and from his breath the world was born.”",
    "historicalContext": "Core cosmogony depicted in Han dynasty tomb murals."
  },
  {
    "id": "genesis-creation",
    "year": -2900,
    "displayDate": "c. 2900 – 1000 BCE",
    "era": "bronze",
    "regionId": "levant",
    "regionName": "Levant & Biblical Traditions",
    "place": "Eden & Canaan",
    "author": "Biblical Scripture (Torah / Genesis)",
    "title": "Genesis: The Garden of Eden, the Fall, and Noah's Deluge",
    "subtitle": "The Tree of Knowledge, the Ark of Gopher Wood, and the Rainbow",
    "summary": "Adam and Eve eat from the forbidden tree of knowledge, entering mortality. Generations later, Noah builds a three-deck ark of gopher wood to preserve all animal kinds through a worldwide deluge.",
    "fullStory": "### Act I: Eden and the Fall\nGod breathes life into Adam and creates Eve. Tempted by the serpent, they eat the forbidden fruit, gaining moral awareness and exile.\n\n### Act II: The Great Flood\nGrieved by human violence, God commands righteous Noah to construct an ark with pairs of every beast.\n\n### Act III: The Dove and the Rainbow\nAfter 150 days of flood, a dove returns with an olive leaf. God sets the rainbow across the clouds as an eternal covenant of mercy.",
    "characters": [
      {
        "name": "Noah",
        "role": "Righteous Builder",
        "desc": "Preserved life through faith."
      },
      {
        "name": "Adam & Eve",
        "role": "First Humans",
        "desc": "Entered moral consciousness."
      }
    ],
    "themes": [
      "Covenant of Mercy",
      "Moral Choice",
      "Cosmic Cleansing"
    ],
    "echoes": "Matches Mesopotamian Utnapishtim and Greek Deucalion flood tales.",
    "famousQuote": "“I have set my rainbow in the clouds, and it will be the sign of the covenant.” — Genesis 9:13",
    "historicalContext": "Foundational narrative for Judaism, Christianity, and Islam."
  },
  {
    "id": "dangun-korea",
    "year": -2333,
    "displayDate": "c. 2333 BCE (Founding Myth)",
    "era": "bronze",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Mount Taebaek & Pyongyang",
    "author": "Recorded in Samguk Yusa by Monk Iryeon",
    "title": "Dangun Wanggeom: The Bear-Woman and the Founding of Gojoseon",
    "subtitle": "100 Days of Mugwort and Garlic in the Dark Cave",
    "summary": "A bear and a tiger ask the heavenly prince Hwanung to make them human. Enduring 100 days eating only sacred mugwort and garlic in a dark cave, only the bear perseveres, becoming the woman Ungnyeo, who gives birth to Dangun, founder of Korea.",
    "fullStory": "### Act I: The Heavenly Prince\nHwanung descended from heaven with three thousand followers to teach agriculture, law, and medicine.\n\n### Act II: The Cave of Garlic\nA bear and tiger prayed to become human. Hwanung gave them 20 cloves of garlic and mugwort, commanding them to stay out of the sunlight for 100 days. The tiger grew impatient and fled; the bear persevered and transformed into a beautiful woman, Ungnyeo.\n\n### Act III: The Birth of Dangun\nUngnyeo married Hwanung, giving birth to Dangun Wanggeom, who founded Gojoseon under the philosophy of Hongik Ingan (Devotion to Human Welfare).",
    "characters": [
      {
        "name": "Dangun Wanggeom",
        "role": "Founding King of Korea",
        "desc": "United heaven and earth to establish Gojoseon."
      },
      {
        "name": "Ungnyeo (Bear-Woman)",
        "role": "Mother of Korea",
        "desc": "Persevered through darkness to achieve humanity."
      }
    ],
    "themes": [
      "Hongik Ingan (Benefit All Humanity)",
      "Patience and Endurance",
      "Harmony of Nature"
    ],
    "echoes": "Parallels totemic animal-human transformation myths across Siberia and the Americas.",
    "famousQuote": "“Govern with devotion to the welfare of all humanity.” — Hongik Ingan Principle",
    "historicalContext": "National Foundation Day (Gaecheonjeol) is celebrated every October 3 in Korea."
  },
  {
    "id": "enheduanna-inanna",
    "year": -2300,
    "displayDate": "c. 2300 BCE",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Ur & Uruk (Sumer / Akkad)",
    "author": "Enheduanna (History's First Named Author)",
    "title": "The Exaltation of Inanna (Nin-me-šara)",
    "subtitle": "The 42 Sacred Hymns of the First Recorded Author",
    "summary": "Princess Enheduanna, High Priestess of Ur, is driven into the desert by a rebel usurper and composes revolutionary hymns exalting Inanna to reclaim her temple throne through the written word.",
    "fullStory": "### Act I: The Priestess of the Moon\nEnheduanna presided over the grand ziggurat of Ur as daughter of Sargon the Great.\n\n### Act II: Banishment into the Dust\nA rebel general named Lugalanne stripped her crown and exiled her into the wasteland.\n\n### Act III: The Birth of Authored Poetry\nCarving clay tablets under the blazing sun, she composed hymns elevating Inanna above all gods, rallying loyalists and regaining her sacred office.",
    "characters": [
      {
        "name": "Enheduanna",
        "role": "High Priestess & Author",
        "desc": "First individual in history to sign her name to literature."
      }
    ],
    "themes": [
      "Power of the Written Word",
      "Divine Justice",
      "Exile & Triumph"
    ],
    "echoes": "Precedes Sappho and biblical King David by over a thousand years.",
    "famousQuote": "“What I recited at night, the singer shall repeat by day.” — Enheduanna",
    "historicalContext": "The alabaster Disk of Enheduanna was discovered in Ur in 1927."
  },
  {
    "id": "gilgamesh-epic",
    "year": -2100,
    "displayDate": "c. 2100 – 1200 BCE",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Uruk & Waters of Death",
    "author": "Attributed to Sîn-lēqi-unninni",
    "title": "The Epic of Gilgamesh: The Quest for Immortality",
    "subtitle": "Enkidu, the Slaying of Humbaba, the Deluge, and the Plant of Youth",
    "summary": "Gilgamesh, the tyrannical king of Uruk, finds brotherhood in Enkidu. When Enkidu dies, Gilgamesh crosses the Waters of Death to seek Utnapishtim and the secret of eternal life.",
    "fullStory": "### Act I: King and Wild Man\nEnkidu is created from clay to humble Gilgamesh. After a titanic duel, they become inseparable brothers.\n\n### Act II: The Cedar Forest and Ishtar's Wrath\nThey slay Humbaba and the Bull of Heaven. The gods punish them by striking Enkidu down with fever.\n\n### Act III: Journey to the Faraway\nTerrified of death, Gilgamesh visits Utnapishtim, hears the story of the great flood, and wins a plant of youth—only for a snake to steal it while he bathes.\n\n### Act IV: Return to Uruk\nGilgamesh returns to Uruk, finding peace in the enduring beauty of the city walls.",
    "characters": [
      {
        "name": "Gilgamesh",
        "role": "King of Uruk",
        "desc": "Two-thirds god whose quest transforms him."
      },
      {
        "name": "Enkidu",
        "role": "Wild Man",
        "desc": "Civilized by love and friendship."
      },
      {
        "name": "Utnapishtim",
        "role": "Flood Survivor",
        "desc": "Granted immortality after building an ark."
      }
    ],
    "themes": [
      "Mortality & Wisdom",
      "Brotherhood",
      "Civilization vs Nature"
    ],
    "echoes": "Flood account matches Noah's Ark; grief matches Achilles for Patroclus.",
    "famousQuote": "“Look upon the burnt-brick walls of Uruk! Did not the Seven Sages lay its foundation?”",
    "historicalContext": "Deciphered from clay tablets from the Library of Ashurbanipal in 1872."
  },
  {
    "id": "houyi-change",
    "year": -2100,
    "displayDate": "c. 2100 BCE",
    "era": "bronze",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Kunlun Mountains & Moon Palace",
    "author": "Traditional Myth (Huainanzi)",
    "title": "Houyi the Archer and Chang'e Flies to the Moon",
    "subtitle": "Shooting Down Nine Suns, the Elixir of Immortality, and the Jade Rabbit",
    "summary": "When ten suns scorch the earth, master archer Houyi shoots down nine with his vermilion bow. Given the elixir of immortality, his wife Chang'e drinks it to protect it from a thief, floating to the Moon.",
    "fullStory": "### Act I: The Ten Scorching Suns\nTen sun-crows flew into the sky at once, boiling rivers and wilting crops.\n\n### Act II: The Nine Divine Arrows\nHouyi climbed Mount Kunlun, shooting down nine suns to save humanity.\n\n### Act III: The Flight to the Moon\nQueen Mother of the West gave Houyi the Elixir of Immortality. To prevent a thief from seizing it, his wife Chang'e drank it, floating up to the Moon with the Jade Rabbit.",
    "characters": [
      {
        "name": "Houyi",
        "role": "Divine Archer",
        "desc": "Saved earth from nine suns."
      },
      {
        "name": "Chang'e",
        "role": "Moon Goddess",
        "desc": "Dwells in the lunar palace of cold cassia trees."
      }
    ],
    "themes": [
      "Selfless Heroism",
      "Longing across Starlit Distances"
    ],
    "echoes": "Parallels Polynesian Maui snaring the sun and Greek Apollo's chariot.",
    "famousQuote": "“Gazing at the bright moon from afar, lovers share their hearts across ten thousand leagues.”",
    "historicalContext": "Celebrated annually worldwide during the Mid-Autumn Festival (Mooncake Festival)."
  },
  {
    "id": "osiris-isis-horus",
    "year": -2000,
    "displayDate": "c. 2000 – 1200 BCE",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Abydos, Delta Marshes & Heliopolis",
    "author": "Ancient Egyptian Priestly Tradition",
    "title": "The Myth of Osiris, Isis, and Horus: Death and Resurrection",
    "subtitle": "The Dismembered King, Isis's Magic, and the Falcon's Triumph",
    "summary": "King Osiris is murdered and cut into fourteen pieces by his jealous brother Set. Queen Isis reassembles his flesh, resurrects him through magic, and bears Horus, who defeats Set to restore Ma'at.",
    "fullStory": "### Act I: The Cedar Chest\nSet tricks Osiris into a golden chest and throws it into the Nile.\n\n### Act II: The Scattered Pieces\nSet cuts Osiris into 14 pieces across Egypt. Isis recovers thirteen, performs the first mummification, and conceives Horus.\n\n### Act III: The 80-Year Contendings\nHorus battles Set across land and sea, losing his eye (the Wedjat) before the divine council declares him the rightful Pharaoh.",
    "characters": [
      {
        "name": "Osiris",
        "role": "Lord of Resurrection",
        "desc": "First mummy and eternal judge of souls."
      },
      {
        "name": "Isis",
        "role": "Goddess of Magic",
        "desc": "Reassembled Osiris with love and spells."
      },
      {
        "name": "Horus",
        "role": "Falcon King",
        "desc": "Avenged his father and united Egypt."
      }
    ],
    "themes": [
      "Resurrection",
      "Ma'at (Cosmic Order)",
      "Divine Kingship"
    ],
    "echoes": "Parallels the death of Baldr in Norse and the Christian resurrection.",
    "famousQuote": "“Arise, Osiris! Isis has found your limbs; awake and rule the Western Lands forever!”",
    "historicalContext": "Core theological foundation for Egyptian mummification and pyramid construction."
  },
  {
    "id": "shipwrecked-sailor",
    "year": -1950,
    "displayDate": "c. 1950 BCE",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Red Sea & Island of the Ka (Punt)",
    "author": "12th Dynasty Royal Scribe",
    "title": "The Tale of the Shipwrecked Sailor and the Golden Serpent",
    "subtitle": "The Monster of the Abyss, the Lost Island, and the Wisdom of Home",
    "summary": "A sailor shipwrecks on a phantom island in the Red Sea, meeting a giant golden serpent with beard of lapis lazuli who consoles him with prophecy before the island sinks beneath the waves.",
    "fullStory": "### Act I: The Storm in the Red Sea\nA ship with 120 brave sailors is smashed by forty-cubit waves; only one sailor washes ashore on a magical island.\n\n### Act II: The Golden Serpent\nThe earth trembles as a thirty-cubit serpent with scales of gold and lapis lazuli corners him, asking gently what brought him to the Island of the Ka.\n\n### Act III: The Prophecy\nThe serpent tells his own tragedy of losing his kin to a falling star, predicting an Egyptian ship will rescue the sailor in four months and advising him to hold his children in his arms.",
    "characters": [
      {
        "name": "The Shipwrecked Sailor",
        "role": "Survivor",
        "desc": "Sole survivor of an imperial trading vessel."
      },
      {
        "name": "The Golden Serpent",
        "role": "Lord of Punt",
        "desc": "Benevolent dragon of wisdom."
      }
    ],
    "themes": [
      "Resilience",
      "Comfort in Shared Grief",
      "Value of Family"
    ],
    "echoes": "Direct ancestor to Sinbad the Sailor and Odysseus on Calypso's island.",
    "famousQuote": "“How joyful it is when someone relates what they have tasted when the crisis has passed!”",
    "historicalContext": "Preserved on a single Middle Kingdom papyrus scroll now in the Hermitage Museum."
  },
  {
    "id": "tale-of-sinuhe",
    "year": -1900,
    "displayDate": "c. 1900 BCE",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Thebes & Canaan",
    "author": "Middle Kingdom Court Scribe",
    "title": "The Story of Sinuhe: The Exile and the Longing for the Nile",
    "subtitle": "Court Intrigue, Desert Warfare, and the Pharaoh's Golden Pardon",
    "summary": "When Pharaoh Amenemhat I is assassinated, courtier Sinuhe flees in panic into Canaan. Becoming a great chieftain, he is gripped by an ache for the Nile and returns home in royal honor.",
    "fullStory": "### Act I: Flight into the Sands\nOverhearing conspiracy in the royal camp, Sinuhe flees across the desert, rescued by Bedouin chiefs.\n\n### Act II: The Hero of Retjenu\nSinuhe becomes a prince in Syria, slaying a giant champion in single combat.\n\n### Act III: The Pharaoh's Letter\nFacing old age, he receives a golden pardon from Senusret I, returning to Egypt to receive an eternal tomb.",
    "characters": [
      {
        "name": "Sinuhe",
        "role": "Exiled Courtier",
        "desc": "Longed for burial in the Nile soil."
      },
      {
        "name": "Senusret I",
        "role": "Pharaoh of Egypt",
        "desc": "Pardoned Sinuhe in royal mercy."
      }
    ],
    "themes": [
      "Exile and Return",
      "Soul's True Home",
      "Mercy"
    ],
    "echoes": "Prefigures the Prodigal Son parable and David vs Goliath.",
    "famousQuote": "“What is greater than that my corpse should rest in the earth where I was born?”",
    "historicalContext": "Widely considered the supreme classic of Middle Kingdom Egyptian prose."
  },
  {
    "id": "the-eloquent-peasant",
    "year": -1850,
    "displayDate": "c. 1,850 BCE",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Literary work from Ancient Egypt",
    "author": "Classical Ancient Egypt Tradition",
    "title": "The Eloquent Peasant",
    "subtitle": "Literary work from Ancient Egypt",
    "summary": "The Eloquent Peasant is an Ancient Egyptian story that was composed around 1850 BCE during the time of the Middle Kingdom in Egypt. It is one of the longest Egyptian tales that has survived completed. The tale is about a peasant, Khun-Anup, who stumbles upon the property of the high steward, the noble Rensi son of Meru, guarded by its harsh overseer, Nemtynakht. It is set in the Ninth or Tenth Dynasty around Herakleopolis. This tale is described as an elaborate reflection on the connection – or disconnection – of ethical order and refined speech, as transliterated into refined writing.",
    "fullStory": "### Act I: The Awakening of The Eloquent Peasant\nThe Eloquent Peasant is an Ancient Egyptian story that was composed around 1850 BCE during the time of the Middle Kingdom in Egypt. It is one of the longest Egyptian tales that has survived completed. The tale is about a peasant, Khun-Anup, who stumbles upon the property of the high steward, the noble Rensi son of Meru, guarded by its harsh overseer, Nemtynakht. It is set in the Ninth or Tenth Dynasty around Herakleopolis. This tale is described as an elaborate reflection on the connection – or disconnection – of ethical order and refined speech, as transliterated into refined writing.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "The Eloquent Peasant",
        "role": "Protagonist",
        "desc": "Literary work from Ancient Egypt"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Ancient Egypt.",
    "famousQuote": "“The memory of The Eloquent Peasant endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "enuma-elish",
    "year": -1800,
    "displayDate": "c. 1800 BCE",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Babylon, Mesopotamia",
    "author": "Babylonian Temple Scribes (Akitu Festival)",
    "title": "Enuma Elish: The Babylonian Creation Epic",
    "subtitle": "The Battle of Marduk and Tiamat, and the Forging of the Cosmos",
    "summary": "When the primordial ocean-dragon Tiamat threatens the gods, Marduk steps forward with the four winds and lightning arrow, splitting Tiamat's body to fashion heaven, earth, and mankind.",
    "fullStory": "### Act I: Primordial Chaos\nApsu and Tiamat mingle in silence before the younger gods awaken.\n\n### Act II: The Dragon's Army\nTiamat spawns eleven monsters and gives Qingu the Tablet of Destinies.\n\n### Act III: Marduk's Victory\nMarduk captures Tiamat in his starlight net, pierces her heart with lightning, and splits her corpse to form the sky and earth.",
    "characters": [
      {
        "name": "Marduk",
        "role": "Champion of Babylon",
        "desc": "Wields the storm winds."
      },
      {
        "name": "Tiamat",
        "role": "Salt Water Dragon",
        "desc": "Cosmic chaos split to form the universe."
      }
    ],
    "themes": [
      "Cosmogony",
      "Order vs Chaos",
      "Divine Kingship"
    ],
    "echoes": "Echoes Zeus fighting Typhon and Yahweh subduing Leviathan.",
    "famousQuote": "“When in the height heaven was not named... Marduk split the dragon like a shellfish.”",
    "historicalContext": "Recited annually at the Akitu New Year Festival in Babylon."
  },
  {
    "id": "hammurabi-code",
    "year": -1750,
    "displayDate": "c. 1750 BCE",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Babylon & Susa",
    "author": "King Hammurabi of Babylon",
    "title": "The Code of Hammurabi: The Laws of the Sun God Shamash",
    "subtitle": "282 Carved Judgments and the Principle of Proportional Justice",
    "summary": "King Hammurabi receives the rod and ring of justice directly from Shamash the Sun God, carving nearly three hundred legal statutes onto a seven-foot diorite stele to protect the weak from the strong.",
    "fullStory": "### Act I: The Mandate of Shamash\nHammurabi stands before the radiant throne of Shamash, receiving the divine mandate to banish injustice from the land.\n\n### Act II: The 282 Laws\nCarved in clear cuneiform, the laws established standardized prices, merchant contracts, marriage protections, and the principle of lex talionis (an eye for an eye).\n\n### Act III: The Stele in the Public Square\nThe black pillar was erected in the temple courtyard so any wronged citizen could read their rights.",
    "characters": [
      {
        "name": "Hammurabi",
        "role": "King of Justice",
        "desc": "United Mesopotamia under a written legal code."
      },
      {
        "name": "Shamash",
        "role": "Sun God of Truth",
        "desc": "Dispenser of divine law and light."
      }
    ],
    "themes": [
      "Written Law vs Arbitrary Power",
      "Proportional Justice"
    ],
    "echoes": "Prefigures the Mosaic Law of Exodus and the Roman Twelve Tables.",
    "famousQuote": "“That the strong might not oppress the weak, that the orphan and widow receive justice.”",
    "historicalContext": "The 7-foot black basalt stele was discovered at Susa in 1901 and now sits in the Louvre."
  },
  {
    "id": "atrahasis-flood",
    "year": -1700,
    "displayDate": "c. 1700 BCE",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Sippar & Mesopotamia",
    "author": "Scribe Ipiq-Aya",
    "title": "The Epic of Atrahasis: The Flood and Human Overpopulation",
    "subtitle": "Enlil's Noise, Ea's Reed Wall Whisper, and the Boat of Life",
    "summary": "When the clamor of humanity keeps the god Enlil awake, he unleashes plagues and a world-cleansing deluge. The wise king Atrahasis is secretly warned by Ea through a reed hut wall to build a giant ship.",
    "fullStory": "### Act I: The Rebellion of the Igigi\nThe younger gods strike against heavy ditch-digging; humanity is molded from clay and a slain god's spirit to carry the work.\n\n### Act II: The Noise of Mankind\nHumanity multiplies so loudly that Enlil cannot sleep. He orders drought, plague, and finally the Deluge.\n\n### Act III: The Reed Hut Warning\nEa whispers to the wall of Atrahasis's hut: 'Dismantle your house, build a boat, save the seed of life!' Atrahasis weathers the storm for seven days.",
    "characters": [
      {
        "name": "Atrahasis",
        "role": "The Exceedingly Wise King",
        "desc": "Preserved life during the Mesopotamian deluge."
      },
      {
        "name": "Enlil",
        "role": "Storm God",
        "desc": "Sought to silence humanity's clamor."
      },
      {
        "name": "Ea",
        "role": "God of Waters & Wisdom",
        "desc": "Humanity's secret protector."
      }
    ],
    "themes": [
      "Human Noise & Divine Rest",
      "Preservation of Life"
    ],
    "echoes": "Direct ancestor to the biblical Noah and Greek Deucalion flood narratives.",
    "famousQuote": "“Wall, listen to me! Reed hut, understand my words! Tear down your house and build a boat!”",
    "historicalContext": "Oldest cuneiform flood tablet copied during the reign of King Ammi-saduqa of Babylon."
  },
  {
    "id": "ishtar-underworld",
    "year": -1600,
    "displayDate": "c. 1600 BCE",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Kur (Mesopotamian Netherworld)",
    "author": "Sumerian / Akkadian Liturgical Priesthood",
    "title": "The Descent of Ishtar (Inanna) to the Underworld",
    "subtitle": "The Seven Gates of Kur, the Naked Goddess, and Dumuzi's Substitute",
    "summary": "Ishtar descends to the dark realm of her sister Ereshkigal. Stripped of her jewelry and garments at seven bronze gates, she is hung upon a meat hook until rescued by water-demons, requiring her lover Dumuzi to take her place.",
    "fullStory": "### Act I: The Seven Gates\nAt each gate of the Underworld, the guardian Neti strips one piece of Ishtar's royal regalia until she stands naked and powerless.\n\n### Act II: The Curse of Ereshkigal\nEreshkigal strikes Ishtar with sixty diseases and hangs her on a spike.\n\n### Act III: The Cosmic Stagnation\nOn earth, all fertility and reproduction cease. Ea creates two genderless spirits from dirt under his fingernails to sprinkle the water of life upon Ishtar.\n\n### Act IV: Dumuzi's Fate\nTo return, Ishtar must offer a living substitute. Finding her husband Dumuzi feasting on a throne instead of mourning, she sends him to the underworld for half of every year.",
    "characters": [
      {
        "name": "Ishtar / Inanna",
        "role": "Queen of Heaven",
        "desc": "Goddess of passion and war."
      },
      {
        "name": "Ereshkigal",
        "role": "Queen of the Great Below",
        "desc": "Dark ruler of the land of no return."
      },
      {
        "name": "Dumuzi (Tammuz)",
        "role": "Shepherd God",
        "desc": "Seasonal dying-and-rising deity."
      }
    ],
    "themes": [
      "Katabasis (Descent)",
      "Seasonal Cycle",
      "Stripping of Ego"
    ],
    "echoes": "Direct blueprint for Greek Persephone and Demeter, and Orpheus descending for Eurydice.",
    "famousQuote": "“To the Land of No Return, the realm of Ereshkigal, Ishtar daughter of Sin turned her mind.”",
    "historicalContext": "Provided the theological basis for ancient Near Eastern seasonal agricultural rites."
  },
  {
    "id": "akhenaten-aten",
    "year": -1350,
    "displayDate": "c. 1350 BCE",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Amarna (Akhetaten), Egypt",
    "author": "Pharaoh Akhenaten",
    "title": "The Great Hymn to the Aten: The Sun Disk and the First Monotheism",
    "subtitle": "The Radiance That Breathes Life into Chicks in the Egg",
    "summary": "Pharaoh Akhenaten breaks with thousands of years of polytheism, moving Egypt's capital to Amarna to worship the solar disk Aten as the sole creator and sustainer of all living creatures on Earth.",
    "fullStory": "### Act I: The Sun at Dawn\nAkhenaten proclaims the Aten as the sole source of life: when the sun rises, darkness flees and all of Egypt awakens to sing.\n\n### Act II: The Universal Creator\nHe praises the Aten for creating the chick inside the egg, nursing birds in the marshes, and giving different languages and skins to all human races across Syria, Nubia, and Egypt.\n\n### Act III: The Night of Oblivion\nWhen the sun sets, the world enters a death-like sleep until the radiant disk returns.",
    "characters": [
      {
        "name": "Akhenaten",
        "role": "Pharaoh & Reformer",
        "desc": "Championed solar monotheism."
      },
      {
        "name": "Aten",
        "role": "The Living Solar Disk",
        "desc": "Universal radiant creator of all races."
      }
    ],
    "themes": [
      "Solar Radiance",
      "Universal Creator",
      "First Monotheism"
    ],
    "echoes": "Shares striking word-for-word literary parallels with Psalm 104 in the Bible.",
    "famousQuote": "“How manifold are your works, O Sole God, beside whom there is no other!” — Great Hymn",
    "historicalContext": "Carved into the tomb of the royal courtier Ay at Amarna around 1350 BCE."
  },
  {
    "id": "moses-exodus",
    "year": -1300,
    "displayDate": "c. 1300 BCE",
    "era": "bronze",
    "regionId": "levant",
    "regionName": "Levant & Biblical Traditions",
    "place": "Nile Delta, Red Sea & Mount Sinai",
    "author": "Biblical Tradition (Book of Exodus)",
    "title": "Moses and the Exodus: The Ten Plagues and the Parting of the Sea",
    "subtitle": "The Burning Bush, the Staff of God, and the Ten Commandments",
    "summary": "Moses, raised in Pharaoh's palace, is called by God from a burning bush to liberate the enslaved Israelites, parting the Red Sea and receiving the Ten Commandments on Mount Sinai.",
    "fullStory": "### Act I: The Burning Bush\nFleeing Egypt, Moses encounters the burning bush in Midian and receives the divine mandate: 'Let my people go!'\n\n### Act II: The Ten Plagues\nWhen Pharaoh hardens his heart, ten plagues strike Egypt—turning the Nile to blood, swarming locusts, and the Passover night.\n\n### Act III: The Parting of the Red Sea\nTrapped between Pharaoh's chariots and the sea, Moses raises his staff; the waters divide, allowing the people to pass on dry ground.\n\n### Act IV: The Tablet on Mount Sinai\nAmidst thunder and smoke on Sinai, Moses receives the Decalogue of divine moral law.",
    "characters": [
      {
        "name": "Moses",
        "role": "Lawgiver & Prophet",
        "desc": "Led the Israelites out of Egyptian bondage."
      },
      {
        "name": "Pharaoh (Ramesses)",
        "role": "Imperial Monarch",
        "desc": "Hardened his heart against liberation."
      }
    ],
    "themes": [
      "Liberation from Slavery",
      "Moral Law",
      "Faith against Empires"
    ],
    "echoes": "Archetype of liberation struggle inspiring civil rights movements across history.",
    "famousQuote": "“The Lord is my strength and my song; he has become my salvation.” — Exodus 15:2",
    "historicalContext": "Forms the liturgical core of the Jewish festival of Passover (Pesach)."
  },
  {
    "id": "ramayana-valmiki",
    "year": -1200,
    "displayDate": "c. 1200 – 500 BCE",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Ayodhya, Dandaka & Lanka",
    "author": "Adi Kavi Sage Valmiki",
    "title": "The Ramayana: The Epic Journey of Rama and Sita",
    "subtitle": "Dharma, Hanuman's Leap, the Ocean Bridge, and the Defeat of Ravana",
    "summary": "Prince Rama accepts a 14-year forest exile to honor his father's vow. When the demon king Ravana abducts Sita to Lanka, Rama allies with Hanuman, building a floating stone bridge to wage a war of righteousness.",
    "fullStory": "### Act I: The Forest Exile\nRama serenely accepts banishment to the Dandaka Forest; Sita and Lakshmana join him.\n\n### Act II: The Golden Deer and Abduction\nRavana lures Rama away with a golden deer and kidnaps Sita to Lanka.\n\n### Act III: Hanuman and the Floating Bridge\nHanuman leaps across the ocean, finds Sita, and burns Lanka. The Vanaras build Ram Setu to cross the sea.\n\n### Act IV: The Fall of Ravana\nRama destroys Ravana with the Brahmastra arrow, returning to Ayodhya celebrated during Diwali.",
    "characters": [
      {
        "name": "Rama",
        "role": "Avatar of Vishnu",
        "desc": "Ideal of righteous conduct (Dharma)."
      },
      {
        "name": "Sita",
        "role": "Princess of Mithila",
        "desc": "Embodiment of devotion and courage."
      },
      {
        "name": "Hanuman",
        "role": "Vanara Hero",
        "desc": "Son of the wind god endowed with supreme loyalty."
      }
    ],
    "themes": [
      "Dharma (Righteous Duty)",
      "Triumph of Light over Darkness",
      "Devotion"
    ],
    "echoes": "Sita's abduction matches Helen of Troy in the Iliad.",
    "famousQuote": "“Mother and motherland are more sacred than heaven itself.” — Valmiki",
    "historicalContext": "The Adi Kavya (First Poem) of Indian classical literature."
  },
  {
    "id": "tale-of-the-two-brothers",
    "year": -1194,
    "displayDate": "c. 1,194 BCE",
    "era": "classical",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Ancient Egyptian literary work",
    "author": "Classical Ancient Egypt Tradition",
    "title": "Tale of the Two Brothers",
    "subtitle": "Ancient Egyptian literary work",
    "summary": "The \"Tale of Two Brothers\" is an ancient Egyptian story that dates from the reign of Seti II, who ruled from 1200 to 1194 BC during the 19th Dynasty of the New Kingdom. The story is preserved on the Papyrus D'Orbiney, which is currently held in the British Museum.",
    "fullStory": "### Act I: The Awakening of Tale of the Two Brothers\nThe \"Tale of Two Brothers\" is an ancient Egyptian story that dates from the reign of Seti II, who ruled from 1200 to 1194 BC during the 19th Dynasty of the New Kingdom. The story is preserved on the Papyrus D'Orbiney, which is currently held in the British Museum.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Tale of the Two Brothers",
        "role": "Protagonist",
        "desc": "Ancient Egyptian literary work"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Ancient Egypt.",
    "famousQuote": "“The memory of Tale of the Two Brothers endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "david-goliath",
    "year": -1000,
    "displayDate": "c. 1000 BCE",
    "era": "classical",
    "regionId": "levant",
    "regionName": "Levant & Biblical Traditions",
    "place": "Valley of Elah, Judea",
    "author": "Biblical Tradition (Books of Samuel)",
    "title": "David and Goliath: The Shepherd Boy and the Philistine Giant",
    "subtitle": "Five Smooth Stones, the Bronze Armor, and the Sling of Faith",
    "summary": "The young shepherd boy David visits the battle lines of Israel and volunteers to face the terrifying nine-foot Philistine champion Goliath, striking him in the forehead with a single sling stone.",
    "fullStory": "### Act I: The Giant's Challenge\nFor forty days, Goliath of Gath mocked the army of King Saul, demanding single combat.\n\n### Act II: The Shepherd in Rags\nDavid refused heavy bronze armor, carrying only his shepherd's staff, sling, and five smooth stones from the brook.\n\n### Act III: The Strike at the Brow\nGoliath laughed in contempt. David whirled his sling; the stone sank into Goliath's forehead, felling the titan to the dust.",
    "characters": [
      {
        "name": "David",
        "role": "Shepherd & Future King",
        "desc": "Relied on agility and faith rather than iron armor."
      },
      {
        "name": "Goliath",
        "role": "Philistine Champion",
        "desc": "Nine-foot giant clad in bronze scales."
      }
    ],
    "themes": [
      "Underdog Triumph",
      "Faith over Physical Might",
      "Courage"
    ],
    "echoes": "Parallels Sinuhe vs the Hero of Retjenu and Irish Cú Chulainn.",
    "famousQuote": "“You come against me with sword and spear, but I come against you in the name of the Lord.”",
    "historicalContext": "Excavations in the Valley of Elah have revealed 10th-century BCE fortified Judean settlements."
  },
  {
    "id": "mahabharata-vyasa",
    "year": -900,
    "displayDate": "c. 900 – 400 BCE",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Hastinapura & Kurukshetra",
    "author": "Sage Krishna Dwaipayana Vyasa",
    "title": "The Mahabharata & Bhagavad Gita: The Great Cosmic War",
    "subtitle": "The Pandavas vs Kauravas, the Dice Game, and Krishna's Teachings",
    "summary": "The conflict between the five Pandavas and hundred Kauravas culminates at Kurukshetra. Facing his own family in battle, Arjuna receives the immortal Bhagavad Gita from Lord Krishna.",
    "fullStory": "### Act I: The Dice Game\nShakuni strips Yudhishthira of kingdom and Draupadi. Krishna saves Draupadi with infinite cloth.\n\n### Act II: The Song of God (Gita)\nAt Kurukshetra, Krishna reveals the immortality of the soul and Karma Yoga to the despondent Arjuna.\n\n### Act III: The 18-Day Battle\nBhishma, Drona, and Karna fall in titanic combat; the Pandavas win at tragic cost.",
    "characters": [
      {
        "name": "Arjuna",
        "role": "Supreme Archer",
        "desc": "Recipient of the Bhagavad Gita."
      },
      {
        "name": "Lord Krishna",
        "role": "Charioteer & Avatar",
        "desc": "Cosmic guide and diplomat."
      },
      {
        "name": "Draupadi",
        "role": "Fiery Queen",
        "desc": "Born of sacrificial flame."
      }
    ],
    "themes": [
      "Karma Yoga (Selfless Duty)",
      "Immortality of the Soul",
      "Moral Conflict"
    ],
    "echoes": "Parallels Norse Ragnarök and Arthurian Battle of Camlann.",
    "famousQuote": "“You have a right only to work, never to the fruits of action.” — Bhagavad Gita 2.47",
    "historicalContext": "At 100,000 verses, it is the longest epic poem in world literature."
  },
  {
    "id": "iliad-odyssey-homer",
    "year": -750,
    "displayDate": "c. 750 – 700 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Troy & Ithaca",
    "author": "Homer (Blind Bard of Ionia)",
    "title": "The Iliad & The Odyssey: The Fall of Troy and the Wanderer's Return",
    "subtitle": "Achilles' Rage, the Wooden Horse, Cyclops, Circe, and Penelope's Shroud",
    "summary": "The dual founding epics of Western literature. The Iliad captures Achilles' wrath at the siege of Troy; the Odyssey follows Odysseus through ten years of monsters and sea perils to reclaim Ithaca.",
    "fullStory": "### Act I: The Wrath of Achilles\nOffended by Agamemnon, Achilles withdraws until Hector kills Patroclus. Re-entering in divine armor, Achilles slays Hector.\n\n### Act II: The Trojan Horse & Sea Perils\nTroy falls by the wooden horse. Blinding the Cyclops Polyphemus, Odysseus wanders for ten years across supernatural seas.\n\n### Act III: The Beggar's Bow\nDisguised in rags, Odysseus strings his legendary bow, slays the arrogant suitors, and reclaims Penelope.",
    "characters": [
      {
        "name": "Achilles",
        "role": "Greek Champion",
        "desc": "Torn between peaceful life and immortal glory."
      },
      {
        "name": "Odysseus",
        "role": "King of Ithaca",
        "desc": "Master strategist of twists and turns."
      },
      {
        "name": "Penelope",
        "role": "Queen of Ithaca",
        "desc": "Fidelity and resilience."
      }
    ],
    "themes": [
      "Glory (Kleos) vs Homecoming (Nostos)",
      "Tragedy of War",
      "Intellect over Force"
    ],
    "echoes": "Achilles and Patroclus match Gilgamesh and Enkidu.",
    "famousQuote": "“Sing in me, Muse, and tell the story of that man of twists and turns...” — Homer",
    "historicalContext": "Excavations at Hisarlik proved Troy was a historical Bronze Age citadel destroyed c. 1180 BCE."
  },
  {
    "id": "hesiod-theogony",
    "year": -700,
    "displayDate": "c. 700 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Mount Helicon & Olympus",
    "author": "Hesiod (Shepherd-Poet)",
    "title": "Theogony & Works and Days: The Titanomachy and Pandora's Box",
    "subtitle": "Cronus's Sickle, Prometheus's Fire, and the Sole Remaining Hope",
    "summary": "Hesiod's genealogical origins of the Greek cosmos: Cronus swallows his children, Zeus leads the Titanomachy war, Prometheus steals fire for mortals, and Pandora's jar unleashes worldly sorrows—leaving only Hope inside.",
    "fullStory": "### Act I: Chaos to Titans\nGaia and Uranus birth the Titans. Cronus overthrows his father with a flint sickle.\n\n### Act II: The Titanomachy\nZeus escapes being swallowed, frees his siblings, and hurls the Titans into Tartarus with thunderbolts.\n\n### Act III: Prometheus and Pandora\nPrometheus steals fire in a fennel stalk. Zeus punishes humanity with Pandora, whose jar releases plagues, leaving Hope trapped inside.",
    "characters": [
      {
        "name": "Zeus",
        "role": "King of the Olympians",
        "desc": "Wielder of the lightning bolt."
      },
      {
        "name": "Prometheus",
        "role": "Titan Friend of Man",
        "desc": "Suffered eternal torment for gifting fire."
      },
      {
        "name": "Pandora",
        "role": "First Woman",
        "desc": "Curiosity released troubles and preserved Hope."
      }
    ],
    "themes": [
      "Cosmic Order",
      "Origin of Suffering",
      "Hope as Anchor"
    ],
    "echoes": "Pandora parallels Eve in Genesis; Prometheus parallels Lucifer/Loki.",
    "famousQuote": "“Only Hope remained within under the rim of the great jar.” — Hesiod",
    "historicalContext": "Established ancient Greece's foundational religious and theological system."
  },
  {
    "id": "aesop-fables",
    "year": -600,
    "displayDate": "c. 600 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Thrace & Delphi, Greece",
    "author": "Aesop (Freed Storyteller & Fabulist)",
    "title": "Aesop's Fables: The Tortoise and the Hare, The Boy Who Cried Wolf",
    "subtitle": "Animal Wisdom and Moral Truths That Outlasted Empires",
    "summary": "Aesop, an enslaved Greek fabulist who won freedom through wit, crafts timeless moral tales showing that steady perseverance overcomes arrogant speed and honesty protects communities.",
    "fullStory": "### Act I: The Tortoise and the Hare\nThe swift Hare mocked the slow Tortoise. Challenged to a race, the overconfident Hare fell asleep under a tree while the steady Tortoise crossed the finish line.\n\n### Act II: The Boy Who Cried Wolf\nA bored shepherd boy repeatedly tricked villagers by shouting 'Wolf!' When a real wolf emerged from the forest, no one believed his cries.",
    "characters": [
      {
        "name": "The Tortoise & Hare",
        "role": "Fable Archetypes",
        "desc": "Proof that slow and steady wins the race."
      },
      {
        "name": "The Shepherd Boy",
        "role": "Tragic Liar",
        "desc": "Learned the cost of broken trust."
      }
    ],
    "themes": [
      "Moral Integrity",
      "Perseverance over Hubris",
      "Practical Wisdom"
    ],
    "echoes": "Parallels Indian Panchatantra and West African Anansi fables.",
    "famousQuote": "“Slow and steady wins the race; no one believes a liar even when he speaks the truth.” — Aesop",
    "historicalContext": "Preserved orally and collected by Demetrius of Phalerum around 300 BCE."
  },
  {
    "id": "raven-steals-sun",
    "year": -500,
    "displayDate": "c. 500 BCE",
    "era": "classical",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Pacific Northwest Coast (Haida / Tlingit)",
    "author": "Haida & Tlingit Elders",
    "title": "Raven Steals the Sun: Bringing Light to the World",
    "subtitle": "The Transformation into Pine Needle, the Box of Daylight, and the Eagle's Sky",
    "summary": "When the world was in total darkness, the trickster Raven discovers that a selfish old chief keeps the Sun, Moon, and Stars locked in nested cedar boxes. Raven shapeshifts into a pine needle, is born as the chief's grandson, and steals the light for humanity.",
    "fullStory": "### Act I: The World in Blackness\nMortals fished in pitch darkness, bumping into rocks in cold fog.\n\n### Act II: The Pine Needle\nRaven shapeshifted into a hemlock needle in the chief's daughter's drinking cup, being born as a spoiled infant grandson.\n\n### Act III: Opening the Nested Boxes\nRaven cried for the shiny cedar boxes. As soon as the sun was handed to him, he transformed back into Raven and flew up the smoke hole, casting the sun into the sky.",
    "characters": [
      {
        "name": "Raven (Yéil)",
        "role": "Trickster Creator",
        "desc": "Brought light, fire, and freshwater to humanity."
      }
    ],
    "themes": [
      "Trickster Heroism",
      "Liberation of Light",
      "Ingenuity"
    ],
    "echoes": "Parallels Prometheus stealing fire and Maui snaring the sun.",
    "famousQuote": "“Raven opened his wings, and the world was filled with golden dawn.”",
    "historicalContext": "Core oral tradition carved on Pacific Northwest cedar totem poles."
  },
  {
    "id": "medea",
    "year": -431,
    "displayDate": "c. 431 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Ancient Greek tragedy by Euripides",
    "author": "Classical Greece & Rome Tradition",
    "title": "Medea",
    "subtitle": "Ancient Greek tragedy by Euripides",
    "summary": "Medea is a tragedy based on a myth, written by the ancient Greek playwright Euripides. It was first performed in 431 BC as part of a trilogy, the other plays of which have not survived. Its plot centers on the actions of Medea, a former princess of the kingdom of Colchis and the wife of Jason. She finds her position in the world threatened as Jason leaves her for a princess of Corinth and takes vengeance on him by murdering his new wife, his new father-in-law, and her own two sons. She then escapes to Athens to start a new life.",
    "fullStory": "### Act I: The Awakening of Medea\nMedea is a tragedy based on a myth, written by the ancient Greek playwright Euripides. It was first performed in 431 BC as part of a trilogy, the other plays of which have not survived. Its plot centers on the actions of Medea, a former princess of the kingdom of Colchis and the wife of Jason. She finds her position in the world threatened as Jason leaves her for a princess of Corinth and takes vengeance on him by murdering his new wife, his new father-in-law, and her own two sons. She then escapes to Athens to start a new life.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Medea",
        "role": "Protagonist",
        "desc": "Ancient Greek tragedy by Euripides"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Medea endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "oedipus-rex",
    "year": -429,
    "displayDate": "c. 429 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Classical Athenian tragedy by Sophocles",
    "author": "Classical Greece & Rome Tradition",
    "title": "Oedipus Rex",
    "subtitle": "Classical Athenian tragedy by Sophocles",
    "summary": "Oedipus Rex, also known by its Greek title, Oedipus Tyrannus, or Oedipus the King, is an Athenian tragedy written by Sophocles. The play is thought to have been first performed c. 429 BC, although this is highly uncertain. Although the play won only second place at its initial performance, it was later considered by Aristotle to be one of the greatest Greek tragedies, and is now widely considered one of the greatest plays of Western literature, and the most famous of all Greek tragedies.",
    "fullStory": "### Act I: The Awakening of Oedipus Rex\nOedipus Rex, also known by its Greek title, Oedipus Tyrannus, or Oedipus the King, is an Athenian tragedy written by Sophocles. The play is thought to have been first performed c. 429 BC, although this is highly uncertain. Although the play won only second place at its initial performance, it was later considered by Aristotle to be one of the greatest Greek tragedies, and is now widely considered one of the greatest plays of Western literature, and the most famous of all Greek tragedies.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Oedipus Rex",
        "role": "Protagonist",
        "desc": "Classical Athenian tragedy by Sophocles"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Oedipus Rex endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "popol-vuh-maya",
    "year": -400,
    "displayDate": "c. 400 BCE – 1550 CE",
    "era": "classical",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Xibalba & Guatemala Highlands",
    "author": "K'iche' Maya Scribes",
    "title": "Popol Vuh: The Hero Twins and the Lords of Death",
    "subtitle": "The Dark Houses of Xibalba, the Decapitation of One Hunahpu, and the Sun & Moon",
    "summary": "When the cruel Lords of Xibalba murder their father, the Hero Twins Hunahpu and Xbalanque descend into the underworld, outwitting razor rooms, bat houses, and ballgames to conquer death and rise as the Sun and Moon.",
    "fullStory": "### Act I: The Failed Creations\nThe gods try making animals, mud people, and wooden mannequins, destroying them when they lack souls.\n\n### Act II: The Underworld Trials\nThe Hero Twins descend to Xibalba, surviving the Dark House, Razor House, Cold House, and Bat House.\n\n### Act III: The Final Trick\nResurrecting as magical dancers, they trick the death lords into asking to be sacrificed and leave them dead, rising into the heavens as the Sun and Moon.",
    "characters": [
      {
        "name": "Hunahpu & Xbalanque",
        "role": "Hero Twins",
        "desc": "Demigod tricksters who conquered the underworld."
      },
      {
        "name": "One Death & Seven Death",
        "role": "Lords of Xibalba",
        "desc": "Underworld rulers of decay."
      }
    ],
    "themes": [
      "Triumph of Intellect over Death",
      "Rebirth through Sacrifice",
      "Maize People"
    ],
    "echoes": "Katabasis descent matches Orpheus and Inanna.",
    "famousQuote": "“Here we shall write the ancient word of the beginning...” — Popol Vuh",
    "historicalContext": "The sacred book of the K'iche' Maya preserved in Guatemala."
  },
  {
    "id": "cupid-and-psyche",
    "year": -350,
    "displayDate": "c. 350 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Classical story of Cupid and Psyche",
    "author": "Classical Greece & Rome Tradition",
    "title": "Cupid and Psyche",
    "subtitle": "Classical story of Cupid and Psyche",
    "summary": "Cupid and Psyche is a story originally from Metamorphoses, written in the 2nd century AD by Lucius Apuleius Madaurensis. The tale concerns the overcoming of obstacles to the love between Psyche and Cupid or Amor, and their ultimate union in a sacred marriage. Although the only extended narrative from antiquity is that of Apuleius from the 2nd century AD, Eros and Psyche appear in Greek art as early as the 4th century BC. The story's Neoplatonic elements and allusions to mystery religions accommodate multiple interpretations, and it has been analyzed as an allegory and in light of folktale, Märchen or fairy tale, and myth.",
    "fullStory": "### Act I: The Awakening of Cupid and Psyche\nCupid and Psyche is a story originally from Metamorphoses, written in the 2nd century AD by Lucius Apuleius Madaurensis. The tale concerns the overcoming of obstacles to the love between Psyche and Cupid or Amor, and their ultimate union in a sacred marriage. Although the only extended narrative from antiquity is that of Apuleius from the 2nd century AD, Eros and Psyche appear in Greek art as early as the 4th century BC. The story's Neoplatonic elements and allusions to mystery religions accommodate multiple interpretations, and it has been analyzed as an allegory and in light of folktale, Märchen or fairy tale, and myth.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Cupid and Psyche",
        "role": "Protagonist",
        "desc": "Classical story of Cupid and Psyche"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Cupid and Psyche endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "panchatantra-fables",
    "year": -300,
    "displayDate": "c. 300 BCE",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Mahilaropya, Ancient India",
    "author": "Sage Vishnu Sharma",
    "title": "The Panchatantra: Animal Fables of Political Wisdom and Wit",
    "subtitle": "The Monkey and the Crocodile, the Lion and the Hare",
    "summary": "Sage Vishnu Sharma educates three foolish princes in statecraft (Niti) using animal fables showing that intellect, foresight, and wit always defeat brute strength.",
    "fullStory": "### Act I: The Princes' Education\nVishnu Sharma promised to teach the royal heirs statecraft in six months using interconnected fables.\n\n### Act II: The Monkey and the Crocodile\nA crocodile befriends a monkey who throws him sweet rose-apples. When the crocodile's wife demands the monkey's heart, the monkey tricks him by claiming he left his heart in a tree branch.\n\n### Act III: The Lion and the Clever Hare\nA tiny hare leads the arrogant lion Damanaka to a deep well, showing him his own reflection; the enraged lion leaps in to fight his shadow and drowns.",
    "characters": [
      {
        "name": "Vishnu Sharma",
        "role": "Sage Educator",
        "desc": "Pioneered educational animal allegories."
      },
      {
        "name": "Clever Monkey & Hare",
        "role": "Trickster Heroes",
        "desc": "Defeated predators through psychological wit."
      }
    ],
    "themes": [
      "Intellect over Brute Force",
      "Prudence in Friendship",
      "Political Realism"
    ],
    "echoes": "Direct ancestor to Aesop, Arabian Nights, and Kalila wa Dimna in the Islamic world.",
    "famousQuote": "“Intelligence is supreme power; for a tiny hare drowned the roaring lion in a well.”",
    "historicalContext": "Translated into Pahlavi, Arabic, Latin, and over 50 world languages by 1600."
  },
  {
    "id": "virgil-aeneid",
    "year": -19,
    "displayDate": "29 – 19 BCE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Troy, Carthage & Tiber Valley",
    "author": "Publius Vergilius Maro (Virgil)",
    "title": "The Aeneid: The Founding of the Roman Destiny",
    "subtitle": "Carrying Father from Burning Troy, Dido's Curse, and the Golden Bough",
    "summary": "Trojan prince Aeneas escapes burning Troy carrying his father Anchises. After a tragic love affair with Queen Dido of Carthage and descending to the Underworld, he reaches Italy to establish the lineage of Rome.",
    "fullStory": "### Act I: Escape from Troy\nAeneas flees burning Troy carrying his crippled father and leading his young son.\n\n### Act II: The Curse of Dido\nIn Carthage, Dido falls passionately in love. When Jupiter commands Aeneas to depart for Italy, Dido stabs herself on a pyre, cursing Rome with eternal enmity.\n\n### Act III: The Underworld and Rome's Future\nGuided by the Sibyl with the Golden Bough, Aeneas visits the underworld, where Anchises reveals the future heroes: Romulus, Caesar, and Augustus.",
    "characters": [
      {
        "name": "Aeneas",
        "role": "Father of Rome",
        "desc": "Embodiment of duty to gods and nation (Pietas)."
      },
      {
        "name": "Dido",
        "role": "Queen of Carthage",
        "desc": "Tragic queen whose dying curse foretold Hannibal."
      }
    ],
    "themes": [
      "Duty (Pietas) over Passion",
      "Imperial Destiny",
      "Cost of Civilization"
    ],
    "echoes": "Blends the wanderings of the Odyssey with the warfare of the Iliad.",
    "famousQuote": "“Roman, remember by your strength to rule Earth's peoples: to impose peace, spare the defeated, and crush the proud.”",
    "historicalContext": "Commissioned by Augustus Caesar to provide Rome with a divine founding epic."
  },
  {
    "id": "ovid-metamorphoses",
    "year": 8,
    "displayDate": "c. 8 CE",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Rome & Mount Parnassus",
    "author": "Publius Ovidius Naso (Ovid)",
    "title": "Metamorphoses: Tales of Transformation (Daedalus & Icarus, Orpheus)",
    "subtitle": "The Wax Wings, Apollo and Daphne, and the Descent to the Underworld",
    "summary": "Ovid's 15-book epic catalog of mythological transformations: Daedalus crafting wax wings for Icarus, Apollo chasing Daphne who becomes a laurel tree, and Orpheus charming Hades with his lyre.",
    "fullStory": "### Act I: Daedalus and Icarus\nTrapped in the Cretan labyrinth, Daedalus fashioned wings of feathers and wax. Young Icarus flew too close to the sun; the wax melted, and he plunged into the Aegean Sea.\n\n### Act II: Apollo and Daphne\nStruck by Cupid's golden arrow, Apollo chased the nymph Daphne, who prayed to her river-god father and transformed into the sacred laurel tree.\n\n### Act III: Orpheus and Eurydice\nWhen viper venom killed his bride Eurydice, Orpheus descended to the underworld, charming Hades with his golden lyre. Granted her return under the condition he not look back, Orpheus glanced behind at the threshold, watching Eurydice vanish forever.",
    "characters": [
      {
        "name": "Orpheus",
        "role": "Master Musician",
        "desc": "Could charm trees and stones with his lyre."
      },
      {
        "name": "Icarus",
        "role": "Youth of Tragic Hubris",
        "desc": "Flew too close to the sun on wax wings."
      }
    ],
    "themes": [
      "Transformation (Mutatas Formas)",
      "Limits of Human Ambition",
      "Love and Loss"
    ],
    "echoes": "Orpheus's descent matches Izanagi in Japan and Gilgamesh crossing the deep.",
    "famousQuote": "“My intention is to tell of bodies changed into new forms... Let my song run continuous from the world's dawn to my own times.”",
    "historicalContext": "The single most influential sourcebook of classical myth for Renaissance painters and poets."
  },
  {
    "id": "kalidasa-shakuntala",
    "year": 400,
    "displayDate": "c. 400 CE",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Kanva's Hermitage & Hastinapura",
    "author": "Mahakavi Kalidasa",
    "title": "Abhijnanashakuntala: The Recognition of Shakuntala",
    "subtitle": "The Forest Hermitage, the Sage's Curse, the Lost Signet Ring, and Emperor Bharata",
    "summary": "King Dushyanta marries forest maiden Shakuntala. An angry sage's curse causes the king to forget her completely until a fisherman recovers a lost signet ring from the belly of a carp.",
    "fullStory": "### Act I: Love in the Sacred Grove\nDushyanta meets Shakuntala in sage Kanva's forest hermitage, exchanging signet rings.\n\n### Act II: Durvasa's Curse\nPreoccupied with love, Shakuntala ignores Sage Durvasa, who curses Dushyanta to forget her until he sees his ring.\n\n### Act III: The Lost Ring and Rejection\nThe ring slips into a river; Dushyanta coldly rejects a pregnant Shakuntala in court.\n\n### Act IV: The Fisherman and Lion Prince\nA fisherman finds the ring inside a fish. Dushyanta's memory returns in agonizing grief, culminating in finding Shakuntala and their lion-taming son Bharata.",
    "characters": [
      {
        "name": "Shakuntala",
        "role": "Forest Maiden",
        "desc": "Daughter of nymph Menaka who bore the founder of India."
      },
      {
        "name": "Dushyanta",
        "role": "Monarch of Hastinapura",
        "desc": "Overcame the curse of oblivion."
      }
    ],
    "themes": [
      "Romantic Separation (Vipralambha)",
      "Fate vs Memory",
      "Nature vs Court"
    ],
    "echoes": "Ring in fish matches Polycrates' ring in Herodotus.",
    "famousQuote": "“I name thee Shakuntala, and all at once is said!” — Goethe on reading Kalidasa",
    "historicalContext": "Pinnacle of Gupta Sanskrit drama; celebrated by European Romantic poets."
  },
  {
    "id": "heracles",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Divine hero in Greek mythology",
    "author": "Classical Greece & Rome Tradition",
    "title": "Heracles",
    "subtitle": "Divine hero in Greek mythology",
    "summary": "Heracles, born Alcaeus or Alcides, was a divine hero in Greek mythology, the son of Zeus and Alcmene, and the foster son of Amphitryon. He was a descendant of Perseus, another son of Zeus.",
    "fullStory": "### Act I: The Awakening of Heracles\nHeracles, born Alcaeus or Alcides, was a divine hero in Greek mythology, the son of Zeus and Alcmene, and the foster son of Amphitryon. He was a descendant of Perseus, another son of Zeus.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Heracles",
        "role": "Protagonist",
        "desc": "Divine hero in Greek mythology"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Heracles endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "jason-and-the-argonauts",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Topics referred to by the same term",
    "author": "Classical Greece & Rome Tradition",
    "title": "Jason and the Argonauts",
    "subtitle": "Topics referred to by the same term",
    "summary": "Jason and the Argonauts are characters from Greek mythology. This title may also refer to:Jason and the Argonauts (film), a 1963 film directed by Don Chaffey with animation by Ray Harryhausen\nJason and the Argonauts (miniseries), a two-part TV movie made in 2000\n\"Jason and the Argonauts\", a song by British pop group XTC on the 1982 album English Settlement\nJason and the Argonauts, a 1913 play by Bertha Newberry",
    "fullStory": "### Act I: The Awakening of Jason and the Argonauts\nJason and the Argonauts are characters from Greek mythology. This title may also refer to:Jason and the Argonauts (film), a 1963 film directed by Don Chaffey with animation by Ray Harryhausen\nJason and the Argonauts (miniseries), a two-part TV movie made in 2000\n\"Jason and the Argonauts\", a song by British pop group XTC on the 1982 album English Settlement\nJason and the Argonauts, a 1913 play by Bertha Newberry\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Jason and the Argonauts",
        "role": "Protagonist",
        "desc": "Topics referred to by the same term"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Jason and the Argonauts endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "perseus",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Ancient Greek hero and founder of Mycenae",
    "author": "Classical Greece & Rome Tradition",
    "title": "Perseus",
    "subtitle": "Ancient Greek hero and founder of Mycenae",
    "summary": "In Greek mythology, Perseus is the legendary founder of the Perseid dynasty. He was, alongside Cadmus and Bellerophon, the greatest Greek hero and slayer of monsters before the days of Heracles. He beheaded the Gorgon Medusa for Polydectes and saved Andromeda from the sea monster Cetus. He was a demigod, being the son of Zeus and the mortal Danaë, as well as the half-brother and great-grandfather of Heracles.",
    "fullStory": "### Act I: The Awakening of Perseus\nIn Greek mythology, Perseus is the legendary founder of the Perseid dynasty. He was, alongside Cadmus and Bellerophon, the greatest Greek hero and slayer of monsters before the days of Heracles. He beheaded the Gorgon Medusa for Polydectes and saved Andromeda from the sea monster Cetus. He was a demigod, being the son of Zeus and the mortal Danaë, as well as the half-brother and great-grandfather of Heracles.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Perseus",
        "role": "Protagonist",
        "desc": "Ancient Greek hero and founder of Mycenae"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Perseus endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "theseus-and-the-minotaur",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Legendary king of Athens who slayed the Minotaur",
    "author": "Classical Greece & Rome Tradition",
    "title": "Theseus and the Minotaur",
    "subtitle": "Legendary king of Athens who slayed the Minotaur",
    "summary": "Theseus was a divine hero in Greek mythology, famous for slaying the Minotaur. The myths surrounding Theseus, his journeys, exploits, and friends, have provided material for storytelling throughout the ages.",
    "fullStory": "### Act I: The Awakening of Theseus and the Minotaur\nTheseus was a divine hero in Greek mythology, famous for slaying the Minotaur. The myths surrounding Theseus, his journeys, exploits, and friends, have provided material for storytelling throughout the ages.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Theseus and the Minotaur",
        "role": "Protagonist",
        "desc": "Legendary king of Athens who slayed the Minotaur"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Theseus and the Minotaur endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "prometheus",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Figure in Greek mythology",
    "author": "Classical Greece & Rome Tradition",
    "title": "Prometheus",
    "subtitle": "Figure in Greek mythology",
    "summary": "In Greek mythology, Prometheus is a Titan responsible for creating or aiding humanity in its earliest days. He defied the Olympian gods by taking fire from them and giving it to humanity in the form of technology, knowledge and, more generally, civilization.",
    "fullStory": "### Act I: The Awakening of Prometheus\nIn Greek mythology, Prometheus is a Titan responsible for creating or aiding humanity in its earliest days. He defied the Olympian gods by taking fire from them and giving it to humanity in the form of technology, knowledge and, more generally, civilization.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Prometheus",
        "role": "Protagonist",
        "desc": "Figure in Greek mythology"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Prometheus endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "daedalus",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Greek mythological figure",
    "author": "Classical Greece & Rome Tradition",
    "title": "Daedalus",
    "subtitle": "Greek mythological figure",
    "summary": "In Greek mythology, Daedalus was a skillful architect and craftsman, seen as a symbol of wisdom, knowledge and power. He is the father of Icarus, the uncle of Perdix, and possibly also the father of Iapyx. Among his most famous creations are the wooden cow for Pasiphaë, the Labyrinth for King Minos of Crete which imprisoned the Minotaur, and wings that he and his son Icarus used to attempt to escape Crete. It was during this escape that Icarus did not listen to his father's warnings and flew too close to the Sun; the wax holding his wings together melted and Icarus fell to his death.",
    "fullStory": "### Act I: The Awakening of Daedalus\nIn Greek mythology, Daedalus was a skillful architect and craftsman, seen as a symbol of wisdom, knowledge and power. He is the father of Icarus, the uncle of Perdix, and possibly also the father of Iapyx. Among his most famous creations are the wooden cow for Pasiphaë, the Labyrinth for King Minos of Crete which imprisoned the Minotaur, and wings that he and his son Icarus used to attempt to escape Crete. It was during this escape that Icarus did not listen to his father's warnings and flew too close to the Sun; the wax holding his wings together melted and Icarus fell to his death.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Daedalus",
        "role": "Protagonist",
        "desc": "Greek mythological figure"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Daedalus endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "bellerophon",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Ancient Greek hero",
    "author": "Classical Greece & Rome Tradition",
    "title": "Bellerophon",
    "subtitle": "Ancient Greek hero",
    "summary": "Bellerophon or Bellerophontes or Hipponous, was a divine Corinthian hero of Greek mythology, the son of Poseidon and Eurynome, and the foster son of Glaukos. He was \"the greatest hero and slayer of monsters, alongside Cadmus and Perseus, before the days of Heracles\". Among his greatest feats was killing the Chimera of the Iliad, a monster that Homer depicted with a lion's head, a goat's body, and a serpent's tail: \"her breath came out in terrible blasts of burning flame.\"",
    "fullStory": "### Act I: The Awakening of Bellerophon\nBellerophon or Bellerophontes or Hipponous, was a divine Corinthian hero of Greek mythology, the son of Poseidon and Eurynome, and the foster son of Glaukos. He was \"the greatest hero and slayer of monsters, alongside Cadmus and Perseus, before the days of Heracles\". Among his greatest feats was killing the Chimera of the Iliad, a monster that Homer depicted with a lion's head, a goat's body, and a serpent's tail: \"her breath came out in terrible blasts of burning flame.\"\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Bellerophon",
        "role": "Protagonist",
        "desc": "Ancient Greek hero"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Bellerophon endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "adapa",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Mesopotamian mythical figure",
    "author": "Classical Mesopotamia & Near East Tradition",
    "title": "Adapa",
    "subtitle": "Mesopotamian mythical figure",
    "summary": "Adapa was a Mesopotamian mythical figure who unknowingly refused the gift of immortality. The story, commonly known as \"Adapa and the South Wind\", is known from fragmentary tablets from Tell el-Amarna in Egypt and from finds from the Library of Ashurbanipal, Assyria. The oldest tradition about him is from Me-Turan/Tell Haddad tablets, which is written in Sumerian.",
    "fullStory": "### Act I: The Awakening of Adapa\nAdapa was a Mesopotamian mythical figure who unknowingly refused the gift of immortality. The story, commonly known as \"Adapa and the South Wind\", is known from fragmentary tablets from Tell el-Amarna in Egypt and from finds from the Library of Ashurbanipal, Assyria. The oldest tradition about him is from Me-Turan/Tell Haddad tablets, which is written in Sumerian.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Adapa",
        "role": "Protagonist",
        "desc": "Mesopotamian mythical figure"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Mesopotamia & Near East.",
    "famousQuote": "“The memory of Adapa endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "etana",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Ancient Mesopotamian king",
    "author": "Classical Mesopotamia & Near East Tradition",
    "title": "Etana",
    "subtitle": "Ancient Mesopotamian king",
    "summary": "Etana was the thirteenth king of the first dynasty of Kish, according to the Sumerian King List. He is listed as the successor of Arwium, the son of Mashda, as king of Kish. The list also calls Etana \"the shepherd, who ascended to heaven and consolidated all the foreign countries\", and states that he ruled 1,500 years before being succeeded by his son Balih, said to have ruled 400 years. The kings on the early part of the SKL are usually not considered historical, except when they are mentioned in contemporary Early Dynastic documents. Etana is one of them.",
    "fullStory": "### Act I: The Awakening of Etana\nEtana was the thirteenth king of the first dynasty of Kish, according to the Sumerian King List. He is listed as the successor of Arwium, the son of Mashda, as king of Kish. The list also calls Etana \"the shepherd, who ascended to heaven and consolidated all the foreign countries\", and states that he ruled 1,500 years before being succeeded by his son Balih, said to have ruled 400 years. The kings on the early part of the SKL are usually not considered historical, except when they are mentioned in contemporary Early Dynastic documents. Etana is one of them.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Etana",
        "role": "Protagonist",
        "desc": "Ancient Mesopotamian king"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Mesopotamia & Near East.",
    "famousQuote": "“The memory of Etana endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "lugalbanda",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Sumerian mythical King",
    "author": "Classical Mesopotamia & Near East Tradition",
    "title": "Lugalbanda",
    "subtitle": "Sumerian mythical King",
    "summary": "Lugalbanda was a deified Sumerian king of Uruk who, according to various sources of Mesopotamian literature, was the father of Gilgamesh. Early sources mention his consort Ninsun and his heroic deeds in an expedition to Aratta by King Enmerkar.",
    "fullStory": "### Act I: The Awakening of Lugalbanda\nLugalbanda was a deified Sumerian king of Uruk who, according to various sources of Mesopotamian literature, was the father of Gilgamesh. Early sources mention his consort Ninsun and his heroic deeds in an expedition to Aratta by King Enmerkar.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Lugalbanda",
        "role": "Protagonist",
        "desc": "Sumerian mythical King"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Mesopotamia & Near East.",
    "famousQuote": "“The memory of Lugalbanda endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "enmerkar-and-the-lord-of-aratta",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Text in Sumerian epic mythology",
    "author": "Classical Mesopotamia & Near East Tradition",
    "title": "Enmerkar and the Lord of Aratta",
    "subtitle": "Text in Sumerian epic mythology",
    "summary": "Enmerkar and the Lord of Aratta is a legendary Sumerian account, preserved in early post-Sumerian copies, composed in the Neo-Sumerian period .\nIt is one of a series of accounts describing the conflicts between Enmerkar, king of Unug-Kulaba, and the unnamed king of Aratta.",
    "fullStory": "### Act I: The Awakening of Enmerkar and the Lord of Aratta\nEnmerkar and the Lord of Aratta is a legendary Sumerian account, preserved in early post-Sumerian copies, composed in the Neo-Sumerian period .\nIt is one of a series of accounts describing the conflicts between Enmerkar, king of Unug-Kulaba, and the unnamed king of Aratta.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Enmerkar and the Lord of Aratta",
        "role": "Protagonist",
        "desc": "Text in Sumerian epic mythology"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Mesopotamia & Near East.",
    "famousQuote": "“The memory of Enmerkar and the Lord of Aratta endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "anz",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Ancient Mesopotamian deity",
    "author": "Classical Mesopotamia & Near East Tradition",
    "title": "Anzû",
    "subtitle": "Ancient Mesopotamian deity",
    "summary": "Anzû, also known as dZû and Imdugud, is a demon in several Mesopotamian religions. He was conceived by the cosmic freshwater ocean Abzu and mother Earth Mami, or as son of Siris. In Babylonian myths Anzû was depicted as a massive bird - also as an eagle with lion head - who can breathe fire and water. This narrative seems to refer to much earlier Sumerian myths, in which he appears as a half-human storm bird who stole the tablet of destiny, challenging Enlil's power over his organisation of different gods that provided Mesopotamia with agriculture.",
    "fullStory": "### Act I: The Awakening of Anzû\nAnzû, also known as dZû and Imdugud, is a demon in several Mesopotamian religions. He was conceived by the cosmic freshwater ocean Abzu and mother Earth Mami, or as son of Siris. In Babylonian myths Anzû was depicted as a massive bird - also as an eagle with lion head - who can breathe fire and water. This narrative seems to refer to much earlier Sumerian myths, in which he appears as a half-human storm bird who stole the tablet of destiny, challenging Enlil's power over his organisation of different gods that provided Mesopotamia with agriculture.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Anzû",
        "role": "Protagonist",
        "desc": "Ancient Mesopotamian deity"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Mesopotamia & Near East.",
    "famousQuote": "“The memory of Anzû endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "tale-of-the-doomed-prince",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Ancient Egyptian literary text",
    "author": "Classical Ancient Egypt Tradition",
    "title": "Tale of the Doomed Prince",
    "subtitle": "Ancient Egyptian literary text",
    "summary": "The \"Tale of the Doomed Prince\" is an ancient Egyptian story, dating to the 18th dynasty, written in hieratic text, which survived partially on the verso of Papyrus Harris 500 currently housed in the British Museum. The papyrus was burned in an explosion; because of this damage the conclusion of the story is missing. Some scholars speculate that the missing ending was mostly likely a happy one and that the tale could be more aptly named \"The Prince who was Threatened by Three Fates\" or the like.",
    "fullStory": "### Act I: The Awakening of Tale of the Doomed Prince\nThe \"Tale of the Doomed Prince\" is an ancient Egyptian story, dating to the 18th dynasty, written in hieratic text, which survived partially on the verso of Papyrus Harris 500 currently housed in the British Museum. The papyrus was burned in an explosion; because of this damage the conclusion of the story is missing. Some scholars speculate that the missing ending was mostly likely a happy one and that the tale could be more aptly named \"The Prince who was Threatened by Three Fates\" or the like.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Tale of the Doomed Prince",
        "role": "Protagonist",
        "desc": "Ancient Egyptian literary text"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Ancient Egypt.",
    "famousQuote": "“The memory of Tale of the Doomed Prince endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "setne-khamwas-and-si-osire",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Demotic Egyptian story",
    "author": "Classical Ancient Egypt Tradition",
    "title": "Setne Khamwas and Si-Osire",
    "subtitle": "Demotic Egyptian story",
    "summary": "The Tale of Setne Khamwas and Si-Osire is a Demotic Egyptian story attested on papyrus in Roman Egypt. Some argue that it is an answer to the biblical account about the Queen of Sheba testing Solomon with hard \"questions\" in 1 Kings 10:1.",
    "fullStory": "### Act I: The Awakening of Setne Khamwas and Si-Osire\nThe Tale of Setne Khamwas and Si-Osire is a Demotic Egyptian story attested on papyrus in Roman Egypt. Some argue that it is an answer to the biblical account about the Queen of Sheba testing Solomon with hard \"questions\" in 1 Kings 10:1.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Setne Khamwas and Si-Osire",
        "role": "Protagonist",
        "desc": "Demotic Egyptian story"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Ancient Egypt.",
    "famousQuote": "“The memory of Setne Khamwas and Si-Osire endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "samudra-manthana",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Hindu legend",
    "author": "Classical India & South Asia Tradition",
    "title": "Samudra Manthana",
    "subtitle": "Hindu legend",
    "summary": "The Samudra Manthana is a major episode in Hinduism that is elaborated in the Vishnu Purana, a major text of Hinduism. The Samudra Manthana explains the origin of the elixir of eternal life, amrita.",
    "fullStory": "### Act I: The Awakening of Samudra Manthana\nThe Samudra Manthana is a major episode in Hinduism that is elaborated in the Vishnu Purana, a major text of Hinduism. The Samudra Manthana explains the origin of the elixir of eternal life, amrita.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Samudra Manthana",
        "role": "Protagonist",
        "desc": "Hindu legend"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across India & South Asia.",
    "famousQuote": "“The memory of Samudra Manthana endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "nala-and-damayanti",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Episode from the Indian epic Mahabharata",
    "author": "Classical India & South Asia Tradition",
    "title": "Nala and Damayanti",
    "subtitle": "Episode from the Indian epic Mahabharata",
    "summary": "Nala and Damayanti, also known as Nalopakhyana, is an episode from the Indian epic Mahabharata. It is about King Nala and his wife Damayanti: Nala loses his kingdom in a game of dice and has to go into exile with his faithful wife Damayanti in the forest, where he leaves her. Separated from each other, the two have many adventures before they are finally reunited and Nala regains his kingdom.",
    "fullStory": "### Act I: The Awakening of Nala and Damayanti\nNala and Damayanti, also known as Nalopakhyana, is an episode from the Indian epic Mahabharata. It is about King Nala and his wife Damayanti: Nala loses his kingdom in a game of dice and has to go into exile with his faithful wife Damayanti in the forest, where he leaves her. Separated from each other, the two have many adventures before they are finally reunited and Nala regains his kingdom.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Nala and Damayanti",
        "role": "Protagonist",
        "desc": "Episode from the Indian epic Mahabharata"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across India & South Asia.",
    "famousQuote": "“The memory of Nala and Damayanti endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "savitri-and-satyavan",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Episode in the Mahabharata",
    "author": "Classical India & South Asia Tradition",
    "title": "Savitri and Satyavan",
    "subtitle": "Episode in the Mahabharata",
    "summary": "Savitri and Satyavan, also called Sāvitrī-Upākhyāna and Pativrata-mahatmya Parva, is an episode from the Indian epic Mahabharata, appearing in the Vana Parva. It tells the story of Princess Savitri, who, through her intelligence and devotion, overcomes a divine prophecy foretelling her husband Satyavan's early death. This episode is a significant literary and religious text in Hindu tradition, emphasizing themes of the power of speech, the tensions between dharma and moksha, and Vedic symbolism associated with the goddess Savitri and the Gayatri Mantra. Scholars dispute whether the story emphasizes marital fidelity or personal autonomy. Scholars have additionally compared it to several stories from other cultures, such as of Alcestis, Orpheus and Eurydice, and Laodamia and Protesilaus.",
    "fullStory": "### Act I: The Awakening of Savitri and Satyavan\nSavitri and Satyavan, also called Sāvitrī-Upākhyāna and Pativrata-mahatmya Parva, is an episode from the Indian epic Mahabharata, appearing in the Vana Parva. It tells the story of Princess Savitri, who, through her intelligence and devotion, overcomes a divine prophecy foretelling her husband Satyavan's early death. This episode is a significant literary and religious text in Hindu tradition, emphasizing themes of the power of speech, the tensions between dharma and moksha, and Vedic symbolism associated with the goddess Savitri and the Gayatri Mantra. Scholars dispute whether the story emphasizes marital fidelity or personal autonomy. Scholars have additionally compared it to several stories from other cultures, such as of Alcestis, Orpheus and Eurydice, and Laodamia and Protesilaus.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Savitri and Satyavan",
        "role": "Protagonist",
        "desc": "Episode in the Mahabharata"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across India & South Asia.",
    "famousQuote": "“The memory of Savitri and Satyavan endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "jataka-tales",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Traditional narratives of the previous lives of Buddha",
    "author": "Classical India & South Asia Tradition",
    "title": "Jataka tales",
    "subtitle": "Traditional narratives of the previous lives of Buddha",
    "summary": "The Jātaka are a voluminous body of literature native to the Indian subcontinent which mainly concern the previous births of Gautama Buddha in both human and animal form. Jataka stories were depicted on the railings and torans of the stupas. According to Peter Skilling, this genre is \"one of the oldest classes of Buddhist literature.\" Some of these texts are also considered great works of literature in their own right. The various Indian Buddhist schools had different collections of jātakas. The largest known collection is the Jātakatthavaṇṇanā of the Theravada school, as a textual division of the Pāli Canon, included in the Khuddaka Nikaya of the Sutta Pitaka.",
    "fullStory": "### Act I: The Awakening of Jataka tales\nThe Jātaka are a voluminous body of literature native to the Indian subcontinent which mainly concern the previous births of Gautama Buddha in both human and animal form. Jataka stories were depicted on the railings and torans of the stupas. According to Peter Skilling, this genre is \"one of the oldest classes of Buddhist literature.\" Some of these texts are also considered great works of literature in their own right. The various Indian Buddhist schools had different collections of jātakas. The largest known collection is the Jātakatthavaṇṇanā of the Theravada school, as a textual division of the Pāli Canon, included in the Khuddaka Nikaya of the Sutta Pitaka.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Jataka tales",
        "role": "Protagonist",
        "desc": "Traditional narratives of the previous lives of Buddha"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across India & South Asia.",
    "famousQuote": "“The memory of Jataka tales endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "baital-pachisi",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Collection of Indian tales",
    "author": "Classical India & South Asia Tradition",
    "title": "Baital Pachisi",
    "subtitle": "Collection of Indian tales",
    "summary": "The Vetala Panchavimshati, or Betal Pachisi, is a collection of tales and legends within a frame story, from India. Internationally, it is also known as Vikram-Vetala. It was originally written in Sanskrit.",
    "fullStory": "### Act I: The Awakening of Baital Pachisi\nThe Vetala Panchavimshati, or Betal Pachisi, is a collection of tales and legends within a frame story, from India. Internationally, it is also known as Vikram-Vetala. It was originally written in Sanskrit.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Baital Pachisi",
        "role": "Protagonist",
        "desc": "Collection of Indian tales"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across India & South Asia.",
    "famousQuote": "“The memory of Baital Pachisi endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "hitopadesha",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Medieval era Sanskrit text with human and animal fables",
    "author": "Classical India & South Asia Tradition",
    "title": "Hitopadesha",
    "subtitle": "Medieval era Sanskrit text with human and animal fables",
    "summary": "Hitopadesha is an Indian text in the Sanskrit language consisting of fables with both human and animal characters. It incorporates maxims, worldly wisdom and advice on political affairs in simple, elegant language, and the work has been widely translated.",
    "fullStory": "### Act I: The Awakening of Hitopadesha\nHitopadesha is an Indian text in the Sanskrit language consisting of fables with both human and animal characters. It incorporates maxims, worldly wisdom and advice on political affairs in simple, elegant language, and the work has been widely translated.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Hitopadesha",
        "role": "Protagonist",
        "desc": "Medieval era Sanskrit text with human and animal fables"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across India & South Asia.",
    "famousQuote": "“The memory of Hitopadesha endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "yu-the-great",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Xia Dynasty king and founder",
    "author": "Classical China & East Asia Tradition",
    "title": "Yu the Great",
    "subtitle": "Xia Dynasty king and founder",
    "summary": "Yu the Great or Yu the Engineer was a legendary king in ancient China who was credited with \"the first successful state efforts at flood control\", his establishment of the Xia dynasty, which inaugurated dynastic rule in China, and for his upright moral character. He figures prominently in the Chinese legend titled \"Great Yu Controls the Waters\". Yu and other sage-kings of ancient China were lauded for their virtues and morals by Confucius and other Chinese teachers. He is one of the few Chinese monarchs who is posthumously honored with the epithet \"the Great\".",
    "fullStory": "### Act I: The Awakening of Yu the Great\nYu the Great or Yu the Engineer was a legendary king in ancient China who was credited with \"the first successful state efforts at flood control\", his establishment of the Xia dynasty, which inaugurated dynastic rule in China, and for his upright moral character. He figures prominently in the Chinese legend titled \"Great Yu Controls the Waters\". Yu and other sage-kings of ancient China were lauded for their virtues and morals by Confucius and other Chinese teachers. He is one of the few Chinese monarchs who is posthumously honored with the epithet \"the Great\".\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Yu the Great",
        "role": "Protagonist",
        "desc": "Xia Dynasty king and founder"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across China & East Asia.",
    "famousQuote": "“The memory of Yu the Great endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "legend-of-the-white-snake",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Chinese legend",
    "author": "Classical China & East Asia Tradition",
    "title": "Legend of the White Snake",
    "subtitle": "Chinese legend",
    "summary": "The Legend of the White Snake is a Chinese legend centered around a romance between a man named Xu Xian and a female snake spirit named Bai Suzhen. It is counted as one of China's Four Great Folktales, the others being Lady Meng Jiang, Butterfly Lovers, and The Cowherd and the Weaver Girl.",
    "fullStory": "### Act I: The Awakening of Legend of the White Snake\nThe Legend of the White Snake is a Chinese legend centered around a romance between a man named Xu Xian and a female snake spirit named Bai Suzhen. It is counted as one of China's Four Great Folktales, the others being Lady Meng Jiang, Butterfly Lovers, and The Cowherd and the Weaver Girl.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Legend of the White Snake",
        "role": "Protagonist",
        "desc": "Chinese legend"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across China & East Asia.",
    "famousQuote": "“The memory of Legend of the White Snake endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "butterfly-lovers",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Chinese legend",
    "author": "Classical China & East Asia Tradition",
    "title": "Butterfly Lovers",
    "subtitle": "Chinese legend",
    "summary": "The Butterfly Lovers is a Chinese legend centered around the tragic romance between Liang Shanbo (梁山伯) and Zhu Yingtai (祝英臺), whose names form the Chinese title of the story. The title is often abbreviated as Liang Zhu (梁祝).",
    "fullStory": "### Act I: The Awakening of Butterfly Lovers\nThe Butterfly Lovers is a Chinese legend centered around the tragic romance between Liang Shanbo (梁山伯) and Zhu Yingtai (祝英臺), whose names form the Chinese title of the story. The title is often abbreviated as Liang Zhu (梁祝).\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Butterfly Lovers",
        "role": "Protagonist",
        "desc": "Chinese legend"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across China & East Asia.",
    "famousQuote": "“The memory of Butterfly Lovers endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "water-margin",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "One of the Chinese Classic Novels",
    "author": "Classical China & East Asia Tradition",
    "title": "Water Margin",
    "subtitle": "One of the Chinese Classic Novels",
    "summary": "Water Margin, also called Outlaws of the Marsh or All Men Are Brothers, is a Chinese novel from the Ming dynasty that is one of the preeminent Classic Chinese Novels. Attributed to Shi Nai'an, Water Margin was one of the earliest Chinese novels written in vernacular Mandarin Chinese.",
    "fullStory": "### Act I: The Awakening of Water Margin\nWater Margin, also called Outlaws of the Marsh or All Men Are Brothers, is a Chinese novel from the Ming dynasty that is one of the preeminent Classic Chinese Novels. Attributed to Shi Nai'an, Water Margin was one of the earliest Chinese novels written in vernacular Mandarin Chinese.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Water Margin",
        "role": "Protagonist",
        "desc": "One of the Chinese Classic Novels"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across China & East Asia.",
    "famousQuote": "“The memory of Water Margin endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "dream-of-the-red-chamber",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Vernacular Chinese novel by Cao Xueqin",
    "author": "Classical China & East Asia Tradition",
    "title": "Dream of the Red Chamber",
    "subtitle": "Vernacular Chinese novel by Cao Xueqin",
    "summary": "Dream of the Red Chamber or The Story of the Stone is an 18th-century Chinese novel authored by Cao Xueqin, considered to be one of the Four Great Classic Novels of Chinese literature. It is known for its psychological scope and its observation of the worldview, aesthetics, lifestyles, and social relations of High Qing China.",
    "fullStory": "### Act I: The Awakening of Dream of the Red Chamber\nDream of the Red Chamber or The Story of the Stone is an 18th-century Chinese novel authored by Cao Xueqin, considered to be one of the Four Great Classic Novels of Chinese literature. It is known for its psychological scope and its observation of the worldview, aesthetics, lifestyles, and social relations of High Qing China.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Dream of the Red Chamber",
        "role": "Protagonist",
        "desc": "Vernacular Chinese novel by Cao Xueqin"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across China & East Asia.",
    "famousQuote": "“The memory of Dream of the Red Chamber endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "urashima-tar",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Protagonist of a Japanese fairy tale",
    "author": "Classical Japan & Korea Tradition",
    "title": "Urashima Tarō",
    "subtitle": "Protagonist of a Japanese fairy tale",
    "summary": "Urashima Tarō  is the protagonist of a Japanese fairy tale, who, in a typical modern version, is a fisherman rewarded for rescuing a sea turtle, and carried on its back to the Dragon Palace (Ryūgū-jō) beneath the sea. There, he is entertained by the princess Otohime as a reward. He spends what he believes to be several days with the princess. But when he returns to his home village, he discovers he has been gone for at least 100 years. When he opens the forbidden jewelled box (tamatebako), given to him by Otohime on his departure, he turns into an old man.",
    "fullStory": "### Act I: The Awakening of Urashima Tarō\nUrashima Tarō  is the protagonist of a Japanese fairy tale, who, in a typical modern version, is a fisherman rewarded for rescuing a sea turtle, and carried on its back to the Dragon Palace (Ryūgū-jō) beneath the sea. There, he is entertained by the princess Otohime as a reward. He spends what he believes to be several days with the princess. But when he returns to his home village, he discovers he has been gone for at least 100 years. When he opens the forbidden jewelled box (tamatebako), given to him by Otohime on his departure, he turns into an old man.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Urashima Tarō",
        "role": "Protagonist",
        "desc": "Protagonist of a Japanese fairy tale"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Japan & Korea.",
    "famousQuote": "“The memory of Urashima Tarō endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "momotar",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Popular hero of Japanese folklore",
    "author": "Classical Japan & Korea Tradition",
    "title": "Momotarō",
    "subtitle": "Popular hero of Japanese folklore",
    "summary": "Momotarō  is a popular hero of Japanese folklore. His name is often translated as Peach Boy, but is directly translated as Peach + Tarō, a common Japanese given name. Momotarō is also the title of various books, films and other works that portray the tale of this hero.",
    "fullStory": "### Act I: The Awakening of Momotarō\nMomotarō  is a popular hero of Japanese folklore. His name is often translated as Peach Boy, but is directly translated as Peach + Tarō, a common Japanese given name. Momotarō is also the title of various books, films and other works that portray the tale of this hero.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Momotarō",
        "role": "Protagonist",
        "desc": "Popular hero of Japanese folklore"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Japan & Korea.",
    "famousQuote": "“The memory of Momotarō endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "chunhyangjeon",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Korean folk tale",
    "author": "Classical Japan & Korea Tradition",
    "title": "Chunhyangjeon",
    "subtitle": "Korean folk tale",
    "summary": "Chunhyangjeon is one of the best known love stories and folk tales of Korea. It is based on the pansori Chunhyangga, the most famous of the five surviving pansori tales.",
    "fullStory": "### Act I: The Awakening of Chunhyangjeon\nChunhyangjeon is one of the best known love stories and folk tales of Korea. It is based on the pansori Chunhyangga, the most famous of the five surviving pansori tales.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Chunhyangjeon",
        "role": "Protagonist",
        "desc": "Korean folk tale"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Japan & Korea.",
    "famousQuote": "“The memory of Chunhyangjeon endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "white-buffalo-calf-woman",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Sacred woman of supernatural origin, central to the Lakota religion",
    "author": "Classical The Americas Tradition",
    "title": "White Buffalo Calf Woman",
    "subtitle": "Sacred woman of supernatural origin, central to the Lakota religion",
    "summary": "White Buffalo Calf Woman or White Buffalo Maiden is a sacred woman of supernatural origin, central to the Lakota religion as the primary cultural prophet. Oral traditions relate that she brought the \"Seven Sacred Rites\" to the Lakota people.",
    "fullStory": "### Act I: The Awakening of White Buffalo Calf Woman\nWhite Buffalo Calf Woman or White Buffalo Maiden is a sacred woman of supernatural origin, central to the Lakota religion as the primary cultural prophet. Oral traditions relate that she brought the \"Seven Sacred Rites\" to the Lakota people.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "White Buffalo Calf Woman",
        "role": "Protagonist",
        "desc": "Sacred woman of supernatural origin, central to the Lakota religion"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across The Americas.",
    "famousQuote": "“The memory of White Buffalo Calf Woman endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "sedna",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "Inuit water deity",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Sedna",
    "subtitle": "Inuit water deity",
    "summary": "Sedna is the goddess of the sea and marine animals in Inuit religion, also known as the Mother of the Sea or Mistress of the Sea. The story of Sedna, which is a creation myth, describes how she came to rule over Adlivun, the Inuit equivalent of the underworld. In sculptures, Sedna is often depicted with the head and upper body of a woman and the tail of a marine mammal, similar to a mermaid.",
    "fullStory": "### Act I: The Awakening of Sedna\nSedna is the goddess of the sea and marine animals in Inuit religion, also known as the Mother of the Sea or Mistress of the Sea. The story of Sedna, which is a creation myth, describes how she came to rule over Adlivun, the Inuit equivalent of the underworld. In sculptures, Sedna is often depicted with the head and upper body of a woman and the tail of a marine mammal, similar to a mermaid.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Sedna",
        "role": "Protagonist",
        "desc": "Inuit water deity"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Sedna endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "nanabozho",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Ojibwe trickster spirit often in the form of a rabbit",
    "author": "Classical The Americas Tradition",
    "title": "Nanabozho",
    "subtitle": "Ojibwe trickster spirit often in the form of a rabbit",
    "summary": "Nanabozho, also known as Nanabush, is a spirit in Anishinaabe aadizookaan, particularly among the Ojibwe of North America. Nanabozho figures prominently in their storytelling, including the story of the world's creation. Nanabozho is the Ojibwe trickster figure and culture hero.",
    "fullStory": "### Act I: The Awakening of Nanabozho\nNanabozho, also known as Nanabush, is a spirit in Anishinaabe aadizookaan, particularly among the Ojibwe of North America. Nanabozho figures prominently in their storytelling, including the story of the world's creation. Nanabozho is the Ojibwe trickster figure and culture hero.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Nanabozho",
        "role": "Protagonist",
        "desc": "Ojibwe trickster spirit often in the form of a rabbit"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across The Americas.",
    "famousQuote": "“The memory of Nanabozho endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "coyote",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "North American mythological character",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Coyote",
    "subtitle": "North American mythological character",
    "summary": "Coyote is a mythological character common to many cultures of the Indigenous peoples of North America, based on the coyote animal. This character is usually male and is generally anthropomorphic, although he may have some coyote-like physical features such as fur, pointed ears, yellow eyes, a tail and blunt claws. The myths and legends which include Coyote vary widely from culture to culture.",
    "fullStory": "### Act I: The Awakening of Coyote\nCoyote is a mythological character common to many cultures of the Indigenous peoples of North America, based on the coyote animal. This character is usually male and is generally anthropomorphic, although he may have some coyote-like physical features such as fur, pointed ears, yellow eyes, a tail and blunt claws. The myths and legends which include Coyote vary widely from culture to culture.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Coyote",
        "role": "Protagonist",
        "desc": "North American mythological character"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Coyote endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "mwindo-epic",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "Oral tale from the Congo told by the Nyanga people",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Mwindo epic",
    "subtitle": "Oral tale from the Congo told by the Nyanga people",
    "summary": "The Mwindo epic is an oral tale from the Congo told by the Nyanga people. The origins and creation of the Mwindo epic are mostly unknown since the story is only passed down orally. A version of the story was recorded by Kahombo Mateene and Daniel Biebuyck and published in 1969.",
    "fullStory": "### Act I: The Awakening of Mwindo epic\nThe Mwindo epic is an oral tale from the Congo told by the Nyanga people. The origins and creation of the Mwindo epic are mostly unknown since the story is only passed down orally. A version of the story was recorded by Kahombo Mateene and Daniel Biebuyck and published in 1969.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Mwindo epic",
        "role": "Protagonist",
        "desc": "Oral tale from the Congo told by the Nyanga people"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Mwindo epic endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "children-of-lir",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Legend from Irish mythology",
    "author": "Classical Northern & Celtic Europe Tradition",
    "title": "Children of Lir",
    "subtitle": "Legend from Irish mythology",
    "summary": "The Children of Lir is a legend from Irish mythology. It is a tale from the post-Christianisation period that mixes magical elements such as wands and spells with a Christian message of faith bringing freedom from suffering.",
    "fullStory": "### Act I: The Awakening of Children of Lir\nThe Children of Lir is a legend from Irish mythology. It is a tale from the post-Christianisation period that mixes magical elements such as wands and spells with a Christian message of faith bringing freedom from suffering.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Children of Lir",
        "role": "Protagonist",
        "desc": "Legend from Irish mythology"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Northern & Celtic Europe.",
    "famousQuote": "“The memory of Children of Lir endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "c-chulainn",
    "year": 500,
    "displayDate": "c. 500 CE",
    "era": "medieval",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Irish mythological hero",
    "author": "Classical The Americas Tradition",
    "title": "Cú Chulainn",
    "subtitle": "Irish mythological hero",
    "summary": "Cú Chulainn, is an Irish warrior hero and demigod in the Ulster Cycle of Irish mythology, as well as in Scottish and Manx folklore. He is believed to be an incarnation of the Irish god Lugh, who is also his father. His mother is the mortal Deichtine, sister of King Conchobar mac Nessa.",
    "fullStory": "### Act I: The Awakening of Cú Chulainn\nCú Chulainn, is an Irish warrior hero and demigod in the Ulster Cycle of Irish mythology, as well as in Scottish and Manx folklore. He is believed to be an incarnation of the Irish god Lugh, who is also his father. His mother is the mortal Deichtine, sister of King Conchobar mac Nessa.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Cú Chulainn",
        "role": "Protagonist",
        "desc": "Irish mythological hero"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across The Americas.",
    "famousQuote": "“The memory of Cú Chulainn endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "irish-tain-cuchulainn",
    "year": 700,
    "displayDate": "c. 700 – 1100 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Ulster & Cooley Peninsula, Ireland",
    "author": "Irish Monastic Scribes & Filí (Bards)",
    "title": "Táin Bó Cúailnge: The Cattle Raid of Cooley & Cú Chulainn",
    "subtitle": "The Pillow Talk of Queen Medb, the Warp-Spasm, and the Ford of Ardee",
    "summary": "Queen Medb invades Ulster to seize the Donn Cúailnge bull. With Ulster warriors paralyzed by a birth-pang curse, 17-year-old demigod Cú Chulainn defends the borders alone in single-combat river duels.",
    "fullStory": "### Act I: The Pillow Talk\nQueen Medb demands the Brown Bull of Cooley to equal her husband's wealth, rallying Ireland to war.\n\n### Act II: The Boy at the Ford\nCú Chulainn holds the river fords alone through the terrifying Warp-Spasm (Ríastrad) battle frenzy.\n\n### Act III: The Duel with Ferdiad\nForced to fight his soul-brother Ferdiad, Cú Chulainn weeps as his barbed spear Gáe Bulg takes his friend's life.",
    "characters": [
      {
        "name": "Cú Chulainn",
        "role": "Hound of Ulster",
        "desc": "Son of sun god Lugh."
      },
      {
        "name": "Queen Medb",
        "role": "Sovereign of Connacht",
        "desc": "Ambitious warlord queen."
      }
    ],
    "themes": [
      "Warrior Honor (Geas)",
      "Tragedy of Fratricide"
    ],
    "echoes": "Grief over Ferdiad mirrors Achilles weeping for Patroclus and Rostam for Sohrab.",
    "famousQuote": "“I care not if I live but a single day, so long as my deeds live forever!” — Cú Chulainn",
    "historicalContext": "Preserved in the 12th-century Book of Leinster."
  },
  {
    "id": "pandora-s-box",
    "year": 700,
    "displayDate": "c. 700 CE",
    "era": "medieval",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Greek mythological artefact",
    "author": "Classical Greece & Rome Tradition",
    "title": "Pandora's box",
    "subtitle": "Greek mythological artefact",
    "summary": "Pandora's box is an artefact in Greek mythology connected with the myth of Pandora in Hesiod's c. 700 B.C. poem Works and Days. Hesiod related that curiosity led her to open a container left in the care of her husband, thus releasing curses upon mankind. Later depictions of the story have been varied, with some literary and artistic treatments focusing more on the contents than on Pandora herself.",
    "fullStory": "### Act I: The Awakening of Pandora's box\nPandora's box is an artefact in Greek mythology connected with the myth of Pandora in Hesiod's c. 700 B.C. poem Works and Days. Hesiod related that curiosity led her to open a container left in the care of her husband, thus releasing curses upon mankind. Later depictions of the story have been varied, with some literary and artistic treatments focusing more on the contents than on Pandora herself.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Pandora's box",
        "role": "Protagonist",
        "desc": "Greek mythological artefact"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Pandora's box endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "shinto-amaterasu",
    "year": 712,
    "displayDate": "c. 712 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Takamagahara & Ama-no-Iwato",
    "author": "Ō no Yasumaro & Hieda no Are (Kojiki)",
    "title": "Kojiki: Amaterasu and the Heavenly Rock Cave",
    "subtitle": "The Jeweled Spear, Susanoo's Tempest, and the Dance That Restored the Sun",
    "summary": "When the storm god Susanoo rampages in Heaven, his sister Amaterasu, the Sun Goddess, hides inside the Heavenly Rock Cave, plunging the world into darkness until a comic dance coaxes her out with a bronze mirror.",
    "fullStory": "### Act I: The Jeweled Spear\nIzanagi and Izanami stir the ocean with a jeweled spear, birthing Japan.\n\n### Act II: The Cave of Darkness\nSusanoo flays a heavenly horse into Amaterasu's weaving hall. Deeply offended, Amaterasu retreats into the Rock Cave, plunging heaven into night.\n\n### Act III: Uzume's Dance\nGoddess Uzume performs an energetic, funny dance on an upturned tub, making eight million gods roar with laughter. Curious, Amaterasu peeks out and sees her radiant reflection in the bronze mirror.",
    "characters": [
      {
        "name": "Amaterasu-ōmikami",
        "role": "Sun Goddess",
        "desc": "Ruler of Heaven and imperial ancestor."
      },
      {
        "name": "Susanoo",
        "role": "Storm God",
        "desc": "Wild brother who slew the 8-headed dragon."
      },
      {
        "name": "Ame-no-Uzume",
        "role": "Goddess of Mirth",
        "desc": "Brought the sun back with laughter."
      }
    ],
    "themes": [
      "Shinto Purification (Misogi)",
      "Laughter over Despair",
      "The Three Sacred Regalia"
    ],
    "echoes": "Amaterasu's withdrawal mirrors Greek Demeter mourning Persephone.",
    "famousQuote": "“When Amaterasu stepped forth from the cave, heaven and earth were flooded with golden light.”",
    "historicalContext": "The sacred foundational mythology of Japan's Shinto religion and imperial line."
  },
  {
    "id": "beowulf-epic",
    "year": 750,
    "displayDate": "c. 750 – 1000 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Heorot (Denmark) & Geatland",
    "author": "Anonymous Anglo-Saxon Scop",
    "title": "Beowulf: The Monster in the Mist and the Dragon's Hoard",
    "subtitle": "Bare-Handed Duel with Grendel, the Mere of the Sea-Hag, and the Fire-Drake",
    "summary": "The Geatish hero Beowulf sails to Denmark to rid King Hrothgar's mead-hall Heorot of the cannibal monster Grendel and his mother, before dying in old age slaying a fire-breathing dragon.",
    "fullStory": "### Act I: The Mead-Hall Heorot\nGrendel haunts Heorot for 12 winters. Beowulf fights him bare-handed, ripping his arm from the socket.\n\n### Act II: The Boiling Mere\nBeowulf dives into the abyss, slaying Grendel's mother with an ancient giant-forged sword.\n\n### Act III: The Dragon's Barrow\nIn old age, Beowulf and loyal Wiglaf slay a treasure-guarding dragon, dying as the last true hero of the age.",
    "characters": [
      {
        "name": "Beowulf",
        "role": "Geatish Champion",
        "desc": "Possessed the strength of thirty men."
      },
      {
        "name": "Grendel",
        "role": "Fiend of the Fens",
        "desc": "Descended from the curse of Cain."
      }
    ],
    "themes": [
      "Heroic Code (Comitatus)",
      "Transience of Glory (Wyrd)"
    ],
    "echoes": "Direct inspiration for Tolkien's The Hobbit and Lord of the Rings.",
    "famousQuote": "“Fate often saves an undoomed man when his courage holds!” — Beowulf",
    "historicalContext": "Preserved in the Nowell Codex in the British Library."
  },
  {
    "id": "scheherazade-1001",
    "year": 850,
    "displayDate": "c. 850 – 1400 CE",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Baghdad, Cairo & Samarkand",
    "author": "Traditional Storytellers (Recorded by al-Jahshiyari)",
    "title": "One Thousand and One Nights: Scheherazade's 1,001 Tales",
    "subtitle": "The Magic Lamp, Sinbad's Voyages, and the Power of Story to Heal",
    "summary": "To halt King Shahryar's murderous cycle of executing new brides at dawn, the brilliant Scheherazade marries him, weaving nested tales of genies, sorcery, and voyages, pausing at cliffhangers to heal the king's heart.",
    "fullStory": "### Act I: The Wounded King\nBetrayed by his first queen, Shahryar executes a bride every dawn until Scheherazade volunteers to marry him.\n\n### Act II: The 1,001 Cliffhangers\nEach night she weaves tales of Aladdin, Sinbad, and Ali Baba, stopping at dawn mid-sentence.\n\n### Act III: The Redemption of Shahryar\nAfter 1,001 nights, the king confesses that her stories have purified his heart of hatred, granting her life and peace to the kingdom.",
    "characters": [
      {
        "name": "Scheherazade",
        "role": "Master Storyteller",
        "desc": "Saved thousands of lives through psychological insight and narrative."
      },
      {
        "name": "King Shahryar",
        "role": "Wounded Monarch",
        "desc": "Healed through 1,001 nights of literature."
      }
    ],
    "themes": [
      "Art as Salvation",
      "Healing Trauma",
      "Framed Storytelling"
    ],
    "echoes": "Inspired Chaucer's Canterbury Tales and Boccaccio's Decameron.",
    "famousQuote": "“Stories are the medicine of the afflicted heart.” — Scheherazade",
    "historicalContext": "Synthesizes Indian, Persian, and Arabic storytelling traditions along the Silk Road."
  },
  {
    "id": "princess-kaguya",
    "year": 900,
    "displayDate": "c. 900 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Bamboo Grove & Mount Fuji, Japan",
    "author": "Anonymous Heian Court Author",
    "title": "The Tale of the Bamboo Cutter (Princess Kaguya)",
    "subtitle": "The Shining Maiden in the Stalk, Five Impossible Tasks, and the Smoke of Mount Fuji",
    "summary": "An elderly bamboo cutter discovers a glowing miniature maiden inside a stalk of bamboo. Growing into radiant Princess Kaguya, she sets five impossible quests for royal suitors before returning to the Moon.",
    "fullStory": "### Act I: The Shining Stalk\nAn old bamboo cutter slices open a glowing stalk, finding a three-inch baby who grows into the luminous Princess Kaguya.\n\n### Act II: The Five Impossible Quests\nFive noble suitors seek her hand; she asks for the stone bowl of the Buddha, the jeweled branch of Horai, the fire-rat robe, the dragon's neck jewel, and the swallow's cowrie shell. All five fail.\n\n### Act III: The Robe of Feathers\nThe celestial host of the Moon descends on cloud-chariots. Donning a feather robe that erases mortal memories, Kaguya ascends to the heavens, leaving an elixir of immortality that the Emperor burns on the peak of Mount Fuji.",
    "characters": [
      {
        "name": "Princess Kaguya",
        "role": "Celestial Moon Maiden",
        "desc": "Exiled to earth before returning to the Moon."
      },
      {
        "name": "The Bamboo Cutter (Taketori no Okina)",
        "role": "Loving Foster Father",
        "desc": "Raised Kaguya with tenderness."
      }
    ],
    "themes": [
      "Celestial Purity vs Earthly Sorrow",
      "Transience of Beauty"
    ],
    "echoes": "Oldest surviving prose narrative (monogatari) in Japanese literature.",
    "famousQuote": "“Mount Fuji's smoke rises forever into the sky, carrying the eternal longing of the Emperor for the Moon Maiden.”",
    "historicalContext": "Often described as early proto-science-fiction in world literature."
  },
  {
    "id": "tale-of-the-bamboo-cutter",
    "year": 950,
    "displayDate": "c. 950 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Japanese fictional prose narrative and folktale",
    "author": "Classical Japan & Korea Tradition",
    "title": "Tale of the Bamboo Cutter",
    "subtitle": "Japanese fictional prose narrative and folktale",
    "summary": "The Tale of the Bamboo Cutter  is a monogatari containing elements of Japanese folklore. Written by an unknown author in the late 9th or early 10th century during the Heian period, it is considered the oldest surviving work in the monogatari form.",
    "fullStory": "### Act I: The Awakening of Tale of the Bamboo Cutter\nThe Tale of the Bamboo Cutter  is a monogatari containing elements of Japanese folklore. Written by an unknown author in the late 9th or early 10th century during the Heian period, it is considered the oldest surviving work in the monogatari form.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Tale of the Bamboo Cutter",
        "role": "Protagonist",
        "desc": "Japanese fictional prose narrative and folktale"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Japan & Korea.",
    "famousQuote": "“The memory of Tale of the Bamboo Cutter endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "maui-fish-islands",
    "year": 1000,
    "displayDate": "c. 1000 CE",
    "era": "medieval",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Aotearoa (New Zealand) & Polynesia",
    "author": "Polynesian Tohunga (Oral Navigators)",
    "title": "Māui Fishes up the North Island (Te Ika-a-Māui)",
    "subtitle": "The Magic Jawbone Hook and the Hauling of Aotearoa",
    "summary": "Using a magic fishhook carved from his grandmother’s jawbone and baited with his own blood, the trickster demigod Māui hauls the North Island of New Zealand up from the ocean abyss.",
    "fullStory": "### Act I: The Stowaway Brother\nMāui hid aboard his brothers' canoe until reaching deep ocean.\n\n### Act II: The Great Catch\nBaited with blood from his nose, his hook caught the sunken temple of Tonganui. Chanting karakia, he hauled up Te Ika-a-Māui.\n\n### Act III: The Mountains\nWhile Māui thanked the gods, his brothers greedily hacked at the fish, creating the rugged mountains of New Zealand.",
    "characters": [
      {
        "name": "Māui-tikitiki-a-Taranga",
        "role": "Demigod Trickster",
        "desc": "Hauled islands and slowed the sun."
      },
      {
        "name": "Murirangawhenua",
        "role": "Ancestral Grandmother",
        "desc": "Provided the enchanted jawbone hook."
      }
    ],
    "themes": [
      "Daring Feats",
      "Voyaging Spirit",
      "Oceanic Connection"
    ],
    "echoes": "Parallels Hercules lifting the Pillars and Krishna lifting Govardhan hill.",
    "famousQuote": "“The fish of Māui is our eternal home.” — Māori Proverb",
    "historicalContext": "Preserved across Pacific island navigators spanning 4,000 miles of open ocean."
  },
  {
    "id": "shahnameh-ferdowsi",
    "year": 1000,
    "displayDate": "c. 977 – 1010 CE",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Greater Iran, Sistan & Tus",
    "author": "Hakim Abul-Qasim Ferdowsi Tusi",
    "title": "Shahnameh: The Persian Book of Kings (Rostam and Sohrab)",
    "subtitle": "The 60,000 Verses That Saved Persian Heritage, Zahhak, and the Simurgh",
    "summary": "Ferdowsi spent thirty years composing 60,000 couplets in pure Persian to preserve Iranian history and language, highlighted by the tragedy of champion Rostam slaying his unknown warrior son Sohrab.",
    "fullStory": "### Act I: The Thirty-Year Monument\nFerdowsi revived the Persian language and ancient Zoroastrian lore following foreign conquests.\n\n### Act II: The Serpent King Zahhak\nZahhak sprouts shoulder snakes fed on youths' brains until Kaveh the Blacksmith raises the banner of rebellion.\n\n### Act III: The Tragedy of Rostam and Sohrab\nRostam battles a Turanian champion in single combat, mortally stabbing him. Seeing the jewel bracelet on the youth's arm, Rostam realizes he has slain his own son Sohrab.",
    "characters": [
      {
        "name": "Rostam",
        "role": "Champion of Iran",
        "desc": "Invincible hero who suffered supreme heartbreak."
      },
      {
        "name": "Sohrab",
        "role": "Youth of Turan",
        "desc": "Noble son seeking his father."
      },
      {
        "name": "Ferdowsi",
        "role": "Immortal Poet",
        "desc": "Preserved the soul of Iranian civilization."
      }
    ],
    "themes": [
      "Tragedy of Blind Warfare",
      "Father vs Son",
      "Cultural Preservation"
    ],
    "echoes": "Father-son combat matches Irish Cú Chulainn and Germanic Hildebrand.",
    "famousQuote": "“For thirty years I endured much toil, but with the Persian tongue I revived Iran.” — Ferdowsi",
    "historicalContext": "Ferdowsi's tomb in Tus is a national sanctuary of Persian culture."
  },
  {
    "id": "norse-ragnarok",
    "year": 1000,
    "displayDate": "c. 800 – 1220 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Yggdrasil & Vigrid",
    "author": "Snorri Sturluson & Poetic Edda Skalds",
    "title": "Ragnarök: The Twilight of the Gods and the Green Rebirth",
    "subtitle": "Yggdrasil, Fimbulwinter, the Slaying of Thor and Odin, and Lif & Lifthrasir",
    "summary": "After the three-year Fimbulwinter, Fenrir snaps his chains and Jörmungandr boils the sea. Gods and monsters clash at Vigrid; the world burns and sinks into the ocean, only to emerge green and renewed.",
    "fullStory": "### Act I: Death of Baldr and Fimbulwinter\nLoki tricks blind Höðr into killing Baldr with mistletoe. Three unbroken winters freeze the world.\n\n### Act II: The Last Stand at Vigrid\nOdin is swallowed by Fenrir; Thor slays the Midgard Serpent but falls dead from venom; Surtr flings fire across the nine worlds.\n\n### Act III: The Green Dawn\nThe blackened earth rises green from the sea; Lif and Lifthrasir emerge from Yggdrasil under a new sun.",
    "characters": [
      {
        "name": "Odin",
        "role": "Allfather",
        "desc": "Embraced his prophesied doom with courage."
      },
      {
        "name": "Thor",
        "role": "God of Thunder",
        "desc": "Defender of mankind who slew the serpent."
      }
    ],
    "themes": [
      "Cyclical Doom and Renewal",
      "Heroic Fatalism"
    ],
    "echoes": "Parallels Hindu Kali Yuga renewal and Aztec Five Suns.",
    "famousQuote": "“The sun turns black, earth sinks into the sea... Now do I see the green earth rise once more.”",
    "historicalContext": "Preserved in the 13th-century Codex Regius manuscript in Iceland."
  },
  {
    "id": "genji-murasaki",
    "year": 1008,
    "displayDate": "c. 1000 – 1012 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Heian-kyō (Kyoto), Japan",
    "author": "Murasaki Shikibu (Noblewoman)",
    "title": "The Tale of Genji (Genji Monogatari)",
    "subtitle": "The World's First Novel: The Shining Prince, Court Poetry, and Mono no Aware",
    "summary": "The world's first psychological novel. Written by noblewoman Murasaki Shikibu at the imperial court in Kyoto, this 54-chapter masterpiece captures the beauty, court intrigues, and Buddhist pathos of impermanence centered on Prince Hikaru Genji.",
    "fullStory": "### Act I: The Shining Prince\nGenji, son of the Emperor, grows into the pinnacle of court elegance, poetry, and calligraphy, haunted by longing for his deceased mother.\n\n### Act II: Exile to Suma\nFollowing scandals, Genji exiles himself to the windswept shore of Suma, composing poetry on the fleeting nature of life.\n\n### Act III: Vanished into Clouds\nIn later life, karmic sadness catches up with him as Lady Murasaki passes away. In a chapter left entirely blank, Genji withdraws from the world.",
    "characters": [
      {
        "name": "Hikaru Genji",
        "role": "The Shining Prince",
        "desc": "Aristocrat whose life explores aesthetic heights and human longing."
      },
      {
        "name": "Murasaki Shikibu",
        "role": "Author",
        "desc": "Founded Japanese narrative realism."
      }
    ],
    "themes": [
      "Mono no Aware (Pathos of Things)",
      "Psychological Realism",
      "Buddhist Impermanence"
    ],
    "echoes": "Preceded European novels by Cervantes and Richardson by six centuries.",
    "famousQuote": "“Can any sorrow be heavier than the parting of those who love?” — Murasaki Shikibu",
    "historicalContext": "Written in phonetic Kana script during the cultural peak of the Heian court."
  },
  {
    "id": "maui-snare-sun",
    "year": 1050,
    "displayDate": "c. 1050 CE",
    "era": "medieval",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Haleakalā (Hawaii) & Pacific Islands",
    "author": "Polynesian Oral Bards",
    "title": "Māui Snares the Sun: Giving Humanity the Gift of Day",
    "subtitle": "Flax Ropes and the Slowing of Tama-nui-te-rā",
    "summary": "Because the sun raced across the sky too quickly for crops to grow or food to cook, Māui wove giant flax ropes, trapped the Sun God in a net, and beat him until he promised to move slowly.",
    "fullStory": "### Act I: Short Days and Starvation\nThe Sun raced across the sky in minutes. Fires could not be lit, crops withered in darkness.\n\n### Act II: The Net of Flax\nMāui and his brothers wove enchanted ropes of flax and traveled to the eastern pit where the sun rises.\n\n### Act III: The Compact with the Sun\nAs Tama-nui-te-rā rose, Māui snared his rays and struck him with the magic jawbone until he agreed to walk slowly forever.",
    "characters": [
      {
        "name": "Tama-nui-te-rā",
        "role": "The Sun God",
        "desc": "Forced to slow his daily march across the sky."
      }
    ],
    "themes": [
      "Mastery over Nature",
      "Sacrifice for Mankind"
    ],
    "echoes": "Parallels Joshua commanding the sun to stand still and Phaethon in Greek myth.",
    "famousQuote": "“Now the sun walks with measured steps, and mortals have time to plant and sing.”",
    "historicalContext": "Haleakalā in Maui literally translates to 'House of the Sun'."
  },
  {
    "id": "yoruba-obatala-shango",
    "year": 1100,
    "displayDate": "c. 1100 CE",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Ile-Ife & Oyo Kingdom (Nigeria)",
    "author": "Yoruba Babalawos (Ifá Diviners)",
    "title": "The Yoruba Orishas: Obatala Molds Mankind and Shango's Thunder",
    "subtitle": "The Sacred Chain from Heaven, the Palm Wine, and the Double-Axe",
    "summary": "Supreme God Olodumare sends Obatala down a gold chain to mold the human body from red clay. Later, King Shango rules Oyo with living lightning and thunderstones.",
    "fullStory": "### Act I: The Gold Chain\nObatala descended from heaven on a long gold chain carrying a snail shell of earth, a five-toed hen, and a chameleon to solidify the land at Ile-Ife.\n\n### Act II: Molding Humanity\nObatala sculpted human bodies from clay, but drank palm wine and molded deformed bodies; upon sobering, he vowed to become the eternal protector of disabled persons.\n\n### Act III: Shango the Thunder King\nKing Shango commanded thunder and double-headed axes (Oshe), ruling Oyo with fiery justice.",
    "characters": [
      {
        "name": "Obatala",
        "role": "Creator Orisha",
        "desc": "Molds human forms and protects the disabled."
      },
      {
        "name": "Shango",
        "role": "God of Thunder & Lightning",
        "desc": "Historic third Alaafin (king) of Oyo."
      }
    ],
    "themes": [
      "Protection of the Vulnerable",
      "Divine Crafting",
      "Justice and Storms"
    ],
    "echoes": "Obatala molding humans parallels Prometheus and Khnum; Shango mirrors Thor and Indra.",
    "famousQuote": "“Obatala is the owner of the white cloth and the sculptor of the human face.” — Ifá Corpus",
    "historicalContext": "Ile-Ife terracotta and bronze sculptures date from the 11th–14th centuries CE."
  },
  {
    "id": "the-tale-of-the-heike",
    "year": 1150,
    "displayDate": "c. 1150 CE",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Japanese epic compiled prior to 1330",
    "author": "Classical Japan & Korea Tradition",
    "title": "The Tale of the Heike",
    "subtitle": "Japanese epic compiled prior to 1330",
    "summary": "The Tale of the Heike  is an epic account compiled prior to 1330 of the struggle between the Taira clan and Minamoto clan for control of Japan at the end of the 12th century in the Genpei War (1180–1185).",
    "fullStory": "### Act I: The Awakening of The Tale of the Heike\nThe Tale of the Heike  is an epic account compiled prior to 1330 of the struggle between the Taira clan and Minamoto clan for control of Japan at the end of the 12th century in the Genpei War (1180–1185).\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "The Tale of the Heike",
        "role": "Protagonist",
        "desc": "Japanese epic compiled prior to 1330"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Japan & Korea.",
    "famousQuote": "“The memory of The Tale of the Heike endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "arthur-holy-grail",
    "year": 1170,
    "displayDate": "c. 1170 – 1485 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Camelot, Avalon & Glastonbury",
    "author": "Chrétien de Troyes & Sir Thomas Malory",
    "title": "King Arthur and the Knights of the Round Table: The Quest for the Holy Grail",
    "subtitle": "Excalibur from the Stone, the Lady of the Lake, Lancelot, and Sir Galahad",
    "summary": "Young Arthur pulls the sword from the anvil to become High King of Britain, establishing the egalitarian Round Table at Camelot, sending knights on the spiritual quest for the Holy Grail before his final voyage to Avalon.",
    "fullStory": "### Act I: The Sword in the Stone\nMerlin places the sword in the stone; humble squire Arthur pulls it out effortlessly.\n\n### Act II: The Round Table\nArthur establishes the Round Table where all knights sit as equals, defending the weak.\n\n### Act III: The Quest for the Holy Grail\nSir Galahad, purest of heart, gazes into the Holy Grail and ascends to heaven.\n\n### Act IV: The Fall of Camelot\nBetrayed by Mordred, Arthur is mortally wounded at Camlann and ferried across the mists to the enchanted isle of Avalon.",
    "characters": [
      {
        "name": "King Arthur",
        "role": "The Once and Future King",
        "desc": "Idealized sovereign of chivalry."
      },
      {
        "name": "Merlin",
        "role": "Enchanter & Prophet",
        "desc": "Guided Arthur with druidic foresight."
      },
      {
        "name": "Sir Galahad",
        "role": "Pure Knight",
        "desc": "Achieved the vision of the Holy Grail."
      }
    ],
    "themes": [
      "Chivalric Honor",
      "Egalitarian Leadership",
      "The Once and Future King"
    ],
    "echoes": "Merlin echoes Gandalf; the Holy Grail mirrors the Vedic Amrita and Golden Fleece.",
    "famousQuote": "“Whoso pulleth out this sword of this stone is rightwise king born of all England.” — Malory",
    "historicalContext": "Synthesized Celtic Welsh folklore with Anglo-Norman chivalric romance."
  },
  {
    "id": "attar-conference-birds",
    "year": 1177,
    "displayDate": "c. 1177 CE",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Nishapur, Greater Khorasan",
    "author": "Farid ud-Din Attar",
    "title": "The Conference of the Birds (Mantiq al-Tayr)",
    "subtitle": "The Hoopoe's Guidance, the Seven Valleys, and the Mirror of the Simurgh",
    "summary": "Thousands of birds gather to seek their mythical king, the Simurgh. Guided by the Hoopoe across seven perilous valleys (Quest, Love, Knowledge, Detachment, Unity, Wonder, Poverty), only thirty birds survive—discovering they themselves are the Simurgh (Si Murgh - Thirty Birds).",
    "fullStory": "### Act I: The Council of Birds\nThe Hoopoe summons the nightingale, falcon, duck, and parrot, challenging their worldly excuses to embark on the spiritual path.\n\n### Act II: The Seven Valleys\nThey cross the Valley of Love (where reason burns), the Valley of Unity, and the Valley of Annihilation (Fana).\n\n### Act III: The Mirror of the Simurgh\nThirty exhausted birds reach the mountain throne. Looking upon the king, they see a mirror reflecting their own faces: the divine was within them all along.",
    "characters": [
      {
        "name": "The Hoopoe",
        "role": "Spiritual Master (Murshid)",
        "desc": "Guided the flock across the cosmic valleys."
      },
      {
        "name": "The Simurgh",
        "role": "Divine Truth",
        "desc": "The transcendent king found within the collective soul."
      }
    ],
    "themes": [
      "Sufi Mysticism (Fana)",
      "The Journey Inward",
      "Unity of Being"
    ],
    "echoes": "Parallels Dante's Paradiso and Bunyan's Pilgrim's Progress.",
    "famousQuote": "“When they looked, they saw that the Simurgh was none other than the thirty birds themselves!”",
    "historicalContext": "A seminal masterpiece of Persian Sufi allegorical poetry."
  },
  {
    "id": "nizami-layla-majnun",
    "year": 1188,
    "displayDate": "c. 1188 CE",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Arabian Desert & Ganja",
    "author": "Nizami Ganjavi",
    "title": "Layla and Majnun: The Supreme Romantic Tragedy of the East",
    "subtitle": "Qays's Madness in the Dunes, the Tamed Wild Beasts, and Transcendent Love",
    "summary": "Young Qays falls into an all-consuming love with Layla. Rejected by her father, Qays flees into the desert as Majnun (the Madman), his grief-filled verses taming lions and wolves, transforming human love into divine union.",
    "fullStory": "### Act I: The Schoolroom Glance\nQays and Layla fall into an immediate, spiritual love that defies tribal conventions.\n\n### Act II: Majnun in the Wilderness\nForbidden from seeing Layla, Qays wanders naked in the desert writing her name on every stone. Lions and gazelles gather peacefully around him.\n\n### Act III: The Garden Meeting and Tomb\nMeeting years later in a walled garden, their love has become pure spirit, unable to touch mortal flesh. They die of grief and are united in Paradise.",
    "characters": [
      {
        "name": "Majnun (Qays)",
        "role": "The Possessed Poet",
        "desc": "Archetype of the egoless mystic lover."
      },
      {
        "name": "Layla",
        "role": "The Beloved",
        "desc": "Luminous beacon of spiritual beauty."
      }
    ],
    "themes": [
      "Transcendent Love (Ishq)",
      "Ego Dissolution",
      "Mystic Union"
    ],
    "echoes": "Directly inspired Shakespeare's Romeo and Juliet and European courtly romances.",
    "famousQuote": "“If I am mad, it is with the wine of love! Only Layla remains in my chest.” — Nizami",
    "historicalContext": "The jewel of Nizami's Khamsa (Five Epics), celebrated from Turkey to India."
  },
  {
    "id": "pele-volcano",
    "year": 1200,
    "displayDate": "c. 1200 CE",
    "era": "medieval",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Kīlauea & Halemaʻumaʻu, Hawaii",
    "author": "Hawaiian Kahuna (Chanters)",
    "title": "Pele: The Fire Goddess and the Creation of the Hawaiian Islands",
    "subtitle": "The Migration from Tahiti, the Sacred Oʻo Stick, and Kīlauea",
    "summary": "Exiled by her water-goddess sister Nāmaka, Pele travels across the Pacific chain, using her digging stick Paʻoa to create volcanic craters until finding her eternal home in Kīlauea.",
    "fullStory": "### Act I: The Ocean Flight\nPele fled across the waves in a canoe guarded by her shark brother Kamohoaliʻi.\n\n### Act II: The Fire Stick\nAt each island she dug into the earth, but water flooded her pits until she reached the Big Island of Hawaii.\n\n### Act III: The Throne of Kīlauea\nAt Halemaʻumaʻu, she struck molten magma, making the volcano her eternal seat of creation and destruction.",
    "characters": [
      {
        "name": "Pele",
        "role": "Goddess of Volcanoes and Fire",
        "desc": "Creator of new land through molten lava."
      },
      {
        "name": "Hiʻiaka",
        "role": "Beloved Sister",
        "desc": "Goddess of the hula and forest rejuvenation."
      }
    ],
    "themes": [
      "Creation and Destruction",
      "Living Land (ʻĀina)"
    ],
    "echoes": "Parallels Vulcan/Hephaestus in Greco-Roman myth.",
    "famousQuote": "“Aia lā ʻo Pele i Kīlauea — There dwells Pele in Kīlauea.” — Traditional Hawaiian Chant",
    "historicalContext": "Accurately maps the geological age of the Hawaiian islands from oldest (Kauai) to youngest (Hawaii)."
  },
  {
    "id": "anansi-spider-stories",
    "year": 1200,
    "displayDate": "c. 1200 CE",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Ashanti Kingdom (Ghana) & Diaspora",
    "author": "Akan Storytellers (Anansesem)",
    "title": "Anansi the Spider: How All Stories Came to Earth",
    "subtitle": "The Golden Box of Nyame, the Hornet Gourd, and the Leopard Trap",
    "summary": "All stories in the universe were locked in Sky God Nyame's golden box. Anansi the clever spider captures the stinging hornets, giant python, and leopard through wit to buy all stories for mankind.",
    "fullStory": "### Act I: The Sky God's Price\nNyame laughed at Anansi's wish to buy the stories, demanding four dangerous creatures.\n\n### Act II: The Four Tricks\nAnansi tricked the hornets into a calabash, tied the python to a palm stick, and trapped the leopard in a pit.\n\n### Act III: The Opening of the Box\nNyame opened the golden box; stories swarmed out like glowing fireflies across the globe.",
    "characters": [
      {
        "name": "Kwaku Anansi",
        "role": "Spider Trickster",
        "desc": "Conquered beasts through psychology rather than force."
      },
      {
        "name": "Nyame",
        "role": "Sky God",
        "desc": "Keeper of celestial wisdom."
      }
    ],
    "themes": [
      "Wit over Force",
      "Liberation of Folklore",
      "Diaspora Resilience"
    ],
    "echoes": "Survived as Br'er Rabbit and Aunt Nancy across the Caribbean and American South.",
    "famousQuote": "“Without stories, we would have no light to see each other in the dark.”",
    "historicalContext": "Core storytelling tradition (Anansesem) of the Akan people of West Africa."
  },
  {
    "id": "nibelungenlied",
    "year": 1200,
    "displayDate": "c. 1200 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "Middle High German epic poem from around 1200",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Nibelungenlied",
    "subtitle": "Middle High German epic poem from around 1200",
    "summary": "The Nibelungenlied, translated as The Song of the Nibelungs, is an epic poem written around 1200 in Middle High German. Its anonymous poet was likely from the region of Passau. The Nibelungenlied is based on an oral tradition of Germanic heroic legend that has some of its origin in historic events and individuals of the 5th and 6th centuries and that spread throughout almost all of Germanic-speaking Europe. Scandinavian parallels to the German poem are found especially in the heroic lays of the Poetic Edda and in the Völsunga saga.",
    "fullStory": "### Act I: The Awakening of Nibelungenlied\nThe Nibelungenlied, translated as The Song of the Nibelungs, is an epic poem written around 1200 in Middle High German. Its anonymous poet was likely from the region of Passau. The Nibelungenlied is based on an oral tradition of Germanic heroic legend that has some of its origin in historic events and individuals of the 5th and 6th centuries and that spread throughout almost all of Germanic-speaking Europe. Scandinavian parallels to the German poem are found especially in the heroic lays of the Poetic Edda and in the Völsunga saga.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Nibelungenlied",
        "role": "Protagonist",
        "desc": "Middle High German epic poem from around 1200"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Nibelungenlied endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "sundiata-mali",
    "year": 1235,
    "displayDate": "c. 1235 CE",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Niani & Kirina, Mali Empire",
    "author": "Preserved by Griots (Djeli Mamadou Kouyaté)",
    "title": "The Epic of Sundiata: The Lion King of Mali",
    "subtitle": "The Miracle of the Iron Rod, the Sorcerer King, and the Mandinka Charter",
    "summary": "Born crippled and mocked until age seven, Sundiata Keita heaves himself up with an iron rod, overcomes seven years of exile, and defeats the sorcerer-king Sumanguru at Kirina to forge the wealthy Mali Empire.",
    "fullStory": "### Act I: The Crippled Boy\nSundiata crawls until age seven. When his mother weeps from mockery, he bends an iron rod like a bow, stands tall, and uproots a baobab tree.\n\n### Act II: The Sorcerer King\nSumanguru Kanté wears robes of human skin and rules with dark magic.\n\n### Act III: The Battle of Kirina\nDiscovering Sumanguru's secret weakness, Sundiata grazes him with an arrow tipped with a white rooster spur, breaking his magic and founding Mali.",
    "characters": [
      {
        "name": "Sundiata Keita",
        "role": "The Lion King",
        "desc": "Disabled prince who founded the Mali Empire."
      },
      {
        "name": "Sumanguru Kanté",
        "role": "Sorcerer King",
        "desc": "Tyrant whose magic was undone by a rooster spur."
      },
      {
        "name": "Balla Fasséké",
        "role": "Master Griot",
        "desc": "Preserved the lineage of Manden."
      }
    ],
    "themes": [
      "Overcoming Adversity",
      "Griot Oral Memory",
      "Human Rights Charter"
    ],
    "echoes": "Directly inspired modern classics like Disney's The Lion King.",
    "famousQuote": "“We are the vessels of speech; without us the names of kings would vanish.” — Kouyaté",
    "historicalContext": "The Kouroukan Fouga charter proclaimed by Sundiata is recognized by UNESCO."
  },
  {
    "id": "epic-of-sundiata",
    "year": 1235,
    "displayDate": "c. 1235 CE",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Epic poem of the Malinke culture",
    "author": "Classical Sub-Saharan Africa Tradition",
    "title": "Epic of Sundiata",
    "subtitle": "Epic poem of the Malinke culture",
    "summary": "The Epic of Sundiata is an epic poem of the Malinke people that tells the story of Sundiata Keita, the founder of the Mali Empire in West Africa, who ruled from 1235 C.E. until his death in 1255 C.E. It details how Sundiata established the empire through strategic alliances and exceptional skill, and is structured as a Hero's journey. The epic is a foundational to Mandé culture and has been narrated for generations by Griots through oral tradition.",
    "fullStory": "### Act I: The Awakening of Epic of Sundiata\nThe Epic of Sundiata is an epic poem of the Malinke people that tells the story of Sundiata Keita, the founder of the Mali Empire in West Africa, who ruled from 1235 C.E. until his death in 1255 C.E. It details how Sundiata established the empire through strategic alliances and exceptional skill, and is structured as a Hero's journey. The epic is a foundational to Mandé culture and has been narrated for generations by Griots through oral tradition.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Epic of Sundiata",
        "role": "Protagonist",
        "desc": "Epic poem of the Malinke culture"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Sub-Saharan Africa.",
    "famousQuote": "“The memory of Epic of Sundiata endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "manco-c-pac",
    "year": 1250,
    "displayDate": "c. 1250 CE",
    "era": "medieval",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Legendary founder of the Inca civilization",
    "author": "Classical The Americas Tradition",
    "title": "Manco Cápac",
    "subtitle": "Legendary founder of the Inca civilization",
    "summary": "Manco Cápac, also known as Manco Inca and Ayar Manco, was, according to some historians, the first governor and founder of the Inca civilisation in Cusco, possibly in the early 13th century. He is also a main figure of Inca mythology, being the protagonist of the two best known legends about the origin of the Inca, both of them connecting him to the foundation of Cusco. His main wife and the mother of his son and successor, Sinchi Ruq'a, was his sister Mama Uqllu. Even though his figure is mentioned in several chronicles, his actual existence remains uncertain.",
    "fullStory": "### Act I: The Awakening of Manco Cápac\nManco Cápac, also known as Manco Inca and Ayar Manco, was, according to some historians, the first governor and founder of the Inca civilisation in Cusco, possibly in the early 13th century. He is also a main figure of Inca mythology, being the protagonist of the two best known legends about the origin of the Inca, both of them connecting him to the foundation of Cusco. His main wife and the mother of his son and successor, Sinchi Ruq'a, was his sister Mama Uqllu. Even though his figure is mentioned in several chronicles, his actual existence remains uncertain.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Manco Cápac",
        "role": "Protagonist",
        "desc": "Legendary founder of the Inca civilization"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across The Americas.",
    "famousQuote": "“The memory of Manco Cápac endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "v-lsunga-saga",
    "year": 1250,
    "displayDate": "c. 1250 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "13th century Icelandic saga",
    "author": "Classical Northern & Celtic Europe Tradition",
    "title": "Völsunga saga",
    "subtitle": "13th century Icelandic saga",
    "summary": "The Völsunga saga is a legendary saga, a late 13th-century prose rendition in Old Norse of the origin and decline of the Völsung clan. It is one of the most famous legendary sagas and an example of a \"heroic saga\" that deals with Germanic heroic legend.",
    "fullStory": "### Act I: The Awakening of Völsunga saga\nThe Völsunga saga is a legendary saga, a late 13th-century prose rendition in Old Norse of the origin and decline of the Völsung clan. It is one of the most famous legendary sagas and an example of a \"heroic saga\" that deals with Germanic heroic legend.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Völsunga saga",
        "role": "Protagonist",
        "desc": "13th century Icelandic saga"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Northern & Celtic Europe.",
    "famousQuote": "“The memory of Völsunga saga endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "kebra-nagast",
    "year": 1300,
    "displayDate": "c. 1300 CE",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Aksum & Jerusalem",
    "author": "Nebura'ed Yeshaq of Aksum",
    "title": "Kebra Nagast: The Glory of Ethiopian Kings",
    "subtitle": "The Queen of Sheba, King Solomon's Riddles, and Menelik I",
    "summary": "The national epic of Ethiopia. Makeda, Queen of Sheba, visits King Solomon in Jerusalem. Their son Menelik I visits his father and brings the sacred Ark of the Covenant back to Aksum.",
    "fullStory": "### Act I: The Queen's Journey\nMakeda journeys across the Red Sea with caravans of frankincense to test Solomon's wisdom.\n\n### Act II: The Union of Kings\nSolomon hosts Makeda, and their union conceives Prince Menelik.\n\n### Act III: The Ark to Aksum\nAs an adult, Menelik visits Jerusalem, bringing the Ark of the Covenant to Ethiopia, establishing the Solomonic dynasty.",
    "characters": [
      {
        "name": "Makeda (Queen of Sheba)",
        "role": "Sovereign Queen",
        "desc": "Ruler of Aksum who tested Solomon's intellect."
      },
      {
        "name": "Menelik I",
        "role": "First Emperor",
        "desc": "Founded Ethiopia's Solomonic royal line."
      }
    ],
    "themes": [
      "Sacred Kingship",
      "Wisdom across Cultures",
      "Guardian of the Ark"
    ],
    "echoes": "Bridges Judeo-Christian and African imperial traditions.",
    "famousQuote": "“The glory of kings is established in righteousness and truth.” — Kebra Nagast",
    "historicalContext": "Ethiopian emperors traced their unbroken lineage to Menelik until 1974."
  },
  {
    "id": "the-decameron",
    "year": 1313,
    "displayDate": "c. 1313 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "14th-century collection of stories by Giovanni Boccaccio",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "The Decameron",
    "subtitle": "14th-century collection of stories by Giovanni Boccaccio",
    "summary": "The Decameron, subtitled Prince Galehaut, is a collection of short stories by the 14th-century Italian author Giovanni Boccaccio (1313–1375). It is sometimes nicknamed l'Umana commedia, as it was Boccaccio that dubbed Dante Alighieri's Comedy \"Divine\". The book is structured as a frame story containing 100 tales told by a group of seven young women and three young men; they shelter in a secluded villa just outside Florence in order to escape the Black Death, which was afflicting the city. The epidemic is likely what Boccaccio used for the basis of the book which was thought to be written between 1348 and 1353. The various tales of love in The Decameron range from the erotic to the tragic. Tales of wit, practical jokes, and life lessons also contribute to the mosaic. In addition to its literary value and widespread influence, it provides a document of life at the time. Written in the vernacular of the Florentine language, it is considered a masterpiece of early Italian prose.",
    "fullStory": "### Act I: The Awakening of The Decameron\nThe Decameron, subtitled Prince Galehaut, is a collection of short stories by the 14th-century Italian author Giovanni Boccaccio (1313–1375). It is sometimes nicknamed l'Umana commedia, as it was Boccaccio that dubbed Dante Alighieri's Comedy \"Divine\". The book is structured as a frame story containing 100 tales told by a group of seven young women and three young men; they shelter in a secluded villa just outside Florence in order to escape the Black Death, which was afflicting the city. The epidemic is likely what Boccaccio used for the basis of the book which was thought to be written between 1348 and 1353. The various tales of love in The Decameron range from the erotic to the tragic. Tales of wit, practical jokes, and life lessons also contribute to the mosaic. In addition to its literary value and widespread influence, it provides a document of life at the time. Written in the vernacular of the Florentine language, it is considered a masterpiece of early Italian prose.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "The Decameron",
        "role": "Protagonist",
        "desc": "14th-century collection of stories by Giovanni Boccaccio"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of The Decameron endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "dante-divine-comedy",
    "year": 1320,
    "displayDate": "1308 – 1320 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Florence & The Three Realms",
    "author": "Dante Alighieri (Il Sommo Poeta)",
    "title": "The Divine Comedy: Inferno, Purgatorio, and Paradiso",
    "subtitle": "The Dark Wood, Virgil's Guidance, Beatrice, and the Love That Moves the Stars",
    "summary": "Guided by Virgil through the nine circles of Hell and seven terraces of Purgatory, Dante is led by Beatrice through the celestial spheres of Paradise to gaze upon the Holy Trinity in radiant light.",
    "fullStory": "### Act I: The Gates of Hell\nLost in a dark wood at midlife, Dante passes the gate: 'Abandon all hope, ye who enter here.'\n\n### Act II: The Inferno & Purgatorio\nWitnessing the contrapasso punishments of sin, he climbs Mount Purgatory to cleanse his soul.\n\n### Act III: Paradiso and the Cosmic Rose\nBeatrice guides him to the Empyrean to behold the Love that moves the sun and other stars.",
    "characters": [
      {
        "name": "Dante",
        "role": "Pilgrim & Poet",
        "desc": "Allegory of human moral redemption."
      },
      {
        "name": "Virgil",
        "role": "Master Guide",
        "desc": "Symbol of human reason."
      },
      {
        "name": "Beatrice",
        "role": "Divine Muse",
        "desc": "Symbol of divine grace."
      }
    ],
    "themes": [
      "Divine Justice (Contrapasso)",
      "Spiritual Transformation"
    ],
    "echoes": "Katabasis parallels Aeneas in Virgil and Gilgamesh crossing the deep.",
    "famousQuote": "“L’Amor che move il sole e l’altre stelle.” (The Love that moves the sun and stars.) — Paradiso",
    "historicalContext": "Established the Tuscan dialect as the modern Italian language."
  },
  {
    "id": "aztec-five-suns",
    "year": 1325,
    "displayDate": "c. 1325 – 1521 CE",
    "era": "medieval",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Teotihuacan & Lake Texcoco (Tenochtitlan)",
    "author": "Mexica Tlamatinime (Wise Scribes)",
    "title": "The Aztec Myth of the Five Suns & the Eagle on the Cactus",
    "subtitle": "Nanahuatzin's Leap, Quetzalcoatl's Bone Theft, and Tenochtitlan",
    "summary": "After four previous worlds perish by jaguars, wind, fire, and flood, the humble god Nanahuatzin leaps into a cosmic bonfire to become the Fifth Sun. Quetzalcoatl steals human bones from Mictlan, and the Mexica follow the sign of an eagle on a cactus.",
    "fullStory": "### Act I: The Four Destroyed Suns\nFour previous worlds were destroyed by cosmic imbalances of jaguars, hurricanes, fire, and flood.\n\n### Act II: The Fire of Teotihuacan\nNanahuatzin, poor and covered in sores, courageously leaps into the cosmic pyre to become the Fifth Sun (Tonatiuh).\n\n### Act III: The Bones of Mictlan\nQuetzalcoatl outwits the Lord of the Dead to retrieve ancestral bones, bleeding his own veins to recreate mankind.\n\n### Act IV: The Eagle on the Cactus\nThe Mexica wander until discovering an eagle perched on a cactus eating a snake on Lake Texcoco, founding Tenochtitlan.",
    "characters": [
      {
        "name": "Nanahuatzin",
        "role": "Humble God & Fifth Sun",
        "desc": "Selfless sacrifice ignited the living sun."
      },
      {
        "name": "Quetzalcoatl",
        "role": "Feathered Serpent",
        "desc": "God of wisdom who resurrected mankind."
      }
    ],
    "themes": [
      "Cosmic Balance",
      "Self-Sacrifice",
      "Sacred City Foundations"
    ],
    "echoes": "Nanahuatzin's leap mirrors Odin's sacrifice on Yggdrasil.",
    "famousQuote": "“As long as the world endures, the glory of Tenochtitlan shall never perish!”",
    "historicalContext": "Carved into the 24-ton Aztec Calendar Sun Stone in Mexico City."
  },
  {
    "id": "three-kingdoms-luo",
    "year": 1350,
    "displayDate": "c. 1350 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Peach Garden, Red Cliffs & Luoyang",
    "author": "Luo Guanzhong",
    "title": "Romance of the Three Kingdoms: The Oath in the Peach Garden",
    "subtitle": "Liu Bei, Guan Yu, Zhang Fei, Zhuge Liang's Borrowed Arrows, and Red Cliffs",
    "summary": "The epic saga of the collapse of the Han dynasty. Liu Bei, Guan Yu, and Zhang Fei swear eternal brotherhood in a blooming peach garden to restore the realm, aided by master strategist Zhuge Liang.",
    "fullStory": "### Act I: The Peach Garden Oath\nThree heroes drink wine under blooming peach blossoms, swearing to die on the same day in service of the empire.\n\n### Act II: The Sleeping Dragon\nLiu Bei visits the thatched cottage of master strategist Zhuge Liang three times in winter snow to enlist his genius.\n\n### Act III: The Battle of Red Cliffs\nZhuge Liang borrows 100,000 arrows using straw boats in morning mist, summoning southeast winds to burn Cao Cao's chained fleet on the Yangtze River.",
    "characters": [
      {
        "name": "Liu Bei",
        "role": "Benevolent Prince",
        "desc": "Leader of Shu Han."
      },
      {
        "name": "Guan Yu",
        "role": "God of War & Loyalty",
        "desc": "Wielder of the Green Dragon Crescent Blade."
      },
      {
        "name": "Zhuge Liang",
        "role": "Master Strategist",
        "desc": "The Sleeping Dragon whose intellect reshaped kingdoms."
      }
    ],
    "themes": [
      "Brotherhood and Loyalty (Yi)",
      "Military Strategy",
      "Cyclical Dynastic Rise and Fall"
    ],
    "echoes": "Shares epic scope with the Iliad and Arthurian romances.",
    "famousQuote": "“The empire, long divided, must unite; long united, must divide.” — Opening Line",
    "historicalContext": "One of the Four Great Classical Novels of Chinese literature."
  },
  {
    "id": "mabinogion",
    "year": 1350,
    "displayDate": "c. 1350 CE",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Earliest Welsh prose stories",
    "author": "Classical Northern & Celtic Europe Tradition",
    "title": "Mabinogion",
    "subtitle": "Earliest Welsh prose stories",
    "summary": "The Mabinogion is a collection of the earliest Welsh prose stories, compiled in Middle Welsh in the 12th–13th centuries from earlier oral traditions. There are two main source manuscripts, created c. 1350–1410, and a few earlier fragments. Often included in the broader mythologies described as the Matter of Britain, the Mabinogion consists of eleven stories of widely different types, offering drama, philosophy, romance, tragedy, fantasy and humour. \nStrictly speaking, the Four Branches of the Mabinogi are the main sequence of related tales, but seven others include a classic hero quest, \"Culhwch and Olwen\"; a historic legend, complete with glimpses of a far off age, in \"Lludd and Llefelys\"; and other tales portraying a very different King Arthur from the later popular versions.",
    "fullStory": "### Act I: The Awakening of Mabinogion\nThe Mabinogion is a collection of the earliest Welsh prose stories, compiled in Middle Welsh in the 12th–13th centuries from earlier oral traditions. There are two main source manuscripts, created c. 1350–1410, and a few earlier fragments. Often included in the broader mythologies described as the Matter of Britain, the Mabinogion consists of eleven stories of widely different types, offering drama, philosophy, romance, tragedy, fantasy and humour. \nStrictly speaking, the Four Branches of the Mabinogi are the main sequence of related tales, but seven others include a classic hero quest, \"Culhwch and Olwen\"; a historic legend, complete with glimpses of a far off age, in \"Lludd and Llefelys\"; and other tales portraying a very different King Arthur from the later popular versions.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Mabinogion",
        "role": "Protagonist",
        "desc": "Earliest Welsh prose stories"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Northern & Celtic Europe.",
    "famousQuote": "“The memory of Mabinogion endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "boccaccio-decameron",
    "year": 1353,
    "displayDate": "1348 – 1353 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Florence & Fiesole Hills, Italy",
    "author": "Giovanni Boccaccio",
    "title": "The Decameron: One Hundred Tales Escaping the Black Death",
    "subtitle": "Seven Young Women, Three Men, and Ten Days of Wit and Resilience",
    "summary": "Fleeing the terrifying Black Death plague in Florence, ten young aristocrats retreat to a country villa, spending ten days telling one hundred witty, romantic, and satirical stories celebrating human ingenuity.",
    "fullStory": "### Act I: The Plague in Florence\nIn 1348, the horrific Black Death wiped out half of Florence, destroying all social bonds and laws.\n\n### Act II: The Villa Sanctuary\nSeven noblewomen and three men retreat to a countryside garden, electing a king/queen each day to rule over story sessions.\n\n### Act III: The 100 Tales of Human Fortune\nStories of clever merchants outwitting corrupt friars, tragic lovers, and resourceful wives celebrate the triumph of human intellect over blind fortune.",
    "characters": [
      {
        "name": "Pampinea",
        "role": "Queen of Day 1",
        "desc": "Organized the refuge in the hills."
      }
    ],
    "themes": [
      "Triumph of Wit over Death",
      "Humanism and Joy",
      "Framed Narrative"
    ],
    "echoes": "Direct source for Shakespeare's All's Well That Ends Well and Chaucer.",
    "famousQuote": "“Human compassion is a noble virtue in all who have known suffering.” — Boccaccio",
    "historicalContext": "The foundational masterpiece of Italian vernacular prose."
  },
  {
    "id": "investiture-of-the-gods",
    "year": 1368,
    "displayDate": "c. 1368 CE",
    "era": "medieval",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "16th-century Chinese novel",
    "author": "Classical China & East Asia Tradition",
    "title": "Investiture of the Gods",
    "subtitle": "16th-century Chinese novel",
    "summary": "The Investiture of the Gods, also known by its Chinese titles Fengshen Yanyi (Chinese: 封神演義; pinyin: Fēngshén Yǎnyì; Wade–Giles: Fêng1-shên2 Yan3-yi4; Jyutping: Fung1 San4 Jin2 Ji6) and Fengshen Bang (封神榜), is a 16th-century Chinese novel and one of the major vernacular Chinese works in the gods and demons (shenmo) genre written during the Ming dynasty (1368–1644). Consisting of 100 chapters, it was first published in book form between 1567 and 1619. Another source claims it was published in a finalized edition in 1605. The work combines elements of history, folklore, mythology, legends and fantasy.",
    "fullStory": "### Act I: The Awakening of Investiture of the Gods\nThe Investiture of the Gods, also known by its Chinese titles Fengshen Yanyi (Chinese: 封神演義; pinyin: Fēngshén Yǎnyì; Wade–Giles: Fêng1-shên2 Yan3-yi4; Jyutping: Fung1 San4 Jin2 Ji6) and Fengshen Bang (封神榜), is a 16th-century Chinese novel and one of the major vernacular Chinese works in the gods and demons (shenmo) genre written during the Ming dynasty (1368–1644). Consisting of 100 chapters, it was first published in book form between 1567 and 1619. Another source claims it was published in a finalized edition in 1605. The work combines elements of history, folklore, mythology, legends and fantasy.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Investiture of the Gods",
        "role": "Protagonist",
        "desc": "16th-century Chinese novel"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across China & East Asia.",
    "famousQuote": "“The memory of Investiture of the Gods endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "chaucer-canterbury",
    "year": 1387,
    "displayDate": "c. 1387 – 1400 CE",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "The Tabard Inn (Southwark) to Canterbury Cathedral",
    "author": "Geoffrey Chaucer (Father of English Poetry)",
    "title": "The Canterbury Tales: The Knight, the Miller, and the Wife of Bath",
    "subtitle": "The Pilgrimage to Saint Thomas Becket, Bawdy Humor, and Female Sovereignty",
    "summary": "A diverse company of twenty-nine pilgrims journey on horseback to Canterbury Cathedral, competing in a storytelling contest at the Tabard Inn, capturing the vibrant panorama of medieval English life.",
    "fullStory": "### Act I: April Showers and the Tabard Inn\nWhen sweet April rains awaken spring blossoms, pilgrims gather in Southwark, agreeing to tell two tales each on the road.\n\n### Act II: The Chivalric Knight & Bawdy Miller\nThe Knight sings of courtly love and honor, immediately interrupted by the drunken Miller's bawdy comedy of an old carpenter and young clerks.\n\n### Act III: The Wife of Bath's Tale\nThe five-times married Dame Alice argues that what women desire most above all things is sovereignty over their own lives and husbands.",
    "characters": [
      {
        "name": "Geoffrey Chaucer",
        "role": "Pilgrim-Narrator",
        "desc": "Chronicled medieval English society."
      },
      {
        "name": "The Wife of Bath (Dame Alice)",
        "role": "Feminist Icon",
        "desc": "Defended female autonomy and joy."
      }
    ],
    "themes": [
      "Social Satire",
      "Female Sovereignty",
      "Diversity of Human Experience"
    ],
    "echoes": "Framed storytelling mirrors Boccaccio's Decameron and 1,001 Nights.",
    "famousQuote": "“What women desire most is to have sovereignty over their husbands as well as their love.” — Wife of Bath",
    "historicalContext": "Established Middle English as a high literary language."
  },
  {
    "id": "doctor-faustus",
    "year": 1550,
    "displayDate": "c. 1550 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "Play by Christopher Marlowe",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Doctor Faustus",
    "subtitle": "Play by Christopher Marlowe",
    "summary": "The Tragical History of the Life and Death of Doctor Faustus, commonly referred to simply as Doctor Faustus, is an Elizabethan tragedy by Christopher Marlowe, based on German stories about a scholar who sells his soul to the devil in exchange for magical power. Written in the late 16th century and first performed around 1594, the play follows Faustus’ rise as a magician through his pact with Lucifer—facilitated by the demon Mephistopheles—and his ultimate downfall as he fails to repent before his damnation.",
    "fullStory": "### Act I: The Awakening of Doctor Faustus\nThe Tragical History of the Life and Death of Doctor Faustus, commonly referred to simply as Doctor Faustus, is an Elizabethan tragedy by Christopher Marlowe, based on German stories about a scholar who sells his soul to the devil in exchange for magical power. Written in the late 16th century and first performed around 1594, the play follows Faustus’ rise as a magician through his pact with Lucifer—facilitated by the demon Mephistopheles—and his ultimate downfall as he fails to repent before his damnation.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Doctor Faustus",
        "role": "Protagonist",
        "desc": "Play by Christopher Marlowe"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Doctor Faustus endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "gargantua-and-pantagruel",
    "year": 1550,
    "displayDate": "c. 1550 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "1532–1564 novels by François Rabelais",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Gargantua and Pantagruel",
    "subtitle": "1532–1564 novels by François Rabelais",
    "summary": "The Five Books of the Lives and Deeds of Gargantua and Pantagruel, often shortened to Gargantua and Pantagruel or the Cinq Livres, is a pentalogy of novels written in the 16th century by François Rabelais. It tells the adventures of two giants, Gargantua and his son Pantagruel. The work is written in an amusing, extravagant, and satirical vein, features much erudition, vulgarity, and wordplay, and is regularly compared with the works of William Shakespeare and James Joyce. Rabelais was a polyglot, and the work introduced \"a great number of new and difficult words ... into the French language\".",
    "fullStory": "### Act I: The Awakening of Gargantua and Pantagruel\nThe Five Books of the Lives and Deeds of Gargantua and Pantagruel, often shortened to Gargantua and Pantagruel or the Cinq Livres, is a pentalogy of novels written in the 16th century by François Rabelais. It tells the adventures of two giants, Gargantua and his son Pantagruel. The work is written in an amusing, extravagant, and satirical vein, features much erudition, vulgarity, and wordplay, and is regularly compared with the works of William Shakespeare and James Joyce. Rabelais was a polyglot, and the work introduced \"a great number of new and difficult words ... into the French language\".\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Gargantua and Pantagruel",
        "role": "Protagonist",
        "desc": "1532–1564 novels by François Rabelais"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Gargantua and Pantagruel endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "orlando-furioso",
    "year": 1550,
    "displayDate": "c. 1550 CE",
    "era": "renaissance",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Epic poem by Ludovico Ariosto",
    "author": "Classical Greece & Rome Tradition",
    "title": "Orlando Furioso",
    "subtitle": "Epic poem by Ludovico Ariosto",
    "summary": "Orlando furioso is an Italian epic poem by Ludovico Ariosto which has exerted a wide influence on later culture. The earliest version appeared in 1516, although the poem was not published in its complete form until 1532. Orlando furioso is a continuation of Matteo Maria Boiardo's unfinished romance Orlando innamorato. In its historical setting and characters, it shares some features with the Old French La Chanson de Roland of the eleventh century, which tells of the death of Roland. The story is also a chivalric romance which stemmed from a tradition beginning in the Late Middle Ages and continuing in popularity in the 16th century and well into the 17th.",
    "fullStory": "### Act I: The Awakening of Orlando Furioso\nOrlando furioso is an Italian epic poem by Ludovico Ariosto which has exerted a wide influence on later culture. The earliest version appeared in 1516, although the poem was not published in its complete form until 1532. Orlando furioso is a continuation of Matteo Maria Boiardo's unfinished romance Orlando innamorato. In its historical setting and characters, it shares some features with the Old French La Chanson de Roland of the eleventh century, which tells of the death of Roland. The story is also a chivalric romance which stemmed from a tradition beginning in the Late Middle Ages and continuing in popularity in the 16th century and well into the 17th.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Orlando Furioso",
        "role": "Protagonist",
        "desc": "Epic poem by Ludovico Ariosto"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Greece & Rome.",
    "famousQuote": "“The memory of Orlando Furioso endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "journey-west-wuchengen",
    "year": 1592,
    "displayDate": "c. 1592 CE",
    "era": "renaissance",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Chang'an to Vulture Peak, India",
    "author": "Wu Cheng'en",
    "title": "Journey to the West: Sun Wukong and the Pilgrimage for Sacred Sutras",
    "subtitle": "Havoc in Heaven, the 81 Perils, Pigsy, Sandy, and the Victorious Buddha",
    "summary": "Monk Xuanzang journeys to India to retrieve Buddhist scriptures, escorted by Sun Wukong (Monkey King), Pigsy, and Sandy through eighty-one supernatural perils along the Silk Road.",
    "fullStory": "### Act I: Havoc in Heaven\nStone monkey Sun Wukong masters 72 transformations, claims the size-shifting iron staff, and battles heaven until Buddha traps him beneath Five Fingers Mountain.\n\n### Act II: The Pilgrims of the Silk Road\nFreed by monk Xuanzang, Monkey joins Pigsy and Sandy to battle the White Bone Demon and Spider Fiends.\n\n### Act III: Enlightenment\nReaching India, Monkey is crowned the Victorious Fighting Buddha as his golden headband dissolves.",
    "characters": [
      {
        "name": "Sun Wukong (Monkey King)",
        "role": "Trickster Hero",
        "desc": "Indestructible master of 72 transformations."
      },
      {
        "name": "Xuanzang (Tripitaka)",
        "role": "Holy Monk",
        "desc": "Spiritual pilgrim seeking wisdom."
      },
      {
        "name": "Zhu Bajie (Pigsy)",
        "role": "Glutton Disciple",
        "desc": "Former heavenly marshal."
      }
    ],
    "themes": [
      "Mind Monkey (Intellect vs Discipline)",
      "Spiritual Cultivation",
      "Brotherhood"
    ],
    "echoes": "Parallels Tolkien's Fellowship of the Ring and the Ramayana.",
    "famousQuote": "“A journey of ten thousand leagues begins with a single sincere step.” — Wu Cheng'en",
    "historicalContext": "Based on the historical 7th-century overland pilgrimage of Xuanzang to Nalanda University."
  },
  {
    "id": "shakespeare-hamlet",
    "year": 1601,
    "displayDate": "1599 – 1601 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Elsinore Castle, Denmark",
    "author": "William Shakespeare (The Bard of Avon)",
    "title": "Hamlet, Prince of Denmark: The Tragedy of Being and Nothingness",
    "subtitle": "The Ghost on the Ramparts, 'To Be or Not to Be', and the Poisoned Duel",
    "summary": "Prince Hamlet is visited by his father's ghost demanding vengeance against his usurping uncle Claudius. Paralyzed by existential doubt, Hamlet feigns madness in the ultimate tragedy of human intellect.",
    "fullStory": "### Act I: The Ghost and Mousetrap\nThe ghost reveals Claudius poisoned his ear. Hamlet stages a play to catch the king's guilty conscience.\n\n### Act II: 'To Be or Not to Be'\nHamlet meditates on suicide and action, confronting Ophelia and killing Polonius through an arras.\n\n### Act III: The Poisoned Duel\nIn a rigged fencing duel, Gertrude, Laertes, Claudius, and Hamlet all perish, ending with: 'The rest is silence.'",
    "characters": [
      {
        "name": "Prince Hamlet",
        "role": "Tragic Philosopher",
        "desc": "Intellectual paralyzed by existential doubt."
      },
      {
        "name": "King Claudius",
        "role": "Usurping Monarch",
        "desc": "Murdered his brother for the crown."
      }
    ],
    "themes": [
      "Action vs Inaction",
      "Appearance vs Reality",
      "Mortality"
    ],
    "echoes": "Echoes Orestes avenging Agamemnon in Aeschylus.",
    "famousQuote": "“There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy.”",
    "historicalContext": "The supreme pinnacle of dramatic poetry in the English language."
  },
  {
    "id": "cervantes-don-quixote",
    "year": 1605,
    "displayDate": "1605 – 1615 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "La Mancha, Spain",
    "author": "Miguel de Cervantes Saavedra",
    "title": "Don Quixote de la Mancha: The Founding Novel of Modern Literature",
    "subtitle": "The Woeful Countenance, Sancho Panza, Windmills, and Dulcinea",
    "summary": "An aging country gentleman driven mad by chivalric romances renames himself Don Quixote, riding a scrawny nag with his earthy squire Sancho Panza to right the wrongs of the world.",
    "fullStory": "### Act I: The Windmill Giants\nQuixote charges thirty windmills mistaking them for giants, blaming sorcery when thrown from his saddle.\n\n### Act II: Sancho's Island\nSancho governs the mock island of Barataria with surprising peasant wisdom and equity.\n\n### Act III: Return to Sanity\nDefeated in a duel, Quixote returns home, regains sanity, and dies peacefully as Alonso the Good.",
    "characters": [
      {
        "name": "Don Quixote",
        "role": "Idealist Knight",
        "desc": "Noble visionary whose madness exposes worldly cynicism."
      },
      {
        "name": "Sancho Panza",
        "role": "Pragmatic Squire",
        "desc": "Donkey-riding peasant of loyal common sense."
      }
    ],
    "themes": [
      "Idealism vs Realism",
      "Power of Imagination",
      "Invention of Modern Novel"
    ],
    "echoes": "Blueprint for buddy duos from Sherlock Holmes & Watson to Frodo & Sam.",
    "famousQuote": "“To dream the impossible dream, to fight the unbeatable foe...” — Quixote Ethos",
    "historicalContext": "Universally recognized as the first modern novel in world literature."
  },
  {
    "id": "macbeth",
    "year": 1606,
    "displayDate": "c. 1606 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Classics & Renaissance",
    "place": "Play by William Shakespeare",
    "author": "Classical Global Classics & Renaissance Tradition",
    "title": "Macbeth",
    "subtitle": "Play by William Shakespeare",
    "summary": "The Tragedy of Macbeth, often shortened to Macbeth, is a tragedy by William Shakespeare, estimated to have been first performed in 1606. It dramatises the physically violent and damaging psychological effects of political ambitions and power. It was first published in the Folio of 1623, possibly from a prompt book, and is Shakespeare's shortest tragedy. Scholars believe Macbeth, of all the plays that Shakespeare wrote during the reign of King James I, contains the most allusions to James, patron of Shakespeare's acting company.",
    "fullStory": "### Act I: The Awakening of Macbeth\nThe Tragedy of Macbeth, often shortened to Macbeth, is a tragedy by William Shakespeare, estimated to have been first performed in 1606. It dramatises the physically violent and damaging psychological effects of political ambitions and power. It was first published in the Folio of 1623, possibly from a prompt book, and is Shakespeare's shortest tragedy. Scholars believe Macbeth, of all the plays that Shakespeare wrote during the reign of King James I, contains the most allusions to James, patron of Shakespeare's acting company.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Macbeth",
        "role": "Protagonist",
        "desc": "Play by William Shakespeare"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Global Classics & Renaissance.",
    "famousQuote": "“The memory of Macbeth endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "hong-gildong-jeon",
    "year": 1650,
    "displayDate": "c. 1650 CE",
    "era": "renaissance",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "16th or 17th century Korean novel",
    "author": "Classical Japan & Korea Tradition",
    "title": "Hong Gildong jeon",
    "subtitle": "16th or 17th century Korean novel",
    "summary": "Hong Gildong jeon is a Korean novel, often translated as The Biography of Hong Gildong, written during the Joseon period. The novel is considered an iconic piece of Korean literature and culture. Its authorship has traditionally been attributed to Joseon statesman, Hŏ Kyun, though recent scholarship has called this into question.",
    "fullStory": "### Act I: The Awakening of Hong Gildong jeon\nHong Gildong jeon is a Korean novel, often translated as The Biography of Hong Gildong, written during the Joseon period. The novel is considered an iconic piece of Korean literature and culture. Its authorship has traditionally been attributed to Joseon statesman, Hŏ Kyun, though recent scholarship has called this into question.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Hong Gildong jeon",
        "role": "Protagonist",
        "desc": "16th or 17th century Korean novel"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Japan & Korea.",
    "famousQuote": "“The memory of Hong Gildong jeon endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  },
  {
    "id": "milton-paradise-lost",
    "year": 1667,
    "displayDate": "1667 – 1674 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Hell, Chaos, Heaven & Eden",
    "author": "John Milton (The Blind English Epicist)",
    "title": "Paradise Lost: The Cosmic Rebellion and the Fall of Man",
    "subtitle": "Pandæmonium, 'Better to Reign in Hell', the Serpent, and the World Before Them",
    "summary": "Dictated while blind by John Milton to 'justify the ways of God to men'. Depicts the rebellion of Satan, the construction of Pandæmonium in Hell, and the temptation and expulsion of Adam and Eve from Eden.",
    "fullStory": "### Act I: The Burning Lake\nSatan awakens in the fire of Hell, declaring: 'Better to reign in Hell than serve in Heaven!'\n\n### Act II: Flight across Chaos\nSatan crosses the abyss to Eden, slipping into the serpent to tempt Eve.\n\n### Act III: The Expulsion\nAdam eats the fruit in solidarity with Eve. Michael reveals human history before they walk out into the open world.",
    "characters": [
      {
        "name": "Satan (Lucifer)",
        "role": "Fallen Archangel",
        "desc": "Charismatic, tragic rebel driven by pride."
      },
      {
        "name": "Adam & Eve",
        "role": "First Parents",
        "desc": "Introduced moral choice into history."
      }
    ],
    "themes": [
      "Free Will and Conscience",
      "Pride and Evil",
      "Redemptive Hope"
    ],
    "echoes": "Dialogues directly with Homer and Dante.",
    "famousQuote": "“The mind is its own place, and in itself can make a Heaven of Hell, a Hell of Heaven.” — Milton",
    "historicalContext": "Dictated in total blindness following the English Civil War."
  },
  {
    "id": "goethe-faust",
    "year": 1808,
    "displayDate": "1772 – 1808 CE",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Wittenberg & Harz Mountains, Germany",
    "author": "Johann Wolfgang von Goethe",
    "title": "Faust: The Pact with Mephistopheles and the Eternal Quest",
    "subtitle": "The Scholar's Disillusionment, the Blood Signature, and Gretchen's Grace",
    "summary": "Aging polymath Dr. Heinrich Faust, disillusioned by bookish learning, signs a blood contract with the devil Mephistopheles: if Faust ever says to any fleeting moment, 'Stay, thou art so fair!', his soul belongs to Hell.",
    "fullStory": "### Act I: The Scholar's Study\nFaust has mastered philosophy, law, and medicine, yet finds no living meaning.\n\n### Act II: The Blood Pact\nMephistopheles appears as a black poodle, offering all worldly pleasures. Faust signs in blood, betting that his striving soul will never be satisfied with mere idle comfort.\n\n### Act III: Gretchen and Redemption\nFaust seduces innocent Gretchen, causing tragic ruin. In Part II, Faust devotes his final years to draining coastal marshes to build a free society for millions, saved by divine grace through the Eternal Feminine.",
    "characters": [
      {
        "name": "Dr. Heinrich Faust",
        "role": "The Striving Human",
        "desc": "Archetype of boundless human ambition."
      },
      {
        "name": "Mephistopheles",
        "role": "The Spirit of Denial",
        "desc": "The devil who constantly wills evil yet works the good."
      }
    ],
    "themes": [
      "The Faustian Bargain",
      "Boundless Human Striving",
      "Grace and Redemption"
    ],
    "echoes": "Transforms the medieval demonic legend into a cosmic meditation on human progress.",
    "famousQuote": "“Whoever strives with all his power, him can we redeem!” — Goethe, Faust Part II",
    "historicalContext": "Goethe spent sixty years writing Faust, the crowning jewel of German literature."
  },
  {
    "id": "kalevala",
    "year": 1835,
    "displayDate": "c. 1835 CE",
    "era": "renaissance",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "1835 Finnish epic poem compiled by Elias Lönnrot",
    "author": "Classical Northern & Celtic Europe Tradition",
    "title": "Kalevala",
    "subtitle": "1835 Finnish epic poem compiled by Elias Lönnrot",
    "summary": "The Kalevala is a 19th-century compilation of epic poetry, compiled by Elias Lönnrot from Finnish, Karelian and Ingrian folklore and mythology, telling a story about the Creation of the Earth, describing the controversies and retaliatory voyages between the peoples of the land of Kalevala called Väinölä and the land of Pohjola and their various protagonists and antagonists, as well as the construction and robbery of the mythical wealth-making machine Sampo.",
    "fullStory": "### Act I: The Awakening of Kalevala\nThe Kalevala is a 19th-century compilation of epic poetry, compiled by Elias Lönnrot from Finnish, Karelian and Ingrian folklore and mythology, telling a story about the Creation of the Earth, describing the controversies and retaliatory voyages between the peoples of the land of Kalevala called Väinölä and the land of Pohjola and their various protagonists and antagonists, as well as the construction and robbery of the mythical wealth-making machine Sampo.\n\n### Act II: The Heroic Ordeals and Trials\nA timeless chronicle of courage, wisdom, and mythological transcendence.\n\n### Act III: Enduring Immortality\nPreserved across world literature as an immortal foundation of human imagination.",
    "characters": [
      {
        "name": "Kalevala",
        "role": "Protagonist",
        "desc": "1835 Finnish epic poem compiled by Elias Lönnrot"
      }
    ],
    "themes": [
      "Mythology",
      "Cultural Heritage",
      "Timeless Wisdom"
    ],
    "echoes": "Shares foundational archetypes with epic literature across Northern & Celtic Europe.",
    "famousQuote": "“The memory of Kalevala endures throughout the ages.”",
    "historicalContext": "Preserved across millennia through oral traditions and classical manuscripts."
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { REGIONS, ERAS, SCRUBBER_DATES, STORIES_DATA };
}
