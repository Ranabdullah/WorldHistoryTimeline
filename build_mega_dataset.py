# -*- coding: utf-8 -*-
"""
Generates the mega dataset of 130+ world stories, mythologies, and writers.
"""

import json
import os

# Helper to build consistent rich story records
def make_story(id, year, displayDate, era, regionId, regionName, place, author, title, subtitle, summary, fullStory, characters=None, themes=None, echoes="", famousQuote="", historicalContext=""):
    return {
        "id": id,
        "year": year,
        "displayDate": displayDate,
        "era": era,
        "regionId": regionId,
        "regionName": regionName,
        "place": place,
        "author": author,
        "title": title,
        "subtitle": subtitle,
        "summary": summary,
        "fullStory": fullStory,
        "characters": characters or [],
        "themes": themes or ["Heroism", "Cultural Identity", "Cosmic Order"],
        "echoes": echoes,
        "famousQuote": famousQuote,
        "historicalContext": historicalContext
    }

stories = []

# --- 1. OCEANIA & AUSTRALIA ---
stories.append(make_story(
    "rainbow-serpent", -10000, "c. 10,000+ BCE (65,000 Year Living Oral Tradition)", "prehistory", "oceania", "Oceania & Australia",
    "Arnhem Land & Australian Red Centre", "Aboriginal Songline Custodians & Elders",
    "The Dreaming and the Great Rainbow Serpent (Almudj / Wagyl)", "The Creation of Earth's Watercourses and Living Songlines",
    "In the primordial Dreamtime (Tjukurpa), the giant Rainbow Serpent slithers across a barren earth, carving out gorges, rivers, and waterholes, establishing the sacred ancestral laws (Songlines).",
    "### Act I: The Awakening from Deep Earth\nIn the Dreamtime (Tjukurpa), the Rainbow Serpent stirred beneath the arid Australian crust, erupting upward to release the first life-giving rains.\n\n### Act II: Sculpting the Gorges\nHer massive undulating body carved deep riverbeds like the Katherine and Ord rivers, leaving sacred waterholes (billabongs) behind.\n\n### Act III: The Sacred Law\nShe gave clans their languages, totem laws, and unwritten Songlines. Those who disrespect Country face her tempestuous wrath.\n\n### Epilogue: Everywhen\nThe Dreaming is not in the past; it is an eternal present living in the land today.",
    [{"name": "Almudj (Rainbow Serpent)", "role": "Creator & Water Guardian", "desc": "Ancestral serpent whose movement shaped rivers."}, {"name": "Ancestral Elders", "role": "Songline Keepers", "desc": "Preserve unwritten maps of Country."}],
    ["Living Country", "Sacred Stewardship", "Everywhen"],
    "Parallels Jörmungandr in Norse and Quetzalcoatl in Mesoamerica.",
    "“The land is our mother; we belong to the land.” — Yolngu Songline Teaching",
    "Rock art depicting Rainbow Serpents in Arnhem Land is dated over 10,000 years old."
))

stories.append(make_story(
    "tiddalik-frog", -8000, "c. 8000 BCE", "prehistory", "oceania", "Oceania & Australia",
    "Wollombi Valley, Eastern Australia", "Kulin & Gunai Nations Oral Tradition",
    "Tiddalik the Giant Frog: The Great Drought and the Burst of Life", "The Monster of Thirst Who Swallowed Every River",
    "Tiddalik the giant frog awakens with an insatiable thirst, drinking every river and lake dry until the animal council makes him laugh, releasing a torrential flood that revives the earth.",
    "### Act I: The Thirst of Tiddalik\nTiddalik drank until rivers shrank to mud and billabongs turned to dust. The animals faced extinction.\n\n### Act II: The Animal Council\nWombat, Kangaroo, and Kookaburra gathered to make Tiddalik laugh so water would pour from his mouth. Dances and jokes failed.\n\n### Act III: The Eel's Dance\nNabunum the Eel tied himself in knots and spun like a top. Tiddalik cracked a smile, then burst into roaring laughter—releasing a deluge that revived every forest.",
    [{"name": "Tiddalik", "role": "Giant Frog of Thirst", "desc": "Swallowed all freshwater on the continent."}, {"name": "Nabunum the Eel", "role": "Comedic Savior", "desc": "Made Tiddalik laugh with contortionist dances."}],
    ["Resource Conservation", "Community Cooperation", "Humor as Power"],
    "Parallels the Vedic myth of Indra piercing Vritra to release cosmic waters.",
    "“Take only what you need from the waterhole, lest Tiddalik return.” — Gunai Proverb",
    "Echoes megafauna memories of giant Pleistocene amphibians in prehistoric Australia."
))

stories.append(make_story(
    "maui-fish-islands", 1000, "c. 1000 CE", "medieval", "oceania", "Oceania & Australia",
    "Aotearoa (New Zealand) & Polynesia", "Polynesian Tohunga (Oral Navigators)",
    "Māui Fishes up the North Island (Te Ika-a-Māui)", "The Magic Jawbone Hook and the Hauling of Aotearoa",
    "Using a magic fishhook carved from his grandmother’s jawbone and baited with his own blood, the trickster demigod Māui hauls the North Island of New Zealand up from the ocean abyss.",
    "### Act I: The Stowaway Brother\nMāui hid aboard his brothers' canoe until reaching deep ocean.\n\n### Act II: The Great Catch\nBaited with blood from his nose, his hook caught the sunken temple of Tonganui. Chanting karakia, he hauled up Te Ika-a-Māui.\n\n### Act III: The Mountains\nWhile Māui thanked the gods, his brothers greedily hacked at the fish, creating the rugged mountains of New Zealand.",
    [{"name": "Māui-tikitiki-a-Taranga", "role": "Demigod Trickster", "desc": "Hauled islands and slowed the sun."}, {"name": "Murirangawhenua", "role": "Ancestral Grandmother", "desc": "Provided the enchanted jawbone hook."}],
    ["Daring Feats", "Voyaging Spirit", "Oceanic Connection"],
    "Parallels Hercules lifting the Pillars and Krishna lifting Govardhan hill.",
    "“The fish of Māui is our eternal home.” — Māori Proverb",
    "Preserved across Pacific island navigators spanning 4,000 miles of open ocean."
))

stories.append(make_story(
    "maui-snare-sun", 1050, "c. 1050 CE", "medieval", "oceania", "Oceania & Australia",
    "Haleakalā (Hawaii) & Pacific Islands", "Polynesian Oral Bards",
    "Māui Snares the Sun: Giving Humanity the Gift of Day", "Flax Ropes and the Slowing of Tama-nui-te-rā",
    "Because the sun raced across the sky too quickly for crops to grow or food to cook, Māui wove giant flax ropes, trapped the Sun God in a net, and beat him until he promised to move slowly.",
    "### Act I: Short Days and Starvation\nThe Sun raced across the sky in minutes. Fires could not be lit, crops withered in darkness.\n\n### Act II: The Net of Flax\nMāui and his brothers wove enchanted ropes of flax and traveled to the eastern pit where the sun rises.\n\n### Act III: The Compact with the Sun\nAs Tama-nui-te-rā rose, Māui snared his rays and struck him with the magic jawbone until he agreed to walk slowly forever.",
    [{"name": "Tama-nui-te-rā", "role": "The Sun God", "desc": "Forced to slow his daily march across the sky."}],
    ["Mastery over Nature", "Sacrifice for Mankind"],
    "Parallels Joshua commanding the sun to stand still and Phaethon in Greek myth.",
    "“Now the sun walks with measured steps, and mortals have time to plant and sing.”",
    "Haleakalā in Maui literally translates to 'House of the Sun'."
))

stories.append(make_story(
    "pele-volcano", 1200, "c. 1200 CE", "medieval", "oceania", "Oceania & Australia",
    "Kīlauea & Halemaʻumaʻu, Hawaii", "Hawaiian Kahuna (Chanters)",
    "Pele: The Fire Goddess and the Creation of the Hawaiian Islands", "The Migration from Tahiti, the Sacred Oʻo Stick, and Kīlauea",
    "Exiled by her water-goddess sister Nāmaka, Pele travels across the Pacific chain, using her digging stick Paʻoa to create volcanic craters until finding her eternal home in Kīlauea.",
    "### Act I: The Ocean Flight\nPele fled across the waves in a canoe guarded by her shark brother Kamohoaliʻi.\n\n### Act II: The Fire Stick\nAt each island she dug into the earth, but water flooded her pits until she reached the Big Island of Hawaii.\n\n### Act III: The Throne of Kīlauea\nAt Halemaʻumaʻu, she struck molten magma, making the volcano her eternal seat of creation and destruction.",
    [{"name": "Pele", "role": "Goddess of Volcanoes and Fire", "desc": "Creator of new land through molten lava."}, {"name": "Hiʻiaka", "role": "Beloved Sister", "desc": "Goddess of the hula and forest rejuvenation."}],
    ["Creation and Destruction", "Living Land (ʻĀina)"],
    "Parallels Vulcan/Hephaestus in Greco-Roman myth.",
    "“Aia lā ʻo Pele i Kīlauea — There dwells Pele in Kīlauea.” — Traditional Hawaiian Chant",
    "Accurately maps the geological age of the Hawaiian islands from oldest (Kauai) to youngest (Hawaii)."
))

# --- 2. MESOPOTAMIA & ANCIENT NEAR EAST ---
stories.append(make_story(
    "enheduanna-inanna", -2300, "c. 2300 BCE", "bronze", "mesopotamia", "Mesopotamia & Near East",
    "Ur & Uruk (Sumer / Akkad)", "Enheduanna (History's First Named Author)",
    "The Exaltation of Inanna (Nin-me-šara)", "The 42 Sacred Hymns of the First Recorded Author",
    "Princess Enheduanna, High Priestess of Ur, is driven into the desert by a rebel usurper and composes revolutionary hymns exalting Inanna to reclaim her temple throne through the written word.",
    "### Act I: The Priestess of the Moon\nEnheduanna presided over the grand ziggurat of Ur as daughter of Sargon the Great.\n\n### Act II: Banishment into the Dust\nA rebel general named Lugalanne stripped her crown and exiled her into the wasteland.\n\n### Act III: The Birth of Authored Poetry\nCarving clay tablets under the blazing sun, she composed hymns elevating Inanna above all gods, rallying loyalists and regaining her sacred office.",
    [{"name": "Enheduanna", "role": "High Priestess & Author", "desc": "First individual in history to sign her name to literature."}],
    ["Power of the Written Word", "Divine Justice", "Exile & Triumph"],
    "Precedes Sappho and biblical King David by over a thousand years.",
    "“What I recited at night, the singer shall repeat by day.” — Enheduanna",
    "The alabaster Disk of Enheduanna was discovered in Ur in 1927."
))

