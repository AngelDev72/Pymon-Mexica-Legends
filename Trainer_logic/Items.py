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
        "description": "A mix of menthol herbs ised to refresh burns.",
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
        "name":
        "description": "A Godly corrupted gift from Mictlantecuhtli. Boosts the power of Ghost type moves.",
        "quantity":
        "effect":
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

#Various hold
class Orbs(Enum):
    Sun_Orb = {
        "name":
        "description":
        "effect":
    }
    Moon_Orb = {
        "name":
        "description":
        "effect":
    }
    Rain_Orb = {
        "name":
        "description":
        "effect":
    }

#Shadobest  hold
class Shadow(Enum):
    Blank_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Darco_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Dread_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Earth_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Fist_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Flame_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Icicle_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Insect_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Iron_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Legend_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Meadow_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Mind_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Pixie_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Salvage_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Sky_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Splash_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Spooky_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Stone_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Toxic_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Zap_Emblem = {
        "name":
        "description":
        "quantity":
        "effect":
    }

#Nightmane hold
class Nightmane(Enum):
    Fang_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Scarab_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Dread_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Mythic_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Power_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Flame_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Icicle_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Zap_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Cute_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Plume_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Skull_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Precipice_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Leaf_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Toxic_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Mystic_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Rock_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Iron_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Wave_Earring = {
        "name":
        "description":
        "quantity":
        "effect":
    }

# Sprectrabane hold
class Spectrabane(Enum):
    Zap_Ring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Frost_Ring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Blaze_Ring = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Soak_Ring = {
        "name":
        "description":
        "quantity":
        "effect":
    }

#Fruit
class Fruit(Enum):
    Orange = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Cherry = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Peach = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Banana = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Strawberry = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Pineapple = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Pear = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Grape = {
        
    }
    Guava = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Blueberry = {
        "name":
        "description":
        "quantity":
        "effect":
    }

#Evolution
class Evolution_Marks(Enum):
    Leaf_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Flame_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Wave_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Moon_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Thunder_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Sun_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Night_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Shiny_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Dawn_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Ice_Mark = {
        "name":
        "description":
        "quantity":
        "effect":
    }

#Crystals
class Crystals(Enum):
    Red_Crystal = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Blue_Crystal = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Yellow_Crystal = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Green_Crystal = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    White_Crystal = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Black_Crystal = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Diamond = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Aquamarine = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Jade = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Turquoise = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Amathist = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Ruby = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Sapphire = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Emerald = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    Topaz = {
        "name":
        "description":
        "quantity":
        "effect":
        "catch rate":
    }
    
capture_rate = {
    "White Crystal": 0.1,
    "Yellow Crystal": 0.15
	"Black Crystal": 0.2,
	"Red Crystal": 0.3, # High chance Fire
	"Blue Crystal": 0.3, # High chance Water
	"Green Crystal": 0.3, # High chance Grass
	"Aquamarine": 0.3, # High chance Ice
	"Turquoise": 0.3, # High chance Steel or Dragon
	"Jade": 0.3, # High chance Bug
	"Topaz": 0.3, # High chance Electric 
	"Amathist": 0.3, # High chance Ghost 
	"Ruby": 0.4, # High chance Solaris 
	"Sapphire": 0.4, # High chance Lunaryx
	"Emerald": 0.4, # High chance Serpentix 
	"Diamond": 1
	}

#Key Items
class Key_items(Enum):
    Instant_Raft = {
        "name":
        "description":
        "effect":
    }
    Lantern = {
        "name":
        "description":
        "effect":
    }
    Fruit_Pouch = {
        "name":
        "description":
        "effect":
    }
    Sharp_Fang = {
        "name":
        "description":
        "effect":
    }
    Fin_Bone = {
        "name":
        "description":
        "effect":
    }
    Rod = {
        "name":
        "description":
        "effect":
    }
    Spirit_Band = {
        "name":
        "description":
        "effect":
    }

        "name":
        "description":
        "quantity":
        "effect":