import pygame as pg
import sys
from enum import Enum

class Attack(Enum):
  def physical(self):
    Veno_Drop = {
        "name": "Veno Drop",
        "type": ,
        "description": "",
        "power": 90,
        "accuracy": 85,
        "usage": 15,
      },
    Earthquake = {
        "name": "Earthquake",
        "type": ,
        "description": ,
        "power": 100,
        "accuracy": 1,
        "usage": 15,
        "effect": 
      },
    Scorch = {
        "name": "Scorch",
        "type": ,
        "description": ,
        "power": 50,
        "accuracy": 80,
        "usage": 20,
        "effect": 
      },
    Chop = {
        "name": "Chop",
        "type": "Fighting",
        "description": ,
        "power": 75,
        "accuracy": 85,
        "usage": 15,
      },
    Wing_Strike = {
        "name": "Wing Strike",
        "type": ,
        "description": ,
        "power": 70,
        "accuracy": 90,
        "usage": 15,
      },
    Leech = {
        "name": "Leech",
        "type": "Bug",
        "description": ,
        "power": 55,
        "accuracy": 85,
        "usage": 20,
        "effect": #restores 1/8 the damage inflicted 
      },
    Bite = {
        "name": "Bite",
        "type": ,
        "description": ,
        "power": 65,
        "accuracy": 90,
        "usage": 15,
      },
    Water_Stride = {
        "name": "Water Stride",
        "type": ,
        "description": "The user charges at the foe with enough force to walk over water.",
        "power": 95,
        "accuracy": 90,
        "usage": 15,
      },
    Draco_Slash = {
        "name": "Draco Slash",
        "type": ,
        "description": ,
        "power": 95,
        "accuracy": 90,
        "usage": 15,
      },
    Flame_Rush = {
        "name": "Flame Rush",
        "type": ,
        "description": ,
        "power": 100,
        "accuracy": 85,
        "usage": 10,
      },
    Frost_Rush = {
        "name": "Frost Rush",
        "type": ,
        "description": ,
        "power": 100,
        "accuracy": 85,
        "usage": 10,
      },
    Avalanche = {
        "name": "Avalanche",
        "type": ,
        "description": ,
        "power": 95,
        "accuracy": 90,
        "usage": 15,
        "effect": 
      },
    Veno_Fang = {
        "name": "Veno Fang",
        "type": ,
        "description": ,
        "power": 70,
        "accuracy": 90,
        "usage": 15,
      },
    Stone_Blade = {
        "name": "Stone Blade",
        "type": ,
        "description": ,
        "power": 85,
        "accuracy": 80,
        "usage": 15,
      },
    Frost_Blade = {
        
    }
    
  def special(self):
    sp_attks = {
      1: {
        "name": "Fright",
        "type": Ghost,
        "description": ,
        "power": 50,
        "accuracy": 100,
        "usage": 15,
      },
      2: {
        "name":
        "type":
        "description": 
        "power":
        "accuracy":
        "usage":
      }
    }
  
class Defense(Enum):
  def defend(self):
    barriers = {
      
    }

class Status(Enum):
  def increase(self):
    boosts = {
      
    }
    
  def lower(self):
    lower = {
      
    }
    
  
class Stats(Enum):
  def condition (self):
    Burn = {
        "name": "Burn",
        "effect": #deals damage every 30s, reduces attack and may cause flinch(if flinched, 15s deley to recover)
        }
    Freeze = {
        "name": "Freeze",
        "effect": #freezes the target for certian amount of time, after defrost target's speed falls 30s
    }
    Paralyze = {
        "name": "Paralyze",
        "effect": #paralizes the target, low chance to attack
    }
    Confusion = {
        "name": "Confused",
        "effect": #swaps the movementent keys for 60s, 50% chance to hit itself 
    }
    Sleep = {
        "name": "Sleep",
        "effect": #makes the target fall into a deep sleep, 10% to awake while in battle. 90s to wake up after battle.
    }