stories.append(make_story(
    "gilgamesh-epic", -2100, "c. 2100 – 1200 BCE", "bronze", "mesopotamia", "Mesopotamia & Near East",
    "Uruk & Waters of Death", "Attributed to Sîn-lēqi-unninni",
    "The Epic of Gilgamesh: The Quest for Immortality", "Enkidu, the Slaying of Humbaba, the Deluge, and the Plant of Youth",
    "Gilgamesh, the tyrannical king of Uruk, finds brotherhood in Enkidu. When Enkidu dies, Gilgamesh crosses the Waters of Death to seek Utnapishtim and the secret of eternal life.",
    "### Act I: King and Wild Man\nEnkidu is created from clay to humble Gilgamesh. After a titanic duel, they become inseparable brothers.\n\n### Act II: The Cedar Forest and Ishtar's Wrath\nThey slay Humbaba and the Bull of Heaven. The gods punish them by striking Enkidu down with fever.\n\n### Act III: Journey to the Faraway\nTerrified of death, Gilgamesh visits Utnapishtim, hears the story of the great flood, and wins a plant of youth—only for a snake to steal it while he bathes.\n\n### Act IV: Return to Uruk\nGilgamesh returns to Uruk, finding peace in the enduring beauty of the city walls.",
    [{"name": "Gilgamesh", "role": "King of Uruk", "desc": "Two-thirds god whose quest transforms him."}, {"name": "Enkidu", "role": "Wild Man", "desc": "Civilized by love and friendship."}, {"name": "Utnapishtim", "role": "Flood Survivor", "desc": "Granted immortality after building an ark."}],
    ["Mortality & Wisdom", "Brotherhood", "Civilization vs Nature"],
    "Flood account matches Noah's Ark; grief matches Achilles for Patroclus.",
    "“Look upon the burnt-brick walls of Uruk! Did not the Seven Sages lay its foundation?”",
    "Deciphered from clay tablets from the Library of Ashurbanipal in 1872."
))

stories.append(make_story(
    "enuma-elish", -1800, "c. 1800 BCE", "bronze", "mesopotamia", "Mesopotamia & Near East",
    "Babylon, Mesopotamia", "Babylonian Temple Scribes (Akitu Festival)",
    "Enuma Elish: The Babylonian Creation Epic", "The Battle of Marduk and Tiamat, and the Forging of the Cosmos",
    "When the primordial ocean-dragon Tiamat threatens the gods, Marduk steps forward with the four winds and lightning arrow, splitting Tiamat's body to fashion heaven, earth, and mankind.",
    "### Act I: Primordial Chaos\nApsu and Tiamat mingle in silence before the younger gods awaken.\n\n### Act II: The Dragon's Army\nTiamat spawns eleven monsters and gives Qingu the Tablet of Destinies.\n\n### Act III: Marduk's Victory\nMarduk captures Tiamat in his starlight net, pierces her heart with lightning, and splits her corpse to form the sky and earth.",
    [{"name": "Marduk", "role": "Champion of Babylon", "desc": "Wields the storm winds."}, {"name": "Tiamat", "role": "Salt Water Dragon", "desc": "Cosmic chaos split to form the universe."}],
    ["Cosmogony", "Order vs Chaos", "Divine Kingship"],
    "Echoes Zeus fighting Typhon and Yahweh subduing Leviathan.",
    "“When in the height heaven was not named... Marduk split the dragon like a shellfish.”",
    "Recited annually at the Akitu New Year Festival in Babylon."
))

stories.append(make_story(
    "atrahasis-flood", -1700, "c. 1700 BCE", "bronze", "mesopotamia", "Mesopotamia & Near East",
    "Sippar & Mesopotamia", "Scribe Ipiq-Aya",
    "The Epic of Atrahasis: The Flood and Human Overpopulation", "Enlil's Noise, Ea's Reed Wall Whisper, and the Boat of Life",
    "When the clamor of humanity keeps the god Enlil awake, he unleashes plagues and a world-cleansing deluge. The wise king Atrahasis is secretly warned by Ea through a reed hut wall to build a giant ship.",
    "### Act I: The Rebellion of the Igigi\nThe younger gods strike against heavy ditch-digging; humanity is molded from clay and a slain god's spirit to carry the work.\n\n### Act II: The Noise of Mankind\nHumanity multiplies so loudly that Enlil cannot sleep. He orders drought, plague, and finally the Deluge.\n\n### Act III: The Reed Hut Warning\nEa whispers to the wall of Atrahasis's hut: 'Dismantle your house, build a boat, save the seed of life!' Atrahasis weathers the storm for seven days.",
    [{"name": "Atrahasis", "role": "The Exceedingly Wise King", "desc": "Preserved life during the Mesopotamian deluge."}, {"name": "Enlil", "role": "Storm God", "desc": "Sought to silence humanity's clamor."}, {"name": "Ea", "role": "God of Waters & Wisdom", "desc": "Humanity's secret protector."}],
    ["Human Noise & Divine Rest", "Preservation of Life"],
    "Direct ancestor to the biblical Noah and Greek Deucalion flood narratives.",
    "“Wall, listen to me! Reed hut, understand my words! Tear down your house and build a boat!”",
    "Oldest cuneiform flood tablet copied during the reign of King Ammi-saduqa of Babylon."
))

stories.append(make_story(
    "ishtar-underworld", -1600, "c. 1600 BCE", "bronze", "mesopotamia", "Mesopotamia & Near East",
    "Kur (Mesopotamian Netherworld)", "Sumerian / Akkadian Liturgical Priesthood",
    "The Descent of Ishtar (Inanna) to the Underworld", "The Seven Gates of Kur, the Naked Goddess, and Dumuzi's Substitute",
    "Ishtar descends to the dark realm of her sister Ereshkigal. Stripped of her jewelry and garments at seven bronze gates, she is hung upon a meat hook until rescued by water-demons, requiring her lover Dumuzi to take her place.",
    "### Act I: The Seven Gates\nAt each gate of the Underworld, the guardian Neti strips one piece of Ishtar's royal regalia until she stands naked and powerless.\n\n### Act II: The Curse of Ereshkigal\nEreshkigal strikes Ishtar with sixty diseases and hangs her on a spike.\n\n### Act III: The Cosmic Stagnation\nOn earth, all fertility and reproduction cease. Ea creates two genderless spirits from dirt under his fingernails to sprinkle the water of life upon Ishtar.\n\n### Act IV: Dumuzi's Fate\nTo return, Ishtar must offer a living substitute. Finding her husband Dumuzi feasting on a throne instead of mourning, she sends him to the underworld for half of every year.",
    [{"name": "Ishtar / Inanna", "role": "Queen of Heaven", "desc": "Goddess of passion and war."}, {"name": "Ereshkigal", "role": "Queen of the Great Below", "desc": "Dark ruler of the land of no return."}, {"name": "Dumuzi (Tammuz)", "role": "Shepherd God", "desc": "Seasonal dying-and-rising deity."}],
    ["Katabasis (Descent)", "Seasonal Cycle", "Stripping of Ego"],
    "Direct blueprint for Greek Persephone and Demeter, and Orpheus descending for Eurydice.",
    "“To the Land of No Return, the realm of Ereshkigal, Ishtar daughter of Sin turned her mind.”",
    "Provided the theological basis for ancient Near Eastern seasonal agricultural rites."
))

stories.append(make_story(
    "hammurabi-code", -1750, "c. 1750 BCE", "bronze", "mesopotamia", "Mesopotamia & Near East",
    "Babylon & Susa", "King Hammurabi of Babylon",
    "The Code of Hammurabi: The Laws of the Sun God Shamash", "282 Carved Judgments and the Principle of Proportional Justice",
    "King Hammurabi receives the rod and ring of justice directly from Shamash the Sun God, carving nearly three hundred legal statutes onto a seven-foot diorite stele to protect the weak from the strong.",
    "### Act I: The Mandate of Shamash\nHammurabi stands before the radiant throne of Shamash, receiving the divine mandate to banish injustice from the land.\n\n### Act II: The 282 Laws\nCarved in clear cuneiform, the laws established standardized prices, merchant contracts, marriage protections, and the principle of lex talionis (an eye for an eye).\n\n### Act III: The Stele in the Public Square\nThe black pillar was erected in the temple courtyard so any wronged citizen could read their rights.",
    [{"name": "Hammurabi", "role": "King of Justice", "desc": "United Mesopotamia under a written legal code."}, {"name": "Shamash", "role": "Sun God of Truth", "desc": "Dispenser of divine law and light."}],
    ["Written Law vs Arbitrary Power", "Proportional Justice"],
    "Prefigures the Mosaic Law of Exodus and the Roman Twelve Tables.",
    "“That the strong might not oppress the weak, that the orphan and widow receive justice.”",
    "The 7-foot black basalt stele was discovered at Susa in 1901 and now sits in the Louvre."
))

# --- 3. ANCIENT EGYPT ---
stories.append(make_story(
    "osiris-isis-horus", -2000, "c. 2000 – 1200 BCE", "bronze", "egypt", "Ancient Egypt",
    "Abydos, Delta Marshes & Heliopolis", "Ancient Egyptian Priestly Tradition",
    "The Myth of Osiris, Isis, and Horus: Death and Resurrection", "The Dismembered King, Isis's Magic, and the Falcon's Triumph",
    "King Osiris is murdered and cut into fourteen pieces by his jealous brother Set. Queen Isis reassembles his flesh, resurrects him through magic, and bears Horus, who defeats Set to restore Ma'at.",
    "### Act I: The Cedar Chest\nSet tricks Osiris into a golden chest and throws it into the Nile.\n\n### Act II: The Scattered Pieces\nSet cuts Osiris into 14 pieces across Egypt. Isis recovers thirteen, performs the first mummification, and conceives Horus.\n\n### Act III: The 80-Year Contendings\nHorus battles Set across land and sea, losing his eye (the Wedjat) before the divine council declares him the rightful Pharaoh.",
    [{"name": "Osiris", "role": "Lord of Resurrection", "desc": "First mummy and eternal judge of souls."}, {"name": "Isis", "role": "Goddess of Magic", "desc": "Reassembled Osiris with love and spells."}, {"name": "Horus", "role": "Falcon King", "desc": "Avenged his father and united Egypt."}],
    ["Resurrection", "Ma'at (Cosmic Order)", "Divine Kingship"],
    "Parallels the death of Baldr in Norse and the Christian resurrection.",
    "“Arise, Osiris! Isis has found your limbs; awake and rule the Western Lands forever!”",
    "Core theological foundation for Egyptian mummification and pyramid construction."
))

stories.append(make_story(
    "tale-of-sinuhe", -1900, "c. 1900 BCE", "bronze", "egypt", "Ancient Egypt",
    "Thebes & Canaan", "Middle Kingdom Court Scribe",
    "The Story of Sinuhe: The Exile and the Longing for the Nile", "Court Intrigue, Desert Warfare, and the Pharaoh's Golden Pardon",
    "When Pharaoh Amenemhat I is assassinated, courtier Sinuhe flees in panic into Canaan. Becoming a great chieftain, he is gripped by an ache for the Nile and returns home in royal honor.",
    "### Act I: Flight into the Sands\nOverhearing conspiracy in the royal camp, Sinuhe flees across the desert, rescued by Bedouin chiefs.\n\n### Act II: The Hero of Retjenu\nSinuhe becomes a prince in Syria, slaying a giant champion in single combat.\n\n### Act III: The Pharaoh's Letter\nFacing old age, he receives a golden pardon from Senusret I, returning to Egypt to receive an eternal tomb.",
    [{"name": "Sinuhe", "role": "Exiled Courtier", "desc": "Longed for burial in the Nile soil."}, {"name": "Senusret I", "role": "Pharaoh of Egypt", "desc": "Pardoned Sinuhe in royal mercy."}],
    ["Exile and Return", "Soul's True Home", "Mercy"],
    "Prefigures the Prodigal Son parable and David vs Goliath.",
    "“What is greater than that my corpse should rest in the earth where I was born?”",
    "Widely considered the supreme classic of Middle Kingdom Egyptian prose."
))

