import sys
import pygame
import random

#Items list
class Heal:
	potions = ["Potion", "Super Potion ", "Hyper Potion", "Max Potion", "Full Restore"]
	vending = ["Water", "Tea", "Cocoa"]
	status = ["Antidote", "Ice heal", "Burn Heal", "Paralyze Heal", "Awakening"]
	herb = ["Bitter Powder", "Energy Root", "Rivaval Herb"]
	special = ["Revive", "Max Revive", "Elixir", "Max Elixir"]
	
	def __init__(self, potions, vending, status, herb, special):
		self.potions = Potions
		self vending = Vending
		self.status = Status
		self.herb = Herb
		self.special = Special

#Boost Items		
class Boost:
 	boosts = ["Miracle Seed", "Charcoal", "Mystic Water", "Silver Powder","Sharp Beak", "Silk Scarf", "Hard Stone", "Soft Sand", "Black Glasses","Black Belt", "Twisted Spoon", "Poison Barb", "Dragon Tooth", "Metal Coat", "Nevermelt Ice", "Spell Tag", "Magnet", "Fang Collar"]
 	def __init__(self, boost):
 			self.boost = Boost
 			for boost in boost[0:17]:
 				Pymon.self.attack * 1.15 = Pymon.self.attack
 				
#Various hold
class Special:
 	special_item = ["Sun Orb", "Moon Orb", "Rain Orb"]
 	
#Shadobest  hold
class Shadow:
 emblem = ["Blank Emblem", "Darco Emblem", "Dread Emblem", "Earth Emblem", "Fist Emblem", "Flame Emblem", "Icicle Emblem", "Insect Emblem", "Iron Emblem", "Legend Emblem", "Meadow Emblem", "Mind Emblem", "Pixie Emblem", "Salvage Emblem", "Sky Emblem", "Splash Emblem", "Spooky Emblem", "Stone Emblem", "Toxic Emblem", "Zap Emblem"]

  def __init__(self, emblem):

#Nightmane hold
class Nightmane:
  earrings = ["Beast Earring","Bug Earring", "Dark Earring", "Dragon Earring", "Fighting Earring", "Fire Earring", "Ice Earring", "Electric Earring", "Fairy Earring", "Flying Earring", "Ghost Earring", "Ground Earring", "Grass Earring", "Poison Earring", "Psychic Earring", "Rock Earring", "Steel Earring", "Water Earring"]
  
  def __init__(self, earrings):
 
# Sprectrabane hold
class Spectrabane:
	ring = ["Shock Ring", "Chill Ring", "Burn Ring", "Douse Ring"]
	def __init__(self, ring):
	  
#Fruit
class Fruit:
  fruit = ["Orange", "Cherry", "Peach", "Banana", "Strawberry", "Pineapple", "Pear", "Grape", "Guava", "Blueberry"]
  def __init__(self, fruit):
	   
#Evolution
class Evolution:
  mark = ["Leaf Mark", "Flame Mark", "Water Mark", "Moon Mark", "Thunder Mark", "Sun Mark", "Night Mark", "Shiny Mark","Dawn Mark", "Ice Mark"]

#Crystals
class Crystals:
  crystals = ["Red Crystal", "Blue Crystal", "Yellow Crystal", "Green Crystal", "White Crystal", "Black Crystal", "Diamond", "Aquamarine", "Jade", "Turquoise", "Amathist", "Ruby", "Sapphire", "Emerald", "Topaz"]
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
		def get_capture_rate(crystal, pymon_type, pymon_name):
		 if crystal in ["Red Crystal", "Blue Crystal", "Green Crystal", "Aquamarine", "Turquoise", "Jade", "Topaz", "Amathist"]:
		   if pymon_type in ["Fire", "Water", "Grass", "Ice", "Dragon", "Steel", "Bug", "Electric", "Ghost"]:
		     return 0.5
		     elif crystal in ["Ruby", "Sapphire", "Emerald"]:
		       elif pymon_name in ["Solaris", "Lunaryx", "Serpentix"]:
		         return 0.5
		          else:
		            return 

#Key Items
class key_items:
	key = ["Instant Raft", "Lantern", "Quartzite", "Fruit Pouch", "Sharp Tooth", "Fin Bone", "Rod", "Spirit Band"]
	def __init__(self):

#Hold item function 
class hold:
	def __init__(self, Heal, Boost, Special, Shadow, Spectrabane, Nightmane, Fruit):