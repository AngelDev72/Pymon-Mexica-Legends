import sys
import pygame
import random
from enum import Enum
from Item_logic import Item_Effects as IE

#Items list
class Heal(Enum):
    Potion = {
        "name": "Potion",
        "description": "A simple house remedy. Restores 20 HP.",
        "quantity": [],
        "effect": []
    }
    Super_Potion = {
        "name": "Super Potion",
        "description": "A somewhat elaborated mix of herbs. Restores 50 HP.",
        "quantity": [],
        "effect": []
    }
    Hyper_Potion = {
        "name": "Hyper Potion",
        "description": "A more elaborated mix of herbs. Restores 150 HP.",
        "quantity": [],
        "effect": []
    }
    Max_Potion = {
        "name": "Max Potion",
        "description": "A complex mix of herbs. Restores full HP",
        "quantity": [],
        "effect": []
    }
    Secret_Medicine = {
        "name": "Secret Medicine"
        "description": "A complicated mix of nutritious herbs. Restores full HP and eliminates Status conditions",
        "quantity": [],
        "effect": []
    }
    Simple_Water = {
        "name": "Simple Water",
        "description": "Refreshing water from the mountains. Restores 25 HP.",
        "quantity": [],
        "effect":[]
    }
    Tea = {
        "name": "Tea",
        "description": "A nutritious tea. Restores 50 HP.",
        "quantity": [],
        "effect": []
    }
    Cocoa = {
        "name": "Cocoa",
        "description": "A delicious hot drink. Restores Status conditions back to normal.",
        "quantity": [],
        "effect": []
    }
    Antidote = {
        "name": "Antidote",
        "description": "A mix of herbs used to cure Poisons.",
        "quantity": [],
        "effect": []
    }
    Thermal_Rock ={
        "name": "Thermal Rock",
        "description": "Preheated rocks used to cure colds.",
        "quantity": [],
        "effect":[]
    }
    Fresh_Pomade = {
        "name": "Fresh Pomade",
        "description": "A mix of menthol herbs used to refresh burns.",
        "quantity": [],
        "effect": []
    }
    Complexed_Pomade = {
        "name": "Complexed Pomade",
        "description": "A highly elaborated pomade that heals any Status condition.",
        "quantity": [],
        "effect": []
    }
    Awakening = {
        "name": "Awakening",
        "description": "A rare type of salt that that snaps awake real quick.",
        "quantity": [],
        "effect": []
    }
    Bitter_Powder = {
        "name": "Bitter Powder",
        "description": "A very bitter substance that restores 50 HP.",
        "quantity": [],
        "effect": []
    }
    Energy_Root = {
        "name": "Energy Root",
        "description": "A very rare and nutritious root that restores 150 HP. Very bitter also.",
        "quantity": [],
        "effect": []
    }
    Miracle_Herb = {
        "name": "Miracle Herb",
        "description": "A rare herb that revives a fainted Pymon by 1/2 its HP.",
        "quantity": [],
        "effect": []
    }
    Secret_Remedy = {
        "name": "Secret Remedy",
        "description": "A miraculous beverage. Fully revives a fainted Pymon.",
        "quantity": [],
        "effect": []
    }
    Elixir = {
        "name": "Elixir"
        "description": "A home made beverage. Retores 10 SP.",
        "quantity": [],
        "effect": []
    }
    Super_Elixir = {
        "name": "Super Elixir",
        "description": " An ancient remedy passed down by generations. Restores full SP.",
        "quantity": [],
        "effect": []
    }

