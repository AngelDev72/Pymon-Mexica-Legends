import sys
import pygame as pg
from enum import Enum

class Map(Enum):
    #cities
    Tenochtitlan = {
        "name": "Tenochtitlán",
        "theme": 
        
    },
    Tlalocan = {
        "name": "Tlalocan",
        "theme": 
        
    },
    Teotihuacan = {
        "name": "Teotihuacán",
        "theme": 
        
    },
    Xochimilco = {
        "name": "Xochimilco",
        "theme": 
        
    },
    Chichen_Itza = {
        "name": "Chichén Itzá",
        "theme": 
        
    },
    Tlatelolco = {
        "name": "Tlatelolco",
        "theme":
        
    },
    Cuzco = {
        "name": "Cuzco",
        "theme": 
        
    },
    Tenayuca = {
        "name": "Tenayuca",
        "theme" :
        
    }
    
    #towns
    Tepoztlan = {
        "name": "Tepoztlán",
        "theme": 
      
    }
    Coatlinchan = {
        "name": "Coatlinchán",
        "theme": 
        
    }
    Malinalco = {
        "name": "Malinalco",
        "theme": 
        
    }
    Tepotzotlan = {
        "name": "Tepotzotlán",
        "theme": 
        
    }
    Xochicalco = {
        "name": "Xochicalco",
        "theme": 
        
    }
    Mitla = {
        "name": "Mitla",
        "theme": 
        
    }
    Izamal = {
        "name": "Izamal",
        "theme:" 
        
    }
    Paquime = {
        "name": "Paquimé",
        "theme": 
        
    }
    Tulum = {
        "name": "Tulum",
        "theme": 
        
    }
    Zacatecas = {
        "name": "Zacatecas"
        "theme": 
        
    }
    
    # Main Routes
    Blossom_Path = {
        "name":"Blossom Path",
        "theme": 
        
    }
    Misty_River = {
        "Misty River",
        "theme":
        
    }
    Ancient_Trial = {
        "Ancient Trail",
        "theme":
        
    }
    Whispering_Woods = {
        "Whispering Woods",
        "theme":
        
    }
    Dragons_Pass = {
        "Dragons Pass",
        "theme":
        
    }
    Sunset_Boulevard = {
        "Sunset Boulevard",
        "theme":
        
    }
    Frostpeak_Path = {
        "Frostpeak Path",
        "theme":
        
    }
    Silent_Ruins = {
        "Silent Ruins",
        "theme":
        
    }
    Crystal_Cascades = {
        "Crystal Cascades",
        "theme":
        
    }
    Starlight_Path = {
        "Starlight Path"
        "theme":
        
    }
    
  # Secondary Routes
    Isle_of_Dolls = {
        "Isle of Dolls",
        "theme":
        
    }
    Ember_Ridge = {
        "Ember Ridge",
        "theme":
        
    }
    Enchanted_Gorve = {
        "Enchanted Grove",
        "theme":
        
    }
    Coral_Reef_Path = {
        "Coral Reef Path",
        "theme":
        
    }
    Celestial_Bridge = {
        "Celestial Bridge",
        "theme":
        
    }
    
    # Caves
    Secret_Chasm {
        "Secret Chasm",
        "theme":
        
    }
    Unexplored_Abyss = {
        "Unexplored Abyss",
        "theme":
        
    }
    Enigmatic_Passage = {
        "Enigmatic Passage",
        "theme":
        
    }
    Challenge_Cave = {
        "Challenge Cave",
        "theme":
        
    }
    Quetzalcoatl_Ruins = {
        "Quetzalcoatl Ruins",
        "theme":
        
    }
    
    
#Buildings
class Temple(Enum):
    # Tenochtitlan
    Sun_Temple = {
        "name": "Sun Temple",
        "Type": [
            "Fire",
            "Fighting"
            ],
        "Leader": "Tonatiuh"
        
    }
    # Tlalocan
    Rain_Temple = {
        "name": "Rain Temple", 
        "Type": [
            "Water", 
            "Electric"
            ], 
        "Leader": "Atl"
        
    }
    # Teotihuacan
    Pyramid_Temple = {
        "name": "Pyramid Temple",
        "Type": [
            "Rock",
            "Ground"
            ], 
        "Leader": "Itzpapalotl"
        
    }
    #Xochimilco
    Gardens_Temple = {
        "name": "Gardens Temple", 
        "Type": [
            "Grass", 
            "Poison"
            ],
        "Leader": "Xochiquetzal"
        
    }
    # Chichen Itza
    Snake_Temple = {
        "name": "Snake Temple", 
        "Type": [
            "Dragon", 
            "Steel"
            ], 
        "Leader": "Quetzalcoatl"
        
    }
    #Tlatelolco
    Plazas_Temple = {
        "name": "Plazas Temple", 
        "Type": [
            "Fairy", 
            "Psychic"
            ], 
        "Leader": "Cihuacoatl"
        
    }
    #Cuzco
    Mountain_Temple = {
        "name": "Mountain Temple", 
        "Type": [
            "Beast", 
            "Ice"
            ],
        "Leader": "Inti"
        
    }
    #Tenayuca
    Ryins_Temple = {
        "name": "Ruins Temple", 
        "Type": [
            "Dark",
            "Ghost"
            ], 
        "Leader": "Tlalocatl"
        
    }