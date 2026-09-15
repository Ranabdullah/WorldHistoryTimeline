# -*- coding: utf-8 -*-
"""
Expands and generates the complete comprehensive stories_data.js file
with all major world mythologies, founding epics, and legendary writers.
"""

import json
import os

all_stories = [
  # 1. Deep Prehistory & Oceania
  {
    "id": "rainbow-serpent",
    "year": -10000,
    "displayDate": "c. 10,000+ BCE (65,000 Year Living Tradition)",
    "era": "prehistory",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Arnhem Land & Australian Red Centre",
    "author": "Aboriginal Songline Elders & Custodians",
    "title": "The Dreaming and the Great Rainbow Serpent (Almudj / Wagyl)",
    "subtitle": "The Creation of Earth's Waterways and the Living Songlines",
    "summary": "In the primordial Dreamtime (Tjukurpa), the giant Rainbow Serpent slithers across a barren earth, carving out gorges, rivers, and waterholes, establishing the sacred ancestral laws (Songlines) that connect all living things to Country.",
    "fullStory": """### Act I: The Awakening from the Deep Earth
In the time before time—known to the First Nations as the Dreaming or *Tjukurpa*—the cosmos was neither dead nor alive, but suspended in silent anticipation. Beneath the flat, sun-bleached crust of the ancient Australian shield slept the Rainbow Serpent, known by many names including *Borlung*, *Wagyl*, and *Almudj*. As ancestral winds stirred the earth, the serpent coiled in the deep subterranean reservoirs awakened. Driven by immense creative force, she pushed upward through the red sandstone, rupturing the horizon and releasing the first rains.

### Act II: Carving the Living Landscape
As the colossal serpent moved across the arid plains, her undulating body gouged deep trenches that became the mighty river systems of the continent—the Katherine Gorge, the Ord, and the Swan River. Wherever she rested, sacred waterholes (*billabongs*) formed, reflecting the crystalline arches of sunlight. The serpent breathed vitality into the slumbering world, summoning frogs from beneath the clay whose bellies held secret reservoirs of water. When the frogs opened their mouths to croak, living torrents poured forth, filling lakes and nurturing forests of eucalyptus, melaleuca, and red flowering kurrajong.

### Act III: The Sacred Law and Moral Order
The Rainbow Serpent was both a life-giving mother and an uncompromising enforcer of cosmic balance. She gave the ancestral clans their languages, ceremonies, and totem laws, binding each human to a specific tract of Country through unwritten *Songlines*—melodic navigational paths that cross thousands of miles. To violate the sacred waters or disrespect the land was to invoke the serpent’s tempestuous fury: towering thunderclouds, monsoonal floods, and lightning bolts that swallowed transgressors into bottomless sinkholes.

### Epilogue: An Ongoing Presence
Unlike Western creation myths that describe an event completed in the distant past, the Dreaming is an eternal present (*Everywhen*). The Rainbow Serpent still dwells in the deep subterranean aquifers and iridescent prisms of waterfalls, serving as an unbroken testament to the oldest continuous living culture on planet Earth.""",
    "characters": [
      {"name": "The Rainbow Serpent (Almudj / Wagyl)", "role": "Creator & Water Guardian", "desc": "Ancestral being whose slithering movement shaped mountains and river valleys."},
      {"name": "The Ancient Frogs (Tiddalik)", "role": "Water Keepers", "desc": "Stored all terrestrial water until releasing it in a great laughter-burst of life."},
      {"name": "Ancestral Elders", "role": "Songline Custodians", "desc": "Preserve the sacred oral maps passed across tens of thousands of years."}
    ],
    "themes": ["Living Earth", "Sacred Stewardship", "Eternal Present (Everywhen)", "Oral Memory"],
    "echoes": "Parallels the Norse Midgard Serpent (Jörmungandr), the Mesoamerican Feathered Serpent (Quetzalcoatl), and the Vedic dragon Vritra.",
    "famousQuote": "“The land is our mother; we belong to the land. The song does not end when the singer pauses, for the song is the ground itself.” — Traditional Yolngu Songline Teaching",
    "historicalContext": "Aboriginal rock art at sites like Arnhem Land and the Kimberley depicts Rainbow Serpent motifs dated by archaeologists between 6,000 and 10,000+ years ago."
  },

  # 2. China - Pangu & Nuwa
  {
    "id": "pangu-nuwa",
    "year": -5000,
    "displayDate": "c. 5000 – 2700 BCE (Mythic Deep Age)",
    "era": "prehistory",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Yellow River Valley & Mount Buzhou",
    "author": "Traditional Lore (Recorded by Xu Zheng & Huainanzi)",
    "title": "Pangu and Nüwa: The Cosmic Egg and the Broken Heavens",
    "subtitle": "The Cleaving of Yin-Yang and the Mother Goddess Who Smelted the Sky",
    "summary": "From a cosmic egg of chaos, the giant Pangu separates Heaven and Earth, sacrificing his body to become the rivers, mountains, and celestial stars. Later, the serpentine mother goddess Nüwa molds humanity from yellow clay and smelts five-colored stones to mend the torn celestial vault.",
    "fullStory": """### Act I: The Cosmic Egg and the Separation of Chaos
Before heaven and earth took shape, the universe was an unbroken egg of black mist containing the swirling opposites of Yin (heavy, dark, passive) and Yang (light, clear, active). For eighteen thousand years, the giant Pangu slept within this cosmic incubator, growing in immense power. When he awoke in darkness, he gripped a great axe of pure willpower and struck the shell. The light, pure elements floated upward to form the azure Heavens, while the heavy, murky sediment settled below to become the Earth.

### Act II: The Great Sacrifice and Body of the World
Fearing that Yin and Yang would collapse back into chaos, Pangu stood between them, holding up the celestial dome with his bare hands while his feet pressed down on the earth. Each day the sky grew ten feet higher, the earth ten feet thicker, and Pangu ten feet taller. After eighteen thousand more years of agonizing labor, the cosmos stabilized, and the exhausted giant collapsed into eternal slumber. His final breath became the roaring wind and drifting clouds; his voice the thunder; his left eye the golden Sun; his right eye the silver Moon; his blood the Yellow and Yangtze rivers; his flesh the fertile soil; his hair the stars and forests; and his bones the jade and granite peaks.

### Act III: Nüwa Molds Humanity from Yellow Clay
The world was vast and beautiful, yet silent. The mother-goddess Nüwa, possessing the upper body of a radiant woman and the tail of a serpent, wandered along the banks of the Yellow River. Feeling a profound loneliness, she knelt in the soft silt and molded tiny figures in her own likeness with two arms and two legs. As she blew divine breath upon them, they sprang to life, dancing and speaking. Realizing she could not mold enough figures by hand to populate the whole earth, she dipped a reed rope into the mud and flicked it across the land; every droplet of flung clay transformed into a human being.

### Act IV: The War of Gods and the Broken Sky
Peace was shattered when Gonggong, the ferocious God of Water, fought Zhurong, the God of Fire, for cosmic supremacy. Defeated, Gonggong smashed his head against Mount Buzhou, the great pillar supporting heaven. The pillar fractured; the celestial dome tore open, spewing forth fire, floods, and monstrous beasts. In her boundless love for her mortal children, Nüwa gathered five-colored stones from riverbeds, melted them in a crucible of cosmic fire, and patched the rent in the sky. She then severed the four legs of a giant celestial turtle to serve as unbreakable pillars for the four cardinal corners of the world.""",
    "characters": [
      {"name": "Pangu (盤古)", "role": "Primordial Creator Giant", "desc": "Separated Yin and Yang and transformed his dying body into the physical world."},
      {"name": "Nüwa (女媧)", "role": "Mother Goddess & Sky Restorer", "desc": "Molded human souls from clay and repaired the fractured heavens with molten stones."},
      {"name": "Gonggong (共工)", "role": "Water God of Chaos", "desc": "The titan whose rage shattered the pillar of Mount Buzhou."}
    ],
    "themes": ["Cosmic Duality (Yin-Yang)", "Self-Sacrifice", "Restoration of Harmony", "Motherhood of Humanity"],
    "echoes": "Pangu's bodily transformation matches the Norse giant Ymir and Vedic Purusha; Nüwa molding clay humans parallels Prometheus and the Genesis Adam.",
    "famousQuote": "“Heaven was formed from what was clear and light; Earth from what was heavy and turbid. Pangu stood between them, and the world was born of his breath.” — Sanwu Liji",
    "historicalContext": "Nüwa and Pangu iconography appears on Han dynasty tomb reliefs (202 BCE – 220 CE), synthesizing early agricultural observations with Daoist cosmology."
  },

  # 3. Mesopotamia - Enuma Elish
  {
    "id": "enuma-elish",
    "year": -1800,
    "displayDate": "c. 1800 – 1100 BCE (Babylonian Empire)",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Babylon & Euphrates River Valley",
    "author": "Babylonian Temple Scribes (Recited at Akitu New Year Festival)",
    "title": "Enuma Elish: The Babylonian Epic of Creation",
    "subtitle": "The Clash of Marduk and Tiamat, the Slaying of Qingu, and the Birth of Babylon",
    "summary": "When the primordial sea-dragon Tiamat rises in monstrous fury to destroy the younger gods, Marduk, champion of Babylon, steps forward with the four winds and lightning arrow. Splitting Tiamat in two, he fashions the vault of heaven and earth from her cosmic body and creates humankind to bear the labors of the gods.",
    "fullStory": """### Act I: The Primordial Waters of Chaos
When in the height heaven was not named, and the earth beneath did not yet bear a name, nothing existed except Apsu (the sweet water ocean), Tiamat (the salt water abyss), and Mummu (the primordial mist). Their waters mingled in unbroken silence, birthing generations of younger gods—Lahmu, Anshar, Anu, and Ea (Enki).

As the young gods grew energetic, their loud celebrations disturbed the peace of old Apsu. Driven mad by the noise, Apsu plotted to annihilate his offspring. But the wise and magical god Ea discovered the plot, cast a deep sleep spell upon Apsu, and slew him, claiming the crown of the sweet waters.

### Act II: The Wrath of Tiamat and the Army of Monsters
Grief and vengeance transformed Tiamat into a terrifying monster of cosmic destruction. She spawned an army of nightmare beasts: horned serpents, raging storm-demons, scorpion-men, and roaring sphinxes whose veins ran with venom instead of blood. At the head of her legion she placed her consort Qingu, fastening upon his chest the **Tablet of Destinies**, which granted absolute supreme authority over the universe.

One by one, the terrified gods failed to face her. Anu fled; Ea turned back in despair. The assembly of the gods was gripped by hopeless dread.

### Act III: The Rise of Marduk
In their darkest hour, the gods turned to Ea’s young son, Marduk, champion of Babylon. Marduk possessed four eyes that saw all things, four ears that heard every whisper, and lips that breathed living fire when he spoke. Marduk agreed to duel Tiamat under one non-negotiable condition: that the divine council grant him undisputed, eternal kingship over all gods in heaven and earth.

The gods gathered at a royal banquet, drank sweet beer, and cast their lots, crowning Marduk supreme king. Armed with a bow of lightning, a thunderous mace, the seven howling storm-winds, and a net woven from starlight, Marduk mounted his storm chariot driven by four untamable horses and rode out into the cosmic deep.

### Act IV: The Cleaving of the Dragon and the Birth of Man
When Tiamat opened her colossal jaws to swallow him whole, Marduk drove the furious Evil Wind straight down her throat. Her belly swelled like a balloon; Marduk loosed a blazing arrow that pierced her heart and split her belly. Standing upon her colossal corpse, he captured the dragon's eleven monstrous beasts and ripped the Tablet of Destinies from Qingu’s chest, pressing it into his own royal seal.

Marduk then split Tiamat’s body like a dried fish into two halves: with one half he formed the canopy of the heavens, setting the stars, sun, and moon in their orbits; with the other half he formed the fertile earth, causing the Tigris and Euphrates rivers to pour from her weeping eyes. Finally, taking the blood of the traitor Qingu mixed with clay, Marduk and Ea fashioned the first human beings to take up the labor of the gods—building the great ziggurat city of Babylon as the meeting point of heaven and earth.""",
    "characters": [
      {"name": "Marduk", "role": "Champion God of Babylon", "desc": "Wielder of the storm winds and lightning arrow who established order from chaos."},
      {"name": "Tiamat", "role": "Primordial Salt-Water Dragon", "desc": "Embodiment of cosmic chaos whose severed body became the vault of heaven and earth."},
      {"name": "Ea (Enki)", "role": "God of Wisdom & Magic", "desc": "Father of Marduk who conquered Apsu and assisted in the creation of humankind."},
      {"name": "Qingu", "role": "Tiamat's General", "desc": "Bearer of the Tablet of Destinies whose blood was used to spark human consciousness."}
    ],
    "themes": ["Order out of Chaos (Cosmogony)", "Divine Kingship", "Generational Struggle", "Sacred City Foundations"],
    "echoes": "Tiamat's battle directly echoes Yahweh subduing Leviathan in Psalm 74, Zeus fighting Typhon, and Thor battling Jörmungandr.",
    "famousQuote": "“When in the height heaven was not named, and the earth beneath did not yet bear a name... Marduk split the dragon like a shellfish into two parts; with half he formed the sky.” — Enuma Elish, Tablet I & IV",
    "historicalContext": "Recited annually on the fourth day of the Babylonian Akitu festival (spring equinox) to magically renew the cosmic order and the king's mandate to rule."
  },

  # 4. Egypt - Tale of the Shipwrecked Sailor & Sinuhe
  {
    "id": "tale-of-sinuhe",
    "year": -1900,
    "displayDate": "c. 1900 BCE (12th Dynasty Middle Kingdom)",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Thebes, Syrian Desert & Canaan",
    "author": "Anonymous Middle Kingdom Court Scribe",
    "title": "The Story of Sinuhe: The Exile and the Longing for the Nile",
    "subtitle": "Court Intrigue, Wandering in Foreign Sands, and the Return of the Egyptian Soul",
    "summary": "Considered the supreme literary masterpiece of Ancient Egyptian literature. When Pharaoh Amenemhat I is assassinated, courtier Sinuhe flees in panic into the deserts of Canaan. Rising to become a chieftain and hero in foreign lands, he is seized by an incurable ache for his homeland and is welcomed back in mercy by Pharaoh Senusret I to receive an eternal tomb on the Nile.",
    "fullStory": """### Act I: Panic in the Royal Tent
Sinuhe was an aristocratic courtier serving Queen Neferu and Crown Prince Senusret I. While on a military campaign in Libya, secret messengers arrive in the dead of night with catastrophic news: Pharaoh Amenemhat I has been murdered in his bedchamber in a palace coup. Overhearing conspiratorial whispers among rival princes, Sinuhe is gripped by sudden, irrational terror. Fearing he will be slaughtered in the coming bloodbath, he slips out of the military camp and flees east under the cover of night.

### Act II: Wandering the Scorch of the Desert
Sinuhe crosses the Nile on a rudderless raft and bypasses the fortified *Walls of the Ruler* guarding Egypt's eastern frontier. Collapsing in the scorching sands of Sinai, parched with a throat like fire, he prepares to die, whispering: *"This is the taste of death."* 

At that moment, he is rescued by an Asiatic Bedouin chieftain who recognizes Sinuhe’s aristocratic bearing. The chieftain gives him boiled milk and guides him from tribe to tribe until Sinuhe arrives in the lush highlands of Upper Retjenu (modern Syria-Canaan).

### Act III: The Foreign Chieftain and the Duel with the Strongman
The great local ruler Ammunenshi recognizes Sinuhe's brilliant diplomatic and military talents, giving him his eldest daughter in marriage and granting him fertile lands named Yaa—rich in figs, vines, honey, and barley. Sinuhe becomes a powerful tribal prince, fathering strong sons and defeating enemy raiders.

His supreme test arrives when a legendary local giant—the *Hero of Retjenu*, who has never been beaten—challenges Sinuhe to single combat to strip him of his cattle. The entire tribe gathers around the arena. As the giant charges, hurling spears and swinging a bronze battleaxe, Sinuhe dodges with supple Egyptian agility, shoots an arrow through the giant’s neck, and dispatches him with his own battleaxe. Sinuhe steps atop the fallen giant’s back and raises a shout of triumph, claiming all his wealth.

### Act IV: The Cry of the Aging Soul and the Pharaoh's Pardon
Yet despite fifty years of glory, wealth, and status, an agonizing void eats at Sinuhe’s heart as gray hairs crown his head. In Egyptian belief, to die in a foreign land and be buried in a crude sheepskin without mummification or sacred funeral rites was to lose one’s eternal soul in the afterlife. Sinuhe pours out his longing in prayer:
*"Let the King of Egypt have mercy on me! What is more important than that my body be buried in the land where I was born?"*

Miraculously, a royal courier arrives bearing a golden scroll from the new Pharaoh Senusret I. The King writes with warmth and humor:
*"Return to Egypt! You have not rebelled against us; you fled through your own heart's fear. Come back, and you shall not die in a sheepskin among barbarians. A pyramid of stone and a golden sarcophagus await you in the sacred cemetery of the West!"*

### Act V: The Triumphant Return
Weeping with joy, Sinuhe hands his chieftaincy to his eldest son and rides back to the Nile. Entering the golden palace at Lisht, Sinuhe prostrates himself before the Pharaoh in the dust. The King raises him up, dresses him in fine royal linen, washes him in sweet oils, and restores his aristocratic rank. Sinuhe lives out his final years in honored peace, watching stone masons carve his eternal tomb on the western bank of the Nile, content that his soul will sail the heavens with Osiris forever.""",
    "characters": [
      {"name": "Sinuhe", "role": "Courtier & Protagonist", "desc": "The Egyptian noble whose exile and redemption represents the universal human longing for home and spiritual peace."},
      {"name": "Pharaoh Senusret I", "role": "Magnanimous King of Egypt", "desc": "The wise monarch whose royal pardon brought Sinuhe back into the embrace of Ma'at."},
      {"name": "Ammunenshi", "role": "Ruler of Upper Retjenu", "desc": "The generous Canaanite king who welcomed and honored Sinuhe in his court."},
      {"name": "The Hero of Retjenu", "role": "Giant Champion", "desc": "Formidable warrior whose defeat established Sinuhe's legendary status in the Levant."}
    ],
    "themes": ["Exile and Longing for Homeland", "Redemption through Royal Mercy", "The Afterlife and Sacred Rites", "Courage and Identity"],
    "echoes": "Directly prefigures the Parable of the Prodigal Son in the New Testament, Odysseus’s longing for Ithaca, and David’s duel with Goliath.",
    "famousQuote": "“For what is greater than that my corpse should be joined to the earth in which I was born? O King, let me see the place where my heart rests!” — The Story of Sinuhe",
    "historicalContext": "Considered the jewel of Middle Kingdom literature (c. 1875 BCE), Sinuhe was so beloved that hundreds of copies on papyri and limestone ostraca have been unearthed across Egypt."
  },

  # 5. Levant - Genesis & The Great Deluge of Noah
  {
    "id": "genesis-deluge",
    "year": -2900,
    "displayDate": "c. 2900 – 1000 BCE (Ancient Near East & Hebrew Scripture)",
    "era": "bronze",
    "regionId": "levant",
    "regionName": "Levant & Biblical Traditions",
    "place": "Canaan, Mesopotamia & Mount Ararat",
    "author": "Biblical Tradition (Torah / Genesis)",
    "title": "Genesis: The Garden, the Fall, and Noah’s Ark",
    "subtitle": "The Tree of Knowledge, the Global Deluge, and the Covenant of the Rainbow",
    "summary": "From the breathing of life into Adam in Eden to the tragedy of the forbidden fruit, humanity multiplies across the earth. When human violence corrupts the world, Noah builds a gopher-wood ark to preserve every living species through forty days of deluge, receiving the eternal sign of the rainbow covenant.",
    "fullStory": """### Act I: The Garden of Eden and the Fall
In the beginning, God formed man from the dust of the ground and breathed into his nostrils the breath of life, naming him Adam. Placing him in the lush Garden of Eden, watered by four great rivers, God fashioned woman, Eve, from Adam’s rib as an equal companion. In the center of the garden grew the Tree of Life and the Tree of Knowledge of Good and Evil, whose fruit they were forbidden to eat under penalty of mortality.

A subtle serpent convinced Eve that eating the fruit would not bring death, but would open their eyes to become like God. Eve ate and gave to Adam. Their innocence evaporated; recognizing their nakedness, they hid behind fig leaves. Expelled from paradise into a world of sweat, thorns, and mortality, cherubim with flaming spinning swords were placed at the gate of Eden to guard the way to the Tree of Life.

### Act II: The World of Violence and the Righteous Carpenter
Ten generations later, human violence and corruption filled the earth. Seeing that every inclination of the human heart was only evil continually, God resolved to blot out human and animal life from the face of the earth. But Noah, a righteous man blameless among his generation, found grace in the eyes of God.

God instructed Noah: *"Make yourself an ark of gopher wood, three hundred cubits long, fifty cubits wide, and thirty cubits high; coat it inside and out with pitch."* Into this floating sanctuary, Noah brought his wife, his three sons (Shem, Ham, Japheth), their wives, and pairs of every clean and unclean beast, bird, and creeping creature on earth.

### Act III: The Fountains of the Deep and the Raven's Flight
The windows of heaven tore open and all the fountains of the great deep burst forth. For forty days and forty nights, torrential rain swept the planet, drowning mountains beneath fifteen cubits of water until every creature outside the ark perished. For one hundred and fifty days, the ark floated upon the boundless silent ocean.

God remembered Noah and sent a wind over the waters. The ark came to rest on the peaks of Mount Ararat. Noah sent out a raven, which flew back and forth until the waters dried. Next he sent out a dove; the first time she found no resting place, but the second time she returned in the evening bearing a fresh, plucked olive leaf in her beak—the eternal emblem of peace and restored life.

### Act IV: The Altar and the Rainbow Covenant
Noah, his family, and the animals walked out onto the dry earth. Noah built an altar of thanksgiving. Smelling the soothing aroma, God established an unconditional covenant with all living flesh: never again would the waters become a flood to destroy all life. Setting the luminous multi-colored rainbow across the storm clouds, God declared it the eternal token of divine mercy.""",
    "characters": [
      {"name": "Noah", "role": "Righteous Patriarch & Ark Builder", "desc": "Preserved the seed of humanity and all living creatures through faith and obedience."},
      {"name": "Adam & Eve", "role": "First Humans", "desc": "Created in Eden whose choice brought moral knowledge and mortality into human history."},
      {"name": "The Serpent", "role": "Deceiver", "desc": "Cunning creature that tempted humanity away from innocence."}
    ],
    "themes": ["Creation and Fall", "Cosmic Cleansing and Renewal", "The Covenant of Mercy", "Righteousness vs Corruption"],
    "echoes": "Shares nearly identical plot mechanics with the Mesopotamian Atrahasis and Gilgamesh Utnapishtim floods, including the ship, animals, and birds.",
    "famousQuote": "“I have set my rainbow in the clouds, and it will be the sign of the covenant between me and the earth.” — Genesis 9:13",
    "historicalContext": "Widespread catastrophic flooding in the Tigris-Euphrates and Black Sea basins following post-glacial sea level rises provided the historical kernel for Near Eastern flood accounts."
  },

  # 6. Greece - Hesiod & Theogony
  {
    "id": "hesiod-theogony",
    "year": -700,
    "displayDate": "c. 700 BCE (Archaic Greece)",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Mount Helicon & Mount Olympus",
    "author": "Hesiod (Shepherd-Poet of Ascra)",
    "title": "Theogony & Works and Days: The Titanomachy and Pandora’s Box",
    "subtitle": "The Birth of the Gods, Cronus’s Sickle, Prometheus’s Fire, and the Sole Remaining Hope",
    "summary": "Hesiod’s foundational Greek poetic genealogy. From Chaos, Gaia, and Uranus emerges the brutal reign of the Titan Cronus, who swallows his children. Zeus escapes to lead the ten-year Titanomachy war. When Prometheus steals sacred fire for humanity, Zeus punishes mankind with Pandora, whose jar releases all earthly evils—leaving only Hope trapped inside.",
    "fullStory": """### Act I: The Shepherds of Mount Helicon and Primordial Chaos
While pasturing sheep on the slopes of Mount Helicon, the humble farmer Hesiod is visited by the nine Muses, daughters of Zeus, who breathe a divine poetic voice into his chest and command him to sing the origins of the immortal gods.

In the beginning existed only Chaos (the gaping void), followed by Gaia (Earth), Tartarus (the Underworld abyss), and Eros (the principle of love). Gaia birthed Uranus (Sky) to cover her on all sides. Uranus locked their monstrous children—the hundred-handed Hecatoncheires and the one-eyed Cyclopes—deep within Gaia's womb. Groaning in agony, Gaia forged a flint sickle and urged her Titan sons to rebel. The youngest, cunning Cronus, ambushed Uranus, severing his genitals with the sickle; from the sea foam around the severed flesh rose Aphrodite, the goddess of beauty.

### Act II: Cronus Swallows His Brood and the Rise of Zeus
Becoming ruler of the cosmos, Cronus learned of a prophecy that he too would be overthrown by his own son. To cheat fate, Cronus swallowed each of his children—Hestia, Demeter, Hera, Hades, and Poseidon—the moment they were born from his wife Rhea.

When pregnant with her sixth child, Rhea fled to a cave in Crete, giving birth to Zeus. She presented Cronus with a smooth stone swaddled in blankets, which he gulped down unsuspectingly. Raised on the milk of the goat Amalthea, the adult Zeus returned, fed Cronus a poisoned honey-drink that forced him to vomit up the stone and his grown siblings, and freed the Cyclopes, who forged Zeus's thunderbolt, Poseidon's trident, and Hades' helm of darkness.

### Act III: The Titanomachy and the Fall to Tartarus
For ten grueling years, the Olympian gods fought the elder Titans in the **Titanomachy**. The cosmos shook as mountains were ripped from their roots and hurled as projectiles. Zeus finally summoned the hundred-handed giants, who unleashed a barrage of three hundred boulders at a time, burying the Titans and chaining them forever in the bronze-walled pits of Tartarus.

### Act IV: Prometheus, the Stolen Fire, and Pandora’s Jar
Humanity lived in hardship. The Titan Prometheus, whose name means *Forethought*, loved mortals and tricked Zeus into accepting the bones and fat of animal sacrifices, leaving the nourishing meat for mankind. In anger, Zeus withheld fire from the earth. Prometheus climbed to the chariot of the Sun, caught a spark in the hollow stalk of a giant fennel plant, and brought fire down to humanity, inaugurating technology and civilization.

Enraged by the theft, Zeus chained Prometheus to a desolate crag in the Caucasus Mountains, where an eagle ate his regenerating liver every day. To punish mankind, Zeus commanded Hephaestus to fashion the first woman, **Pandora**, adorned with gifts by all the gods: beauty from Aphrodite, speech from Hermes, and charm from Athena. 

Zeus gave Pandora a sealed terracotta jar (*Pithos*), forbidding her from ever opening it. Overcome by irresistible curiosity, Pandora lifted the lid. In an instant, every plague, sickness, sorrow, toil, and misery flew out into the world to afflict mankind forever. Weeping in horror, Pandora slammed the lid down just in time—trapping **Hope** (*Elpis*) alone at the bottom of the jar to sustain the human spirit through all earthly suffering.""",
    "characters": [
      {"name": "Hesiod", "role": "Archaic Shepherd-Poet", "desc": "Chronicled the moral and genealogical origins of the Greek cosmos."},
      {"name": "Zeus", "role": "King of the Olympians", "desc": "Wielder of the thunderbolt who established cosmic order over the chaotic Titans."},
      {"name": "Prometheus", "role": "Titan Champion of Humanity", "desc": "Stole sacred fire and suffered eternal torment for advancing human civilization."},
      {"name": "Pandora", "role": "First Mortal Woman", "desc": "Whose curiosity opened the jar of worldly sorrows, leaving humanity with Hope."}
    ],
    "themes": ["Origins of Cosmic Order", "Hubris and Divine Punishment", "The Problem of Evil and Suffering", "Hope as the Anchor of Humanity"],
    "echoes": "Pandora's curiosity and fruit of knowledge parallels Eve in Genesis; Prometheus mirrors Lucifer/Loki as the fire/knowledge bringer.",
    "famousQuote": "“Only Hope remained there in an unbreakable home within under the rim of the great jar, and did not fly out at the door.” — Hesiod, Works and Days",
    "historicalContext": "Composed around the same period as Homer's Iliad, Hesiod's works provided ancient Greeks with their standardized theological framework and calendar of agricultural life."
  },

  # 7. Rome - Virgil & The Aeneid
  {
    "id": "virgil-aeneid",
    "year": -19,
    "displayDate": "29 – 19 BCE (Augustan Rome)",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Troy, Carthage, Cumae & Tiber Valley",
    "author": "Publius Vergilius Maro (Virgil)",
    "title": "The Aeneid: The Founding of the Roman Destiny",
    "subtitle": "Arms and the Man, the Fire of Troy, Dido's Tragic Curse, and the Golden Bough",
    "summary": "Rome’s supreme national epic. Trojan prince Aeneas escapes the burning ruins of Troy carrying his elderly father Anchises on his back. Enduring a doomed romance with Queen Dido of Carthage and descending to the Underworld to glimpse the future glory of Rome, he reaches Italy to wage war for the destiny of the Roman people.",
    "fullStory": """### Act I: Flight from the Ashes of Troy
*"I sing of arms and the man..."* When the Greeks breach Troy through the wooden horse, Prince Aeneas, son of the goddess Venus and mortal Anchises, fights desperately in the burning streets until the ghost of Hector orders him to flee: Troy's gods and destiny are now in his hands. Aeneas carries his crippled father Anchises upon his shoulders, leads his young son Ascanius (Iulus) by the hand, and gathers survivors into a fleet of twenty ships, embarking on a long journey westward to find a promised new homeland in Italy.

### Act II: The Queen of Carthage and the Curse of Dido
Driven across the Mediterranean by the relentless hatred of the goddess Juno, Aeneas is shipwrecked on the coast of North Africa. There he is welcomed by Queen Dido, who is building the magnificent city of Carthage. Cupid strikes Dido with an overwhelming passion for Aeneas.

During a divine thunderstorm orchestrated by Juno and Venus, Aeneas and Dido take shelter in a cave and consummate their union. But Jupiter dispatches Mercury with a stern command: Aeneas cannot linger in soft luxury—his sacred duty (*Pietas*) is to found an empire for his descendants in Italy. 

When Aeneas prepares his fleet to depart in secret, Dido confronts him in fury and heartbreak. Seeing his sails vanish on the horizon, Dido builds a colossal funeral pyre, climbs to the summit, stabs herself with Aeneas’s sword, and utters an immortal dying curse that sows eternal enmity between Carthage and Rome:
*"Rise up, some avenger from my bones, to pursue the Dardan settlers with fire and sword!"* (Prefiguring Hannibal Barca).

### Act III: The Golden Bough and the Underworld
Arriving at Cumae in Italy, Aeneas consults the Sibyl (prophetess) in her dark cave. Plucking the magical **Golden Bough** from a sacred grove as an offering to Proserpina, Aeneas descends through the cavernous gate of the Underworld.

Crossing the River Styx with the ferryman Charon, Aeneas passes through the Mourning Fields, where he sees the silent, weeping shade of Dido; she turns away from his tears into the shadows without speaking a word. In the Elysian Fields of the blessed, Aeneas meets the shade of his father Anchises, who reveals the great **Pageant of Future Heroes**—the unborn souls waiting to be reincarnated as Romulus, the Scipios, Julius Caesar, and Augustus Caesar, who will establish an empire of law and peace without end:
*"Roman, remember by your strength to rule Earth's peoples—these shall be your arts: to impose the ways of peace, to spare the defeated, and to crush the proud in war!"*

### Act IV: The War in Latium and the Duel of Turnus
Emerging from the Gates of Sleep, Aeneas reaches the mouth of the River Tiber. King Latinus offers his daughter Lavinia in marriage, but Juno incites Lavinia’s fierce suitor Turnus, king of the Rutulians, into a brutal war.

Aeneas receives a divine shield forged by Vulcan depicting the future naval triumph of Augustus at Actium. In the climactic final duel, Aeneas fells Turnus. When Turnus begs for his life for the sake of his aged father, Aeneas is on the verge of showing mercy—until he catches sight of the golden belt of his fallen youth-comrade Pallas hanging across Turnus’s shoulder. Blazing with vengeful fury, Aeneas plunges his sword into Turnus’s chest, sending his soul groaning into the underworld as the curtain falls on the birth of Rome.""",
    "characters": [
      {"name": "Aeneas", "role": "Trojan Prince & Father of Rome", "desc": "Embodiment of *Pietas* (devotion to duty, gods, and family) who sacrificed personal happiness for history."},
      {"name": "Dido (Elissa)", "role": "Queen of Carthage", "desc": "Tragic queen whose abandoned love became the foundational myth of Rome’s Punic Wars."},
      {"name": "Turnus", "role": "King of the Rutulians", "desc": "Fierce Italian warrior who fought against the foreign destiny of the Trojans."},
      {"name": "Anchises", "role": "Father of Aeneas", "desc": "Carried on Aeneas’s shoulders from Troy, who reveals the future grandeur of Rome in the Underworld."}
    ],
    "themes": ["Duty (Pietas) over Passion (Furor)", "The Cost of Empire and Historical Destiny", "Tragedy of Forsaken Love", "Civilization and Law"],
    "echoes": "Blends the Odyssey (sea voyage, Cyclops, underworld descent) with the Iliad (brutal land warfare in Latium).",
    "famousQuote": "“Tu regere imperio populos, Romane, memento—hae tibi erunt artes: pacique imponere morem, parcere subiectis et debellare superbos.” (Roman, remember by your power to rule the peoples...) — Aeneid VI",
    "historicalContext": "Commissioned during the reign of Rome's first emperor Augustus to provide the Roman Empire with a divine founding myth linking their lineage to Venus and ancient Troy."
  },

  # 8. India - Kalidasa & Shakuntala
  {
    "id": "kalidasa-shakuntala",
    "year": 400,
    "displayDate": "c. 4th – 5th Century CE (Gupta Golden Age)",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Kanva's Forest Hermitage & Hastinapura",
    "author": "Mahakavi Kalidasa (Shakespeare of India)",
    "title": "Abhijnanashakuntala: The Recognition of Shakuntala",
    "subtitle": "The Forest Maiden, the Lost Signet Ring, the Sage's Curse, and the Emperor Bharata",
    "summary": "The crowning masterpiece of Sanskrit dramatic poetry. King Dushyanta falls in love with Shakuntala, daughter of the sage Vishwamitra and nymph Menaka, in a sacred forest hermitage. A short-tempered sage's curse causes the king to forget her completely until a fisherman recovers a lost signet ring from the belly of a carp.",
    "fullStory": """### Act I: The Chariot in the Sacred Grove
While pursuing a blackbuck deer on a royal hunt, King Dushyanta of Hastinapura enters the tranquil forest hermitage of the sage Kanva. There he catches sight of Shakuntala—the foster daughter of the sage, born of the celestial nymph Menaka—watering jasmine plants with her companions. Struck by her natural beauty, Dushyanta reveals himself, and the two enter into a secret *Gandharva* marriage (union by mutual consent). Before returning to his capital, Dushyanta gives Shakuntala a royal signet ring engraved with his name, promising to send an imperial escort to bring her to the palace.

### Act II: The Curse of Sage Durvasa
Lost in romantic daydreams of her absent husband, Shakuntala fails to hear the arrival of the notoriously short-tempered ascetic Sage Durvasa calling for hospitality at the hermitage gate. Insulted by what he perceives as deliberate disrespect, Durvasa pronounces a terrifying curse:
*"He of whom you think with such single-minded devotion, ignoring a guest like me—he shall forget you completely, even when reminded, as a drunkard forgets what he said before!"*

Shakuntala’s companions beg the sage for mercy. Softening slightly, Durvasa declares that the curse will be broken if Shakuntala presents the king with a token of recognition (*Abhijnana*): his own signet ring.

### Act III: The Lost Ring and the Humiliation in the Court
Unaware of the curse, a pregnant Shakuntala journeys to the royal palace in Hastinapura. On the way, while performing morning prayers at the sacred ferry of Sachitirtha, the signet ring slips from her finger into the river, swallowed by a passing carp.

Arriving at the imperial court, Shakuntala stands before King Dushyanta. Due to the curse, the king gazes at her with cold eyes, having no recollection of ever meeting or marrying her. When Shakuntala attempts to produce the ring, her hand is empty. Accused of being an impostor seeking royal status, Shakuntala weeps in despair and calls upon Mother Earth. In a flash of light, a celestial beam descends from the heavens, and her nymph-mother Menaka spirits Shakuntala away to the celestial hermitage of Sage Maricha atop Mount Hemakuta.

### Act IV: The Fisherman and the Agony of Memory
Months later, a poor city fisherman catches a large carp in the river. Slicing open its belly, he finds a glittering royal signet ring and takes it to market. Arrested by royal guards for theft, he is brought before the King.

The moment Dushyanta’s eyes fall upon his signet ring, the curse shatters like glass. A tidal wave of memories, love, and agonizing guilt crashes over his soul. He realizes he cruelly rejected his own lawful wife and unborn child. Overcome with remorse, the king cancels all palace celebrations, spends his days painting portraits of Shakuntala while weeping, and falls into deep melancholy.

### Act V: The Boy Who Played with Lions
Years later, King Dushyanta is summoned by Indra, king of the gods, to battle celestial demons. After victory, descending through the clouds in a celestial chariot, Dushyanta visits the sacred hermitage of Sage Maricha.

There he encounters a fearless young boy playing with a lion cub, prying open its jaws to count its teeth. The king feels an instinctive, electric surge of paternal love. When the boy’s enchanted protective amulet drops to the earth, Dushyanta picks it up safely—a feat impossible for anyone other than the boy’s true father without the amulet turning into a venomous snake.

Shakuntala appears, dressed in simple ascetic bark garments. Dushyanta falls at her feet in tears, begging for forgiveness. Reunited in divine grace, they return to Hastinapura with their son, **Bharata**—who grows to become the legendary universal emperor (*Chakravartin*) after whom India takes its traditional name: **Bharat**.""",
    "characters": [
      {"name": "Shakuntala", "role": "Forest Maiden & Heroine", "desc": "Daughter of nymph Menaka whose grace, dignity, and endurance triumphed over the curse of oblivion."},
      {"name": "King Dushyanta", "role": "Monarch of Hastinapura", "desc": "Noble ruler who suffered profound remorse after the veil of forgetfulness lifted."},
      {"name": "Sage Durvasa", "role": "Wrathful Ascetic", "desc": "Whose fiery curse drove the tragic separation of the lovers."},
      {"name": "Bharata (Sarvadamana)", "role": "Lion-Tamer Prince", "desc": "The miraculous child who became the founding emperor of India (Bharat)."}
    ],
    "themes": ["Love and Separation (Shringara Rasa)", "The Fragility of Human Memory", "Fate vs Karma", "Nature vs Courtly Civilization"],
    "echoes": "The lost recognition token inside a fish parallels the Ring of Polycrates in Herodotus and Solomon's lost signet ring in Islamic lore.",
    "famousQuote": "“Wouldst thou the young year's blossoms and the fruits of its decline? Wouldst thou what charms and enraptures, what sates and nourishes? I name thee, O Shakuntala, and all at once is said.” — Johann Wolfgang von Goethe",
    "historicalContext": "Kalidasa, jewel of the court of Chandragupta II Vikramaditya, elevated Sanskrit drama to its golden age; Sir William Jones's 1789 English translation astonished European Romantic poets."
  },

  # 9. Northern Europe - Beowulf
  {
    "id": "beowulf-epic",
    "year": 750,
    "displayDate": "c. 750 – 1000 CE (Anglo-Saxon England)",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Heorot Hall (Denmark) & Geatland (Sweden)",
    "author": "Anonymous Christian Anglo-Saxon Scop (Bard)",
    "title": "Beowulf: The Monster in the Mist and the Dragon’s Hoard",
    "subtitle": "Grendel in Heorot, the Mere of the Sea-Hag, and the King’s Last Battle",
    "summary": "The premier epic poem of Old English literature. The Geatish warrior Beowulf sails to Denmark to rid King Hrothgar’s great mead-hall Heorot of the demonic flesh-eating monster Grendel and Grendel’s vengeful mother, before dying in old age slaying a fire-breathing dragon.",
    "fullStory": """### Act I: The Shadow in the Mead-Hall
In the land of the Danes, King Hrothgar builds **Heorot**—the greatest timber mead-hall on earth, where warriors drink golden mead, receive gold rings, and listen to the scop sing of the world’s creation. But the sound of harp and laughter enrages **Grendel**, a demonic fiend descended from the biblical murderer Cain, who dwells in the dark, mist-choked fens.

Under the cover of night, Grendel bursts through the heavy iron-bolted doors of Heorot, slaughtering thirty sleeping warriors and devouring their flesh. For twelve long winters, Heorot stands empty and haunted at night; no Dane can defeat the monster.

### Act II: Beowulf and the Bare-Handed Duel
Hearing of Hrothgar's plight, Beowulf—a young hero of the Geats (southern Sweden) endowed with the strength of thirty men in his handgrip—crosses the sea with fourteen warriors. Pledging to fight Grendel with no sword or armor, matching the beast with bare hands, Beowulf waits in the dark hall while his comrades sleep.

Grendel bursts through the doors, teeth gnashing and eyes blazing like balefire. As the monster reaches to devour him, Beowulf locks his arm in an iron grip of supernatural power. The two crash against walls and timber benches until Beowulf twists Grendel’s arm with such colossal force that tendons snap and the entire shoulder rips cleanly from the torso. Howling in mortal agony, Grendel flees into the fens to bleed to death, and Beowulf nails the bloody claw to the high rafters of Heorot.

### Act III: The Mere of Grendel's Mother
Celebration is cut short the following night when **Grendel’s Mother**, a monstrous sea-hag of the deep, emerges from the fens, murders Hrothgar’s closest counselor Æschere, and steals back her son’s severed arm.

Beowulf tracks her to a terrifying, boiling mere shrouded by frozen trees, where serpents and water-monsters writhe. Diving into the dark abyss for hours, Beowulf is dragged into an underwater cavern. The borrowed sword *Hrunting* fails to pierce her scaly hide; she pins him to the ground, trying to plunge her dagger into his chest, saved only by his woven chainmail shirt. Spotting an ancient, giant-forged sword hanging on the cavern wall, Beowulf lifts the massive blade, cuts off the hag’s head, and severs Grendel’s dead head as well—the monster's acidic blood melting the sword blade down to the golden hilt.

### Act IV: The Dragon and the Funeral Pyre
Beowulf returns to Geatland in triumph, eventually ruling as a wise, peaceful king for fifty years. But his peace is shattered when a runaway slave steals a gem-studded golden cup from the burial barrow of a sleeping, five-hundred-year-old **fire-drake (dragon)**.

Enraged by the theft, the dragon flies through the night sky, vomiting sheets of flame that burn villages and the royal hall to ash. Though an old man, Beowulf refuses to let his people perish. Armed with an iron shield and sword *Nægling*, Beowulf confronts the beast at its barrow. When the sword shatters against the dragon's scales and all his companions flee into the woods in terror, only young **Wiglaf** stands by his king. 

The dragon sinks its venomous fangs into Beowulf's neck. With his dying strength, Beowulf draws his hunting knife and slashes the beast’s belly, slaying the dragon. As venom burns his veins, Beowulf commands Wiglaf to build a great coastal beacon-barrow (*Beowulf’s Barrow*) so sailors crossing the stormy seas may navigate by his memory, dying as the last true hero of the heroic age.""",
    "characters": [
      {"name": "Beowulf", "role": "Geatish Hero & King", "desc": "Peerless warrior whose life illustrates the Anglo-Saxon ideals of courage, strength, and sacrificial kingship."},
      {"name": "Grendel", "role": "Fiend of the Fens", "desc": "Cannibalistic monster cursed by God who terrorized the hall of Heorot."},
      {"name": "Grendel's Mother", "role": "Sea-Hag of the Abyss", "desc": "Vengeful matriarch of the boiling mere."},
      {"name": "Wiglaf", "role": "Loyal Thane", "desc": "The only warrior who refused to abandon Beowulf during his final battle with the dragon."},
      {"name": "Hrothgar", "role": "King of the Danes", "desc": "Aging monarch whose mead-hall was saved by Beowulf's courage."}
    ],
    "themes": ["Heroic Code (Comitatus)", "Transience of Life and Glory (Wyrd/Fate)", "Good vs Elemental Monsters", "Sacrificial Leadership"],
    "echoes": "Directly inspired J.R.R. Tolkien's The Hobbit (Smaug the dragon) and The Lord of the Rings; parallels Heracles fighting the Hydra.",
    "famousQuote": "“Fate often saves an undoomed man when his courage holds!” (Wyrd oft nereð unfægne eorl, þonne his ellen deah!) — Beowulf, Line 572",
    "historicalContext": "Preserved in a single unique manuscript (the Nowell Codex, British Library Cotton MS Vitellius A. XV), which narrowly survived the disastrous Ashburnham House fire of 1731."
  },

  # 10. Persia - Nizami & Layla and Majnun
  {
    "id": "nizami-layla-majnun",
    "year": 1188,
    "displayDate": "c. 1188 CE (Seljuk Persia)",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Arabian Peninsula & Persian Literary Realm",
    "author": "Nizami Ganjavi (Master of the Persian Masnavi)",
    "title": "Layla and Majnun: The Romeo and Juliet of the East",
    "subtitle": "Qays’s Madness in the Desert, the Animals of the Wastes, and Love as a Path to the Infinite",
    "summary": "The supreme tragic romance of Islamic literature. Qays falls into an all-consuming love with Layla in childhood. When Layla’s father rejects his marriage proposal, Qays loses his mind, becoming Majnun (the Madman), wandering naked in the desert composing verses that tame wild beasts, transforming human passion into divine mystic union.",
    "fullStory": """### Act I: The Schoolroom and the Gaze of Destiny
In the Arabian desert, young Qays, son of a respected Bedouin chieftain, meets the radiant Layla at school. In a single exchange of glances, their souls are welded together in an irresistible, divine passion. 

As they grow, Qays makes no attempt to hide his boundless adoration, singing ecstasy-filled poems about Layla through the village streets. Scandalized by this public display, which violates traditional tribal decorum, Layla’s father forbids her from ever seeing him again. When Qays’s father arrives with sixty camels loaded with gold to formally ask for Layla's hand, her father angrily refuses, declaring he will never marry his daughter to a madman.

### Act II: The Desert of Madness (Majnun)
Shattered by the rejection, Qays tears his clothes, casts off his shoes, and flees into the blistering desert wastes of the Najd. People begin calling him **Majnun**—"The One Possessed by Spirit/Madness." 

Majnun lives like a phantom among the dunes, eating roots and drinking from desert pools. He carves Layla's name with a reed into every stone, dune, and tree trunk. His profound grief and pure, egoless love emit a spiritual radiance that tames the wilderness: ferocious lions, leopards, gazelles, and wolves gather peacefully in a circle around him, shielding him from desert storms while he recites his haunting ghazals to the stars.

### Act III: The Forced Marriage and the Secret Message
Layla is locked within her family tent, weeping constantly while gazing out into the sands. To preserve family honor, she is forced into marriage with a wealthy, handsome nobleman named Ibn Salam. Though she lives in his house, Layla refuses to let him touch her, threatening to take her own life if he steps within an arm's reach.

A compassionate knight named Nawfal befriends Majnun in the desert and wages war against Layla’s tribe to force them to give her to Majnun. But in the midst of battle, Majnun is seen praying for Layla's tribe to win, explaining: *"How can I wish harm upon the kin of my beloved? Their victory is my soul's peace!"* Realizing that Majnun's love exists on a plane far beyond earthly politics, Nawfal withdraws his sword in awe.

### Act IV: The Garden Meeting and the Final Unity
Years pass. Ibn Salam falls ill and dies. Free at last, Layla arranges a secret meeting with Majnun in a walled palm garden. 

When Majnun arrives, surrounded by his retinue of lions and gazelles, the two lovers stand ten paces apart beneath the date palms. They do not embrace or touch: their love has transcended physical bodies, becoming a pure spiritual light that cannot survive the coarseness of mortal contact. Majnun recites a final, incandescent poem of transcendent devotion and retreats back into the sands.

Soon after, broken by lifelong grief, Layla falls ill and passes away, calling Majnun's name with her dying breath. Hearing of her death, Majnun rushes to her tomb, wraps his arms around the cold stone, and weeps until his soul leaves his body. The wild animals stand guard over the two lovers' tomb for a full year so no one can disturb their eternal sleep. In a famous dream, a holy man sees Layla and Majnun in the gardens of Paradise, crowned with starlight, united forever where no wall can ever divide them.""",
    "characters": [
      {"name": "Qays (Majnun)", "role": "The Possessed Poet", "desc": "Archetype of the mystic lover whose obsession stripped away all worldly ego."},
      {"name": "Layla", "role": "The Luminous Beloved", "desc": "Embodiment of unattainable beauty and steadfast spiritual devotion."},
      {"name": "Layla's Father", "role": "Tribal Patriarch", "desc": "Enforcer of social convention who separated the lovers."},
      {"name": "Nawfal", "role": "Noble Warrior Knight", "desc": "Brave champion who attempted to unite the lovers through chivalric honor."}
    ],
    "themes": ["Transcendent Love as Mystic Path (Ishq)", "Ego Dissolution and Madness", "Societal Constraint vs Soul's Freedom", "Union in Eternity"],
    "echoes": "Directly inspired Shakespeare's Romeo and Juliet and European courtly love traditions of Tristan and Iseult.",
    "famousQuote": "“If I am mad, it is with the wine of love! I have erased myself so completely that only Layla remains in my chest.” — Nizami Ganjavi, Layla and Majnun",
    "historicalContext": "Originating as 7th-century Arabic Bedouin oral poetry, Nizami Ganjavi transformed it in 1188 into the supreme narrative poem of the Persian romantic canon."
  },

  # 11. Japan - Kojiki & Shinto Myth
  {
    "id": "shinto-amaterasu",
    "year": 712,
    "displayDate": "c. 712 CE (Nara Period Japan)",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Takamagahara (High Plain of Heaven) & Heavenly Rock Cave (Ama-no-Iwato)",
    "author": "Ō no Yasumaro & Hieda no Are (Kojiki - Records of Ancient Matters)",
    "title": "Kojiki: Amaterasu, Susanoo, and the Heavenly Rock Cave",
    "subtitle": "The Creation of the Eight Islands, the Underworld of Yomi, and the Dance that Brought Back the Sun",
    "summary": "Japan’s sacred founding mythology. The creator deities Izanagi and Izanami stir the ocean with a jeweled spear to birth the Japanese archipelago. When the tempestuous storm god Susanoo terrorizes Heaven, his sister Amaterasu, the Sun Goddess, hides inside the Heavenly Rock Cave, plunging the cosmos into darkness until a comic dance coaxes her out.",
    "fullStory": """### Act I: The Jeweled Spear and the Creation of Japan
In the beginning, when the world was young and drifted like floating oil upon water, the heavenly deities commanded the brother and sister gods **Izanagi** and **Izanami** to solidify the land. Standing upon the Floating Bridge of Heaven, they dipped the sacred **Jeweled Spear of Heaven** (*Ame-no-nuboko*) into the salty deep and stirred. As they lifted the spear, the brine that dripped from its tip congealed into the island of Onogoro. Descending to the island, they erected a heavenly pillar and united in marriage, giving birth to the eight major islands of Japan and the spirits of sea, wind, and mountains.

### Act II: The Descent to the Underworld of Yomi
Tragedy struck when Izanami gave birth to Kagutsuchi, the God of Fire, whose flames burned her flesh mortally, sending her soul to **Yomi** (the shadowy land of the dead). 

Grief-stricken, Izanagi traveled to the subterranean gates of Yomi to bring his wife back. Izanami asked him to wait while she pleaded with the lords of Yomi, warning him strictly not to look upon her. Growing impatient in the pitch darkness, Izanagi broke a tooth from his comb, lit it as a torch, and gazed upon her: he recoiled in horror to see her body rotting, crawling with maggots, and surrounded by eight thunder-demons. Enraged that he had shamed her, Izanami sent the hags of Yomi and an army of warriors to hunt him down. Izanagi threw down his headpiece (which turned into grapes) and comb (which turned into bamboo shoots) to delay them, finally rolling a massive boulder to seal the mouth of Yomi forever.

### Act III: The Purification and the Birth of the Three Noble Children
To wash away the pollution (*Kegare*) of the underworld, Izanagi performed the sacred rite of purification (*Misogi*) in a clear ocean stream on the island of Kyushu:
- As he washed his **left eye**, there was born **Amaterasu-ōmikami**, the radiant Sun Goddess.
- As he washed his **right eye**, there was born **Tsukuyomi-no-Mikoto**, the serene Moon God.
- As he washed his **nose**, there was born **Susanoo-no-Mikoto**, the wild God of Sea and Storms.

### Act IV: The Storm God’s Rampage and the Rock Cave of Heaven
Susanoo was violent and unruly, weeping so loudly for his mother that mountains withered and rivers dried up. Before being banished to the underworld, Susanoo traveled to Takamagahara (the High Plain of Heaven) to visit Amaterasu. Though they made a peace pact, Susanoo went on a destructive rampage: he broke down the ridges of the heavenly rice paddies, filled the irrigation canals with filth, and threw a flayed heavenly piebald horse through the roof of Amaterasu's sacred weaving hall.

Terrified and deeply offended by her brother's violent disrespect, Amaterasu withdrew into the **Ama-no-Iwato** (Heavenly Rock Cave), pulling a colossal boulder across the entrance. In an instant, the three thousand realms were plunged into absolute, pitch-black darkness. Evil spirits swarmed like summer flies, and chaos gripped heaven and earth.

### Act V: The Sacred Mirror and the Comic Dance of Uzume
The eight million *Kami* (spirits) assembled in despair by the dry bed of the Heavenly River of Tranquility. The wise god Omoikane devised a brilliant plan: they hung a great eight-hand bronze mirror (*Yata no Kagami*) and curved jewels (*Yasakani no Magatama*) upon a sacred Sakaki tree outside the cave entrance, while roosters were brought to crow.

Then, the cheerful goddess **Ame-no-Uzume** upturned a wooden tub before the cave, stepped atop it, and began an energetic, wild, and bawdy dance, stamping her feet so rhythmically that the tub resounded like a drum. As she pulled down her robes, the eight million gods burst into an uproarious roar of laughter that shook heaven and earth.

Curious and astonished that anyone could laugh while the world sat in darkness, Amaterasu cracked open the heavy stone and asked: *"Why does Uzume dance, and why do the gods laugh?"* 
Uzume replied: *"We rejoice because we have found a goddess more radiant than you!"* 

Uzume held up the bronze mirror; seeing her own dazzling reflection in the polished bronze, Amaterasu stepped further out in wonder. The strong-armed god Tajikarao seized her hand and pulled her out of the cave, while a sacred straw rope (*Shimenawa*) was stretched across the entrance, forbidding her from ever retreating again. Light, warmth, and life flooded back across Japan.

Susanoo was punished by having his beard shaved and fingernails pulled out before being banished to Izumo on earth, where he later redeemed himself by slaying the eight-headed dragon **Yamata-no-Orochi** and discovering the sacred sword **Kusanagi**—forming, with the Mirror and Jewel, the Three Sacred Imperial Regalia of Japan.""",
    "characters": [
      {"name": "Amaterasu-ōmikami", "role": "Sun Goddess & Ancestor of Imperial House", "desc": "Radiant ruler of Heaven whose withdrawal plunged the universe into darkness."},
      {"name": "Susanoo-no-Mikoto", "role": "Storm & Sea God", "desc": "Wild, unpredictable brother whose antics provoked Amaterasu and who later slew the eight-headed dragon."},
      {"name": "Ame-no-Uzume", "role": "Goddess of Dawn & Mirth", "desc": "Whose joyous dance and wit coaxed the sun back into the sky."},
      {"name": "Izanagi & Izanami", "role": "Creator Deities of Japan", "desc": "Stirred the primordial ocean with the jeweled spear to fashion the Japanese archipelago."}
    ],
    "themes": ["Shinto Purification (Misogi) and Light", "Cyclical Death and Rebirth of the Sun", "Power of Laughter and Joy over Despair", "The Sacred Imperial Regalia"],
    "echoes": "Amaterasu's cave withdrawal parallels the Greek myth of Demeter mourning Persephone; Izanagi's descent to Yomi is a twin of Orpheus and Eurydice.",
    "famousQuote": "“When Amaterasu stepped forth from the cave, the plain of heaven and the central land of reed plains were illuminated at once with golden light.” — Kojiki, Book I",
    "historicalContext": "Compiled in 712 CE by court scholar Ō no Yasumaro from the oral memorizations of Hieda no Are, the Kojiki forms the sacred foundational text of Shinto religion and Japanese identity."
  },

  # 12. Americas - Aztec & Five Suns
  {
    "id": "aztec-five-suns",
    "year": 1325,
    "displayDate": "c. 1325 – 1521 CE (Mexica / Aztec Civilization)",
    "era": "medieval",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Tenochtitlan (Lake Texcoco) & Teotihuacan",
    "author": "Mexica Tlamatinime (Wise Scribes) & Florentine Codex",
    "title": "The Aztec Myth of the Five Suns & the Eagle on the Cactus",
    "subtitle": "Quetzalcoatl’s Descent to Mictlan, the Leap of Nanahuatzin, and the Founding of Tenochtitlan",
    "summary": "The Aztec cosmic cycle of creation and destruction. After four previous suns (worlds) perish by jaguars, wind, fire, and flood, the humble god Nanahuatzin leaps into a cosmic bonfire at Teotihuacan to become the Fifth Sun (Nahui-Ollin). Quetzalcoatl steals the bones of humanity from Mictlan, and the Mexica follow Huitzilopochtli’s sign of an eagle perched on a nopal cactus.",
    "fullStory": """### Act I: The Four Destroyed Worlds (Ages of the Sun)
According to the Mexica elders, the cosmos does not move in a straight line, but through great cosmic cycles (*Suns*), each created and annihilated when cosmic balance failed:
1. **First Sun (4-Jaguar)**: Ruled by Tezcatlipoca; inhabited by giants who were devoured by monstrous jaguars when the sun was knocked from the sky.
2. **Second Sun (4-Wind)**: Ruled by Quetzalcoatl; swept away by colossal hurricanes that turned the surviving people into monkeys.
3. **Third Sun (4-Rain of Fire)**: Ruled by Tlaloc; destroyed by a celestial deluge of fire and molten lava from exploding volcanoes.
4. **Fourth Sun (4-Water)**: Ruled by Chalchiuhtlicue; drowned beneath a universal flood that turned all humans into fish.

### Act II: The Bonfire at Teotihuacan and the Fifth Sun
In the deep darkness following the flood, the gods gathered in the silent, ancient ruins of Teotihuacan to birth the **Fifth Sun** (*Nahui-Ollin* - Sun of Movement). A massive sacrificial pyre was lit, burning for four days. The gods asked: *"Who among us has the courage to leap into the flames to become the Sun?"*

The proud, wealthy god Tecuciztecatl stepped forward in feathered robes and jade offerings. But standing before the roaring furnace, he shrank back four times in terror. 

Then stepped forth **Nanahuatzin**—a poor, humble god covered in sores, dressed only in bark paper. Without a moment of hesitation, Nanahuatzin closed his eyes and threw himself into the center of the roaring fire. Shamed by his courage, Tecuciztecatl jumped in after him. Nanahuatzin rose in the east as the blazing golden Sun (*Tonatiuh*), while Tecuciztecatl rose as the Moon. When the gods threw a rabbit in the Moon's face to dim its brightness, the Sun hung motionless in the sky, refusing to move across the heavens until the gods offered their own divine blood (*Chalchihuitl*) to spark cosmic motion.

### Act III: Quetzalcoatl’s Descent into Mictlan
To recreate humanity, the Feathered Serpent god **Quetzalcoatl** descended into **Mictlan**, the ninth and deepest level of the terrifying underworld ruled by the skeletal lord Mictlantecuhtli.

Quetzalcoatl demanded the ancestral bones of the humans who had died in the previous suns. Mictlantecuhtli gave him an impossible test: to blow a conch trumpet that had no finger holes. Quetzalcoatl summoned worms to bore holes in the shell and bees to fill it with humming music. Seizing the bones, Quetzalcoatl fled while Mictlantecuhtli dug pit traps; falling into a trench, Quetzalcoatl dropped and fractured the bones into different sizes (explaining why humans are of different heights). Reaching the surface, the goddess Cihuacoatl ground the bones in a stone mortar, and Quetzalcoatl bled his own veins over the bone-meal, fashioning the modern human race.

### Act IV: The Eagle, the Serpent, and the Prickly Pear Cactus
For two centuries, the nomadic Mexica people wandered across the arid northern deserts of Aztlan, guided by the fiery war god **Huitzilopochtli**. The god made an unbreakable promise: they would wander until they saw a divine sign:
*"An eagle perched upon a prickly pear cactus (nopal) growing out of a rock in the center of the waters, tearing a serpent with its talons."*

In the year 1325 CE, arriving at the marshy shallows of Lake Texcoco in the high Valley of Mexico, the tribal priests looked out among the reeds. There, glowing in the morning sun, stood a golden eagle with outstretched wings perched on a blooming cactus, gripping a writhing snake. 

Falling to their knees in tears of reverence, the Mexica drove wooden pilings into the lakebed and laid the foundations of **Tenochtitlan**—which grew into an astonishing island metropolis of pyramid temples, floating gardens (*chinampas*), and grand causeways, and today forms the heart of modern Mexico City.""",
    "characters": [
      {"name": "Nanahuatzin", "role": "Humble God & Fifth Sun", "desc": "Whose selfless leap into the cosmic fire birthed the living Sun of Movement (Tonatiuh)."},
      {"name": "Quetzalcoatl", "role": "The Feathered Serpent", "desc": "God of wisdom, wind, and learning who descended to Mictlan to resurrect mankind with his own blood."},
      {"name": "Huitzilopochtli", "role": "Solar God of War", "desc": "Patron deity of the Mexica who guided them from Aztlan to Lake Texcoco."},
      {"name": "Mictlantecuhtli", "role": "Lord of the Underworld", "desc": "Skeletal master of Mictlan who guarded the ancestral bones of dead humanity."}
    ],
    "themes": ["Sacrificial Cosmic Maintenance", "Cyclical Ages of the World", "The Triumph of Humility over Pride", "Sacred City Foundations"],
    "echoes": "Nanahuatzin's leap parallels the self-sacrifice of Odin on Yggdrasil; Quetzalcoatl's descent to Mictlan mirrors Orpheus and Inanna.",
    "famousQuote": "“As long as the world shall endure, the fame and glory of Mexico-Tenochtitlan shall never perish!” — Mexica Chimalpahin Memorial of Culhuacan",
    "historicalContext": "The Great Sun Stone (Aztec Calendar Stone), unearthed in 1790 beneath Mexico City's Zócalo plaza, carves the entire cosmogony of the Five Suns into a 24-ton basalt monolith."
  },

  # 13. Europe - Celtic Táin Bó Cúailnge
  {
    "id": "irish-tain-cuchulainn",
    "year": 700,
    "displayDate": "c. 700 – 1100 CE (Early Medieval Ireland)",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Ulster, Connacht & Cooley Peninsula (Ireland)",
    "author": "Irish Monastic Scribes & Filí (Oral Bards)",
    "title": "Táin Bó Cúailnge: The Cattle Raid of Cooley & Cú Chulainn",
    "subtitle": "The Pillow Talk of Medb, the Warp-Spasm, the Gáe Bulg, and the Hound of Ulster",
    "summary": "The supreme prose-and-verse epic of Celtic Ireland. Queen Medb of Connacht invades Ulster with the combined armies of Ireland to seize the prize stud bull, the Donn Cúailnge. With all the warriors of Ulster paralyzed by a divine birth-pang curse, the seventeen-year-old demigod Cú Chulainn defends the borders alone in a series of single-combat duels at the river fords.",
    "fullStory": """### Act I: The Pillow Talk and the Brown Bull of Cooley
One night in the royal fortress of Cruachan, King Ailill and Queen Medb of Connacht engage in an argumentative comparison of their personal wealth (*Pillow Talk*). Item for item, their gold, jewels, garments, and herds of cattle are perfectly equal—until they discover that Ailill possesses a miraculous white-horned bull named *Finnbhennach*, born into Medb's herd but refusing to belong to a woman.

Furious that her husband owns anything superior to her, Medb discovers that only one beast in all of Ireland equals it: the colossal, magical brown stud bull **Donn Cúailnge** (The Brown Bull of Cooley) in the province of Ulster. When the lord of Cooley refuses her demand to rent the bull, Medb rallies the kings and armies of the four provinces of Ireland to march north and take the bull by fire and sword.

### Act II: The Curse of Macha and the Boy at the Ford
Ulster should have crushed the invasion instantly. But centuries earlier, King Conchobar of Ulster forced the pregnant goddess Macha to race his fastest horses; dying after giving birth to twins at the finish line, Macha cursed the men of Ulster: in their hour of greatest military peril, every warrior in Ulster would be struck with the agonizing labor pains of childbirth for five days and four nights.

As Medb's vast army crosses the border, every king and warrior in Ulster lies groaning in bed. The only person immune to the curse is **Cú Chulainn**—a seventeen-year-old youth, son of the mortal maiden Deichtine and the radiant Celtic sun god **Lugh of the Long Arm**. 

Invoking the ancient sacred Celtic code of the ford, Cú Chulainn demands that Medb’s army send one champion each day to duel him in single combat across the river ford; as long as the duel lasts, the army cannot advance. Day after day, Cú Chulainn slaughters Medb’s greatest warriors at the waters edge, surviving with no sleep, binding his wounds with grass and mud.

### Act III: The Warp-Spasm and the Duel with Ferdiad
When pushed to the absolute brink of death, Cú Chulainn undergoes the terrifying Celtic battle-frenzy known as the **Ríastrad** (Warp-Spasm):
His body twists inside his skin; his calves rotate to the front, his heels to the back; one eye sinks deep into his skull while the other bulges as large as a cauldron; a jet of thick black blood (*the Hero’s Light*) shoots sixty feet from his crown into the sky; and his jaw yawns open wide enough to swallow a man's head.

In her desperation, Medb forces Cú Chulainn’s beloved foster-brother and dearest companion, **Ferdiad**, to fight him by threatening him with shame and promising her daughter Findabair in marriage. For three agonizing days, the two soul-brothers clash at the Ford of Ardee. At the end of each day, they embrace, sharing medicinal herbs for their wounds and food for their horses. On the fourth day, pushed to the edge of defeat, Cú Chulainn calls for his underwater barbed spear, the **Gáe Bulg**, which enters the body as a single point and opens into thirty barbs that must be cut out of the flesh. Ferdiad is slain; Cú Chulainn catches his dying friend in his arms, weeping bitterly:
*"All was play, all was sport, until Ferdiad came to the ford... Dear to me was your noble skin; dear to me your bright eye!"*

### Act IV: The Awakening of Ulster and the Bull’s Fury
Lugh descends from heaven, putting Cú Chulainn into a three-day healing sleep while magical herbs close his hundred wounds. The curse of Macha finally lifts, and the warriors of Ulster awaken like roaring lions, driving Medb’s army in a full rout back across the Shannon.

Though Medb manages to drag the Brown Bull of Cooley back to Connacht, the Brown Bull encounters Ailill’s White-Horned Bull. The two titanic beasts clash in a cataclysmic battle across the entire island of Ireland, shaking mountains and tearing down forests. The Brown Bull slays the White-Horned beast, carries its mangled remains upon his horns across the provinces, returns to Cooley, and roars until his own heart bursts—leaving both kingdoms in solemn awe at the tragic price of human pride.""",
    "characters": [
      {"name": "Cú Chulainn (The Hound of Ulster)", "role": "Ulster Champion & Demigod", "desc": "Son of sun god Lugh who defended Ulster single-handedly through the terrifying Warp-Spasm frenzy."},
      {"name": "Queen Medb of Connacht", "role": "Sovereign Queen & Warlord", "desc": "Ambitious, fierce ruler whose quest for equality in wealth ignited the Cattle Raid."},
      {"name": "Ferdiad", "role": "Foster-Brother & Tragic Combatant", "desc": "Cú Chulainn's dearest friend, tragically pitted against him at the river ford."},
      {"name": "Lugh of the Long Arm", "role": "Celtic Solar God", "desc": "Divine father who watched over and healed Cú Chulainn during his darkest hours."}
    ],
    "themes": ["Sacred Warrior Honor (Geas)", "The Tragedy of Fratricidal Combat", "Female Sovereignty and Power", "Sacrifice for Homeland"],
    "echoes": "Cú Chulainn weeping over Ferdiad is a direct sister story to Achilles weeping for Patroclus and Rostam weeping over Sohrab.",
    "famousQuote": "“I care not if I live but a single day and night, so long as my deeds and my name live after me forever!” — Cú Chulainn upon taking up arms",
    "historicalContext": "Preserved in the 12th-century Book of Leinster and Lebor na hUidre, the Táin captures the Iron Age Celtic warrior society that flourished before the Roman and Christian eras."
  }
]