#Boost Items
class Boost(Enum):
    Miracle_Seed = {
        "name": "Miracle Seed",
        "description": "A Godly gift from Xochipilli. Boosts the power of Grass type moves.",
        "quantity": [],
        "effect": []
    }
    Honorable_Flame = {
        "name": "Honorable Flame",
        "description": "A Godly gift from Tonatiuh. Boosts the power of Fire type moves.",
        "quantity": [],
        "effect": []
    }
    Celestial_Water = {
        "name": "Celestial Water",
        "description": "A Godly gift from Tlaloc. Boosts the power of Water type moves.",
        "quantity": [],
        "effect": []
    }
    Sensitive_Claw = {
        "name": "Sensitive Claw",
        "description": "A Godly gift from Chicomecoatl. Boosts the power of Bug type moves.",
        "quantity": [],
        "effect": []
    }
    Sharp_Feather = {
        "name": "Sharp Feather",
        "description": "A Godly gift from Huitzilopochtli. Boosts the power of Flying type moves.",
        "quantity": [],
        "effect": []
    }
    Soft_Huipil = {
        "name": "Soft Huipil",
        "description": "A Godly gift from Tezcatlipoca. Boosts the power of Normal type moves.",
        "quantity": [],
        "effect": []
    }
    Obsidian_Stone = {
        "name": "Obsidian Stone",
        "description": "A Godly gift from Tlaltecuhtli. Boosts the power of Rock type moves.",
        "quantity": [],
        "effect": []
    }
    Ancient_Sand = {
        "name": "Ancient Sand",
        "description": "A Godly gift from Tlalzolteotl. Boosts the power of Ground type moves.",
        "quantity": [],
        "effect": []
    }
    Forbbiden_Scrolls = {
        "name": "Forbbiden Scrolls",
        "description": "A Godly corrupted gift from Mictlantecuhtli. Boosts the power of Dark type moves.",
        "quantity": [],
        "effect": []
    }
    Warrior_Cloth = {
        "name": "warrior Cloth",
        "description": "A Godly gift from Huitzilopochtli. Boosts the power of Fighting type moves.",
        "quantity": [],
        "effect":[]
    }
    Gifted_Eye = {
        "name": "Gifted Eye",
        "description": "A Godly gift from Quetzalcoatl. Boosts the power of Psychic type moves.",
        "quantity": [],
        "effect": []
    }
    Poison_Dart = {
        "name": "Poison Dart",
        "description": "A Godly gift from Itzpapalotl. Boosts the power of Poison type moves.",
        "quantity": [],
        "effect": []
    }
    Sharp_Fang = {
        "name": "Sharp Fang",
        "description": "A Godly gift from Quetzalcoatl. Boosts the power of Dragon type moves.",
        "quantity": [],
        "effect": []
    }
    Enchanted_Scroll = {
        "name": "Enchanted Scroll",
        "description": "A Godly gift from Tlalzolteotl. Boosts the power of Fairy type moves.",
        "quantity": [],
        "effect": []
    }
    Iron_Chunk = {
        "name": "Iron Chunk",
        "description": "A Godly gift from Xipe Totec. Boosts the power of Steel type moves.",
        "quantity": [],
        "effect": []
    }
    Eternal_Ice = {
        "name": "Eternal Ice",
        "description": "A Godly gift from Tonantzin. Boosts the power of Ice type moves.",
        "quantity": [],
        "effect": []
    }
    Omninuos_Scroll = {
        "name": "Omninuos Scroll",
        "description": "A Godly corrupted gift from Mictlantecuhtli. Boosts the power of Ghost type moves.",
        "quantity": [],
        "effect": []
    }
    Magnetic_Rock = {
        "name": "Magnetic Rock",
        "description": "A Godly gift from Tlaloc. Boosts the power of Electric type moves.",
        "quantity": [],
        "effect": []
    }
    Fang Collar = {
        "name": "Fang Collar",
        "description": "A Godly gift from Xolotl. Boosts the power of Beast type moves.",
        "quantity": [],
        "effect": []
    }

