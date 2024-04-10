import sys
import pygame
from enum import Enum


class Mons(Enum):
  Leaflet = {
    "name" :"Leaflet",
    "type" : "Grass",
    "stats" : { 
      "Hp" : 150,
      "Attack" : 68,
      "Defense" : 70,
      "Sp_Atk" : 85,
      "Sp_Def" : 80,
      "Speed" : 118
      
    }
    
  }
  Floraleaf = {
    "name" : "Floraleaf",
    "type" : "Grass",
    "stats" : {
      "Hp" : 160,
      "Attack" 73:,
      "Defense" 75:,
      "Sp_Atk" : 93,
      "Sp_Def" : 88,
      "Speed" : 125
      
    }
    
  }
  Vinyldra = {
    "name" : "Vinyldra",
    "type" : [
      "Grass", 
      "Dragon"
      ],
    "stats" : {
      "Hp" : 170,
      "Attack" : 88,
      "Defense" : 88,
      "Sp_Atk" : 115,
      "Sp_Def" : 100,
      "Speed" : 130
      
    }
    
  }
  Flamepup = {
    "name" : "Flamepup",
    "type" : "Fire",
    "stats" : {
      "Hp" : 155,
      "Attack" : 70,
      "Defense" : 60,
      "Sp_Atk" : 65,
      "Sp_Def" : 60,
      "Speed" : 100
      
    }
    
  }
  Blazejaw = {
    "name" : "Blazejaw",
    "type" : "Fire",
    "stats" : {
      "Hp" : 165,
      "Attack" : 85,
      "Defense" : 74,
      "Sp_Atk" : 80,
      "Sp_Def" : 74,
      "Speed" : 115
      
    }
    
  }
  Inferchomp = {
    "name" : "Inferchomp",
    "type" : [
      "Fire", 
      "Beast"
      ],
    "stats" : {
      "Hp" : 175,
      "Attack" : 100,
      "Defense" : 88,
      "Sp_Atk" : 95,
      "Sp_Def" : 93,
      "Speed" : 123
      
    }
    
  }
  Mudlope {
    "name" : "Mudlope",
    "type" : "Water",
    "stats" : {
      "Hp" : 163,
      "Attack" : 73,
      "Defense" : 75,
      "Sp_Atk" : 75,
      "Sp_Def" : 78,
      "Speed" : 90
      
    }
    
  }
  Mudskipper = {
    "name" : "Mudskipper",
    "type" : "Water",
    "stats" : {
      "Hp" : 174,
      "Attack" : 83,
      "Defense" : 85,
      "Sp_Atk" : 85,
      "Sp_Def" : 88,
      "Speed" : 105
      
    }
    
  }
  Quakelotl {
    "name" : "Quakelotl",
    "type" : [
      "Water",
      "Ground"
      ],
    "stats" : {
      "Hp" : 190,
      "Attack" : 100,
      "Defense" : 95,
      "Sp_Atk" : 103,
      "Sp_Def" : 100,
      "Speed" : 115
      
    }
    
  }
  Breezowl = {
    "name" : "Breezowl",
    "type" : "Flying",
    "stats" : {
      "Hp" : 154,
      "Attack" : 65,
      "Defense" : 65,
      "Sp_Atk" : 60,
      "Sp_Def" : 63,
      "Speed" : 100
      
    }
    
  }
  Gustwing = {
    "name" : "Gustwing",
    "type" : "Flying",
    "stats" : {
      "Hp" : 162,
      "Attack" : 75,
      "Defense" : 73,
      "Sp_Atk" : 73,
      "Sp_Def" : 75,
      "Speed" : 118
      
      }
    
  }
  Cyclohawk = {
    "name" : "Cyclohawk",
    "type" : [
      "Flying",
      "Electric"
      ],
    "stats" : {
      "Hp" : 172,
      "Attack" : 90,
      "Defense" : 85,
      "Sp_Atk" : 100,
      "Sp_Def" : 88,
      "Speed" : 140
      
    }
    
  }
  Rochling = {
    "name" : "Rochling",
    "type" : "Bug",
    "stats" : {
      "Hp" : 130,
      "Attack" : 65,
      "Defense" : 65,
      "Sp_Atk" : 60,
      "Sp_Def" : 65,
      "Speed" : 105
      
    }
    
  }
  Shedroch = {
    "name" : "Shedroch",
    "type" : "Bug",
    "stats" : {
      "Hp" : 160,
      "Attack" : 80,
      "Defense" : 50,
      "Sp_Atk" : 75,    
      "Sp_Def" : 50,
      "Speed" : 118
      
    }
    
  }
  Beheroch = {
    "name" : "Beheroch",
    "type" : [
      "Bug", 
      "Dark"
      ],
    "stats" : {
      "Hp" : 195,
      "Attack" : 115,
      "Defense" : 110,
      "Sp_Atk" : 110,
      "Sp_Def" : 110,
      "Speed" : 135
      
    }
    
  }
  Kickora = {
    "name" : "Kickora",
    "type" : [
      "Fighting",
      "Flying"
      ],
    "stats" : {
      "Hp" : 175,
      "Attack" : 100,
      "Defense" : 95,
      "Sp_Atk" : 85,
      "Sp_Def" : 88,
      "Speed" : 115
      
    }
    
  }
  Siphonbite = {
    "name" : "Siphonbite",
    "type" : "Dark",
    "stats" : {
      "Hp" : 158,
      "Attack" : 70,
      "Defense" : 85,
      "Sp_Atk" : 70,
      "Sp_Def" : 85,
      "Speed" : 100
      
    }
    
  }
  Souldevoir = {
    "name" : "Souldevoir",
    "type" : [
      "Dark",
      "Beast"
    ],
    "stats" : {
      "Hp" : 190,
      "Attack" : 85,
      "Defense" : 100,
      "Sp_Atk" : 95,
      "Sp_Def" : 100,
      "Speed" : 120
      
    }
    
  }
  Essenfest = {
    "name" : "Essenfest",
    "type" : [
      "Dark",
      "Beast"
      ],
    "stats" : {
      "Hp" : 180,
      "Attack" : 100,
      "Defense" : 98,
      "Sp_Atk" : 90,
      "Sp_Def" : 95,
      "Speed" : 122
      
    }
    
  }
  Sparkitt = {
    "name" : "Sparkitt",
    "type" : "Electric",
    "stats" : {
      "Hp" : 155,
      "Attack" : 75,
      "Defense" : 68,
      "Sp_Atk" : 80,
      "Sp_Def" : 80,
      "Speed" : 115
      
    }
    
  }
  Joltflash = {
    "name" : "Joltflash",
    "type" : "Electric",
    "stats" : {
      "Hp" : 175,
      "Attack" : 85,
      "Defense" : 80,
      "Sp_Atk" : 105,
      "Sp_Def" : 110,
      "Speed" : 130
      
    }
    
  }
  Luminara {
    "name" : "Luminara",
    "type" : [
      "Water",
      "Dark"
      ],
    "stats" : {
      "Hp" : 170,
      "Attack" : 100,
      "Defense" : 88,
      "Sp_Atk" : 95,
      "Sp_Def" : 93,
      "Speed" : 110
      
    }
    
  }
  Thundhoof = {
    "name" : "Thundhoof",
    "type" : [
      "Electric",
      "Fairy"
      ],
    "stats" : {
      "Hp" : 175,
      "Attack" : 93,
      "Defense" : 95,
      "Sp_Atk" : 100,
      "Sp_Def" : 92,
      "Speed" : 110
      
    }
    
  }
  Swoopscar = {
    "name" : "Swoopscar",
    "type" : [
      "Bug",
      "Flying"
      ],
    "stats" : {
      "Hp" : 170,
      "Attack" : 95,
      "Defense" : 90,
      "Sp_Atk" : 90,
      "Sp_Def" : 100,
      "Speed" : 102
    
    }
    
  }
  Sandove = {
    "name" : "Sandove",
    "type" : [
      "Ground",
      "Flying"
      ],
    "stats" : {
      "Hp" : 165,
      "Attack" : 98,
      "Defense" : 88,
      "Sp_Atk" : 92,
      "Sp_Def" : 93,
      "Speed" : 105
      
    }
    
  }
  Dunebeak = {
    "name" : "Dunebeak",
    "type" : [
      "Ground",
      "Flying"
      ],
    "stats" : {
      "Hp" : 180,
      "Attack" : 105,
      "Defense" : 95,
      "Sp_Atk" : 107,
      "Sp_Def" : 99,
      "Speed" : 112
    
    }
    
  }
  Mossclaw = {
    "name" : "Mossclaw",
    "type" : "Grass",
    "stats" : {
      "Hp" : 168,
      "Attack" : 83,
      "Defense" : 85,
      "Sp_Atk" : 83,
      "Sp_Def" : 92,
      "Speed" : 102
      
    }
    
  }
  Thornpaw = {
    "name" : "Thornpaw",
    "type" : "Grass",
    "stats" : {
      "Hp" : 183,
      "Attack" : 110,
      "Defense" : 90,
      "Sp_Atk" : 98,
      "Sp_Def" : 102,
      "Speed" : 112
      
    }
    
  }
  Spectrora = {
    "name" : "Spectrora",
    "type" : [
      "Ghost",
      "Flying"
      ],
    "stats" : {
      "Hp" : 187,
      "Attack" : 91,
      "Defense" : 90,
      "Sp_Atk" : 105,
      "Sp_Def" : 102,
      "Speed" : 112
      
    }
    
  }
  Tulehag = {
    "name" : "Tulehag",
    "type" : [
      "Ghost",
      "Grass"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Mistlion = {
    "name" : "Mistlion",
    "type" : "Ice",
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Hazeleo = {
    "name" : "Hazeleo",
    "type" : [
      "Ice",
      "Steel"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Stormlion = {
    "name" : "Stormlion"
    "type" : "Electric",
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Roarstom {
    "name" : "Roarstom",
    "type" : [
      "Electric",
      "Steel"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Floracorn = {
    "name" : "Floracorn",
    "type" : [
      "Fairy",
      "Flying"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Verdantus = {
    "name" : "Verdantus",
    "type" : [
      "Grass",
      "Poison"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Electray = {
    "name" : "Electray",
    "type" : [
      "Electric",
      "Water"
      ],
    "stats" :{
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Frostpaw = {
    "name" : "Frostpaw",
    "type" : "Ice",
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Hailclaw = {
    "name" : "Hailclaw",
    "type" : "Ice",
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Frostcub = {
    "name" : "Frostcub",
    "type" : [
      "Ice",
      "Water"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Chillber = {
      "name" : "Chillber",
      "type" : [
        "Ice",
        "Water"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
  Polarclaw = {
    "name" : "Polarclaw",
    "type" : [
      "Ice",
      "Water"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Terrathorn = {
    "name" : "Terrathorn",
    "type" : [
      "Grass",
      "Ground"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Searageist = {
    "name" : "Searageist",
    "type" : [
      "Ghost",
      "Fire"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Shadeimp = {
    "name" : "Shadeimp",
    "type" : [
      "Ghost",
      "Rock"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
    46: {
      "name" : "Brawlion",
      "type" : [
        "Fighting",
        "Fire"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    47: {
      "name" : "Scorpinch",
      "type" : [
        "Fire",
        "Poison"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    48: {
      "name" : "Toxinip",
      "type" : [
        "Fire",
        "Poison"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    49: {
      "name" : "Pyrotox",
      "type" : [
        "Fire",
        "Poison"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    50: {
      "name" : "Fangrend",
      "type" : [
        "Fighting",
        "Ice"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    51: {
      "name" : "Effigy",
      "type" : "Ghost",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    52: {
      "name" : "Vexdoll",
      "type" : [
        "Ghost",
        "Psychic"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    53: {
      "name" : "Vexweav",
      "type" : [
        "Ghost",
        "Dark"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    54: {
      "name" : "Aqualith",
      "type" : "Water",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    55: {
      "name" : "Aquadon",
      "type" : [
        "Water",
        "Beast"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    56: {
      "name" : "Plesyodrake",
      "type" : [
        "Dragon",
        "Beast"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    57: {
      "name" : "Veloscale",
      "type" : "Grass",
      "stats" {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    58: {
      "name" : "Predaptor",
      "type" : [
        "Grass",
        "Beast"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    59: {
      "name" : "Velocydrake",
      "type" : [
        "Dragon",
        "Beast"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    60: {
      "name" : "Sprinkleaf",
      "type" : "Fairy",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    61: {
      "name" : "Glitterose",
      "type" : [
        "Fairy",
        "Psychic"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    62: {
      "name" : "Pebbleon",
      "type" : "Rock",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    63: {
      "name" : "Granitear",
      "type" : [
        "Rock",
        "Ground"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    64: {
      "name" : "Crysantis",
      "type" : [
        "Ice",
        "Bug"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    65: {
      "name" : "Slapshling",
      "type" : "Water",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    66: {
      "name" : "Wavelet",
      "type" : [
        "Water",
        "Psychic"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    67: {
      "name" : "Venofang",
      "type" : "Poison",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    68: {
      "name" : "Serpentide",
      "type" : [
        "Poison",
        "Dragon"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    69: {
      "name" : "Zyephblade",
      "type" : [
        "Steel",
        "Rock"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    70: {
      "name" : "Aurostride",
      "type" : [
        "Ice",
        "Rock"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    71: {
      "name" : "Embstrike",
      "type" : [
        "Fire",
        "Rock"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    72: {
      "name" : "Webbing",
      "type" : [
        "Poison",
        "Dark"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    73: {
      "name" : "Plaguefly",
      "type" : [
        "Poison",
        "Flying"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    74: {
      "name" : "Whimsiren",
      "type" : [
        "Fairy",
        "Steel"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    75: {
      "name" : "Glailhorn",
      "type" : "Ice",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    76: {
      "name" : "Frosthorn",
      "type" : [
        "Ice",
        "Steel"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    77: {
      "name" : "Duskbat",
      "type" : [
        "Dark",
        "Flying"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    78: {
      "name" : "Eclipsbat",
      "type" : [
        "Dark",
        "Flying"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    79: {
      "name" : "Xtabay",
      "type" : [
        "Fairy",
        "Grass"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    80: {
      "name" : "Spectrabane",
      "type" : [
        "Ghost",
        "Fairy"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    81: {
      "name" : "Nightmane",
      "type" : [
        "Ghost",
        "Fire"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    82: {
      " name" : "Tuskdrill",
      "type" : [
        "Ground",
        "Steel"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    83: {
      "name" : "Sylphora",
      "type" : "Fairy",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    84: {
      "name" : "Galepetal",
      "type" : [
        "Fairy",
        "Psychic"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    85: {
      "name" : "Sylvantrix",
      "type" : [
        "Fairy",
        "Psychic"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    86: {
      "name" : "Teratot",
      "type" : [
        "Ground",
        "Rock"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    87: {
      "name" : "Terraforge",
      "type" : [
        "Ground",
        "Grass"
        ],  
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    88: {
      "name" : "Gaialith",
      "type" : [
        "Ground",
        "Psychic"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    89: {
      "name" : "Teraguard",
      "type" : "Ground",
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    90: {
      "name" : "Fistquake",
      "type" : [
        "Ground",
        "Fighting"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    91: {
      "name" : "Tectoknight",
      "type" : [
        "Fighting",
        "Steel"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    92: {
      "name" : "Earthrend",
      "type" : [
        "Ground",
        "Dragon"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    93: {
      "name" : "Terrascale",
      "type" : [
        "Dragon",
        "Steel"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    94: {
      "name": "Astralynx",
      "type" : [
        "Psychic",
        "Fighting"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    95: {
      "name" : "Novastrike",
      "type" : [
        "Fire",
        "Flying"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
    96: {
      "name" : "Feralstorm",
      "type" : [
        "Beast",
        "Electric"
        ],
      "stats" : {
        "Hp" : ,
        "Attack" : ,
        "Defense" : ,
        "Sp_Atk" : ,
        "Sp_Def" : ,
        "Speed" :
        
      }
      
    }
  Lunaryx {
    "name" : "Lunaryx",
    "type" : [
      "Ice",
      "Dark"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Solaris = {
    "name": "Solaris",
    "type" : [
      "Fire",
      "Psychic"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Serpentix = {
    "name" : "Serpentix",
    "type" : [
      "Dragon",
      "Fairy"
      ],
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  Shadow = {
    "name" : "Shadow",
    "type" : "Ghost",
    "stats" : {
      "Hp" : ,
      "Attack" : ,
      "Defense" : ,
      "Sp_Atk" : ,
      "Sp_Def" : ,
      "Speed" :
      
    }
    
  }
  }