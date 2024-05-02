import pygame as pg
import sys
from enum import Enum

class Attack(Enum):
    def physical(self):
        Earthquake = {
            "name": "Earthquake",
            "type": ,
            "description": ,
            "power": 100,
            "accuracy": 1,
            "usage": 15,
            "effect": #hits all targets on the field except Flying types
            
        }
        Chop = {
            "name": "Chop",
            "type": "Fighting",
            "description": ,
            "power": 75,
            "accuracy": 85,
            "usage": 15,
            
        }
        Wing_Strike = {
            "name": "Wing Strike",
            "type": ,
            "description": ,
            "power": 70,
            "accuracy": 90,
            "usage": 15,
            
        }
        Leech = {
            "name": "Leech",
            "type": "Bug",
            "description": ,
            "power": 55,
            "accuracy": 85,
            "usage": 20,
            "effect": #restores 1/8 the damage inflicted 
      }
        Bite = {
            "name": "Bite",
            "type": ,
            "description": ,
            "power": 65,
            "accuracy": 90,
            "usage": 15,
            "effect": #20% chance to make the target flinch
            
        }
        Water_Stride = {
            "name": "Water Stride",
            "type": ,
            "description": [
                "The user charges at the foe with enough force to walk over water."
                ],
            "power": 95,
            "accuracy": 90,
            "usage": 15,
            
        }
        Draco_Slash = {
            "name": "Draco Slash",
            "type": ,
            "description": ,
            "power": 95,
            "accuracy": 90,
            "usage": 15,
            
        }
        Flame_Rush = {
            "name": "Flame Rush",
            "type": ,
            "description": ,
            "power": 100,
            "accuracy": 85,
            "usage": 10,
            "effect": #30% chance to inlfict a Burn
        }
        Frost_Rush = {
            "name": "Frost Rush",
            "type": ,
            "description": ,
            "power": 100,
            "accuracy": 85,
            "usage": 10,
            "effect": #30% chance to Freeze the target
        }
        Avalanche = {
            "name": "Avalanche",
            "type": ,
            "description": ,
            "power": 95,
            "accuracy": 90,
            "usage": 15,
            "effect": #changes type depanding on the terrain. 30% chance to make the target flinch
      }
        Veno_Fang = {
            "name": "Veno Fang",
            "type": ,
            "description": ,
            "power": 70,
            "accuracy": 90,
            "usage": 15,
            "effect": #15% chance to Poison the target
      }
        Stone_Blade = {
        "name": "Stone Blade",
        "type": ,
        "description": ,
        "power": 85,
        "accuracy": 80,
        "usage": 15,
      }
        Frost_Blade = {
        "name": "Frost Blade",
        "type": ,
        "description": ,
        "power": 85,
        "accuracy": 80,
        "usage": 15,
        "effect": #15% chance to freeze the target
    }
        Vine_Lash = {
        "name": "Vine Lash",
        "type": ,
        "description": ,
        "power": 75,
        "accuracy": 90,
        "usage": 20,
        "effect": #hits the target within a certain range
    }
        Headbutt = {
        "name": "Headbutt",
        "type": ,
        "description": ,
        "power": 85,
        "accuracy": 80,
        "usage": 20,
        "effect": #25% chance to make the target flinch
        
    }
        Leaf_Scythe = {
        "name": "Leaf Scythe",
        "type": ,
        "description": ,
        "power": 90,
        "accuracy": 85,
        "usage": 15
    }
        Ice_Fist = {
        "name": "Ice Fist",
        "type": ,
        "description": ,
        "power": 80,
        "accuracy": 80,
        "usage": 15,
        "effect": #20% chance to Freeze the target
    }
        Scratch = {
        "name": "Scratch",
        "type": ,
        "description": ,
        "power": 40,
        "accuracy": 80,
        "usage": 20
    }
        Tackle = {
        "name": "Tackle",
        "type": ,
        "description": ,
        "power": 40,
        "accuracy": 80,
        "usage": 20
    }
        Multi_Scratch = {
        "name": "Multi Scratch",
        "type": ,
        "description": ,
        "power": 20,
        "accuracy": 80,
        "usage": 25,
        "effect": #may hit the target up to 6 times
    }
        Shatter = {
        "name": "Shatter",
        "type": "Fighting",
        "description": ,
        "power": 80,
        "accuracy": 80,
        "usage": 15,
        "effect": #destroys special barriers and cancels their effects
    }
        

    def special(self):
        Fright= {
            "name": "Fright",
            "type": Ghost,
            "description": ,
            "power": 50,
            "accuracy": 1,
            "usage": 15,
            "effect": #25% chance to make the target flinch
        }
        Scorch = {
            "name": "Scorch",
            "type": ,
            "description": ,
            "power": 50,
            "accuracy": 80,
            "usage": 20,
            "effect": #15% to inflict a Burn, hits in a certain range
            
        }
        Veno_Drop = {
            "name": "Veno Drop",
            "type": ,
            "description": "",
            "power": 90,
            "accuracy": 85,
            "usage": 15,
            "effect": #20% chance to Poison the target
        }
        Flame_Gulf = {
            "name": "Falme Gulf",
            "type": ,
            "description": ,
            "power": 95,
            "accuracy": 90,
            "usage": 15,
            "effect": #Hits in a certian range of the field, 18% chance to Burn the target. 
        }
        Cyclone = {
            "name": "Cyclone",
            "type": ,
            "description": ,
            "power": 100,
            "accuracy": 1,
            "usage": 10,
            "effect": #hits everything on the field except the user, 40% chanche to cuase Confusion
        }
        Twister = {
            "name": "Twister",
            "type": "Dragon",
            "description": ,
            "power": 70,
            "accuracy": 90,
            "usage": 15,
            "effect": # draws the nearest target in the attack, 20% chance of Confusion
        }
        Aurora_Blast = {
            "name": "Aurora Blast",
            "type": "Ice",
            "description": ,
            "power": 75,
            "accuracy": 90,
            "usage": 15,
            "effect": #15% chance to lower the targets Special Attack. hits in a certain range.
        }
        Ice_Ray = {
            "name": "Ice Ray",
            "type": "Ice",
            "description": ,
            "power": 90,
            "accuracy": 90,
            "usage": 10,
            "effect": #freezes the target, hits in a certain range
        }