#Lunaryx Solaris Serpentix summoning items
class Orbs(Enum):
    Sun_Orb = {
        "name": "Sun Orb",
        "description": "A mystirious golden Orb that exhales a soothing heat. Legend says it is connected to Solaris",
        "effect": []
    }
    Moon_Orb = {
        "name": "Moon Orb",
        "description": "A mystirious silver Orb that emites a soothing light. Legend says it is connected to Lunaryx",
        "effect": []
    }
    Scaled_Orb = {
        "name": "Scaled Orb",
        "description": "A mystirious Orb with scales. An ancient folktale says that the spirit of Serpentix  is connected to this Orb.",
        "effect": []
    }

#Shadow exclusive
class Emblems(Enum):
    Blank_Emblem = {
        "name": "Blank Emblem",
        "description": "A badge from an ancient era. Boosts the power of Normal type moves.",
        "quantity": [],
        "effect": []
    }
    Darco_Emblem = {
        "name": "Draco Emblem",
        "description": "A badge from an ancient era. Boosts the power of Dragon type moves.",
        "quantity": [],
        "effect": []
    }
    Dread_Emblem = {
        "name": "Dread Emblem",
        "description": "A badge from an ancient era. Boosts the power of Dark type moves",
        "quantity": [],
        "effect": []
    }
    Earth_Emblem = {
        "name": "Earth Emblem",
        "description": "A badge from an ancient era. Boosts the power of Ground tyoe moves.",
        "quantity": [],
        "effect": []
    }
    Fist_Emblem = {
        "name": "Fist Emblem",
        "description": "A badge from an ancient era. Boosts the power of Fighting type moves.",
        "quantity": [],
        "effect": []
    }
    Flame_Emblem = {
        "name": "Flame Emblem",
        "description": "A badge from an ancient era. Boosts the power of Fire tyoe moves.",
        "quantity": [],
        "effect": []
    }
    Icicle_Emblem = {
        "name": "Icicle Emblem",
        "description": "A badge from an ancient era. Boosts the power of Ice type moves.",
        "quantity": [],
        "effect": []
    }
    Insect_Emblem = {
        "name": "Insect Emblem",
        "description": "A badge from an ancient era. Boosts the power of Bug type moves.",
        "quantity": [],
        "effect": []
    }
    Iron_Emblem = {
        "name": "Iron_Emblem",
        "description": "A badge from an ancient era. Boosts the power of Steel type moves.",
        "quantity": [],
        "effect": []
    }
    Legend_Emblem = {
        "name": "Legend Emblem",
        "description": "A star-shaped badge from an ancient era. It wields an unseen power.",
        "quantity": [],
        "effect": []
    }
    Meadow_Emblem = {
        "name": "Meadow Emblem",
        "description": "A badge from an ancient era. Boosts the power of Grass type moves.",
        "quantity": [],
        "effect": []
    }
    Mind_Emblem = {
        "name": "Mind Emblem",
        "description": "A badge from an ancient era. Boosts the power of Psychic type moves.",
        "quantity": [],
        "effect": []
    }
    Pixie_Emblem = {
        "name": "Pixie Emblem",
        "description": "A badge from an ancient era. Boosts the power of Fairy type moves.",
        "quantity": [],
        "effect": []
    }
    Salvage_Emblem = {
        "name": "Salvage Emblem",
        "description": "A badge from an ancient era. Boosts the power of Beast type moves.",
        "quantity": [],
        "effect": []
    }
    Sky_Emblem = {
        "name": "Sky Emblem",
        "description": "A badge from an ancient era. Boosts the power of Flying type moves.",
        "quantity": [],
        "effect": []
    }
    Splash_Emblem = {
        "name": "Splash Emblem",
        "description": "A badge from an ancient era. Boosts the power of Water type moves.",
        "quantity": [],
        "effect": []
    }
    Spooky_Emblem = {
        "name": "Spooky Emblem",
        "description": "A badge from an ancient era. Boosts the power of Ghost type moves.",
        "quantity": [],
        "effect": []
    }
    Stone_Emblem = {
        "name": "Stone Emblem",
        "description": "A badge from an ancient era. Boosts the power of Rock type moves.",
        "quantity": [],
        "effect": []
    }
    Toxic_Emblem = {
        "name": "Toxic Emblem",
        "description": "A badge from an ancient era. Boosts the power of Poison type moves.",
        "quantity": [],
        "effect": []
    }
    Zap_Emblem = {
        "name": "Zap Emblem",
        "description": "A badge from an ancient era. Boosts the power of Electric type moves.",
        "quantity": [],
        "effect": []
    }