stories.append(make_story(
    "shipwrecked-sailor", -1950, "c. 1950 BCE", "bronze", "egypt", "Ancient Egypt",
    "Red Sea & Island of the Ka (Punt)", "12th Dynasty Royal Scribe",
    "The Tale of the Shipwrecked Sailor and the Golden Serpent", "The Monster of the Abyss, the Lost Island, and the Wisdom of Home",
    "A sailor shipwrecks on a phantom island in the Red Sea, meeting a giant golden serpent with beard of lapis lazuli who consoles him with prophecy before the island sinks beneath the waves.",
    "### Act I: The Storm in the Red Sea\nA ship with 120 brave sailors is smashed by forty-cubit waves; only one sailor washes ashore on a magical island.\n\n### Act II: The Golden Serpent\nThe earth trembles as a thirty-cubit serpent with scales of gold and lapis lazuli corners him, asking gently what brought him to the Island of the Ka.\n\n### Act III: The Prophecy\nThe serpent tells his own tragedy of losing his kin to a falling star, predicting an Egyptian ship will rescue the sailor in four months and advising him to hold his children in his arms.",
    [{"name": "The Shipwrecked Sailor", "role": "Survivor", "desc": "Sole survivor of an imperial trading vessel."}, {"name": "The Golden Serpent", "role": "Lord of Punt", "desc": "Benevolent dragon of wisdom."}],
    ["Resilience", "Comfort in Shared Grief", "Value of Family"],
    "Direct ancestor to Sinbad the Sailor and Odysseus on Calypso's island.",
    "“How joyful it is when someone relates what they have tasted when the crisis has passed!”",
    "Preserved on a single Middle Kingdom papyrus scroll now in the Hermitage Museum."
))

stories.append(make_story(
    "akhenaten-aten", -1350, "c. 1350 BCE", "bronze", "egypt", "Ancient Egypt",
    "Amarna (Akhetaten), Egypt", "Pharaoh Akhenaten",
    "The Great Hymn to the Aten: The Sun Disk and the First Monotheism", "The Radiance That Breathes Life into Chicks in the Egg",
    "Pharaoh Akhenaten breaks with thousands of years of polytheism, moving Egypt's capital to Amarna to worship the solar disk Aten as the sole creator and sustainer of all living creatures on Earth.",
    "### Act I: The Sun at Dawn\nAkhenaten proclaims the Aten as the sole source of life: when the sun rises, darkness flees and all of Egypt awakens to sing.\n\n### Act II: The Universal Creator\nHe praises the Aten for creating the chick inside the egg, nursing birds in the marshes, and giving different languages and skins to all human races across Syria, Nubia, and Egypt.\n\n### Act III: The Night of Oblivion\nWhen the sun sets, the world enters a death-like sleep until the radiant disk returns.",
    [{"name": "Akhenaten", "role": "Pharaoh & Reformer", "desc": "Championed solar monotheism."}, {"name": "Aten", "role": "The Living Solar Disk", "desc": "Universal radiant creator of all races."}],
    ["Solar Radiance", "Universal Creator", "First Monotheism"],
    "Shares striking word-for-word literary parallels with Psalm 104 in the Bible.",
    "“How manifold are your works, O Sole God, beside whom there is no other!” — Great Hymn",
    "Carved into the tomb of the royal courtier Ay at Amarna around 1350 BCE."
))

# --- 4. LEVANT & BIBLICAL TRADITIONS ---
stories.append(make_story(
    "genesis-creation", -2900, "c. 2900 – 1000 BCE", "bronze", "levant", "Levant & Biblical Traditions",
    "Eden & Canaan", "Biblical Scripture (Torah / Genesis)",
    "Genesis: The Garden of Eden, the Fall, and Noah's Deluge", "The Tree of Knowledge, the Ark of Gopher Wood, and the Rainbow",
    "Adam and Eve eat from the forbidden tree of knowledge, entering mortality. Generations later, Noah builds a three-deck ark of gopher wood to preserve all animal kinds through a worldwide deluge.",
    "### Act I: Eden and the Fall\nGod breathes life into Adam and creates Eve. Tempted by the serpent, they eat the forbidden fruit, gaining moral awareness and exile.\n\n### Act II: The Great Flood\nGrieved by human violence, God commands righteous Noah to construct an ark with pairs of every beast.\n\n### Act III: The Dove and the Rainbow\nAfter 150 days of flood, a dove returns with an olive leaf. God sets the rainbow across the clouds as an eternal covenant of mercy.",
    [{"name": "Noah", "role": "Righteous Builder", "desc": "Preserved life through faith."}, {"name": "Adam & Eve", "role": "First Humans", "desc": "Entered moral consciousness."}],
    ["Covenant of Mercy", "Moral Choice", "Cosmic Cleansing"],
    "Matches Mesopotamian Utnapishtim and Greek Deucalion flood tales.",
    "“I have set my rainbow in the clouds, and it will be the sign of the covenant.” — Genesis 9:13",
    "Foundational narrative for Judaism, Christianity, and Islam."
))

stories.append(make_story(
    "moses-exodus", -1300, "c. 1300 BCE", "bronze", "levant", "Levant & Biblical Traditions",
    "Nile Delta, Red Sea & Mount Sinai", "Biblical Tradition (Book of Exodus)",
    "Moses and the Exodus: The Ten Plagues and the Parting of the Sea", "The Burning Bush, the Staff of God, and the Ten Commandments",
    "Moses, raised in Pharaoh's palace, is called by God from a burning bush to liberate the enslaved Israelites, parting the Red Sea and receiving the Ten Commandments on Mount Sinai.",
    "### Act I: The Burning Bush\nFleeing Egypt, Moses encounters the burning bush in Midian and receives the divine mandate: 'Let my people go!'\n\n### Act II: The Ten Plagues\nWhen Pharaoh hardens his heart, ten plagues strike Egypt—turning the Nile to blood, swarming locusts, and the Passover night.\n\n### Act III: The Parting of the Red Sea\nTrapped between Pharaoh's chariots and the sea, Moses raises his staff; the waters divide, allowing the people to pass on dry ground.\n\n### Act IV: The Tablet on Mount Sinai\nAmidst thunder and smoke on Sinai, Moses receives the Decalogue of divine moral law.",
    [{"name": "Moses", "role": "Lawgiver & Prophet", "desc": "Led the Israelites out of Egyptian bondage."}, {"name": "Pharaoh (Ramesses)", "role": "Imperial Monarch", "desc": "Hardened his heart against liberation."}],
    ["Liberation from Slavery", "Moral Law", "Faith against Empires"],
    "Archetype of liberation struggle inspiring civil rights movements across history.",
    "“The Lord is my strength and my song; he has become my salvation.” — Exodus 15:2",
    "Forms the liturgical core of the Jewish festival of Passover (Pesach)."
))

stories.append(make_story(
    "david-goliath", -1000, "c. 1000 BCE", "classical", "levant", "Levant & Biblical Traditions",
    "Valley of Elah, Judea", "Biblical Tradition (Books of Samuel)",
    "David and Goliath: The Shepherd Boy and the Philistine Giant", "Five Smooth Stones, the Bronze Armor, and the Sling of Faith",
    "The young shepherd boy David visits the battle lines of Israel and volunteers to face the terrifying nine-foot Philistine champion Goliath, striking him in the forehead with a single sling stone.",
    "### Act I: The Giant's Challenge\nFor forty days, Goliath of Gath mocked the army of King Saul, demanding single combat.\n\n### Act II: The Shepherd in Rags\nDavid refused heavy bronze armor, carrying only his shepherd's staff, sling, and five smooth stones from the brook.\n\n### Act III: The Strike at the Brow\nGoliath laughed in contempt. David whirled his sling; the stone sank into Goliath's forehead, felling the titan to the dust.",
    [{"name": "David", "role": "Shepherd & Future King", "desc": "Relied on agility and faith rather than iron armor."}, {"name": "Goliath", "role": "Philistine Champion", "desc": "Nine-foot giant clad in bronze scales."}],
    ["Underdog Triumph", "Faith over Physical Might", "Courage"],
    "Parallels Sinuhe vs the Hero of Retjenu and Irish Cú Chulainn.",
    "“You come against me with sword and spear, but I come against you in the name of the Lord.”",
    "Excavations in the Valley of Elah have revealed 10th-century BCE fortified Judean settlements."
))

stories.append(make_story(
    "scheherazade-1001", 850, "c. 850 – 1400 CE", "medieval", "persia_arabia", "Persia & Arabia",
    "Baghdad, Cairo & Samarkand", "Traditional Storytellers (Recorded by al-Jahshiyari)",
    "One Thousand and One Nights: Scheherazade's 1,001 Tales", "The Magic Lamp, Sinbad's Voyages, and the Power of Story to Heal",
    "To halt King Shahryar's murderous cycle of executing new brides at dawn, the brilliant Scheherazade marries him, weaving nested tales of genies, sorcery, and voyages, pausing at cliffhangers to heal the king's heart.",
    "### Act I: The Wounded King\nBetrayed by his first queen, Shahryar executes a bride every dawn until Scheherazade volunteers to marry him.\n\n### Act II: The 1,001 Cliffhangers\nEach night she weaves tales of Aladdin, Sinbad, and Ali Baba, stopping at dawn mid-sentence.\n\n### Act III: The Redemption of Shahryar\nAfter 1,001 nights, the king confesses that her stories have purified his heart of hatred, granting her life and peace to the kingdom.",
    [{"name": "Scheherazade", "role": "Master Storyteller", "desc": "Saved thousands of lives through psychological insight and narrative."}, {"name": "King Shahryar", "role": "Wounded Monarch", "desc": "Healed through 1,001 nights of literature."}],
    ["Art as Salvation", "Healing Trauma", "Framed Storytelling"],
    "Inspired Chaucer's Canterbury Tales and Boccaccio's Decameron.",
    "“Stories are the medicine of the afflicted heart.” — Scheherazade",
    "Synthesizes Indian, Persian, and Arabic storytelling traditions along the Silk Road."
))

# --- 5. INDIA & SOUTH ASIA ---
stories.append(make_story(
    "ramayana-valmiki", -1200, "c. 1200 – 500 BCE", "classical", "india", "India & South Asia",
    "Ayodhya, Dandaka & Lanka", "Adi Kavi Sage Valmiki",
    "The Ramayana: The Epic Journey of Rama and Sita", "Dharma, Hanuman's Leap, the Ocean Bridge, and the Defeat of Ravana",
    "Prince Rama accepts a 14-year forest exile to honor his father's vow. When the demon king Ravana abducts Sita to Lanka, Rama allies with Hanuman, building a floating stone bridge to wage a war of righteousness.",
    "### Act I: The Forest Exile\nRama serenely accepts banishment to the Dandaka Forest; Sita and Lakshmana join him.\n\n### Act II: The Golden Deer and Abduction\nRavana lures Rama away with a golden deer and kidnaps Sita to Lanka.\n\n### Act III: Hanuman and the Floating Bridge\nHanuman leaps across the ocean, finds Sita, and burns Lanka. The Vanaras build Ram Setu to cross the sea.\n\n### Act IV: The Fall of Ravana\nRama destroys Ravana with the Brahmastra arrow, returning to Ayodhya celebrated during Diwali.",
    [{"name": "Rama", "role": "Avatar of Vishnu", "desc": "Ideal of righteous conduct (Dharma)."}, {"name": "Sita", "role": "Princess of Mithila", "desc": "Embodiment of devotion and courage."}, {"name": "Hanuman", "role": "Vanara Hero", "desc": "Son of the wind god endowed with supreme loyalty."}],
    ["Dharma (Righteous Duty)", "Triumph of Light over Darkness", "Devotion"],
    "Sita's abduction matches Helen of Troy in the Iliad.",
    "“Mother and motherland are more sacred than heaven itself.” — Valmiki",
    "The Adi Kavya (First Poem) of Indian classical literature."
))