class Defense(Enum):
    def shield(self):
        Protect = {
            "name": "Protect",
            "type": ,
            "description": [
                "Creates an energy field to protect the user from attaks and effects"],
            "usage": 10,
            "effect": #negates damage, stat reduction or status inflection.
            
        }

class Stats(Enum):
    def increase(self):
        Howl = {
            "name": "Howl",
            "type": ,
            "description": ,
            "usage": 20,
            "effect": #raises the users attack 10%
            }
        Reflect = {
            "name": "Reflect",
            "type": ,
            "description": ,
            "usage": 20,
            "effect": #raises the users defense 10%
            }
        Aura_Veil = {
            "name": "Aura Veil",
            "type": "Fairy",
            "description": ,
            "usage": 20,
            "effect": #protects the user from stat and status conditions
        }
        Light_Wall = {
            "name": "Light Wall",
            "type": ,
            "description": ,
            "usage": 20,
            "effect":#raises the users Special Defense
        }

    def lower(self):
        Growl = {
            "name": "Growl",
            "type": ,
            "description": ,
            "accuracy": 95,
            "usage": 20,
            "effect": #reduces the targets attack 10%
            }
        Sand_Hurl = {
            "name": "Sand Hurl",
            "type": "Ground",
            "description": ,
            "accuracy": 90,
            "usage": 20,
            "effect": #lowers the targets accuracy 10%, hits in a certain range
            
        }


class Status(Enum):
    def condition (self):
        Burn = {
            "name": "Burn",
            "effect": #deals damage every 30s, reduces attack and may cause flinch(if flinched, 15s deley to recover)
            }
        Freeze = {
            "name": "Freeze",
            "effect": #freezes the target for 50s, after defrost target's speed falls 30s
            }
        Paralyze = {
            "name": "Paralyze",
            "effect": #paralizes the target, low chance to attack. Speed falls 10%
            }
        Poison = {
            "name": "Poison",
            "effect": #Target losess HP every 10s in battle. Outside battle losess HP every 6 steps.
        }
        Confusion = {
            "name": "Confused",
            "effect": #swaps the movementent keys for 60s, 50% chance to hit itself
            }
        Sleep = {
            "name": "Sleep",
            "effect": #makes the target fall into a deep sleep, 10% to awake while in battle. 90s to wake up after battle.
            }

            "name": "",
            "type": ,
            "description": ,
            "power": ,
            "accuracy": ,
            "usage": ,

            "name": "",
            "type": ,
            "description": ,
            "accuracy": ,
            "usage": ,
            "effect":