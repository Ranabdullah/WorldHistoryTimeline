# -*- coding: utf-8 -*-
"""
Script to assemble the complete world repository of stories, writers, and mythologies.
"""

import json
import os

# We will read both sets or compile them into a unified list
from build_stories import all_stories as set2

# Let's define the first set (from our earlier manual creation)
set1 = [
  {
    "id": "enheduanna-inanna",
    "year": -2300,
    "displayDate": "c. 2300 BCE (Akkadian Empire)",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Ur & Uruk (Modern Iraq)",
    "author": "Enheduanna (High Priestess of Ur — World’s First Named Author)",
    "title": "The Exaltation of Inanna (Nin-me-šara)",
    "subtitle": "The Sacred Hymns of History’s First Recorded Author and High Priestess",
    "summary": "Princess Enheduanna, daughter of Sargon the Great, writes history’s first authored literary texts. Cast into the desert by a rebel warlord, she composes 42 passionate hymns exalting Inanna, goddess of love and cosmic storms, reclaiming her temple throne through the power of the stylus.",
    "fullStory": """### Act I: The Daughter of Sargon and the Moon Temple
In the great ziggurat city of Ur, around 2300 BCE, Enheduanna held the supreme spiritual office of *En-Priestess* of Nanna, the Moon God. She was the daughter of Sargon of Akkad, the world’s first empire builder who united the Sumerian city-states with the Akkadian north. Enheduanna was not merely a ceremonial figurehead; she was a master of the cuneiform stylus, an astronomer-theologian, and the first individual in human history whose name is signed to literary works that survive to this day.

### Act II: Rebellion, Betrayal, and Banishment
When Sargon died, political rebellion swept Sumer. A warlord named Lugalanne seized Ur and attempted to overthrow the Akkadian dynasty. He stormed the sacred precinct of the Gipar, stripped Enheduanna of her high crown, and cast her out into the harsh Mesopotamian desert, mocking her prayers and denying her sacred status.

### Act III: The Birth of Authored Poetry in the Wilderness
Alone in the barren waste, Enheduanna turned not to the peaceful moon god, but to Inanna (Ishtar)—the fierce, unpredictable goddess of storm, passion, battle, and justice. Carving wet clay tablets under the blinding sun, Enheduanna poured her raw anguish and intellectual genius into *Nin-me-šara* ("The Exaltation of Inanna"). She elevated Inanna above all male gods of the pantheon, depicting her as a roaring lioness riding the cosmic tempests:
*"Queen of all the cosmic powers, radiant light, righteous woman clothed in brilliance, beloved of Heaven and Earth..."*

### Act IV: The Triumph of the Stylus
In her hymn, Enheduanna makes an unprecedented claim in world literature: she explicitly describes the creative act of composing poetry in the first person (*"I gave birth to this song for you, my Lady; what I recited at night, the singer shall repeat by day"*). Her hymns electrified the loyalist armies and populace; the rebellion collapsed, Lugalanne was defeated, and Enheduanna was restored to her seat of power at Ur. Her tablets were copied by scribes in Mesopotamian schools for over five hundred years after her death.""",
    "characters": [
      {"name": "Enheduanna", "role": "High Priestess & First Named Author", "desc": "Historical poet-theologian whose cuneiform hymns unified Sumerian and Semitic religious traditions."},
      {"name": "Inanna (Ishtar)", "role": "Goddess of Love, War & Transformation", "desc": "The fierce Mesopotamian deity who descends to the underworld and commands the cosmic *Me* (divine laws)."},
      {"name": "Lugalanne", "role": "Rebel Usurper of Ur", "desc": "The insurgent general who drove Enheduanna into exile before being overthrown."}
    ],
    "themes": ["Birth of Authored Literature", "Power of the Written Word", "Divine Justice", "Exile & Restoration"],
    "echoes": "Prefigures the devotional poetry of Sappho, Mirabai, and biblical psalms attributed to King David by over a thousand years.",
    "famousQuote": "“I am Enheduanna, the high priestess... I carried the ritual basket; I sang the hymns of joy. But now I am cast out, a stranger in the dust. Queen of Heaven, hear my plea!” — Enheduanna, Nin-me-šara",
    "historicalContext": "The alabaster Disk of Enheduanna, discovered by British archaeologist Sir Leonard Woolley in Ur in 1927, depicts her presiding over sacred libations with her name inscribed in clear cuneiform script."
  },
  {
    "id": "gilgamesh-epic",
    "year": -2100,
    "displayDate": "c. 2100 – 1200 BCE (Standard Babylonian Epic)",
    "era": "bronze",
    "regionId": "mesopotamia",
    "regionName": "Mesopotamia & Near East",
    "place": "Uruk, Cedar Forest & Waters of Death",
    "author": "Attributed to Sîn-lēqi-unninni (based on Sumerian oral tales)",
    "title": "The Epic of Gilgamesh: The Quest for Immortality",
    "subtitle": "The Friendship of Enkidu, the Slaying of Humbaba, and the Secret of Eternal Life",
    "summary": "Gilgamesh, the tyrannical two-thirds divine King of Uruk, finds his match in the wild man Enkidu. When Enkidu dies as punishment for slaying the Bull of Heaven, Gilgamesh is gripped by existential dread and journeys across the Waters of Death to find Utnapishtim, survivor of the Great Deluge.",
    "fullStory": """### Act I: The Tyrant King and the Wild Man
Gilgamesh rules the sun-baked city of Uruk with an iron fist. Two-thirds god and one-third man, he exhausts his subjects, demanding first-night rights with every bride and driving young men in endless martial contests. In desperation, the citizens cry out to the sky-god Anu, who instructs the mother goddess Aruru to fashion Enkidu—a hairy wild man who runs with gazelles and drinks from watering holes. A temple priestess named Shamhat is sent to civilize Enkidu; through six days and seven nights of human intimacy, she teaches him speech, bread-eating, and garments.

### Act II: The Great Friendship and the Cedar Forest
Enkidu travels to Uruk and blocks Gilgamesh’s path at a wedding chamber. The two titans clash with such fury that doorposts splinter and the earth trembles. Finding themselves evenly matched, they break apart and embrace in profound brotherhood. Desiring to carve his name into eternity, Gilgamesh convinces Enkidu to journey to the sacred Cedar Forest of Lebanon. Together, they slay Humbaba, the monstrous roaring guardian appointed by Enlil, cutting down the tallest cedar trees to build grand gates for Uruk.

### Act III: The Bull of Heaven and Enkidu’s Tragic Death
Upon their return, the goddess Ishtar proposes marriage to Gilgamesh. Gilgamesh rejects her, cataloging how all her past lovers were turned into broken beasts. Enraged, Ishtar unleashes the Bull of Heaven upon Uruk, whose snorting opens chasms swallowing hundreds of men. Gilgamesh and Enkidu slay the beast. The gods decree that Enkidu must die. Enkidu contracts a wasting fever and dies in Gilgamesh’s weeping arms.

### Act IV: The Journey Beyond the World and the Great Deluge
Shattered by grief and terrified of his own mortality, Gilgamesh wanders the desolation. He crosses the Mount of Mashu guarded by Scorpion-men, walks through twelve leagues of darkness, and meets the tavern-keeper Siduri at the edge of the cosmic ocean. Siduri advises him to cherish mortal life: *"Fill your belly with good things; dance and be merry day and night; cherish the child holding your hand; make your wife happy in your embrace!"*

Ignoring her wisdom, Gilgamesh crosses the Waters of Death with Urshanabi the ferryman and reaches Utnapishtim, the sole mortal granted immortality after building a giant boat to survive the great deluge. Utnapishtim challenges Gilgamesh: *"Can you conquer sleep, the younger brother of death? Stay awake for six days and seven nights."* Gilgamesh sits, but instantly falls asleep, proven by seven rotting loaves of bread at his feet.

### Act V: The Serpent and the Return to Uruk
Moved by pity, Utnapishtim reveals that deep on the sea bed grows a thorny plant with the power to restore youth. Gilgamesh dives into the abyss and plucks the plant. But on his return, while bathing in a cool mountain spring, a water snake steals it—instantly shedding its old skin and slithering away rejuvenated. 

Gilgamesh sits by the pool and weeps bitter tears. Realizing that physical immortality is denied to mankind, he returns to Uruk. Standing before the majestic ramparts of burnt brick, he gazes upon his city and finds peace: human immortality is found in the enduring civilization we build and the stories we leave behind.""",
    "characters": [
      {"name": "Gilgamesh", "role": "King of Uruk & Tragic Hero", "desc": "Two-thirds divine monarch whose quest transforms him from a tyrant to a wise protector."},
      {"name": "Enkidu", "role": "Wild Man & Soul Brother", "desc": "Created from clay to check Gilgamesh’s pride; his death triggers Gilgamesh’s existential quest."},
      {"name": "Utnapishtim", "role": "Survivor of the Deluge", "desc": "The Mesopotamian Noah who preserved all living seeds in a great ark and received immortality."},
      {"name": "Shamhat", "role": "Priestess of Inanna", "desc": "The wise woman who civilized Enkidu through compassion and human connection."},
      {"name": "Siduri", "role": "Alewife of the Underworld Edge", "desc": "Philosopher of joy who urged Gilgamesh to embrace mortal life."}
    ],
    "themes": ["Mortality and Existential Dread", "Sacred Brotherhood", "Civilization vs Wilderness", "Comparative Flood Myth"],
    "echoes": "The flood narrative with birds sent out (dove, swallow, raven) matches Noah’s Ark; Gilgamesh’s grief mirrors Achilles weeping for Patroclus.",
    "famousQuote": "“Look upon the walls of Uruk! Examine its masonry, inspect its burnt-brick foundations! Did not the Seven Sages lay its groundplan? One square mile of city, one of date groves, one of clay pits... This is the work of Gilgamesh.” — Tablet I",
    "historicalContext": "Twelve clay tablets containing the standard version were found in the Library of Ashurbanipal in Nineveh and deciphered by George Smith in 1872."
  },
  {
    "id": "osiris-isis-horus",
    "year": -2000,
    "displayDate": "c. 2000 – 1200 BCE (Egyptian Middle & New Kingdom)",
    "era": "bronze",
    "regionId": "egypt",
    "regionName": "Ancient Egypt",
    "place": "Abydos, Delta Marshes & Heliopolis",
    "author": "Ancient Egyptian Priestly Tradition (Pyramid Texts & Plutarch)",
    "title": "The Myth of Osiris, Isis, and Horus: Death and Resurrection",
    "subtitle": "The Murder of Osiris, Isis’s Magic, and the Celestial Battle for the Double Crown",
    "summary": "King Osiris brings agriculture and law to Egypt, but is murdered and dismembered by his brother Set. His queen Isis, greatest of sorceresses, searches the world to reassemble his flesh and miraculously conceives Horus, who wages an epic generational war against Set to restore cosmic order (Ma’at).",
    "fullStory": """### Act I: The Golden Reign and the Treacherous Banquet
In the first age of Egypt, Osiris ruled as a benevolent king, teaching humanity farming, law, and music. Under his guidance, the land flourished in harmony with *Ma'at* (cosmic truth). Yet dark envy festered in the heart of his brother Set, the god of desert storms and red sands.

Set secretly measured Osiris’s body and constructed a magnificent cedar chest inlaid with gold and lapis lazuli. At a royal banquet, Set announced that whoever could lie perfectly inside the chest would claim it as a gift. When Osiris stepped inside, seventy-two conspirators slammed the lid shut, nailed it with lead, and threw the casket into the Nile, which carried it to the sea.

### Act II: The Agony and Magic of Isis
Queen Isis sheared her hair and set out in relentless mourning across the Mediterranean world. She tracked the chest to Byblos (Lebanon), where a fragrant tamarisk tree had grown around it as a pillar. Isis secured the pillar and brought Osiris’s body back to the papyrus marshes of the Delta.

Set discovered the hidden corpse while hunting under the full moon. In a frenzy, he cut Osiris’s body into fourteen pieces and scattered them across Egypt. Undaunted, Isis transformed into a falcon and, aided by Nephthys and Anubis, combed every reed bed. She recovered thirteen pieces and, through the power of the first mummification rites, breathed life into Osiris just long enough to conceive a divine heir: Horus.

### Act III: The Contendings of Horus and Set
Osiris descended to the Duat (Underworld) as eternal Judge of Souls. Isis raised the infant Horus in hiding in the marshes of Chemmis. When Horus reached manhood, he stepped forward before the divine council of gods to claim his throne.

For eighty years, Horus and Set engaged in grueling contests—shapeshifting into hippopotamuses beneath the water, racing stone boats, and clashing in martial combat. Set tore out Horus’s left eye, while Horus emasculated his uncle. The wise god Thoth healed Horus’s eye, creating the *Wedjat* (Eye of Horus), the eternal symbol of healing and royal protection.

### Act IV: The Restoration of Ma’at
The divine council finally declared Horus the undisputed King of Egypt, uniting the White and Red Crowns. Ever after, every living Pharaoh was worshipped as the earthly incarnation of Horus, while every deceased Pharaoh was transfigured as Osiris in eternity.""",
    "characters": [
      {"name": "Osiris", "role": "Lord of the Afterlife & Resurrection", "desc": "The murdered king whose rebirth inaugurated the eternal promise of life after death."},
      {"name": "Isis (Aset)", "role": "Goddess of Magic & Healing", "desc": "The supreme sorceress whose intellect and love overcame death itself."},
      {"name": "Horus", "role": "Falcon God & Legitimate King", "desc": "Son of Osiris and Isis whose triumph established cosmic justice across Egypt."},
      {"name": "Set", "role": "God of Desert & Chaos", "desc": "The antagonistic brother whose destructive envy challenged Ma’at."}
    ],
    "themes": ["Death and Resurrection", "Cosmic Order (Ma’at) vs Chaos (Isfet)", "Filial Piety and Justice", "Divine Kingship"],
    "echoes": "Mirrors the Norse Baldr’s murder by Loki, Greek Dionysus torn apart by Titans, and Christian resurrection theology.",
    "famousQuote": "“Arise, Osiris! Isis has embraced your limbs; she has found all your scattered bones. Awake, O King, and rule the Western Lands forever!” — Pyramid Texts, Utterance 412",
    "historicalContext": "The Osiris myth formed the ideological core of ancient Egyptian kingship for over three millennia and provided the theological blueprint for mummification."
  },
  {
    "id": "ramayana-valmiki",
    "year": -1200,
    "displayDate": "c. 1200 – 500 BCE (Vedic to Classical India)",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Ayodhya, Dandaka Forest & Lanka",
    "author": "Adi Kavi Sage Valmiki",
    "title": "The Ramayana: The Epic Journey of Rama and Sita",
    "subtitle": "Dharma, Devotion, the Bridge Across the Ocean, and the Defeat of Ravana",
    "summary": "Prince Rama of Ayodhya, avatar of Vishnu, accepts a fourteen-year forest exile to honor his father’s vow. When the ten-headed demon king Ravana abducts his wife Sita to Lanka, Rama allies with Hanuman and the Vanara army, building a floating stone bridge across the ocean to wage a war of cosmic righteousness.",
    "fullStory": """### Act I: The Boon and the Exile
In Ayodhya, King Dasharatha prepares to crown his eldest son Rama. On the eve of coronation, Queen Kaikeyi demands two ancient boons: that her son Bharata be crowned, and Rama be exiled to the Dandaka Forest for fourteen years. Rama accepts his banishment with serene grace, stating that a son’s highest duty (*Dharma*) is to honor his father’s word. Sita and his loyal brother Lakshmana accompany him into the wilderness.

### Act II: The Golden Deer and the Abduction
In the forest of Panchavati, the demon king Ravana enlists the shapeshifting sorcerer Maricha, who takes the form of an irresistible golden deer. When Rama and Lakshmana are lured away, Ravana approaches disguised as a wandering ascetic, seizes Sita, and flies south in his celestial chariot *Pushpaka Vimana*, imprisoning her in Lanka.

### Act III: Hanuman’s Leap and the Floating Bridge
Rama and Lakshmana ally with Sugriva and the monkey warrior Hanuman. Endowed with immense strength, Hanuman leaps thousands of leagues across the Indian Ocean to find Sita in the Ashoka grove, delivering Rama's signet ring and burning Lanka's towers with his flaming tail. The Vanara army builds the miraculous *Ram Setu* bridge of floating boulders to cross the sea.

### Act IV: The War in Lanka and Return to Ayodhya
A cataclysmic war erupts. Lakshmana is mortally wounded by Indrajit, but saved when Hanuman carries an entire mountain of *Sanjeevani* herbs across the night sky. In the climactic duel, Rama invokes the fiery *Brahmastra* arrow to slay Ravana. Rama and Sita return to Ayodhya atop the Pushpaka Vimana, welcomed by millions of citizens who light clay lamps (*diyas*)—celebrated worldwide during **Diwali**.""",
    "characters": [
      {"name": "Rama", "role": "Seventh Avatar of Vishnu & Ideal Man", "desc": "Embodiment of righteous duty (Dharma), courage, and unyielding honor."},
      {"name": "Sita", "role": "Avatar of Lakshmi & Princess of Mithila", "desc": "Embodiment of courage, purity, and steadfast devotion."},
      {"name": "Hanuman", "role": "Son of the Wind God & Supreme Devotee", "desc": "Loyal Vanara hero endowed with immense strength, humility, and agility."},
      {"name": "Ravana", "role": "Ten-Headed King of Lanka", "desc": "Brilliant scholar whose fatal flaw of pride brought his destruction."}
    ],
    "themes": ["Dharma (Righteous Duty)", "Devotion and Loyalty", "Triumph of Light over Darkness", "Sacred Brotherhood"],
    "echoes": "Sita’s abduction and the sea expedition mirrors the Trojan War in the Iliad; Hanuman’s leaps parallel Sun Wukong.",
    "famousQuote": "“Mother and motherland are more sacred than heaven itself.” (Janani Janmabhoomischa Swargadapi Gariyasi) — Sage Valmiki, Ramayana",
    "historicalContext": "Valmiki’s Ramayana is considered the *Adi Kavya* (the First Poem) of Indian literature, giving rise to hundreds of regional adaptations across Asia."
  },
  {
    "id": "mahabharata-vyasa",
    "year": -900,
    "displayDate": "c. 900 – 400 BCE (Epic Antiquity)",
    "era": "classical",
    "regionId": "india",
    "regionName": "India & South Asia",
    "place": "Hastinapura & Kurukshetra Field",
    "author": "Sage Krishna Dwaipayana Vyasa (Scribe: Lord Ganesha)",
    "title": "The Mahabharata & Bhagavad Gita: The Great Cosmic War",
    "subtitle": "The Pandavas vs Kauravas, the Dice Game, and Krishna’s Divine Discourse",
    "summary": "The longest epic in world literature chronicles the conflict between the five righteous Pandavas and the hundred Kauravas. On the battlefield of Kurukshetra, Lord Krishna reveals the immortal Bhagavad Gita to the despondent warrior Arjuna.",
    "fullStory": """### Act I: The House of Kuru and the Game of Dice
The five sons of Pandu—Yudhishthira, Bhima, Arjuna, Nakula, and Sahadeva—are blessed with divine qualities, inciting the jealousy of their cousin Duryodhana. In a rigged game of dice in Hastinapura, Shakuni strips Yudhishthira of his kingdom, brothers, and Queen Draupadi. When Dushasana attempts to disrobe Draupadi in court, Lord Krishna renders her sari an infinite bolt of silk, protecting her honor.

### Act II: Exile and the Bhagavad Gita
After thirteen years of exile, Duryodhana refuses to return a needlepoint of land. Millions assemble for war at Kurukshetra. Seeing his revered elders and kin across the line, Arjuna drops his bow in grief. Lord Krishna delivers the **Bhagavad Gita**, teaching the immortality of the soul (*Atman*) and *Karma Yoga* (selfless duty without attachment to results).

### Act III: The Eighteen-Day War
For eighteen days, titanic battles rage. Bhishma, Drona, and Karna fall. Bhima breaks Duryodhana’s thighs in single combat. The Pandavas win, but at devastating cost, leaving almost an entire generation dead upon the field before the Pandavas undertake their final Himalayan pilgrimage to heaven.""",
    "characters": [
      {"name": "Arjuna", "role": "Third Pandava & Supreme Archer", "desc": "Hero who receives the immortal teachings of the Bhagavad Gita."},
      {"name": "Lord Krishna", "role": "Avatar of Vishnu & Divine Guide", "desc": "Diplomat, philosopher, and supreme cosmic guide."},
      {"name": "Draupadi", "role": "Fiery Queen of the Pandavas", "desc": "Born of sacrificial fire, whose dignity sparked the war of justice."},
      {"name": "Duryodhana", "role": "Eldest Kaurava Prince", "desc": "Ambitious prince whose pride triggered the world war."}
    ],
    "themes": ["Karma and Selfless Duty (Nishkama Karma)", "Immortality of the Soul", "Moral Complexity", "Inevitability of Destiny"],
    "echoes": "Civil war between kin parallels the Norse Ragnarök and Arthurian Battle of Camlann.",
    "famousQuote": "“You have a right only to perform your duty, never to the fruits of your actions.” — Bhagavad Gita 2.47",
    "historicalContext": "With over 100,000 verses (*shlokas*), it is eight times the length of Homer’s Iliad and Odyssey combined."
  },
  {
    "id": "iliad-odyssey-homer",
    "year": -750,
    "displayDate": "c. 750 – 700 BCE (Archaic Greece)",
    "era": "classical",
    "regionId": "greece_rome",
    "regionName": "Greece & Rome",
    "place": "Troy, Aegean Sea, Ithaca & Mount Olympus",
    "author": "Homer (Blind Bard of Ionia)",
    "title": "The Iliad & The Odyssey: The Fall of Troy and the Wanderer’s Return",
    "subtitle": "Achilles’ Rage, the Trojan Horse, the Cyclops, Circe, and Penelope’s Shroud",
    "summary": "Homer’s twin foundational epics. The Iliad captures the tragic fury of Achilles at the siege of Troy. The Odyssey chronicles the ten-year voyage of Odysseus as he outwits monsters and sorceresses to reclaim Ithaca and his faithful wife Penelope.",
    "fullStory": """### Act I: The Wrath of Achilles and the Fall of Patroclus
In the tenth year of the Trojan War, Agamemnon offends Achilles, who withdraws from battle in fury. Without Achilles, the Greeks are driven back to their ships by Prince Hector. Patroclus dons Achilles’ divine armor to save the fleet, but is slain by Hector. Devastated, Achilles re-enters the war, slays Hector in single combat, and drags his corpse behind his chariot until King Priam begs for his son's body.

### Act II: The Trojan Horse and the Perilous Sea
Troy falls through Odysseus’s stratagem of the wooden horse. Sailing home, Odysseus blinds the Cyclops Polyphemus, incurring the wrath of Poseidon. He outwits the sorceress Circe, journeys to the Underworld, resists the Sirens, and endures seven years on Calypso's island before washing ashore in Ithaca.

### Act III: The Beggar and the Great Bow
Disguised as a beggar, Odysseus enters his palace, which is overrun by suitors demanding Penelope’s hand. Penelope promises to marry whoever can string Odysseus’s great bow and shoot through twelve axe heads. Odysseus strings the bow with ease, slays the suitors with his son Telemachus, and reclaims his queen and throne.""",
    "characters": [
      {"name": "Achilles", "role": "Champion of the Greeks", "desc": "Invulnerable except for his heel; torn between a long peaceful life and eternal glory."},
      {"name": "Odysseus", "role": "King of Ithaca", "desc": "Master strategist renowned for intellect, endurance, and cunning."},
      {"name": "Penelope", "role": "Queen of Ithaca", "desc": "Archetype of fidelity, brilliance, and resilience."},
      {"name": "Hector", "role": "Trojan Crown Prince", "desc": "Noble defender fighting to protect his family and city."}
    ],
    "themes": ["Tragic Cost of War", "Glory (Kleos) vs Homecoming (Nostos)", "Cunning vs Brute Force", "Hospitality (Xenia)"],
    "echoes": "Achilles and Patroclus mirror Gilgamesh and Enkidu; Odysseus's sea voyage parallels Sinbad the Sailor.",
    "famousQuote": "“Sing in me, Muse, and through me tell the story of that man skilled in all ways of contending...” — Homer, The Odyssey",
    "historicalContext": "Archaeological excavations by Schliemann at Hisarlik proved Troy was a historical Bronze Age city destroyed around 1180 BCE."
  },
  {
    "id": "popol-vuh-maya",
    "year": -400,
    "displayDate": "c. 400 BCE – 1550 CE (Maya Classic to K’iche’ Epic)",
    "era": "classical",
    "regionId": "americas",
    "regionName": "The Americas",
    "place": "Xibalba (The Underworld) & Highlands of Guatemala",
    "author": "K’iche’ Maya Scribes (Preserved by Father Francisco Ximénez)",
    "title": "Popol Vuh: The Hero Twins and the Lords of Death",
    "subtitle": "The Creation of the Maize People and the Descent into Xibalba",
    "summary": "The sacred book of the Maya. When the Lords of Xibalba murder their father, the Hero Twins Hunahpu and Xbalanque descend into the underworld, surviving lethal trap houses and ballgame matches to conquer death and rise as the Sun and Moon.",
    "fullStory": """### Act I: The Failed Creations and the Underworld
The gods fashion animals, mud people, and wooden mannequins, but destroy them with flood when they lack souls. Deep beneath the earth, the cruel Lords of Xibalba murder the elder twins One Hunahpu and Seven Hunahpu over a rubber ballgame. Lady Blood approaches One Hunahpu’s skull on a calabash tree, which spits into her hand, conceiving the Hero Twins Hunahpu and Xbalanque.

### Act II: The Ordeals of Xibalba
Summoned to the underworld, the young Hero Twins outwit the death lords in six lethal houses: Dark House, Razor House, Cold House, Jaguar House, Fire House, and Bat House. Decapitated by a death bat, Hunahpu uses a carved pumpkin head until retrieving his real head during a ballgame.

### Act III: The Ascent of the Sun and Moon
The twins allow themselves to be burned in a pit, ground to dust, and thrown into the river, resurrecting as magical dancers. Tricking the lords into asking to be sacrificed and revived, the twins cut their throats and leave them dead. Ascending into the heavens, Hunahpu becomes the golden Sun and Xbalanque the silver Moon, after which the gods create the true race of Maize People.""",
    "characters": [
      {"name": "Hunahpu & Xbalanque", "role": "The Hero Twins", "desc": "Demigods who conquered the underworld through wit and ascended as Sun and Moon."},
      {"name": "One Death & Seven Death", "role": "Supreme Lords of Xibalba", "desc": "Cruel subterranean rulers of decay and disease."},
      {"name": "Huracan & Gucumatz", "role": "Creator Gods", "desc": "Plumed Serpent and Heart of Sky who designed the world."}
    ],
    "themes": ["Triumph of Intellect over Death", "Rebirth through Sacrifice", "Sacred Maize Essence", "Cyclical Time"],
    "echoes": "Descent to the underworld mirrors Inanna, Orpheus, and Heracles.",
    "famousQuote": "“Here we shall write, we shall implant the ancient word of the beginning...” — Opening of the Popol Vuh",
    "historicalContext": "Transcribed in K’iche’ Maya using Latin script around 1550 to preserve traditions from the Spanish conquest."
  },
  {
    "id": "shahnameh-ferdowsi",
    "year": 1000,
    "displayDate": "c. 977 – 1010 CE (Persian Golden Age)",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Greater Iran, Sistan & Turan",
    "author": "Hakim Abul-Qasim Ferdowsi Tusi",
    "title": "Shahnameh: The Epic of Kings (Rostam and Sohrab)",
    "subtitle": "The 60,000 Verses of Persian Kings and the Tragedy of Rostam",
    "summary": "The national epic of the Persian world. Ferdowsi spent thirty years composing 50,000 couplets in pure Persian to preserve Iranian heritage, highlighted by the heartbreaking tragedy of champion Rostam and his son Sohrab.",
    "fullStory": """### Act I: The 30-Year Monument to the Persian Language
Following foreign conquests, Ferdowsi spent thirty years recording the history of Iranian kings from creation to the Islamic era, declaring: *"For thirty years I endured much toil, but with the Persian language I revived Iran."*

### Act II: Zahhak the Snake King and Rostam's Labors
Zahhak sprouts venomous snakes from his shoulders that feed on youths' brains until Kaveh the Blacksmith raises the royal banner of rebellion. Later, Rostam and his warhorse Rakhsh perform the Seven Labors to protect Iran.

### Act III: The Tragedy of Rostam and Sohrab
Rostam spends one night with Princess Tahmineh of Samangan, leaving a jewel bracelet for their unborn child. Their son Sohrab grows into a mighty warrior and leads an army to find his father. Meeting in single combat without knowing each other's identity, Rostam mortally stabs Sohrab. As Sohrab dies, Rostam spots the jewel bracelet on his arm and weeps in boundless agony.""",
    "characters": [
      {"name": "Rostam", "role": "Supreme Champion of Iran", "desc": "Invincible defender who unknowingly struck down his own son."},
      {"name": "Sohrab", "role": "Youth Champion of Turan", "desc": "Noble son whose quest to find his father ended in tragedy."},
      {"name": "Ferdowsi", "role": "Master Poet", "desc": "Preserved the Persian language and culture through 60,000 verses."}
    ],
    "themes": ["Tragedy of Blind War", "Father vs Son", "Cultural Preservation", "Transience of Power"],
    "echoes": "Father-son duel matches Irish Cú Chulainn and Connla, and Germanic Hildebrandslied.",
    "famousQuote": "“I have built a towering palace of verse that neither wind nor rain can ever erode.” — Ferdowsi",
    "historicalContext": "Ferdowsi's tomb in Tus is a national monument celebrating the enduring spirit of Persian literature."
  },
  {
    "id": "sundiata-mali",
    "year": 1235,
    "displayDate": "c. 1235 CE (Mali Empire)",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Niani & Battle of Kirina (West Africa)",
    "author": "Preserved by Griots (Djeli Mamadou Kouyaté)",
    "title": "The Epic of Sundiata: The Lion King of Mali",
    "subtitle": "The Miracle of the Iron Rod and the Defeat of Sorcerer Sumanguru",
    "summary": "West Africa's founding epic. Born crippled and mocked until age seven, Sundiata Keita stands with an iron rod, overcomes exile, and defeats the sorcerer-king Sumanguru Kanté at Kirina to forge the wealthy Mali Empire.",
    "fullStory": """### Act I: The Crippled Prince and the Baobab Tree
Born unable to walk, Sundiata crawls on all fours until age seven, suffering mockery with his mother Sogolon. When his mother weeps, Sundiata commands blacksmiths to forge an enormous iron rod. Using it to hoist himself up, he bends the iron like a bow, walks on his own feet, and uproots an entire baobab tree to place before his mother's door.

### Act II: Exile, the Sorcerer King, and the Battle of Kirina
Exiled for seven years, Sundiata gains military renown across West Africa. The cruel sorcerer Sumanguru Kanté invades Manden. Discovering Sumanguru's magical weakness, Sundiata grazes him with an arrow tipped with a white rooster spur at the Battle of Kirina. Sumanguru loses his powers and vanishes into the mountains. Sundiata unites Mali and proclaims the Kouroukan Fouga charter of human rights.""",
    "characters": [
      {"name": "Sundiata Keita", "role": "The Lion King & Founder of Mali", "desc": "Disabled prince who rose to become one of history’s greatest rulers."},
      {"name": "Sumanguru Kanté", "role": "Sorcerer King of Sosso", "desc": "Tyrant warlord whose magic was broken by a rooster spur."},
      {"name": "Balla Fasséké", "role": "Master Griot", "desc": "Oral historian who preserved the memory of Manden."}
    ],
    "themes": ["Overcoming Adversity", "Oral History & Griots", "Liberation from Tyranny", "Human Rights Charter"],
    "echoes": "Directly inspired modern adaptations like Disney’s *The Lion King*.",
    "famousQuote": "“We are the vessels of speech; we harbor secrets centuries old.” — Djeli Mamadou Kouyaté",
    "historicalContext": "The Kouroukan Fouga charter proclaimed by Sundiata in 1236 is recognized by UNESCO as Intangible Cultural Heritage."
  },
  {
    "id": "genji-murasaki",
    "year": 1008,
    "displayDate": "c. 1000 – 1012 CE (Heian Period Japan)",
    "era": "medieval",
    "regionId": "japan_korea",
    "regionName": "Japan & Korea",
    "place": "Heian-kyō (Kyoto)",
    "author": "Murasaki Shikibu (Noblewoman & Lady-in-Waiting)",
    "title": "The Tale of Genji (Genji Monogatari)",
    "subtitle": "The World’s First Novel: Courtly Elegance and Mono no Aware",
    "summary": "The world's first psychological novel. Written by Murasaki Shikibu at the Heian court, this 54-chapter masterpiece captures the beauty, romantic intrigues, and Buddhist pathos of impermanence centered on the Shining Prince Hikaru Genji.",
    "fullStory": """### Act I: The Shining Prince and Courtly Aesthetics
Hikaru Genji, son of the Emperor, is renowned for beauty, poetry, and music. Longing for his deceased mother, he falls into a forbidden passion with Lady Fujitsubo, and later discovers young Lady Murasaki, raising and loving her as his lifelong soulmate.

### Act II: Exile to Suma and Vanishing into Clouds
Following political scandals, Genji exiles himself to the windswept shore of Suma, composing poignant poetry on impermanence. Restored to imperial honor, his later life is shadowed by karma and the death of Lady Murasaki. In a famous chapter left entirely blank (Vanished into Clouds), Genji withdraws from the world, leaving a legacy of Mono no Aware (the pathos of things).""",
    "characters": [
      {"name": "Hikaru Genji", "role": "The Shining Prince", "desc": "Brilliant courtier whose life explores aesthetic heights and human longing."},
      {"name": "Murasaki Shikibu", "role": "Master Novelist", "desc": "Heian lady whose psychological depth founded Japanese narrative art."},
      {"name": "Lady Murasaki", "role": "Genji’s True Love", "desc": "Ideal of elegance and grace in the Heian world."}
    ],
    "themes": ["Mono no Aware (Pathos of Impermanence)", "Psychological Realism", "Courtly Poetry", "Buddhist Karma"],
    "echoes": "Preceded Western psychological novels (Cervantes, Proust) by over six centuries.",
    "famousQuote": "“Can any sorrow be heavier than the parting of those who love?” — Murasaki Shikibu",
    "historicalContext": "Written in Japanese Kana phonetic script during the peak of the Fujiwara regency in Kyoto."
  },
  {
    "id": "dante-divine-comedy",
    "year": 1320,
    "displayDate": "1308 – 1320 CE (Late Medieval Italy)",
    "era": "medieval",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Florence & The Three Afterlife Realms",
    "author": "Dante Alighieri (Il Sommo Poeta)",
    "title": "The Divine Comedy (La Divina Commedia)",
    "subtitle": "Inferno, Purgatorio, and Paradiso: The Soul’s Journey to the Stars",
    "summary": "The crowning masterpiece of medieval literature. Guided by Virgil through the nine circles of Hell and seven terraces of Purgatory, Dante is led by Beatrice through the spheres of Paradise to gaze upon the Love that moves the sun and stars.",
    "fullStory": """### Act I: The Dark Wood and the Gates of Hell
Lost in a dark wood at midlife, Dante is rescued by the shade of Virgil, sent by Beatrice. They pass the stone gate inscribed: *"Abandon all hope, ye who enter here."*

### Act II: The Inferno, Purgatorio, and Paradiso
They descend through nine circles of Hell, witnessing the contrapasso punishments of lust, greed, violence, and treachery, reaching Lucifer frozen in Lake Cocytus. Ascending Mount Purgatory, Dante is cleansed of the seven deadly sins. Beatrice guides him through the celestial spheres to the Empyrean, where Dante beholds the Holy Trinity in blinding radiant light.""",
    "characters": [
      {"name": "Dante Alighieri", "role": "Pilgrim & Poet", "desc": "Exiled Florentine whose spiritual crisis became the allegory of redemption."},
      {"name": "Virgil", "role": "Master Guide & Reason", "desc": "Roman poet who guides Dante through Hell and Purgatory."},
      {"name": "Beatrice", "role": "Divine Muse & Grace", "desc": "Dante's beloved who leads him to the vision of God."}
    ],
    "themes": ["Divine Justice (Contrapasso)", "Spiritual Transformation", "Moral Allegory", "Cosmic Love"],
    "echoes": "Aeneas’s descent in the Aeneid and Prophet Muhammad’s Isra and Mi’raj.",
    "famousQuote": "“L’Amor che move il sole e l’altre stelle.” (The Love that moves the sun and the other stars.) — Paradiso XXXIII",
    "historicalContext": "Written during Dante's exile from Florence, establishing the Tuscan dialect as the Italian language."
  },
  {
    "id": "journey-west-wuchengen",
    "year": 1592,
    "displayDate": "c. 1592 CE (Ming Dynasty China)",
    "era": "renaissance",
    "regionId": "china",
    "regionName": "China & East Asia",
    "place": "Chang’an to India",
    "author": "Wu Cheng’en",
    "title": "Journey to the West: Sun Wukong and the Sacred Sutras",
    "subtitle": "Havoc in Heaven, the 81 Perils, and the Pilgrimage of Xuanzang",
    "summary": "The epic pilgrimage of monk Xuanzang to India to retrieve Buddhist scriptures, escorted by Sun Wukong (the Monkey King), Pigsy, and Sandy through 81 supernatural perils.",
    "fullStory": """### Act I: Havoc in Heaven and the Five Fingers Mountain
Born from a magic stone, Sun Wukong masters 72 transformations, claims a size-shifting iron staff from the Dragon King, and wreaks havoc in Heaven. Buddha traps him beneath a mountain for 500 years until monk Xuanzang frees him.

### Act II: The Silk Road and Enlightenment
Joined by Pigsy and Sandy, the pilgrims battle demons across burning deserts and mountains, defeating the White Bone Demon and Spider Fiends. Reaching Vulture Peak, Sun Wukong attains enlightenment as the Victorious Fighting Buddha.""",
    "characters": [
      {"name": "Sun Wukong (Monkey King)", "role": "Trickster Hero", "desc": "Indestructible warrior wielding the magic iron staff."},
      {"name": "Xuanzang (Tripitaka)", "role": "Holy Monk", "desc": "Spiritual pilgrim seeking sacred scriptures."},
      {"name": "Zhu Bajie (Pigsy)", "role": "Gluttonous Disciple", "desc": "Former heavenly marshal wielding a nine-toothed rake."}
    ],
    "themes": ["Spiritual Enlightenment", "Mind Monkey (Intellect vs Discipline)", "Brotherhood", "Syncretism"],
    "echoes": "Parallels the fellowship of Tolkien's Lord of the Rings and the Ramayana.",
    "famousQuote": "“A single step taken in sincerity brings you closer to the Western Paradise.” — Wu Cheng’en",
    "historicalContext": "Based on the 7th-century historical pilgrimage of monk Xuanzang along the Silk Road."
  },
  {
    "id": "cervantes-don-quixote",
    "year": 1605,
    "displayDate": "1605 – 1615 CE (Spanish Golden Age)",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "La Mancha, Spain",
    "author": "Miguel de Cervantes Saavedra",
    "title": "Don Quixote de la Mancha",
    "subtitle": "The Knight of the Woeful Countenance, Sancho Panza, and the Windmills",
    "summary": "An aging country gentleman driven mad by chivalric romances renames himself Don Quixote, riding with his squire Sancho Panza to right the world’s wrongs in the founding novel of modern literature.",
    "fullStory": """### Act I: Madness and the Windmills
Alonso Quijano crowns himself Don Quixote, mounts Rocinante, names peasant girl Aldonza his lady Dulcinea, and recruits Sancho Panza. Charging windmills mistaking them for giants, he blames sorcery when thrown from his saddle.

### Act II: Sancho's Island and Return to Sanity
Sancho governs the mock island of Barataria with surprising wisdom. Defeated on Barcelona beach by the Knight of the White Moon, Quixote honors his vow, returns home, regains sanity, and dies peacefully as Alonso the Good.""",
    "characters": [
      {"name": "Don Quixote", "role": "Idealist Knight", "desc": "Visionary whose noble madness exposes the cynicism of reality."},
      {"name": "Sancho Panza", "role": "Earthy Squire", "desc": "Pragmatic peasant whose loyalty balances Quixote’s dreams."}
    ],
    "themes": ["Idealism vs Realism", "Power of Fiction", "Friendship", "Invention of Modern Novel"],
    "echoes": "Blueprint for literary buddy pairs from Holmes & Watson to Frodo & Sam.",
    "famousQuote": "“To dream the impossible dream, to fight the unbeatable foe...” — Don Quixote ethos",
    "historicalContext": "Written by Cervantes after imprisonment, establishing the modern European novel."
  },
  {
    "id": "shakespeare-hamlet",
    "year": 1601,
    "displayDate": "1599 – 1601 CE (Elizabethan England)",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Elsinore Castle, Denmark",
    "author": "William Shakespeare (The Bard of Avon)",
    "title": "Hamlet, Prince of Denmark",
    "subtitle": "The Ghost, 'To Be or Not to Be', and the Poisoned Duel",
    "summary": "Prince Hamlet is commanded by his father’s ghost to avenge his murder by uncle Claudius. Paralyzed by existential doubt, Hamlet feigns madness in the ultimate tragedy of human intellect.",
    "fullStory": """### Act I: The Ghost and the Mousetrap
On the ramparts of Elsinore, King Hamlet's ghost reveals he was poisoned by Claudius. Hamlet stages *The Mousetrap* play to catch the King's conscience, confirms his guilt, and delivers his iconic *"To be or not to be"* soliloquy.

### Act II: Ophelia and the Poisoned Rapier
Ophelia drowns in grief. Claudius arranges a fencing duel between Hamlet and Laertes using a poisoned rapier and wine. Gertrude drinks the poison, Laertes and Hamlet are both struck by the lethal blade, and Hamlet kills Claudius before whispering: *"The rest is silence."*""",
    "characters": [
      {"name": "Prince Hamlet", "role": "Tragic Philosopher", "desc": "Intellectual prince torn between action and contemplation."},
      {"name": "King Claudius", "role": "Usurping Monarch", "desc": "Murdered his brother to seize crown and queen."},
      {"name": "Ophelia", "role": "Tragic Maiden", "desc": "Innocent victim of court intrigue."}
    ],
    "themes": ["Action vs Inaction", "Appearance vs Reality", "Mortality", "Conscience"],
    "echoes": "Orestes avenging Agamemnon in Aeschylus and the Norse Amleth saga.",
    "famousQuote": "“There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy.” — Hamlet",
    "historicalContext": "The supreme pinnacle of English dramatic literature during Queen Elizabeth I's reign."
  }
]