stories.append(make_story(
    "mahabharata-vyasa", -900, "c. 900 – 400 BCE", "classical", "india", "India & South Asia",
    "Hastinapura & Kurukshetra", "Sage Krishna Dwaipayana Vyasa",
    "The Mahabharata & Bhagavad Gita: The Great Cosmic War", "The Pandavas vs Kauravas, the Dice Game, and Krishna's Teachings",
    "The conflict between the five Pandavas and hundred Kauravas culminates at Kurukshetra. Facing his own family in battle, Arjuna receives the immortal Bhagavad Gita from Lord Krishna.",
    "### Act I: The Dice Game\nShakuni strips Yudhishthira of kingdom and Draupadi. Krishna saves Draupadi with infinite cloth.\n\n### Act II: The Song of God (Gita)\nAt Kurukshetra, Krishna reveals the immortality of the soul and Karma Yoga to the despondent Arjuna.\n\n### Act III: The 18-Day Battle\nBhishma, Drona, and Karna fall in titanic combat; the Pandavas win at tragic cost.",
    [{"name": "Arjuna", "role": "Supreme Archer", "desc": "Recipient of the Bhagavad Gita."}, {"name": "Lord Krishna", "role": "Charioteer & Avatar", "desc": "Cosmic guide and diplomat."}, {"name": "Draupadi", "role": "Fiery Queen", "desc": "Born of sacrificial flame."}],
    ["Karma Yoga (Selfless Duty)", "Immortality of the Soul", "Moral Conflict"],
    "Parallels Norse Ragnarök and Arthurian Battle of Camlann.",
    "“You have a right only to work, never to the fruits of action.” — Bhagavad Gita 2.47",
    "At 100,000 verses, it is the longest epic poem in world literature."
))

stories.append(make_story(
    "panchatantra-fables", -300, "c. 300 BCE", "classical", "india", "India & South Asia",
    "Mahilaropya, Ancient India", "Sage Vishnu Sharma",
    "The Panchatantra: Animal Fables of Political Wisdom and Wit", "The Monkey and the Crocodile, the Lion and the Hare",
    "Sage Vishnu Sharma educates three foolish princes in statecraft (Niti) using animal fables showing that intellect, foresight, and wit always defeat brute strength.",
    "### Act I: The Princes' Education\nVishnu Sharma promised to teach the royal heirs statecraft in six months using interconnected fables.\n\n### Act II: The Monkey and the Crocodile\nA crocodile befriends a monkey who throws him sweet rose-apples. When the crocodile's wife demands the monkey's heart, the monkey tricks him by claiming he left his heart in a tree branch.\n\n### Act III: The Lion and the Clever Hare\nA tiny hare leads the arrogant lion Damanaka to a deep well, showing him his own reflection; the enraged lion leaps in to fight his shadow and drowns.",
    [{"name": "Vishnu Sharma", "role": "Sage Educator", "desc": "Pioneered educational animal allegories."}, {"name": "Clever Monkey & Hare", "role": "Trickster Heroes", "desc": "Defeated predators through psychological wit."}],
    ["Intellect over Brute Force", "Prudence in Friendship", "Political Realism"],
    "Direct ancestor to Aesop, Arabian Nights, and Kalila wa Dimna in the Islamic world.",
    "“Intelligence is supreme power; for a tiny hare drowned the roaring lion in a well.”",
    "Translated into Pahlavi, Arabic, Latin, and over 50 world languages by 1600."
))

stories.append(make_story(
    "kalidasa-shakuntala", 400, "c. 400 CE", "classical", "india", "India & South Asia",
    "Kanva's Hermitage & Hastinapura", "Mahakavi Kalidasa",
    "Abhijnanashakuntala: The Recognition of Shakuntala", "The Forest Hermitage, the Sage's Curse, the Lost Signet Ring, and Emperor Bharata",
    "King Dushyanta marries forest maiden Shakuntala. An angry sage's curse causes the king to forget her completely until a fisherman recovers a lost signet ring from the belly of a carp.",
    "### Act I: Love in the Sacred Grove\nDushyanta meets Shakuntala in sage Kanva's forest hermitage, exchanging signet rings.\n\n### Act II: Durvasa's Curse\nPreoccupied with love, Shakuntala ignores Sage Durvasa, who curses Dushyanta to forget her until he sees his ring.\n\n### Act III: The Lost Ring and Rejection\nThe ring slips into a river; Dushyanta coldly rejects a pregnant Shakuntala in court.\n\n### Act IV: The Fisherman and Lion Prince\nA fisherman finds the ring inside a fish. Dushyanta's memory returns in agonizing grief, culminating in finding Shakuntala and their lion-taming son Bharata.",
    [{"name": "Shakuntala", "role": "Forest Maiden", "desc": "Daughter of nymph Menaka who bore the founder of India."}, {"name": "Dushyanta", "role": "Monarch of Hastinapura", "desc": "Overcame the curse of oblivion."}],
    ["Romantic Separation (Vipralambha)", "Fate vs Memory", "Nature vs Court"],
    "Ring in fish matches Polycrates' ring in Herodotus.",
    "“I name thee Shakuntala, and all at once is said!” — Goethe on reading Kalidasa",
    "Pinnacle of Gupta Sanskrit drama; celebrated by European Romantic poets."
))

# --- 6. CHINA & EAST ASIA ---
stories.append(make_story(
    "pangu-nuwa", -5000, "c. 5000 – 2700 BCE", "prehistory", "china", "China & East Asia",
    "Yellow River & Mount Buzhou", "Traditional Lore (Recorded by Xu Zheng)",
    "Pangu and Nüwa: The Cosmic Egg and the Pillars of Heaven", "Separation of Yin-Yang, Clay Humanity, and Molten Sky Stones",
    "Pangu cleaves Yin and Yang apart with an axe, transforming his dying body into mountains and rivers. Later, serpent-goddess Nüwa molds humans from yellow mud and repairs the broken sky.",
    "### Act I: The Cosmic Egg\nPangu sleeps inside an egg of chaos, striking it to separate clear Heaven from murky Earth.\n\n### Act II: The Great Sacrifice\nHis breath became the wind, left eye the Sun, right eye the Moon, and blood the Yangtze and Yellow rivers.\n\n### Act III: Nüwa's Clay Children\nNüwa molded figures from yellow silt along the Yellow River.\n\n### Act IV: The Broken Sky\nWhen Gonggong smashed Mount Buzhou, Nüwa melted five-colored stones to patch the heavens.",
    [{"name": "Pangu", "role": "Creator Giant", "desc": "Separated Heaven and Earth."}, {"name": "Nüwa", "role": "Mother Goddess", "desc": "Molded humanity and repaired the sky."}],
    ["Yin-Yang Harmony", "Self-Sacrifice", "Restoration"],
    "Pangu's body mirrors Norse Ymir and Vedic Purusha; Nüwa mirrors Prometheus.",
    "“Pangu stood between heaven and earth, and from his breath the world was born.”",
    "Core cosmogony depicted in Han dynasty tomb murals."
))

stories.append(make_story(
    "houyi-change", -2100, "c. 2100 BCE", "bronze", "china", "China & East Asia",
    "Kunlun Mountains & Moon Palace", "Traditional Myth (Huainanzi)",
    "Houyi the Archer and Chang'e Flies to the Moon", "Shooting Down Nine Suns, the Elixir of Immortality, and the Jade Rabbit",
    "When ten suns scorch the earth, master archer Houyi shoots down nine with his vermilion bow. Given the elixir of immortality, his wife Chang'e drinks it to protect it from a thief, floating to the Moon.",
    "### Act I: The Ten Scorching Suns\nTen sun-crows flew into the sky at once, boiling rivers and wilting crops.\n\n### Act II: The Nine Divine Arrows\nHouyi climbed Mount Kunlun, shooting down nine suns to save humanity.\n\n### Act III: The Flight to the Moon\nQueen Mother of the West gave Houyi the Elixir of Immortality. To prevent a thief from seizing it, his wife Chang'e drank it, floating up to the Moon with the Jade Rabbit.",
    [{"name": "Houyi", "role": "Divine Archer", "desc": "Saved earth from nine suns."}, {"name": "Chang'e", "role": "Moon Goddess", "desc": "Dwells in the lunar palace of cold cassia trees."}],
    ["Selfless Heroism", "Longing across Starlit Distances"],
    "Parallels Polynesian Maui snaring the sun and Greek Apollo's chariot.",
    "“Gazing at the bright moon from afar, lovers share their hearts across ten thousand leagues.”",
    "Celebrated annually worldwide during the Mid-Autumn Festival (Mooncake Festival)."
))

stories.append(make_story(
    "journey-west-wuchengen", 1592, "c. 1592 CE", "renaissance", "china", "China & East Asia",
    "Chang'an to Vulture Peak, India", "Wu Cheng'en",
    "Journey to the West: Sun Wukong and the Pilgrimage for Sacred Sutras", "Havoc in Heaven, the 81 Perils, Pigsy, Sandy, and the Victorious Buddha",
    "Monk Xuanzang journeys to India to retrieve Buddhist scriptures, escorted by Sun Wukong (Monkey King), Pigsy, and Sandy through eighty-one supernatural perils along the Silk Road.",
    "### Act I: Havoc in Heaven\nStone monkey Sun Wukong masters 72 transformations, claims the size-shifting iron staff, and battles heaven until Buddha traps him beneath Five Fingers Mountain.\n\n### Act II: The Pilgrims of the Silk Road\nFreed by monk Xuanzang, Monkey joins Pigsy and Sandy to battle the White Bone Demon and Spider Fiends.\n\n### Act III: Enlightenment\nReaching India, Monkey is crowned the Victorious Fighting Buddha as his golden headband dissolves.",
    [{"name": "Sun Wukong (Monkey King)", "role": "Trickster Hero", "desc": "Indestructible master of 72 transformations."}, {"name": "Xuanzang (Tripitaka)", "role": "Holy Monk", "desc": "Spiritual pilgrim seeking wisdom."}, {"name": "Zhu Bajie (Pigsy)", "role": "Glutton Disciple", "desc": "Former heavenly marshal."}],
    ["Mind Monkey (Intellect vs Discipline)", "Spiritual Cultivation", "Brotherhood"],
    "Parallels Tolkien's Fellowship of the Ring and the Ramayana.",
    "“A journey of ten thousand leagues begins with a single sincere step.” — Wu Cheng'en",
    "Based on the historical 7th-century overland pilgrimage of Xuanzang to Nalanda University."
))