#Nightmane exclusive
class Earring(Enum):
    Fang_Earring = {
        "name": "Fang Earring",
        "description": "A mythical object related to an ancient folktale. It has a fang hanging from it.",
        "quantity": [],
        "effect": []
    }
    Scarab_Earring = {
        "name": "Scarab Earring",
        "description": "A mythical object related to an ancient folktale. It has a scarab hanging from it.",
        "quantity": [],
        "effect": []
    }
    Dread_Earring = {
        "name": "Dread Earring",
        "description": "A mythical object related to an ancient folktale. It has a black moon hanging from it.",
        "quantity": [],
        "effect": []
    }
    Mythic_Earring = {
        "name": "Mythic Earring",
        "description": "A mythical object related to an ancient folktale. It has big scales hanging from it.",
        "quantity": [],
        "effect": []
    }
    Power_Earring = {
        "name": "Power Earring",
        "description": "A mythical object related to an ancient folktale. It has a fist hanging from it.",
        "quantity": [],
        "effect": []
    }
    Flame_Earring = {
        "name": "Flame Earring",
        "description": "A mythical object related to an ancient folktale. It has a flame hanging from it.",
        "quantity": [],
        "effect": []
    }
    Icicle_Earring = {
        "name": "Icicle Earring",
        "description": "A mythical object related to an ancient folktale. It has an icicle hanging from it.",
        "quantity": [],
        "effect": []
    }
    Zap_Earring = {
        "name": "Zap Earring",
        "description": "A mythical object related to an ancient folktale. It has a lightning hanging from it.",
        "quantity": [],
        "effect": []
    }
    Love_Earring = {
        "name": "Love Earring",
        "description": "A mythical object related to an ancient folktale. It has a heart hanging from it.",
        "quantity": [],
        "effect": []
    }
    Plume_Earring = {
        "name": "Plume Earring",
        "description": "A mythical object related to an ancient folktale. It has a feather hanging from it.",
        "quantity": [],
        "effect": []
    }
    Skull_Earring = {
        "name": "Skull Earring",
        "description": "A mythical object related to an ancient folktale. It has a skull hanging from it.",
        "quantity": [],
        "effect": []
    }
    Stalactite_Earring = {
        "name": "Stalactite Earring",
        "description": "A mythical object related to an ancient folktale. It has a stalactite hanging from it.",
        "quantity": [],
        "effect": []
    }
    Leaf_Earring = {
        "name": "Leaf Earring",
        "description": "A mythical object related to an ancient folktale. It has a leaf hanging from it.",
        "quantity": [],
        "effect": []
    }
    Toxic_Earring = {
        "name": "Toxic Earring",
        "description": "A mythical object related to an ancient folktale. It has an purple bubble hanging from it.",
        "quantity": [],
        "effect": []
    }
    Mystic_Earring = {
        "name": "Mystic Earring",
        "description": "A mythical object related to an ancient folktale. It has an eye hanging from it.",
        "quantity": [],
        "effect": []
    }
    Obsidian_Earring = {
        "name": "Obsidian Earring",
        "description": "A mythical object related to an ancient folktale. It has a pice of obsidian hanging from it.",
        "quantity": [],
        "effect": []
    }
    Iron_Earring = {
        "name": "Iron Earring",
        "description": "A mythical object related to an ancient folktale. It has a pice of iron hanging from it.",
        "quantity": [],
        "effect": []
    }
    Wave_Earring = {
        "name": "Wave Earring",
        "description": "A mythical object related to an ancient folktale. It has a seashell hanging from it.",
        "quantity": [],
        "effect": []
    }

