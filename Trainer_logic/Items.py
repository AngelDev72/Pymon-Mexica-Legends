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
class Evolution(Enum):
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
class key_items(Enum):
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