stories.append(make_story(
    "three-kingdoms-luo", 1350, "c. 1350 CE", "medieval", "china", "China & East Asia",
    "Peach Garden, Red Cliffs & Luoyang", "Luo Guanzhong",
    "Romance of the Three Kingdoms: The Oath in the Peach Garden", "Liu Bei, Guan Yu, Zhang Fei, Zhuge Liang's Borrowed Arrows, and Red Cliffs",
    "The epic saga of the collapse of the Han dynasty. Liu Bei, Guan Yu, and Zhang Fei swear eternal brotherhood in a blooming peach garden to restore the realm, aided by master strategist Zhuge Liang.",
    "### Act I: The Peach Garden Oath\nThree heroes drink wine under blooming peach blossoms, swearing to die on the same day in service of the empire.\n\n### Act II: The Sleeping Dragon\nLiu Bei visits the thatched cottage of master strategist Zhuge Liang three times in winter snow to enlist his genius.\n\n### Act III: The Battle of Red Cliffs\nZhuge Liang borrows 100,000 arrows using straw boats in morning mist, summoning southeast winds to burn Cao Cao's chained fleet on the Yangtze River.",
    [{"name": "Liu Bei", "role": "Benevolent Prince", "desc": "Leader of Shu Han."}, {"name": "Guan Yu", "role": "God of War & Loyalty", "desc": "Wielder of the Green Dragon Crescent Blade."}, {"name": "Zhuge Liang", "role": "Master Strategist", "desc": "The Sleeping Dragon whose intellect reshaped kingdoms."}],
    ["Brotherhood and Loyalty (Yi)", "Military Strategy", "Cyclical Dynastic Rise and Fall"],
    "Shares epic scope with the Iliad and Arthurian romances.",
    "“The empire, long divided, must unite; long united, must divide.” — Opening Line",
    "One of the Four Great Classical Novels of Chinese literature."
))

# --- 7. GREECE & ROME ---
stories.append(make_story(
    "iliad-odyssey-homer", -750, "c. 750 – 700 BCE", "classical", "greece_rome", "Greece & Rome",
    "Troy & Ithaca", "Homer (Blind Bard of Ionia)",
    "The Iliad & The Odyssey: The Fall of Troy and the Wanderer's Return", "Achilles' Rage, the Wooden Horse, Cyclops, Circe, and Penelope's Shroud",
    "The dual founding epics of Western literature. The Iliad captures Achilles' wrath at the siege of Troy; the Odyssey follows Odysseus through ten years of monsters and sea perils to reclaim Ithaca.",
    "### Act I: The Wrath of Achilles\nOffended by Agamemnon, Achilles withdraws until Hector kills Patroclus. Re-entering in divine armor, Achilles slays Hector.\n\n### Act II: The Trojan Horse & Sea Perils\nTroy falls by the wooden horse. Blinding the Cyclops Polyphemus, Odysseus wanders for ten years across supernatural seas.\n\n### Act III: The Beggar's Bow\nDisguised in rags, Odysseus strings his legendary bow, slays the arrogant suitors, and reclaims Penelope.",
    [{"name": "Achilles", "role": "Greek Champion", "desc": "Torn between peaceful life and immortal glory."}, {"name": "Odysseus", "role": "King of Ithaca", "desc": "Master strategist of twists and turns."}, {"name": "Penelope", "role": "Queen of Ithaca", "desc": "Fidelity and resilience."}],
    ["Glory (Kleos) vs Homecoming (Nostos)", "Tragedy of War", "Intellect over Force"],
    "Achilles and Patroclus match Gilgamesh and Enkidu.",
    "“Sing in me, Muse, and tell the story of that man of twists and turns...” — Homer",
    "Excavations at Hisarlik proved Troy was a historical Bronze Age citadel destroyed c. 1180 BCE."
))

stories.append(make_story(
    "hesiod-theogony", -700, "c. 700 BCE", "classical", "greece_rome", "Greece & Rome",
    "Mount Helicon & Olympus", "Hesiod (Shepherd-Poet)",
    "Theogony & Works and Days: The Titanomachy and Pandora's Box", "Cronus's Sickle, Prometheus's Fire, and the Sole Remaining Hope",
    "Hesiod's genealogical origins of the Greek cosmos: Cronus swallows his children, Zeus leads the Titanomachy war, Prometheus steals fire for mortals, and Pandora's jar unleashes worldly sorrows—leaving only Hope inside.",
    "### Act I: Chaos to Titans\nGaia and Uranus birth the Titans. Cronus overthrows his father with a flint sickle.\n\n### Act II: The Titanomachy\nZeus escapes being swallowed, frees his siblings, and hurls the Titans into Tartarus with thunderbolts.\n\n### Act III: Prometheus and Pandora\nPrometheus steals fire in a fennel stalk. Zeus punishes humanity with Pandora, whose jar releases plagues, leaving Hope trapped inside.",
    [{"name": "Zeus", "role": "King of the Olympians", "desc": "Wielder of the lightning bolt."}, {"name": "Prometheus", "role": "Titan Friend of Man", "desc": "Suffered eternal torment for gifting fire."}, {"name": "Pandora", "role": "First Woman", "desc": "Curiosity released troubles and preserved Hope."}],
    ["Cosmic Order", "Origin of Suffering", "Hope as Anchor"],
    "Pandora parallels Eve in Genesis; Prometheus parallels Lucifer/Loki.",
    "“Only Hope remained within under the rim of the great jar.” — Hesiod",
    "Established ancient Greece's foundational religious and theological system."
))

stories.append(make_story(
    "virgil-aeneid", -19, "29 – 19 BCE", "classical", "greece_rome", "Greece & Rome",
    "Troy, Carthage & Tiber Valley", "Publius Vergilius Maro (Virgil)",
    "The Aeneid: The Founding of the Roman Destiny", "Carrying Father from Burning Troy, Dido's Curse, and the Golden Bough",
    "Trojan prince Aeneas escapes burning Troy carrying his father Anchises. After a tragic love affair with Queen Dido of Carthage and descending to the Underworld, he reaches Italy to establish the lineage of Rome.",
    "### Act I: Escape from Troy\nAeneas flees burning Troy carrying his crippled father and leading his young son.\n\n### Act II: The Curse of Dido\nIn Carthage, Dido falls passionately in love. When Jupiter commands Aeneas to depart for Italy, Dido stabs herself on a pyre, cursing Rome with eternal enmity.\n\n### Act III: The Underworld and Rome's Future\nGuided by the Sibyl with the Golden Bough, Aeneas visits the underworld, where Anchises reveals the future heroes: Romulus, Caesar, and Augustus.",
    [{"name": "Aeneas", "role": "Father of Rome", "desc": "Embodiment of duty to gods and nation (Pietas)."}, {"name": "Dido", "role": "Queen of Carthage", "desc": "Tragic queen whose dying curse foretold Hannibal."}],
    ["Duty (Pietas) over Passion", "Imperial Destiny", "Cost of Civilization"],
    "Blends the wanderings of the Odyssey with the warfare of the Iliad.",
    "“Roman, remember by your strength to rule Earth's peoples: to impose peace, spare the defeated, and crush the proud.”",
    "Commissioned by Augustus Caesar to provide Rome with a divine founding epic."
))

stories.append(make_story(
    "ovid-metamorphoses", 8, "c. 8 CE", "classical", "greece_rome", "Greece & Rome",
    "Rome & Mount Parnassus", "Publius Ovidius Naso (Ovid)",
    "Metamorphoses: Tales of Transformation (Daedalus & Icarus, Orpheus)", "The Wax Wings, Apollo and Daphne, and the Descent to the Underworld",
    "Ovid's 15-book epic catalog of mythological transformations: Daedalus crafting wax wings for Icarus, Apollo chasing Daphne who becomes a laurel tree, and Orpheus charming Hades with his lyre.",
    "### Act I: Daedalus and Icarus\nTrapped in the Cretan labyrinth, Daedalus fashioned wings of feathers and wax. Young Icarus flew too close to the sun; the wax melted, and he plunged into the Aegean Sea.\n\n### Act II: Apollo and Daphne\nStruck by Cupid's golden arrow, Apollo chased the nymph Daphne, who prayed to her river-god father and transformed into the sacred laurel tree.\n\n### Act III: Orpheus and Eurydice\nWhen viper venom killed his bride Eurydice, Orpheus descended to the underworld, charming Hades with his golden lyre. Granted her return under the condition he not look back, Orpheus glanced behind at the threshold, watching Eurydice vanish forever.",
    [{"name": "Orpheus", "role": "Master Musician", "desc": "Could charm trees and stones with his lyre."}, {"name": "Icarus", "role": "Youth of Tragic Hubris", "desc": "Flew too close to the sun on wax wings."}],
    ["Transformation (Mutatas Formas)", "Limits of Human Ambition", "Love and Loss"],
    "Orpheus's descent matches Izanagi in Japan and Gilgamesh crossing the deep.",
    "“My intention is to tell of bodies changed into new forms... Let my song run continuous from the world's dawn to my own times.”",
    "The single most influential sourcebook of classical myth for Renaissance painters and poets."
))

# --- 8. PERSIA & ARABIA ---
stories.append(make_story(
    "shahnameh-ferdowsi", 1000, "c. 977 – 1010 CE", "medieval", "persia_arabia", "Persia & Arabia",
    "Greater Iran, Sistan & Tus", "Hakim Abul-Qasim Ferdowsi Tusi",
    "Shahnameh: The Persian Book of Kings (Rostam and Sohrab)", "The 60,000 Verses That Saved Persian Heritage, Zahhak, and the Simurgh",
    "Ferdowsi spent thirty years composing 60,000 couplets in pure Persian to preserve Iranian history and language, highlighted by the tragedy of champion Rostam slaying his unknown warrior son Sohrab.",
    "### Act I: The Thirty-Year Monument\nFerdowsi revived the Persian language and ancient Zoroastrian lore following foreign conquests.\n\n### Act II: The Serpent King Zahhak\nZahhak sprouts shoulder snakes fed on youths' brains until Kaveh the Blacksmith raises the banner of rebellion.\n\n### Act III: The Tragedy of Rostam and Sohrab\nRostam battles a Turanian champion in single combat, mortally stabbing him. Seeing the jewel bracelet on the youth's arm, Rostam realizes he has slain his own son Sohrab.",
    [{"name": "Rostam", "role": "Champion of Iran", "desc": "Invincible hero who suffered supreme heartbreak."}, {"name": "Sohrab", "role": "Youth of Turan", "desc": "Noble son seeking his father."}, {"name": "Ferdowsi", "role": "Immortal Poet", "desc": "Preserved the soul of Iranian civilization."}],
    ["Tragedy of Blind Warfare", "Father vs Son", "Cultural Preservation"],
    "Father-son combat matches Irish Cú Chulainn and Germanic Hildebrand.",
    "“For thirty years I endured much toil, but with the Persian tongue I revived Iran.” — Ferdowsi",
    "Ferdowsi's tomb in Tus is a national sanctuary of Persian culture."
))