# Sprectrabane exclusive
class Ring(Enum):
    Zap_Ring = {
        "name": "Zap Ring",
        "description": "A ring crafted from pure gold. It has a Lightning engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }
    Frost_Ring = {
        "name": "Frost Ring",
        "description": "A ring crafted from pure gold. It has a snowflake engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }
    Blaze_Ring = {
        "name": "Blaze Ring",
        "description": "A ring crafted from pure gold. It has a flame engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }
    Wave_Ring = {
        "name": "Wave Ring",
        "description": "A ring crafted from pure gold. It has a waved pattern engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }

#Fruit
class Fruit(Enum):
    Orange = {
        "name": "Orange",
        "description": "A delicious citric fruit. Restores 30 HP.",
        "quantity": [],
        "effect": []
    }
    Lemon = {
        "name": "Lemon",
        "description": "A delicious sour citric fruit. Just a few drops wakes a Pymon instantly.",
        "quantity": [],
        "effect": []
    }
    Cherry = {
        "name": "Cherry",
        "description": "A delicious small, round stone fruit. Helps heal paralisis.",
        "quantity": [],
        "effect": []
    }
    Peach = {
        "name": "Peach",
        "description": "A soft round fruit. Helps heal poisoning.",
        "quantity": [],
        "effect": []
    }
    Banana = {
        "name": "Banana",
        "description": "A soft and nutritious fruit. Helps heal Confusion. It is also used to elaborate the Secret Remedy.",
        "quantity": [],
        "effect": []
    }
    Strawberry = {
        "name": "Strawberry",
        "description": "A small, sweet and delicious red berry. Helps cure burns.",
        "quantity": [],
        "effect": []
    }
    Pineapple = {
        "name": "Pineapple",
        "description": "A big sweet and juicy fruit. It is used to elaborate Secret Remedy.",
        "quantity": [],
        "effect": []
    }
    Pear = {
        "name": "Pear",
        "description": "A dry, juicy fruit. Helps cure colds.",
        "quantity": [],
        "effect": []
    }
    Grape = {
        "name": "Grape",
        "description": "A small round and juicy fruit. Restores 10 HP. It is an ingrediant to elaborate the Secret Remedy.",
        "quantity": [],
        "effect": []
    }
    Guava = {
        "name": "Guava",
        "description": "A round, sweet  fruit used to elaborate Secret Remedy.",
        "quantity": [],
        "effect": []
    }
    Blueberry = {
        "name": "Blueberry",
        "description": "A small round berry. Heal any Status condition",
        "quantity": [],
        "effect": []
    }

#Evolution
class Evolution_Marks(Enum):
    Leaf_Mark = {
        "name": "Leaf Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Grass element on it.",
        "quantity": [],
        "effect": []
    }
    Flame_Mark = {
        "name": "Flame Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Fire element on it.",
        "quantity": [],
        "effect": []
    }
    Wave_Mark = {
        "name": "Wave Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Water element on it.",
        "quantity": [],
        "effect": []
    }
    Moon_Mark = {
        "name": "Moon Mark",
        "description":"A mystic mark encarved within a rare stone. It has the Moon marked on it.",
        "quantity": [],
        "effect": []
    }
    Thunder_Mark = {
        "name": "Thunder Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Electric element on it.",
        "quantity": [],
        "effect": []
    }
    Sun_Mark = {
        "name": "Sun_Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Sun marked on it.",
        "quantity": [],
        "effect": []
    }
    Night_Mark = {
        "name": "Night Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Dark element on it.",
        "quantity": [],
        "effect": []
    }
    Shiny_Mark = {
        "name": "Shiny Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Fairy element on it.",
        "quantity": [],
        "effect": []
    }
    Dawn_Mark = {
        "name": "Dawn Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Psychic element on it.",
        "quantity": [],
        "effect": []
    }
    Ice_Mark = {
        "name": "Ice_Mark",
        "description": "A mystic mark encarved within a rare stone. It has the Ice element on it.",
        "quantity": [],
        "effect": []
    }

#Crystals
class Crystals(Enum):
    White_Crystal = {
        "name": "White Crystal",
        "description": "An oridnary crystal used to capture the spirit of wild Pymon.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Yellow_Crystal = {
        "name": "Yellow Crystal",
        "description": "A somewhat better crystal used to capture the spirit of wild Pymon. Has a higher catch rate than a White Crystal.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Black_Crystal = {
        "name": "Black Crystal",
        "description": "A better crystal used to capture the spirit of wild Pymon. Has a higher catch rate than a Yellow Crystal.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Green_Crystal = {
        "name": "Green Crystal",
        "description": "A spiritual crystal. It shines with a blazing green and calming light. Better chance at Grass type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Red_Crystal = {
        "name": "Red Crystal",
        "description": "A spiritual crystal. It shines with a blazing red and warm light. Better chance at Fire type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Blue_Crystal = {
        "name": "Blue Crystal",
        "description": "A spiritual crystal. It shines with a blazing blue and soothing light. Better chance at Water type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Aquamarine = {
        "name": "Aquamarine",
        "description": "A spiritual crystal. It shines with a dazzling blueish green light. Better chance at Ice type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Jade = {
        "name": "Jade",
        "description": "A spiritual crystal. It shines with an intense greenish light. Better chance at Bug type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Turquoise = {
        "name": "Turquoise",
        "description": "A spiritual crystal. It shines with a beautiful blueish light with metalic glares. Better chance at Dragon and Steel type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Topaz = {
        "name": "Topaz",
        "description": "A spiritual crystal. It shimmers with a dazzling yellow and energetic light. Better chance at Electric type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Amathist = {
        "name": "Amathist",
        "description": "A spiritual crystal. It shimmers with a beautiful violet light. Better chance at Ghost type Pymons.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Ruby = {
        "name": "Ruby",
        "description": "A mystical gem. It shines with a blazing red and intense light. Wields the power of the Sun.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Sapphire = {
        "name": "Sapphire",
        "description": "A mystical gem. It shines with a blazing blue and intense light. Wields the power of the Moon.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Emerald = {
        "name": "Emerald",
        "description": "A mystical gem. It shines with a blazing green and intense light. Wields the power of the Earth.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Diamond = {
        "name": "Diamond",
        "description": "A beautiful mystical gem. It shines with an intense and brilliant light. Its aura soothes any spirit to be caught.",
        "image": [],
        "quantity": [],
        "effect": [],
        "catch rate": []
    }

#Key Items
class Key_items(Enum):
    Raft_Plots = {
        "name": "Raft Plots",
        "description": "The instructions to build a raft.",
        "effect": []
    }
    Torch = {
        "name": "Torch",
        "description": "A simple torch used to give light in dark areas.",
        "effect": []
    }
    Fruit_Pouch = {
        "name": "Fruit Pouch",
        "description": "A knitted bag to store fruit. Very elastic. and resistant.",
        "effect": []
    }
    Sharp_Claw = {
        "name": "Sharp Claw",
        "description": "A very sharp claw stuck into stone. Looks very old.",
        "effect": []
    }
    Fin_Bone = {
        "name": " Fin Bone",
        "description": "A fin bone traped in stone. Looks very old.",
        "effect": []
    }
    Rod = {
        "name": "Rod",
        "description": "A rod elaborated to fish.",
        "effect": []
    }
    Spirit_Band = {
        "name": "Spirit Band",
        "description": "A spiritual object. Has the power to communicate with certain deities.",
        "effect": []
    }
