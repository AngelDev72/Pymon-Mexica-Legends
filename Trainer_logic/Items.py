import sys
import pygame
import random
from enum import Enum

#Items list
class Heal(Enum):
    Potion = {
        "name": "Potion",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Super_Potion = {
        "name": "Super Potion",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Hyper_Potion = {
        "name": "Hyper Potion",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Max_Potion = {
        "name": "Max Potion",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Full_Restore = {
        "name": "Full Restore"
        "description": "",
        "quantity": [],
        "effect": []
    }
    Simple_Water = {
        "name": "Simple Water",
        "description": "",
        "quantity": [],
        "effect":[]
    }
    Tea = {
        "name": "Tea",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Cocoa = {
        "name": "Cocoa",
        "description": "",
        "quantity": [],
        "effect": []
    }
    Antidote = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Ice_heal ={
        "name":
        "description":
        "quantity":
        "effect":
    }
    Burn_Heal = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Paralyze_Heal = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Awakening = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Bitter_Powder = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Energy_Root = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Miracle_Herb = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Revive = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Max_Revive = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Elixir = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Max_Elixir = {
        "name":
        "description":
        "quantity":
        "effect":
    }

#Boost Items		
class Boost(Enum):
    Miracle_Seed = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Honorable_Flame = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Celestial_Water = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Sensitive_Claw = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Sharp_Feather = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Soft_Huipil = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Obsidian_Stone = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Ancient_Sand = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Forbbiden_Scrolls = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Warrior_Cloth = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Gifted_Eye = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Poison_Dart = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Sharp_Fang = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Iron_Chunk = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Eternal_Ice = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Omninuos_Scroll = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Magnetic_Rock = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    Fang Collar = {
        "name":
        "description":
        "quantity":
        "effect":
    }
    
#Various hold
class Special(Enum):
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
    Blank Emblem
    Darco Emblem
    Dread Emblem
    Earth Emblem
    Fist Emblem
    Flame Emblem
    Icicle Emblem
    Insect Emblem
    Iron Emblem
    Legend Emblem
    Meadow Emblem
    Mind Emblem
    Pixie Emblem
    Salvage Emblem
    Sky Emblem
    Splash Emblem
    Spooky Emblem
    Stone Emblem
    Toxic Emblem
    Zap Emblem


#Nightmane hold
class Nightmane(Enum):
    Beast Earring
    Bug Earring
    Dark Earring
    Dragon Earring
    Fighting Earring
    Fire Earring
    Ice Earring
    Electric Earring
    Fairy Earring
    Flying Earring
    Ghost Earring
    Ground Earring
    Grass Earring
    Poison Earring
    Psychic Earring
    Rock Earring
    Steel Earring
    Water Earring
    

# Sprectrabane hold
class Spectrabane(Enum):
    Shock Ring
    Chill Ring
    Burn Ring
    Douse Ring

#Fruit
class Fruit(Enum):
    Orange
    Cherry
    Peach
    Banana
    Strawberry
    Pineapple
    Pear
    Grape
    Guava
    Blueberry

#Evolution
class Evolution(Enum):
    Leaf Mark
    Flame Mark
    Water Mark
    Moon Mark
    Thunder Mark
    Sun Mark
    Night Mark
    Shiny Mark
    Dawn Mark
    Ice Mark

#Crystals
class Crystals(Enum):
    Red Crystal
    Blue Crystal
    Yellow Crystal
    Green Crystal
    White Crystal
    Black Crystal
    Diamond
    Aquamarine
    Jade
    Turquoise
    Amathist
    Ruby
    Sapphire
    Emerald
    Topaz
    
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
class key_items(Enum):
    Instant Raft
    Lantern
    Quartzite
    Fruit Pouch
    Sharp Tooth
    Fin Bone
    Rod
    Spirit Band

        "name":
        "description":
        "quantity":
        "effect":