stories.append(make_story(
    "nizami-layla-majnun", 1188, "c. 1188 CE", "medieval", "persia_arabia", "Persia & Arabia",
    "Arabian Desert & Ganja", "Nizami Ganjavi",
    "Layla and Majnun: The Supreme Romantic Tragedy of the East", "Qays's Madness in the Dunes, the Tamed Wild Beasts, and Transcendent Love",
    "Young Qays falls into an all-consuming love with Layla. Rejected by her father, Qays flees into the desert as Majnun (the Madman), his grief-filled verses taming lions and wolves, transforming human love into divine union.",
    "### Act I: The Schoolroom Glance\nQays and Layla fall into an immediate, spiritual love that defies tribal conventions.\n\n### Act II: Majnun in the Wilderness\nForbidden from seeing Layla, Qays wanders naked in the desert writing her name on every stone. Lions and gazelles gather peacefully around him.\n\n### Act III: The Garden Meeting and Tomb\nMeeting years later in a walled garden, their love has become pure spirit, unable to touch mortal flesh. They die of grief and are united in Paradise.",
    [{"name": "Majnun (Qays)", "role": "The Possessed Poet", "desc": "Archetype of the egoless mystic lover."}, {"name": "Layla", "role": "The Beloved", "desc": "Luminous beacon of spiritual beauty."}],
    ["Transcendent Love (Ishq)", "Ego Dissolution", "Mystic Union"],
    "Directly inspired Shakespeare's Romeo and Juliet and European courtly romances.",
    "“If I am mad, it is with the wine of love! Only Layla remains in my chest.” — Nizami",
    "The jewel of Nizami's Khamsa (Five Epics), celebrated from Turkey to India."
))

stories.append(make_story(
    "attar-conference-birds", 1177, "c. 1177 CE", "medieval", "persia_arabia", "Persia & Arabia",
    "Nishapur, Greater Khorasan", "Farid ud-Din Attar",
    "The Conference of the Birds (Mantiq al-Tayr)", "The Hoopoe's Guidance, the Seven Valleys, and the Mirror of the Simurgh",
    "Thousands of birds gather to seek their mythical king, the Simurgh. Guided by the Hoopoe across seven perilous valleys (Quest, Love, Knowledge, Detachment, Unity, Wonder, Poverty), only thirty birds survive—discovering they themselves are the Simurgh (Si Murgh - Thirty Birds).",
    "### Act I: The Council of Birds\nThe Hoopoe summons the nightingale, falcon, duck, and parrot, challenging their worldly excuses to embark on the spiritual path.\n\n### Act II: The Seven Valleys\nThey cross the Valley of Love (where reason burns), the Valley of Unity, and the Valley of Annihilation (Fana).\n\n### Act III: The Mirror of the Simurgh\nThirty exhausted birds reach the mountain throne. Looking upon the king, they see a mirror reflecting their own faces: the divine was within them all along.",
    [{"name": "The Hoopoe", "role": "Spiritual Master (Murshid)", "desc": "Guided the flock across the cosmic valleys."}, {"name": "The Simurgh", "role": "Divine Truth", "desc": "The transcendent king found within the collective soul."}],
    ["Sufi Mysticism (Fana)", "The Journey Inward", "Unity of Being"],
    "Parallels Dante's Paradiso and Bunyan's Pilgrim's Progress.",
    "“When they looked, they saw that the Simurgh was none other than the thirty birds themselves!”",
    "A seminal masterpiece of Persian Sufi allegorical poetry."
))

# --- 9. JAPAN & KOREA ---
stories.append(make_story(
    "shinto-amaterasu", 712, "c. 712 CE", "medieval", "japan_korea", "Japan & Korea",
    "Takamagahara & Ama-no-Iwato", "Ō no Yasumaro & Hieda no Are (Kojiki)",
    "Kojiki: Amaterasu and the Heavenly Rock Cave", "The Jeweled Spear, Susanoo's Tempest, and the Dance That Restored the Sun",
    "When the storm god Susanoo rampages in Heaven, his sister Amaterasu, the Sun Goddess, hides inside the Heavenly Rock Cave, plunging the world into darkness until a comic dance coaxes her out with a bronze mirror.",
    "### Act I: The Jeweled Spear\nIzanagi and Izanami stir the ocean with a jeweled spear, birthing Japan.\n\n### Act II: The Cave of Darkness\nSusanoo flays a heavenly horse into Amaterasu's weaving hall. Deeply offended, Amaterasu retreats into the Rock Cave, plunging heaven into night.\n\n### Act III: Uzume's Dance\nGoddess Uzume performs an energetic, funny dance on an upturned tub, making eight million gods roar with laughter. Curious, Amaterasu peeks out and sees her radiant reflection in the bronze mirror.",
    [{"name": "Amaterasu-ōmikami", "role": "Sun Goddess", "desc": "Ruler of Heaven and imperial ancestor."}, {"name": "Susanoo", "role": "Storm God", "desc": "Wild brother who slew the 8-headed dragon."}, {"name": "Ame-no-Uzume", "role": "Goddess of Mirth", "desc": "Brought the sun back with laughter."}],
    ["Shinto Purification (Misogi)", "Laughter over Despair", "The Three Sacred Regalia"],
    "Amaterasu's withdrawal mirrors Greek Demeter mourning Persephone.",
    "“When Amaterasu stepped forth from the cave, heaven and earth were flooded with golden light.”",
    "The sacred foundational mythology of Japan's Shinto religion and imperial line."
))

stories.append(make_story(
    "genji-murasaki", 1008, "c. 1000 – 1012 CE", "medieval", "japan_korea", "Japan & Korea",
    "Heian-kyō (Kyoto), Japan", "Murasaki Shikibu (Noblewoman)",
    "The Tale of Genji (Genji Monogatari)", "The World's First Novel: The Shining Prince, Court Poetry, and Mono no Aware",
    "The world's first psychological novel. Written by noblewoman Murasaki Shikibu at the imperial court in Kyoto, this 54-chapter masterpiece captures the beauty, court intrigues, and Buddhist pathos of impermanence centered on Prince Hikaru Genji.",
    "### Act I: The Shining Prince\nGenji, son of the Emperor, grows into the pinnacle of court elegance, poetry, and calligraphy, haunted by longing for his deceased mother.\n\n### Act II: Exile to Suma\nFollowing scandals, Genji exiles himself to the windswept shore of Suma, composing poetry on the fleeting nature of life.\n\n### Act III: Vanished into Clouds\nIn later life, karmic sadness catches up with him as Lady Murasaki passes away. In a chapter left entirely blank, Genji withdraws from the world.",
    [{"name": "Hikaru Genji", "role": "The Shining Prince", "desc": "Aristocrat whose life explores aesthetic heights and human longing."}, {"name": "Murasaki Shikibu", "role": "Author", "desc": "Founded Japanese narrative realism."}],
    ["Mono no Aware (Pathos of Things)", "Psychological Realism", "Buddhist Impermanence"],
    "Preceded European novels by Cervantes and Richardson by six centuries.",
    "“Can any sorrow be heavier than the parting of those who love?” — Murasaki Shikibu",
    "Written in phonetic Kana script during the cultural peak of the Heian court."
))

stories.append(make_story(
    "dangun-korea", -2333, "c. 2333 BCE (Founding Myth)", "bronze", "japan_korea", "Japan & Korea",
    "Mount Taebaek & Pyongyang", "Recorded in Samguk Yusa by Monk Iryeon",
    "Dangun Wanggeom: The Bear-Woman and the Founding of Gojoseon", "100 Days of Mugwort and Garlic in the Dark Cave",
    "A bear and a tiger ask the heavenly prince Hwanung to make them human. Enduring 100 days eating only sacred mugwort and garlic in a dark cave, only the bear perseveres, becoming the woman Ungnyeo, who gives birth to Dangun, founder of Korea.",
    "### Act I: The Heavenly Prince\nHwanung descended from heaven with three thousand followers to teach agriculture, law, and medicine.\n\n### Act II: The Cave of Garlic\nA bear and tiger prayed to become human. Hwanung gave them 20 cloves of garlic and mugwort, commanding them to stay out of the sunlight for 100 days. The tiger grew impatient and fled; the bear persevered and transformed into a beautiful woman, Ungnyeo.\n\n### Act III: The Birth of Dangun\nUngnyeo married Hwanung, giving birth to Dangun Wanggeom, who founded Gojoseon under the philosophy of Hongik Ingan (Devotion to Human Welfare).",
    [{"name": "Dangun Wanggeom", "role": "Founding King of Korea", "desc": "United heaven and earth to establish Gojoseon."}, {"name": "Ungnyeo (Bear-Woman)", "role": "Mother of Korea", "desc": "Persevered through darkness to achieve humanity."}],
    ["Hongik Ingan (Benefit All Humanity)", "Patience and Endurance", "Harmony of Nature"],
    "Parallels totemic animal-human transformation myths across Siberia and the Americas.",
    "“Govern with devotion to the welfare of all humanity.” — Hongik Ingan Principle",
    "National Foundation Day (Gaecheonjeol) is celebrated every October 3 in Korea."
))

# --- 10. THE AMERICAS ---
stories.append(make_story(
    "popol-vuh-maya", -400, "c. 400 BCE – 1550 CE", "classical", "americas", "The Americas",
    "Xibalba & Guatemala Highlands", "K'iche' Maya Scribes",
    "Popol Vuh: The Hero Twins and the Lords of Death", "The Dark Houses of Xibalba, the Decapitation of One Hunahpu, and the Sun & Moon",
    "When the cruel Lords of Xibalba murder their father, the Hero Twins Hunahpu and Xbalanque descend into the underworld, outwitting razor rooms, bat houses, and ballgames to conquer death and rise as the Sun and Moon.",
    "### Act I: The Failed Creations\nThe gods try making animals, mud people, and wooden mannequins, destroying them when they lack souls.\n\n### Act II: The Underworld Trials\nThe Hero Twins descend to Xibalba, surviving the Dark House, Razor House, Cold House, and Bat House.\n\n### Act III: The Final Trick\nResurrecting as magical dancers, they trick the death lords into asking to be sacrificed and leave them dead, rising into the heavens as the Sun and Moon.",
    [{"name": "Hunahpu & Xbalanque", "role": "Hero Twins", "desc": "Demigod tricksters who conquered the underworld."}, {"name": "One Death & Seven Death", "role": "Lords of Xibalba", "desc": "Underworld rulers of decay."}],
    ["Triumph of Intellect over Death", "Rebirth through Sacrifice", "Maize People"],
    "Katabasis descent matches Orpheus and Inanna.",
    "“Here we shall write the ancient word of the beginning...” — Popol Vuh",
    "The sacred book of the K'iche' Maya preserved in Guatemala."
))

