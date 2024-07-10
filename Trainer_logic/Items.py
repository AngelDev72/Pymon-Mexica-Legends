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
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Dread_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Mythic_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Power_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Flame_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Icicle_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Zap_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Love_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Plume_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Skull_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Stalactite_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Leaf_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Toxic_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Mystic_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Rock_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Iron_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }
    Wave_Earring = {
        "name": "",
        "description": "A mythical object related to an ancient folktale. It has a  hanging from it.",
        "quantity": [],
        "effect": []
    }

# Sprectrabane exclusive
class Ring(Enum):
    Zap_Ring = {
        "name": "",
        "description": "A ring crafted from pure gold. It has a Lightning engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }
    Frost_Ring = {
        "name": "",
        "description": "A ring crafted from pure gold. It has a  engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }
    Blaze_Ring = {
        "name": "",
        "description": "A ring crafted from pure gold. It has a  engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }
    Wave_Ring = {
        "name": "",
        "description": "A ring crafted from pure gold. It has a  engraved on it with a powerful spell.",
        "quantity": [],
        "effect": []
    }

#Fruit
class Fruit(Enum):
    Orange = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Cherry = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Peach = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Banana = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Strawberry = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Pineapple = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Pear = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Grape = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Guava = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Blueberry = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }

#Evolution
class Evolution_Marks(Enum):
    Leaf_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Flame_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Wave_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Moon_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Thunder_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Sun_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Night_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Shiny_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Dawn_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Ice_Mark = {
        "name": "",
        "description": "",
        "quantity": [],
        "effect": []
    }

#Crystals
class Crystals(Enum):
    Red_Crystal = {
        "name": "Red Crystal",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Blue_Crystal = {
        "name": "Blue Crystal",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Yellow_Crystal = {
        "name": "Yellow Crystal",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Green_Crystal = {
        "name": "Green Crystal",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    White_Crystal = {
        "name": "White Crystal",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Black_Crystal = {
        "name": "Black Crystal",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Diamond = {
        "name": "Diamond",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Aquamarine = {
        "name": "Aquamarine",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Jade = {
        "name": "Jade",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Turquoise = {
        "name": "Turquoise",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Amathist = {
        "name": "Amathist",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Ruby = {
        "name": "Ruby",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Sapphire = {
        "name": "Sapphire",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Emerald = {
        "name": "Emerald",
        "description": "",
        "quantity": [],
        "effect": [],
        "catch rate": []
    }
    Topaz = {
        "name": "Topaz",
        "description": "",
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
    Lantern = {
        "name": "Lantern",
        "description": "A petrolium based instrument to give light.",
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
