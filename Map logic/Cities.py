import sys
import pygame as pg

class Map:
  Cities = {
    1: {
     "name": "Tenochtitlán",
     "theme": 
      
    },
    2: {
     "name": "Tlalocan",
     "theme": 
      
    },
    3: {
     "name": "Teotihuacán",
     "theme": 
      
    },
    4: {
     "name": "Xochimilco",
     "theme": 
      
    },
    5: {
     "name": "Chichén Itzá",
     "theme": 
      
    },
    6: {
     "name": "Tlatelolco",
     "theme":
      
    },
    7: {
     "name": "Cuzco",
     "theme": 
      
    },
    8: {
     "name": "Tenayuca",
     "theme" :
      
    }
  
  }
  
  Towns = {
    1: {
      "name": "Tepoztlán",
    "theme": 
      
    },
    2: {
      "name": "Coatlinchán",
      "theme": 
      
    },
    3: {
      "name": "Malinalco",
      "theme": 
    },
    4: {
      "name": "Tepotzotlán",
      "theme": 
      
    },
    5: {
      "name": "Xochicalco",
      "theme": 
      
    },
    6: {
      "name": "Mitla",
      "theme": 
      
    },
    7: {
      "name": "Izamal",
      "theme:" 
      
    },
    8: {
      "name": "Paquimé",
      "theme": 
      
    },
    9: {
      "name": "Tulum",
      "theme": 
      
    },
    10: {
      "name": "Zacatecas"
      "theme": 
      
    },
    
  }

  Main_Routes = {
    1: {
      "name":"Blossom Path",
      "theme": 
      
    },
    2: {
      "Misty River",
      "theme":
    },
    3: {
      "Ancient Trail",
      "theme":
    },
    4: {
      "Whispering Woods",
      "theme":
    },
    5: {
      "Dragon's Pass",
      "theme":
    },
    6: {
      "Sunset Boulevard",
      "theme":
    },
    7: {
      "Frostpeak Path",
      "theme":
    },
    8: {
      "Silent Ruins",
      "theme":
    },
    9: {
      "Crystal Cascades",
      "theme":
    },
    10: {
      "Starlight Path"
      "theme":
    }
    
  }

  Secondary_routes = {
    1: {
      "Isle of Dolls",
      "theme":
    },
    2: {
      "Ember Ridge",
      "theme":
    },
    3: {
      "Enchanted Grove",
      "theme":
    },
    4: {
      "Coral Reef Path",
      "theme":
    },
    5: {
      "Celestial Bridge",
      "theme":
    }
    
  }

  Caves = {
    1: {
      "Secret Chasm",
      "theme":
    },
    2: {
      "Unexplored Abyss",
      "theme":
    },
    3: {
      "Enigmatic Passage",
      "theme":
    },
    4: {
      "Challenge Cave",
      "theme":
    },
    5: {
      "Quetzalcoatl Ruins",
      "theme":
    }
    
  }

#Buildings
class Temple:
  Temples = {
    1: {
      "City": "Tenochtitlán",
      "Sun Temple",
      "Type": [
        "Fire",
        "Fighting"
      ],
      "Leader": "Tonatiuh"
      
    },
    2: {
      "City": "Tlalocan",
      "Rain Temple", 
      "Type": [
        "Water", 
        "Electric"
        ], 
        "Leader": "Atl"
      
    },
    3: {
      "City": "Teotihuacán",
      "Pyramid Temple",
      "Type": [
        "Rock",
        "Ground"
        ], 
        "Leader": "Itzpapalotl"
      
    },
    4: {
      "City": "Xochimilco",
      "Gardens Temple", 
      "Type": [
        "Grass", 
        "Poison"
        ],
        "Leader": "Xochiquetzal"
      
    },
    5: {
      "City": "Chichén Itzá",
      "Snake Temple", 
      "Type": [
        "Dragon", 
        "Steel"
        ], 
        "Leader": "Quetzalcoatl"
      
    },
    6: {
      "City": "Tlatelolco",
      " Plazas Temple", 
      "Type": [
        "Fairy", 
        "Psychic"
        ], 
        "Leader": "Cihuacoatl"
      
    },
    7: {
      "City": "Cuzco",
      "Mountain Temple", 
      "Type": [
        "Beast", 
        "Ice"
        ],
        "Leader": "Inti"
      
    },
    8: {
      "City": "Tenayuca",
      "Ruins Temple", 
      "Type": [
        "Dark",
        "Ghost"
        ], 
        "Leader": "Tlalocatl"
      
    }
    
  }