# Additional legendary stories to complete the global collection:
set3 = [
  {
    "id": "norse-ragnarok",
    "year": 1000,
    "displayDate": "c. 800 – 1220 CE (Viking Age / Eddas)",
    "era": "medieval",
    "regionId": "n_europe",
    "regionName": "Northern & Celtic Europe",
    "place": "Yggdrasil & the Plain of Vigrid",
    "author": "Snorri Sturluson & Anonymous Poetic Edda Skalds",
    "title": "Ragnarök: The Twilight of the Gods and the Green Rebirth",
    "subtitle": "Yggdrasil, the Murder of Baldr, the Fimbulwinter, and the New Sun",
    "summary": "The ultimate doom and renewal of the Norse cosmos. Following the three-year Fimbulwinter, the wolf Fenrir breaks free, the Midgard Serpent boils the ocean, and gods and giants clash at Vigrid. The world burns and sinks into the sea, only to emerge renewed and green.",
    "fullStory": """### Act I: The World Tree and the Death of Baldr
The cosmos is held together by Yggdrasil, the great ash tree connecting nine worlds. But doom is foretold when Baldr, the beloved god of light, is killed by a mistletoe dart through the trickery of Loki. The gods bind Loki with the entrails of his son beneath a dripping venomous serpent.

### Act II: Fimbulwinter and the Breaking of Chains
Three unbroken winters of freezing snow and moral collapse (*Fimbulwinter*) grip the earth. The giant wolf Fenrir snaps his magical ribbon *Gleipnir*, opening jaws that stretch from earth to heaven. Jörmungandr the Midgard Serpent thrashes out of the ocean, spitting venom across sky and sea. The fire giant Surtr marches from Muspelheim, his flaming sword shattering the rainbow bridge Bifröst.

### Act III: The Last Stand at Vigrid
Gods and Einherjar warriors meet the monsters on the plain of Vigrid:
- Odin is swallowed by Fenrir, avenged by his son Vidar tearing the wolf's jaws apart.
- Thor slays the Midgard Serpent with his hammer Mjölnir, but takes nine steps and falls dead from its venom.
- Freyr is slain by Surtr; Heimdall and Loki kill each other.
Surtr flings fire across the nine worlds, and the black earth sinks beneath boiling waves.

### Act IV: The Green Dawn
The darkness lifts. Out of the calm sea rises a new, fertile green earth where crops grow unsown. Baldr returns from Hel. Two humans, Lif and Lifthrasir, who hid in the trunk of Yggdrasil surviving on morning dew, emerge to repopulate the world under a new, warmer sun.""",
    "characters": [
      {"name": "Odin (Allfather)", "role": "King of the Gods", "desc": "God of wisdom and war who sacrificed his eye and embraced his prophesied doom."},
      {"name": "Thor", "role": "God of Thunder", "desc": "Defender of mankind who slew the world-serpent."},
      {"name": "Loki", "role": "Trickster & Catalyst of Doom", "desc": "Blood-brother of Odin who led the army of monsters at Ragnarök."}
    ],
    "themes": ["Cyclical Destruction and Renewal", "Heroic Defiance in the Face of Inevitable Doom", "Cosmic Balance"],
    "echoes": "Parallels the Aztec destruction of the suns, the Greek Titanomachy, and the Apocalypse of John.",
    "famousQuote": "“The sun turns black, earth sinks into the sea, the bright stars vanish from the sky... Now do I see the green earth rise once more from the ocean.” — Völuspá, Poetic Edda",
    "historicalContext": "Preserved in the 13th-century Codex Regius and Snorri's Prose Edda, reflecting the fatalistic courage of Viking culture."
  },
  {
    "id": "arabian-nights-scheherazade",
    "year": 850,
    "displayDate": "c. 850 – 1400 CE (Abbasid Golden Age & Mamluk Cairo)",
    "era": "medieval",
    "regionId": "persia_arabia",
    "regionName": "Persia & Arabia",
    "place": "Baghdad, Basra, Cairo & Samarkand",
    "author": "Traditional Storytellers (Recorded by Abu Abd-Allah al-Jahshiyari)",
    "title": "One Thousand and One Nights (Arabian Nights)",
    "subtitle": "Scheherazade’s 1,001 Cliffhangers, Sinbad’s Seven Voyages, and Aladdin’s Lamp",
    "summary": "To stop the bitter King Shahryar from executing a new bride every morning, the courageous, learned Scheherazade volunteers to marry him, telling captivating tales each night and pausing at cliffhangers at dawn—healing the king’s broken soul through 1,001 nights of storytelling.",
    "fullStory": """### Act I: The Wounded King and the Brave Storyteller
Betrayed by his first wife, King Shahryar vows to marry a virgin bride each night and execute her at dawn so she can never deceive him. Terror grips the kingdom until Scheherazade, the vizier’s brilliant daughter who has memorized thousands of history chronicles, poetry, and philosophy, volunteers to marry the king.

That night, Scheherazade asks permission for her sister Dunyazad to sit in the chamber. Near dawn, Scheherazade begins a spellbinding tale of genies, sorcerers, and magical voyages. Just as the climax arrives, the morning light breaks; Scheherazade falls silent. Enraptured, the King postpones her execution for one day to hear the conclusion.

### Act II: The Great Nested Tales (Sinbad, Aladdin, Ali Baba)
Night after night, Scheherazade weaves interconnected, nested stories:
- **Sinbad the Sailor**: Seven perilous voyages across the Indian Ocean facing giant Roc birds, cyclopean giants, and magnetic mountains.
- **Aladdin and the Magic Lamp**: A poor youth in China discovers a magical jinni in a subterranean treasure cave.
- **Ali Baba and the Forty Thieves**: The magic password *"Open Sesame"* unlocks a cavern of gold.

### Act III: The Healing of Shahryar
After 1,001 nights and bearing three healthy princes, Scheherazade steps before the King, presenting her sons and asking if she may live. The King weeps, kissing her forehead, declaring that her wisdom, courage, and stories have purified his heart of hatred and restored his faith in humanity. A grand celebration is proclaimed across the realm.""",
    "characters": [
      {"name": "Scheherazade", "role": "Heroic Storyteller & Queen", "desc": "Used intellect, psychological insight, and narrative genius to save countless lives."},
      {"name": "King Shahryar", "role": "Wounded Monarch", "desc": "Embittered ruler whose soul was redeemed through literature."},
      {"name": "Sinbad the Sailor", "role": "Merchant Adventurer", "desc": "Endured seven shipwrecks to become a paragon of resilience."}
    ],
    "themes": ["Storytelling as Salvation", "Healing Trauma through Art", "Compassion over Vengeance", "Nested Realities"],
    "echoes": "Nested frame-story structure directly influenced Boccaccio’s Decameron and Chaucer’s Canterbury Tales.",
    "famousQuote": "“O King, stories are the medicine of the afflicted heart; through them we travel where no horse can carry us.” — Scheherazade",
    "historicalContext": "Compiled over centuries in Baghdad and Cairo, synthesizing Persian (Hezar Afsan), Indian, and Arabic storytelling traditions."
  },
  {
    "id": "maui-polynesian-myths",
    "year": 1000,
    "displayDate": "c. 1000 CE (Polynesian & Māori Oral Epic)",
    "era": "medieval",
    "regionId": "oceania",
    "regionName": "Oceania & Australia",
    "place": "Aotearoa (New Zealand), Hawaii & Hawaiki",
    "author": "Polynesian Tohunga (Master Navigators & Priests)",
    "title": "The Legends of Māui: The Demigod Who Fished Up Islands",
    "subtitle": "Snaring the Sun, the Secret of Fire from Mahuika, and Te Ika-a-Māui",
    "summary": "The supreme trickster hero of the Pacific. Using a magic hook carved from his grandmother’s jawbone, Māui fishes up the North Island of New Zealand from the ocean abyss, snares the blazing sun with flax ropes to slow its speed, and steals sacred fire from Mahuika.",
    "fullStory": """### Act I: The Casting Out and the Magic Fishhook
Born prematurely, Māui is wrapped in his mother Taranga's hair and cast into the sea foam. Nourished by jellyfish and raised by the sea god Tangaroa, he returns home to amaze his brothers with his quick wit and supernatural power. He claims the enchanted jawbone of his ancestral grandmother Murirangawhenua, fashioning it into a sacred fishhook (*Manaiakalani*).

### Act II: Fishing Up the North Island (Te Ika-a-Māui)
Hiding beneath the deck of his brothers' fishing waka (canoe), Māui waits until they reach the deep open ocean. Smearing the hook with blood from his own nose, he drops the line into the abyss. The hook catches the carved gable of the sunken house of Tonganui. 

Straining with immense strength, chanting ancient karakia incantations, Māui hauls a colossal, writhing fish to the surface: **Te Ika-a-Māui** (The Fish of Māui), which becomes the North Island of New Zealand, while the canoe becomes the South Island (*Te Waka a Māui*).

### Act III: Snaring the Sun and the Gift of Fire
In the ancient days, Tama-nui-te-rā (the Sun) raced across the sky so swiftly that humans could not finish cooking food or planting crops before night fell. Māui and his brothers wove heavy ropes of flax, journeyed to the eastern horizon, and trapped the Sun in a net. Māui struck the Sun with the magic jawbone until it promised to travel slowly across the heavens forever.

Later, Māui journeyed to the Underworld to visit Mahuika, the goddess of fire. By cunningly asking for one fingernail of fire after another until she had only one left, Māui preserved the spark of fire inside the Kaikomako and Mahoe trees, teaching mankind how to rub firesticks together.""",
    "characters": [
      {"name": "Māui-tikitiki-a-Taranga", "role": "Demigod & Culture Hero", "desc": "Brilliant trickster who lifted the skies, fished up lands, and brought fire to humanity."},
      {"name": "Tama-nui-te-rā", "role": "The Sun God", "desc": "Forced by Māui to slow his daily march across the Pacific sky."},
      {"name": "Mahuika", "role": "Goddess of Fire", "desc": "Keeper of sacred flame in her fingernails and toenails."}
    ],
    "themes": ["Trickster Intellect over Raw Nature", "Human Benefit through Daring Feats", "Connection to the Ocean", "Voyaging Spirit"],
    "echoes": "Stealing fire from Mahuika directly parallels Prometheus in Greek myth and Coyote in Native American lore.",
    "famousQuote": "“The canoe is the South Island, the anchor stone is Stewart Island, and the great fish pulled from the deep is our home.” — Māori Proverb on Te Ika-a-Māui",
    "historicalContext": "Spread across thousands of miles from Hawaii to Easter Island and New Zealand during the great Polynesian ocean migrations."
  },
  {
    "id": "anansi-spider-tales",
    "year": 1200,
    "displayDate": "c. 1200 CE (Akan & Ashanti Traditions / Diaspora)",
    "era": "medieval",
    "regionId": "africa",
    "regionName": "Sub-Saharan Africa",
    "place": "Ashanti Kingdom (Ghana) & Transatlantic Diaspora",
    "author": "Akan Storytellers & Griots (Anansesem)",
    "title": "Anansi the Spider: How All Stories Came to Earth",
    "subtitle": "Buying the Golden Box of Stories from Sky God Nyame with Hornets and Pythons",
    "summary": "In the beginning, all stories in the universe belonged to the Sky God Nyame in a golden box. Anansi the clever spider tricks the deadly hornets, python, and leopard to win the stories for humanity, becoming the beloved trickster symbol of resilience across Africa and the Caribbean.",
    "fullStory": """### Act I: The Empty Earth and the Sky God’s Price
In the earliest days, the earth was silent and boring: no human had ever told a fable, sung a riddle, or shared an evening tale, for all stories (*Anansesem*) were locked away in a golden box kept beside the throne of Nyame the Sky God.

**Kwaku Anansi**, the clever spider, spun a web up to the heavens and offered to buy the stories. Nyame laughed: *"Kings with armies of gold cannot buy my stories! How can a weak little spider?"* 

Nyame demanded an impossible price:
1. **Mmoboro**: the swarm of ferocious, stinging hornets.
2. **Onini**: the giant python who can swallow a man whole.
3. **Osebo**: the leopard with teeth of obsidian.
4. **Mmoatia**: the invisible fairy of the forest.

### Act II: The Four Tricks of Anansi
Anansi did not use brute strength; he used his quick wits:
1. He filled a hollow calabash gourd with water, poured it over his head and a hornets' nest while holding a banana leaf: *"The rains have come! Fly into my dry calabash!"* When the hornets flew inside, Anansi plugged the hole.
2. He walked past the python carrying a long palm branch, muttering loudly: *"My wife says you are shorter than this stick, but I know you are longer!"* The proud python stretched out along the branch to prove his length, and Anansi tied him to the wood with vines.
3. He dug a deep pit on the leopard's hunting trail. When Osebo fell in, Anansi offered to help him out with a bent sapling; when the leopard caught the branch, Anansi pulled the trigger, flinging the leopard into a net.
4. He carved a wooden doll, coated it in sticky sap, and placed a bowl of mashed yams in its lap. When the forest fairy greeted the doll and received silence, she slapped it, becoming stuck to the sap.

### Act III: The Opening of the Golden Box
Anansi carried the four prizes to Nyame's celestial court. Stunned by the spider's genius, the Sky God bowed before him: *"No man or god has ever achieved this. From this day forward, all stories shall be called Anansi Stories!"*

Nyame opened the golden box, and thousands of luminous, colorful stories swarmed out like fireflies, scattering across the four corners of the earth into the hearts and tongues of human beings. Across the centuries, when enslaved Africans were taken to the Caribbean and the Americas, the spirit of Anansi survived as *Aunt Nancy* and *Br'er Rabbit*, a beacon of survival and intellect overcoming oppression.""",
    "characters": [
      {"name": "Kwaku Anansi", "role": "Master Trickster & Spider Hero", "desc": "Weak in physical stature but supreme in wit, strategy, and humor."},
      {"name": "Nyame", "role": "Sky God & Keeper of Wisdom", "desc": "Ruler of the heavens whose challenge was met by Anansi."},
      {"name": "Osebo & Onini", "role": "Forest Predators", "desc": "Formidable creatures conquered through psychology rather than force."}
    ],
    "themes": ["Wit and Cunning over Brute Force", "Liberation of Knowledge and Art", "Survival under Oppression", "Diaspora Resilience"],
    "echoes": "Parallels Prometheus bringing fire, Hermes stealing Apollo's cattle, and Native American Coyote trickster tales.",
    "famousQuote": "“We do not really mean that what we say is true, but without stories, we would have no light to see each other in the dark.” — Akan Storyteller Opening Blessing",
    "historicalContext": "Anansesem remains one of the most vibrant folklore traditions in West Africa and spread across Jamaica, Suriname, and the American South."
  },
  {
    "id": "milton-paradise-lost",
    "year": 1667,
    "displayDate": "1667 – 1674 CE (English Epic Poetry)",
    "era": "renaissance",
    "regionId": "world_classics",
    "regionName": "Global Masterpieces & Renaissance",
    "place": "Hell, Chaos, Heaven & The Garden of Eden",
    "author": "John Milton (The Blind English Epicist)",
    "title": "Paradise Lost: The Fall of Lucifer and Man",
    "subtitle": "The War in Heaven, Pandæmonium, 'Better to Reign in Hell', and the Expulsion from Eden",
    "summary": "The monumental epic poem of the English language. Dictated while blind by John Milton to 'justify the ways of God to men'. It depicts the rebellion of Satan and the fallen angels, their descent into Hell, the construction of Pandæmonium, and the temptation and expulsion of Adam and Eve.",
    "fullStory": """### Act I: The Lake of Fire and Pandæmonium
Cast down from Heaven after a catastrophic three-day war against the Archangel Michael and the Son of God, Satan and his legion of rebel angels awaken stunned and chained upon a burning lake of liquid fire in Hell.

Refusing to submit to divine authority, Satan raises his spear and addresses his fallen comrades with defiant eloquence:
*"What though the field be lost? All is not lost; the unconquerable will, and study of revenge, immortal hate, and courage never to submit or yield... Better to reign in Hell than serve in Heaven!"*

The fallen angels build **Pandæmonium**, a glittering golden temple designed by the architect Mulciber. In the great council of devils, Moloch counsels open war, Belial peaceful ignominy, and Mammon building a wealthy empire in Hell. But Beelzebub reveals God's creation of a new world and a new favored creature: Man. Satan volunteers to cross the terrifying gulf of Chaos alone to corrupt humanity.

### Act II: The Flight through Chaos and the Garden of Eden
Satan bypasses Sin and Death at the iron gates of Hell and flies across the howling abyss of Chaos, arriving on the pristine, newly created Earth. Gazing upon the bliss of the Garden of Eden and the innocent love of Adam and Eve, Satan feels a momentary pang of sorrow and remorse: *"Farewell remorse! All good to me is lost; Evil, be thou my Good!"*

The Archangel Raphael is sent from Heaven to warn Adam of the approaching danger, narrating the cosmic War in Heaven and urging obedience.

### Act III: The Temptation and the Fall
Entering the Garden as a morning mist, Satan slips inside the sleeping body of a magnificent serpent. Finding Eve alone tending the roses, he speaks with a human voice, flattering her beauty and intellect. 

When Eve notes that eating from the Tree of Knowledge brings death, the serpent argues that he ate and gained speech and higher consciousness: *"God will not destroy you for gaining knowledge! He desires to keep you low and dependent!"* Eve eats the fruit. The earth trembles in agony. When Adam discovers her deed, knowing she is doomed, his boundless love forces his choice: he willingly eats alongside her so they may share one fate together.

### Act IV: The Vision of the Future and the Open World
Their innocence stripped away, shame and recrimination poison their hearts. The Son of God descends in gentle judgment, clothing them in animal skins. 

The Archangel Michael leads Adam to the highest mountain of Eden, revealing the future pageant of human history—Cain and Abel, the Flood, the prophets, and the coming of the Redeemer who will restore paradise inside the human heart (*"A Paradise within thee, happier far"*).

Wiping away their tears, Adam and Eve clasp hands, stepping out through the eastern gate guarded by the flaming brand of the cherubim, walking out together into the vast, open world before them.""",
    "characters": [
      {"name": "Satan (Lucifer)", "role": "Fallen Archangel & Antihero", "desc": "Charismatic, tragic rebel whose boundless pride brought about his cosmic downfall."},
      {"name": "Adam & Eve", "role": "First Parents of Humanity", "desc": "Innocent beings whose fall introduced moral choice and redemptive hope into history."},
      {"name": "The Son of God", "role": "Divine Champion & Redeemer", "desc": "Drove the rebels from heaven and stepped forward as the sacrifice of mercy."},
      {"name": "Archangel Michael", "role": "General of the Heavenly Host", "desc": "Guided Adam with the vision of the future world."}
    ],
    "themes": ["Free Will and Moral Responsibility", "Pride and the Psychology of Evil", "Love and Sacrifice", "Justifying Divine Providence"],
    "echoes": "Directly dialogs with Dante’s Inferno and Homer’s heroic code, transforming martial combat into spiritual warfare.",
    "famousQuote": "“The mind is its own place, and in itself can make a Heaven of Hell, a Hell of Heaven.” — John Milton, Paradise Lost, Book I",
    "historicalContext": "Composed by Milton in total blindness following the collapse of the English Commonwealth, dictated to his daughters line by line."
  }
]

# Combine all unique stories
all_combined = []
seen_ids = set()

for story in set1 + set2 + set3:
    if story["id"] not in seen_ids:
        seen_ids.add(story["id"])
        all_combined.append(story)

# Sort chronologically by year
all_combined.sort(key=lambda s: s["year"])

print(f"Total compiled unique world stories: {len(all_combined)}")

# Output to stories_data.js
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

const STORIES_DATA = """ + json.dumps(all_combined, indent=2, ensure_ascii=False) + """;

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { REGIONS, ERAS, STORIES_DATA };
}
"""

out_path = r"f:\AntiGravity\Apps Data\WorldHistoryTimeline\js\stories_data.js"
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully written {len(all_combined)} stories to {out_path}!")