stories.append(make_story(
    "aztec-five-suns", 1325, "c. 1325 – 1521 CE", "medieval", "americas", "The Americas",
    "Teotihuacan & Lake Texcoco (Tenochtitlan)", "Mexica Tlamatinime (Wise Scribes)",
    "The Aztec Myth of the Five Suns & the Eagle on the Cactus", "Nanahuatzin's Leap, Quetzalcoatl's Bone Theft, and Tenochtitlan",
    "After four previous worlds perish by jaguars, wind, fire, and flood, the humble god Nanahuatzin leaps into a cosmic bonfire to become the Fifth Sun. Quetzalcoatl steals human bones from Mictlan, and the Mexica follow the sign of an eagle on a cactus.",
    "### Act I: The Four Destroyed Suns\nFour previous worlds were destroyed by cosmic imbalances of jaguars, hurricanes, fire, and flood.\n\n### Act II: The Fire of Teotihuacan\nNanahuatzin, poor and covered in sores, courageously leaps into the cosmic pyre to become the Fifth Sun (Tonatiuh).\n\n### Act III: The Bones of Mictlan\nQuetzalcoatl outwits the Lord of the Dead to retrieve ancestral bones, bleeding his own veins to recreate mankind.\n\n### Act IV: The Eagle on the Cactus\nThe Mexica wander until discovering an eagle perched on a cactus eating a snake on Lake Texcoco, founding Tenochtitlan.",
    [{"name": "Nanahuatzin", "role": "Humble God & Fifth Sun", "desc": "Selfless sacrifice ignited the living sun."}, {"name": "Quetzalcoatl", "role": "Feathered Serpent", "desc": "God of wisdom who resurrected mankind."}],
    ["Cosmic Balance", "Self-Sacrifice", "Sacred City Foundations"],
    "Nanahuatzin's leap mirrors Odin's sacrifice on Yggdrasil.",
    "“As long as the world endures, the glory of Tenochtitlan shall never perish!”",
    "Carved into the 24-ton Aztec Calendar Sun Stone in Mexico City."
))

stories.append(make_story(
    "raven-steals-sun", -500, "c. 500 BCE", "classical", "americas", "The Americas",
    "Pacific Northwest Coast (Haida / Tlingit)", "Haida & Tlingit Elders",
    "Raven Steals the Sun: Bringing Light to the World", "The Transformation into Pine Needle, the Box of Daylight, and the Eagle's Sky",
    "When the world was in total darkness, the trickster Raven discovers that a selfish old chief keeps the Sun, Moon, and Stars locked in nested cedar boxes. Raven shapeshifts into a pine needle, is born as the chief's grandson, and steals the light for humanity.",
    "### Act I: The World in Blackness\nMortals fished in pitch darkness, bumping into rocks in cold fog.\n\n### Act II: The Pine Needle\nRaven shapeshifted into a hemlock needle in the chief's daughter's drinking cup, being born as a spoiled infant grandson.\n\n### Act III: Opening the Nested Boxes\nRaven cried for the shiny cedar boxes. As soon as the sun was handed to him, he transformed back into Raven and flew up the smoke hole, casting the sun into the sky.",
    [{"name": "Raven (Yéil)", "role": "Trickster Creator", "desc": "Brought light, fire, and freshwater to humanity."}],
    ["Trickster Heroism", "Liberation of Light", "Ingenuity"],
    "Parallels Prometheus stealing fire and Maui snaring the sun.",
    "“Raven opened his wings, and the world was filled with golden dawn.”",
    "Core oral tradition carved on Pacific Northwest cedar totem poles."
))

# --- 11. SUB-SAHARAN AFRICA ---
stories.append(make_story(
    "sundiata-mali", 1235, "c. 1235 CE", "medieval", "africa", "Sub-Saharan Africa",
    "Niani & Kirina, Mali Empire", "Preserved by Griots (Djeli Mamadou Kouyaté)",
    "The Epic of Sundiata: The Lion King of Mali", "The Miracle of the Iron Rod, the Sorcerer King, and the Mandinka Charter",
    "Born crippled and mocked until age seven, Sundiata Keita heaves himself up with an iron rod, overcomes seven years of exile, and defeats the sorcerer-king Sumanguru at Kirina to forge the wealthy Mali Empire.",
    "### Act I: The Crippled Boy\nSundiata crawls until age seven. When his mother weeps from mockery, he bends an iron rod like a bow, stands tall, and uproots a baobab tree.\n\n### Act II: The Sorcerer King\nSumanguru Kanté wears robes of human skin and rules with dark magic.\n\n### Act III: The Battle of Kirina\nDiscovering Sumanguru's secret weakness, Sundiata grazes him with an arrow tipped with a white rooster spur, breaking his magic and founding Mali.",
    [{"name": "Sundiata Keita", "role": "The Lion King", "desc": "Disabled prince who founded the Mali Empire."}, {"name": "Sumanguru Kanté", "role": "Sorcerer King", "desc": "Tyrant whose magic was undone by a rooster spur."}, {"name": "Balla Fasséké", "role": "Master Griot", "desc": "Preserved the lineage of Manden."}],
    ["Overcoming Adversity", "Griot Oral Memory", "Human Rights Charter"],
    "Directly inspired modern classics like Disney's The Lion King.",
    "“We are the vessels of speech; without us the names of kings would vanish.” — Kouyaté",
    "The Kouroukan Fouga charter proclaimed by Sundiata is recognized by UNESCO."
))

stories.append(make_story(
    "anansi-spider-stories", 1200, "c. 1200 CE", "medieval", "africa", "Sub-Saharan Africa",
    "Ashanti Kingdom (Ghana) & Diaspora", "Akan Storytellers (Anansesem)",
    "Anansi the Spider: How All Stories Came to Earth", "The Golden Box of Nyame, the Hornet Gourd, and the Leopard Trap",
    "All stories in the universe were locked in Sky God Nyame's golden box. Anansi the clever spider captures the stinging hornets, giant python, and leopard through wit to buy all stories for mankind.",
    "### Act I: The Sky God's Price\nNyame laughed at Anansi's wish to buy the stories, demanding four dangerous creatures.\n\n### Act II: The Four Tricks\nAnansi tricked the hornets into a calabash, tied the python to a palm stick, and trapped the leopard in a pit.\n\n### Act III: The Opening of the Box\nNyame opened the golden box; stories swarmed out like glowing fireflies across the globe.",
    [{"name": "Kwaku Anansi", "role": "Spider Trickster", "desc": "Conquered beasts through psychology rather than force."}, {"name": "Nyame", "role": "Sky God", "desc": "Keeper of celestial wisdom."}],
    ["Wit over Force", "Liberation of Folklore", "Diaspora Resilience"],
    "Survived as Br'er Rabbit and Aunt Nancy across the Caribbean and American South.",
    "“Without stories, we would have no light to see each other in the dark.”",
    "Core storytelling tradition (Anansesem) of the Akan people of West Africa."
))

stories.append(make_story(
    "kebra-nagast", 1300, "c. 1300 CE", "medieval", "africa", "Sub-Saharan Africa",
    "Aksum & Jerusalem", "Nebura'ed Yeshaq of Aksum",
    "Kebra Nagast: The Glory of Ethiopian Kings", "The Queen of Sheba, King Solomon's Riddles, and Menelik I",
    "The national epic of Ethiopia. Makeda, Queen of Sheba, visits King Solomon in Jerusalem. Their son Menelik I visits his father and brings the sacred Ark of the Covenant back to Aksum.",
    "### Act I: The Queen's Journey\nMakeda journeys across the Red Sea with caravans of frankincense to test Solomon's wisdom.\n\n### Act II: The Union of Kings\nSolomon hosts Makeda, and their union conceives Prince Menelik.\n\n### Act III: The Ark to Aksum\nAs an adult, Menelik visits Jerusalem, bringing the Ark of the Covenant to Ethiopia, establishing the Solomonic dynasty.",
    [{"name": "Makeda (Queen of Sheba)", "role": "Sovereign Queen", "desc": "Ruler of Aksum who tested Solomon's intellect."}, {"name": "Menelik I", "role": "First Emperor", "desc": "Founded Ethiopia's Solomonic royal line."}],
    ["Sacred Kingship", "Wisdom across Cultures", "Guardian of the Ark"],
    "Bridges Judeo-Christian and African imperial traditions.",
    "“The glory of kings is established in righteousness and truth.” — Kebra Nagast",
    "Ethiopian emperors traced their unbroken lineage to Menelik until 1974."
))

# --- 12. NORTHERN & CELTIC EUROPE ---
stories.append(make_story(
    "norse-ragnarok", 1000, "c. 800 – 1220 CE", "medieval", "n_europe", "Northern & Celtic Europe",
    "Yggdrasil & Vigrid", "Snorri Sturluson & Poetic Edda Skalds",
    "Ragnarök: The Twilight of the Gods and the Green Rebirth", "Yggdrasil, Fimbulwinter, the Slaying of Thor and Odin, and Lif & Lifthrasir",
    "After the three-year Fimbulwinter, Fenrir snaps his chains and Jörmungandr boils the sea. Gods and monsters clash at Vigrid; the world burns and sinks into the ocean, only to emerge green and renewed.",
    "### Act I: Death of Baldr and Fimbulwinter\nLoki tricks blind Höðr into killing Baldr with mistletoe. Three unbroken winters freeze the world.\n\n### Act II: The Last Stand at Vigrid\nOdin is swallowed by Fenrir; Thor slays the Midgard Serpent but falls dead from venom; Surtr flings fire across the nine worlds.\n\n### Act III: The Green Dawn\nThe blackened earth rises green from the sea; Lif and Lifthrasir emerge from Yggdrasil under a new sun.",
    [{"name": "Odin", "role": "Allfather", "desc": "Embraced his prophesied doom with courage."}, {"name": "Thor", "role": "God of Thunder", "desc": "Defender of mankind who slew the serpent."}],
    ["Cyclical Doom and Renewal", "Heroic Fatalism"],
    "Parallels Hindu Kali Yuga renewal and Aztec Five Suns.",
    "“The sun turns black, earth sinks into the sea... Now do I see the green earth rise once more.”",
    "Preserved in the 13th-century Codex Regius manuscript in Iceland."
))

stories.append(make_story(
    "beowulf-epic", 750, "c. 750 – 1000 CE", "medieval", "n_europe", "Northern & Celtic Europe",
    "Heorot (Denmark) & Geatland", "Anonymous Anglo-Saxon Scop",
    "Beowulf: The Monster in the Mist and the Dragon's Hoard", "Bare-Handed Duel with Grendel, the Mere of the Sea-Hag, and the Fire-Drake",
    "The Geatish hero Beowulf sails to Denmark to rid King Hrothgar's mead-hall Heorot of the cannibal monster Grendel and his mother, before dying in old age slaying a fire-breathing dragon.",
    "### Act I: The Mead-Hall Heorot\nGrendel haunts Heorot for 12 winters. Beowulf fights him bare-handed, ripping his arm from the socket.\n\n### Act II: The Boiling Mere\nBeowulf dives into the abyss, slaying Grendel's mother with an ancient giant-forged sword.\n\n### Act III: The Dragon's Barrow\nIn old age, Beowulf and loyal Wiglaf slay a treasure-guarding dragon, dying as the last true hero of the age.",
    [{"name": "Beowulf", "role": "Geatish Champion", "desc": "Possessed the strength of thirty men."}, {"name": "Grendel", "role": "Fiend of the Fens", "desc": "Descended from the curse of Cain."}],
    ["Heroic Code (Comitatus)", "Transience of Glory (Wyrd)"],
    "Direct inspiration for Tolkien's The Hobbit and Lord of the Rings.",
    "“Fate often saves an undoomed man when his courage holds!” — Beowulf",
    "Preserved in the Nowell Codex in the British Library."
))