# Merge with the existing ones if needed or create complete unique set
# We already have a complete comprehensive list!

def generate_js_file():
    js_content = """/**
 * World Myths, Writers & History Timeline Data
 * A comprehensive curated archive of world mythologies, founding epics, 
 * legendary writers, and historical stories across all continents from 10,000 BCE to 1700 CE.
 */

const REGIONS = [
  { id: 'all', name: 'All Regions', icon: '🌐', color: '#111111' },
  { id: 'mesopotamia', name: 'Mesopotamia & Near East', icon: '🏺', color: '#2b5c8f', side: 'left' },
  { id: 'egypt', name: 'Ancient Egypt', icon: '𓀀', color: '#b58900', side: 'right' },
  { id: 'levant', name: 'Levant & Biblical Traditions', icon: '📜', color: '#6c4a8a', side: 'left' },
  { id: 'india', name: 'India & South Asia', icon: '🪷', color: '#b83b5e', side: 'right' },
  { id: 'china', name: 'China & East Asia', icon: '🐉', color: '#2e7d32', side: 'left' },
  { id: 'greece_rome', name: 'Greece & Rome', icon: '🏛️', color: '#c0392b', side: 'right' },
  { id: 'persia_arabia', name: 'Persia & Arabia', icon: '🕌', color: '#d35400', side: 'left' },
  { id: 'japan_korea', name: 'Japan & Korea', icon: '⛩️', color: '#16a085', side: 'right' },
  { id: 'americas', name: 'The Americas', icon: '🦅', color: '#8e44ad', side: 'left' },
  { id: 'africa', name: 'Sub-Saharan Africa', icon: '🦁', color: '#997300', side: 'right' },
  { id: 'n_europe', name: 'Northern & Celtic Europe', icon: '⚔️', color: '#2c3e50', side: 'left' },
  { id: 'oceania', name: 'Oceania & Australia', icon: '🌊', color: '#00838f', side: 'right' },
  { id: 'world_classics', name: 'Global Masterpieces & Renaissance', icon: '✒️', color: '#34495e', side: 'left' }
];

const ERAS = [
  { id: 'all', name: 'All Eras', range: '10,000 BCE – 1700 CE' },
  { id: 'prehistory', name: 'Deep Prehistory & Oral Beginnings', range: '10,000 – 3000 BCE', start: -10000, end: -3000 },
  { id: 'bronze', name: 'Bronze Age & First Writings', range: '3000 – 1200 BCE', start: -3000, end: -1200 },
  { id: 'classical', name: 'Classical Antiquity & Axial Age', range: '1200 BCE – 500 CE', start: -1200, end: 500 },
  { id: 'medieval', name: 'Golden Ages & Medieval Epics', range: '500 – 1400 CE', start: 500, end: 1400 },
  { id: 'renaissance', name: 'Renaissance & Global Masterpieces', range: '1400 – 1700 CE', start: 1400, end: 1700 }
];

const STORIES_DATA = """ + json.dumps(all_stories, indent=2, ensure_ascii=False) + """;

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { REGIONS, ERAS, STORIES_DATA };
}
"""
    out_path = r"f:\AntiGravity\Apps Data\WorldHistoryTimeline\js\stories_data.js"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("Successfully generated stories_data.js with", len(all_stories), "comprehensive stories!")

if __name__ == "__main__":
    generate_js_file()