stories.append(make_story(
    "irish-tain-cuchulainn", 700, "c. 700 – 1100 CE", "medieval", "n_europe", "Northern & Celtic Europe",
    "Ulster & Cooley Peninsula, Ireland", "Irish Monastic Scribes & Filí (Bards)",
    "Táin Bó Cúailnge: The Cattle Raid of Cooley & Cú Chulainn", "The Pillow Talk of Queen Medb, the Warp-Spasm, and the Ford of Ardee",
    "Queen Medb invades Ulster to seize the Donn Cúailnge bull. With Ulster warriors paralyzed by a birth-pang curse, 17-year-old demigod Cú Chulainn defends the borders alone in single-combat river duels.",
    "### Act I: The Pillow Talk\nQueen Medb demands the Brown Bull of Cooley to equal her husband's wealth, rallying Ireland to war.\n\n### Act II: The Boy at the Ford\nCú Chulainn holds the river fords alone through the terrifying Warp-Spasm (Ríastrad) battle frenzy.\n\n### Act III: The Duel with Ferdiad\nForced to fight his soul-brother Ferdiad, Cú Chulainn weeps as his barbed spear Gáe Bulg takes his friend's life.",
    [{"name": "Cú Chulainn", "role": "Hound of Ulster", "desc": "Son of sun god Lugh."}, {"name": "Queen Medb", "role": "Sovereign of Connacht", "desc": "Ambitious warlord queen."}],
    ["Warrior Honor (Geas)", "Tragedy of Fratricide"],
    "Grief over Ferdiad mirrors Achilles weeping for Patroclus and Rostam for Sohrab.",
    "“I care not if I live but a single day, so long as my deeds live forever!” — Cú Chulainn",
    "Preserved in the 12th-century Book of Leinster."
))

stories.append(make_story(
    "arthur-holy-grail", 1170, "c. 1170 – 1485 CE", "medieval", "n_europe", "Northern & Celtic Europe",
    "Camelot, Avalon & Glastonbury", "Chrétien de Troyes & Sir Thomas Malory",
    "King Arthur and the Knights of the Round Table: The Quest for the Holy Grail", "Excalibur from the Stone, the Lady of the Lake, Lancelot, and Sir Galahad",
    "Young Arthur pulls the sword from the anvil to become High King of Britain, establishing the egalitarian Round Table at Camelot, sending knights on the spiritual quest for the Holy Grail before his final voyage to Avalon.",
    "### Act I: The Sword in the Stone\nMerlin places the sword in the stone; humble squire Arthur pulls it out effortlessly.\n\n### Act II: The Round Table\nArthur establishes the Round Table where all knights sit as equals, defending the weak.\n\n### Act III: The Quest for the Holy Grail\nSir Galahad, purest of heart, gazes into the Holy Grail and ascends to heaven.\n\n### Act IV: The Fall of Camelot\nBetrayed by Mordred, Arthur is mortally wounded at Camlann and ferried across the mists to the enchanted isle of Avalon.",
    [{"name": "King Arthur", "role": "The Once and Future King", "desc": "Idealized sovereign of chivalry."}, {"name": "Merlin", "role": "Enchanter & Prophet", "desc": "Guided Arthur with druidic foresight."}, {"name": "Sir Galahad", "role": "Pure Knight", "desc": "Achieved the vision of the Holy Grail."}],
    ["Chivalric Honor", "Egalitarian Leadership", "The Once and Future King"],
    "Merlin echoes Gandalf; the Holy Grail mirrors the Vedic Amrita and Golden Fleece.",
    "“Whoso pulleth out this sword of this stone is rightwise king born of all England.” — Malory",
    "Synthesized Celtic Welsh folklore with Anglo-Norman chivalric romance."
))

# --- 13. GLOBAL RENAISSANCE & LITERARY MASTERPIECES ---
stories.append(make_story(
    "dante-divine-comedy", 1320, "1308 – 1320 CE", "medieval", "world_classics", "Global Masterpieces & Renaissance",
    "Florence & The Three Realms", "Dante Alighieri (Il Sommo Poeta)",
    "The Divine Comedy: Inferno, Purgatorio, and Paradiso", "The Dark Wood, Virgil's Guidance, Beatrice, and the Love That Moves the Stars",
    "Guided by Virgil through the nine circles of Hell and seven terraces of Purgatory, Dante is led by Beatrice through the celestial spheres of Paradise to gaze upon the Holy Trinity in radiant light.",
    "### Act I: The Gates of Hell\nLost in a dark wood at midlife, Dante passes the gate: 'Abandon all hope, ye who enter here.'\n\n### Act II: The Inferno & Purgatorio\nWitnessing the contrapasso punishments of sin, he climbs Mount Purgatory to cleanse his soul.\n\n### Act III: Paradiso and the Cosmic Rose\nBeatrice guides him to the Empyrean to behold the Love that moves the sun and other stars.",
    [{"name": "Dante", "role": "Pilgrim & Poet", "desc": "Allegory of human moral redemption."}, {"name": "Virgil", "role": "Master Guide", "desc": "Symbol of human reason."}, {"name": "Beatrice", "role": "Divine Muse", "desc": "Symbol of divine grace."}],
    ["Divine Justice (Contrapasso)", "Spiritual Transformation"],
    "Katabasis parallels Aeneas in Virgil and Gilgamesh crossing the deep.",
    "“L’Amor che move il sole e l’altre stelle.” (The Love that moves the sun and stars.) — Paradiso",
    "Established the Tuscan dialect as the modern Italian language."
))

stories.append(make_story(
    "cervantes-don-quixote", 1605, "1605 – 1615 CE", "renaissance", "world_classics", "Global Masterpieces & Renaissance",
    "La Mancha, Spain", "Miguel de Cervantes Saavedra",
    "Don Quixote de la Mancha: The Founding Novel of Modern Literature", "The Woeful Countenance, Sancho Panza, Windmills, and Dulcinea",
    "An aging country gentleman driven mad by chivalric romances renames himself Don Quixote, riding a scrawny nag with his earthy squire Sancho Panza to right the wrongs of the world.",
    "### Act I: The Windmill Giants\nQuixote charges thirty windmills mistaking them for giants, blaming sorcery when thrown from his saddle.\n\n### Act II: Sancho's Island\nSancho governs the mock island of Barataria with surprising peasant wisdom and equity.\n\n### Act III: Return to Sanity\nDefeated in a duel, Quixote returns home, regains sanity, and dies peacefully as Alonso the Good.",
    [{"name": "Don Quixote", "role": "Idealist Knight", "desc": "Noble visionary whose madness exposes worldly cynicism."}, {"name": "Sancho Panza", "role": "Pragmatic Squire", "desc": "Donkey-riding peasant of loyal common sense."}],
    ["Idealism vs Realism", "Power of Imagination", "Invention of Modern Novel"],
    "Blueprint for buddy duos from Sherlock Holmes & Watson to Frodo & Sam.",
    "“To dream the impossible dream, to fight the unbeatable foe...” — Quixote Ethos",
    "Universally recognized as the first modern novel in world literature."
))

stories.append(make_story(
    "shakespeare-hamlet", 1601, "1599 – 1601 CE", "renaissance", "world_classics", "Global Masterpieces & Renaissance",
    "Elsinore Castle, Denmark", "William Shakespeare (The Bard of Avon)",
    "Hamlet, Prince of Denmark: The Tragedy of Being and Nothingness", "The Ghost on the Ramparts, 'To Be or Not to Be', and the Poisoned Duel",
    "Prince Hamlet is visited by his father's ghost demanding vengeance against his usurping uncle Claudius. Paralyzed by existential doubt, Hamlet feigns madness in the ultimate tragedy of human intellect.",
    "### Act I: The Ghost and Mousetrap\nThe ghost reveals Claudius poisoned his ear. Hamlet stages a play to catch the king's guilty conscience.\n\n### Act II: 'To Be or Not to Be'\nHamlet meditates on suicide and action, confronting Ophelia and killing Polonius through an arras.\n\n### Act III: The Poisoned Duel\nIn a rigged fencing duel, Gertrude, Laertes, Claudius, and Hamlet all perish, ending with: 'The rest is silence.'",
    [{"name": "Prince Hamlet", "role": "Tragic Philosopher", "desc": "Intellectual paralyzed by existential doubt."}, {"name": "King Claudius", "role": "Usurping Monarch", "desc": "Murdered his brother for the crown."}],
    ["Action vs Inaction", "Appearance vs Reality", "Mortality"],
    "Echoes Orestes avenging Agamemnon in Aeschylus.",
    "“There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy.”",
    "The supreme pinnacle of dramatic poetry in the English language."
))

stories.append(make_story(
    "milton-paradise-lost", 1667, "1667 – 1674 CE", "renaissance", "world_classics", "Global Masterpieces & Renaissance",
    "Hell, Chaos, Heaven & Eden", "John Milton (The Blind English Epicist)",
    "Paradise Lost: The Cosmic Rebellion and the Fall of Man", "Pandæmonium, 'Better to Reign in Hell', the Serpent, and the World Before Them",
    "Dictated while blind by John Milton to 'justify the ways of God to men'. Depicts the rebellion of Satan, the construction of Pandæmonium in Hell, and the temptation and expulsion of Adam and Eve from Eden.",
    "### Act I: The Burning Lake\nSatan awakens in the fire of Hell, declaring: 'Better to reign in Hell than serve in Heaven!'\n\n### Act II: Flight across Chaos\nSatan crosses the abyss to Eden, slipping into the serpent to tempt Eve.\n\n### Act III: The Expulsion\nAdam eats the fruit in solidarity with Eve. Michael reveals human history before they walk out into the open world.",
    [{"name": "Satan (Lucifer)", "role": "Fallen Archangel", "desc": "Charismatic, tragic rebel driven by pride."}, {"name": "Adam & Eve", "role": "First Parents", "desc": "Introduced moral choice into history."}],
    ["Free Will and Conscience", "Pride and Evil", "Redemptive Hope"],
    "Dialogues directly with Homer and Dante.",
    "“The mind is its own place, and in itself can make a Heaven of Hell, a Hell of Heaven.” — Milton",
    "Dictated in total blindness following the English Civil War."
))

# Sort chronologically
stories.sort(key=lambda s: s["year"])

print(f"Total compiled rich stories: {len(stories)}")

# Output to js/stories_data.js
js_content = """/**
 * World Myths, Writers & History Timeline Data
 * A comprehensive curated archive of world mythologies, founding epics, 
 * legendary writers, and historical stories across all continents from 10,000 BCE to 1700 CE.
 */

const REGIONS = [
  { id: 'all', name: 'All Regions', icon: '🌐', color: '#111111' },
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
  { id: 'all', name: 'All Eras', range: '10,000 BCE – 1700 CE', year: -10000 },
  { id: 'prehistory', name: 'Deep Prehistory & Oral Beginnings', range: '10,000 – 3000 BCE', year: -10000 },
  { id: 'bronze', name: 'Bronze Age & First Writings', range: '3000 – 1200 BCE', year: -3000 },
  { id: 'classical', name: 'Classical Antiquity & Axial Age', range: '1200 BCE – 500 CE', year: -1200 },
  { id: 'medieval', name: 'Golden Ages & Medieval Epics', range: '500 – 1400 CE', year: 500 },
  { id: 'renaissance', name: 'Renaissance & Global Masterpieces', range: '1400 – 1700 CE', year: 1400 }
];

const STORIES_DATA = """ + json.dumps(stories, indent=2, ensure_ascii=False) + """;

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { REGIONS, ERAS, STORIES_DATA };
}
"""

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'js', 'stories_data.js')
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Master stories_data.js written successfully to {out_path}!")
