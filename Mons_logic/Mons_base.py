import sys
import pygame
from enum import Enum
from Stats import Stats, Types

class Mons(Enum):
    Leaflet = {
        "name": "Leaflet",
        "type": "Grass",
        "level": [],
        "stats": { 
            "Hp": 160,
            "Attack": 78,
            "Defense": 80,
            "Sp_Atk": 85,
            "Sp_Def": 90,
            "Speed": 118
            
        }
        
    }
    Floraleaf = {
        "name: "Floraleaf",
        "type": "Grass",
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack":  83,
            "Defense": 85,
            "Sp_Atk": 100,
            "Sp_Def": 98,
            "Speed": 125
            
        }
        
    }
    Vinyldra = {
        "name": "Vinyldra",
        "type": [
            "Grass", 
            "Dragon"
            ],
            "level": [],
        "stats": {
            "Hp": 180,
            "Attack": 98,
            "Defense": 98,
            "Sp_Atk": 120,
            "Sp_Def": 110,
            "Speed": 130
            
        }
        
    }
    Flamepup = {
        "name": "Flamepup",
        "type": "Fire",
        "level": [],
        "stats": {
            "Hp": 165,
            "Attack": 78,
            "Defense": 60,
            "Sp_Atk": 75,
            "Sp_Def": 70,
            "Speed": 100
            
        }
        
    }
    Blazejaw = {
        "name": "Blazejaw",
        "type": "Fire",
        "level": [],
        "stats": {
            "Hp": 175,
            "Attack": 90,
            "Defense": 84,
            "Sp_Atk": 90,
            "Sp_Def": 84,
            "Speed": 115
            
        }
        
    }
    Inferchomp = {
        "name": "Inferchomp",
        "type": [
            "Fire", 
            "Beast"
        ],
        "level": [],
        "stats": {
            "Hp": 185,
            "Attack": 110,
            "Defense": 98,
            "Sp_Atk": 105,
            "Sp_Def": 103,
            "Speed": 123
            
        }
        
    }
    Mudlope = {
        "name": "Mudlope",
        "type": "Water",
        "level": [],
        "stats": {
            "Hp": 173,
            "Attack": 83,
            "Defense": 85,
            "Sp_Atk": 85,
            "Sp_Def": 88,
            "Speed": 90
            
        }
        
    }
    Mudskipper = {
        "name": "Mudskipper",
        "type": "Water",
        "level": [],
        "stats": {
            "Hp": 184,
            "Attack": 93,
            "Defense": 95,
            "Sp_Atk": 95,
            "Sp_Def": 98,
            "Speed": 105
            
        }
        
    }
    Quakelotl = {
        "name": "Quakelotl",
        "type": [
            "Water",
            "Ground"
        ],
        "level": [],
        "stats": {
            "Hp": 200,
            "Attack": 110,
            "Defense": 105,
            "Sp_Atk": 113,
            "Sp_Def": 110,
            "Speed": 115
            
        }
        
    }
    Breezowl = {
        "name": "Breezowl",
        "type": "Flying",
        "level": [],
        "stats": {
            "Hp": 164,
            "Attack": 70,
            "Defense": 75,
            "Sp_Atk": 70,
            "Sp_Def": 63,
            "Speed": 100
            
        }
        
    }
    Gustwing = {
        "name": "Gustwing",
        "type": "Flying",
        "level": [],
        "stats": {
            "Hp": 172,
            "Attack": 85,
            "Defense": 83,
            "Sp_Atk": 83,
            "Sp_Def": 85,
            "Speed": 118
            
        }
        
    }
    Cyclohawk = {
        "name": "Cyclohawk",
        "type": [
            "Flying",
            "Electric"
            ],
        "level": [],
        "stats": {
            "Hp": 185,
            "Attack": 100,
            "Defense": 95,
            "Sp_Atk": 110,
            "Sp_Def": 98,
            "Speed": 145
        
        }
        
    }
    Rochling = {
        "name": "Rochling",
        "type": "Bug",
        "level": [],
        "stats": {
            "Hp": 140,
            "Attack": 65,
            "Defense": 65,
            "Sp_Atk": 60,
            "Sp_Def": 65,
            "Speed": 105
            
        }
        
    }
    Shedroch = {
        "name": "Shedroc",
        "type": "Bug",
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 80,
            "Defense": 50,
            "Sp_Atk": 75,    
            "Sp_Def": 50,
            "Speed": 118
            
        }
        
    }
    Beheroch = {
        "name": "Beheroch",
        "type": [
            "Bug", 
            "Dark"
            ],
        "level": [],
        "stats": {
            "Hp": 195,
            "Attack": 120,
            "Defense": 114,
            "Sp_Atk": 115,
            "Sp_Def": 113,
            "Speed": 140
            
        }
        
    }
    Normulin = {
        "name": "Normulin",
        "type": "Normal",
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 70,
            "Defense": 72,
            "Sp_Atk": 60,
            "Sp_Def": 75,
            "Speed": 70
        
    }
    
  }
    Normuza = {
        "name": "Normuza",
        "type": "Normal",
        "level": [],
        "stats": {
            "Hp": 180,
            "Attack": 85,
            "Defense": 88,
            "Sp_Atk": 72,
            "Sp_Def": 85,
            "Speed": 80
            
        }
    }
    Normine = {
        "name": "Normine",
        "type": [
            "Normal",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp": 195,
            "Attack" : 100,
            "Defense" : 105,
            "Sp_Atk" : 85,
            "Sp_Def" : 110,
            "Speed" : 90
            
        }
    }
    Kickora = {
        "name": "Kickora",
        "type": [
            "Fighting",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 185,
            "Attack": 110,
            "Defense": 95,
            "Sp_Atk": 85,
            "Sp_Def": 98,
            "Speed": 115
            
        }
        
    }
    Siphonbite = {
        "name": "Siphonbite",
        "type": "Dark",
        "level": [],
        "stats": {
            "Hp": 168,
            "Attack": 70,
            "Defense": 85,
            "Sp_Atk": 70,
            "Sp_Def": 85,
            "Speed": 100
            
        }
        
    }
    Souldevoir = {
        "name": "Souldevoir",
        "type": [
            "Dark",
            "Beast"
            ],
        "level": [],
        "stats": {
            "Hp": 190,
            "Attack": 85,
            "Defense": 100,
            "Sp_Atk": 95,
            "Sp_Def": 100,
            "Speed": 120
            
        }
        
    }
    Essenfest = {
        "name": "Essenfest",
        "type": [
            "Dark",
            "Beast"
            ],
        "level": [],
        "stats" : {
            "Hp": 180,
            "Attack": 100,
            "Defense": 98,
            "Sp_Atk": 90,
            "Sp_Def": 95,
            "Speed": 122
            
        }
        
    }
    Coatliris = {
        "name": "Coatliris",
        "type": [
            "Normal",
            "Ground"
            ],
        "level": [],
        "stats": {
            "Hp": 165,
            "Attack": 75,
            "Defense": 70,
            "Sp_Atk": 65,
            "Sp_Def": 70,
            "Speed": 90
            
        }
    }
    Coatluz = {
        "name": "Coatluz",
        "type": [
            "Normal",
            "Ground"
            ],
        "level": [],
        "stats": {
            "Hp": 175,
            "Attack": 88,
            "Defense": 83,
            "Sp_Atk": 75,
            "Sp_Def": 80,
            "Speed": 103
            
        }
    }
    Coatlum = {
        "name": "Coatlum",
        "type": [
            "Normal",
            "Ground"
            ],
        "level": [],
        "stats": {
            "Hp": 190,
            "Attack": 103,
            "Defense": 95,
            "Sp_Atk": 90,
            "Sp_Def": 95,
            "Speed": 113
            
        }
    }
    Sparkitt = {
        "name": "Sparkitt",
        "type": "Electric",
        "level": [],
        "stats": {
            "Hp": 165,
            "Attack": 75,
            "Defense": 68,
            "Sp_Atk": 80,
            "Sp_Def": 80,
            "Speed": 115
            
        }
        
    }
    Joltflash = {
        "name": "Joltflash",
        "type": "Electric",
        "level": [],
        "stats": {
            "Hp": 175,
            "Attack": 85,
            "Defense": 80,
            "Sp_Atk": 105,
            "Sp_Def": 110,
            "Speed": 130
            
        }
        
    }
    Luminara {
        "name": "Luminara",
        "type": [
            "Water",
            "Dark"
            ],
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 100,
            "Defense": 88,
            "Sp_Atk": 95,
            "Sp_Def": 93,
            "Speed": 110
            
        }
        
    }
    Thundhoof = {
        "name": "Thundhoof",
        "type": [
            "Electric",
            "Fairy"
            ],
        "level": [],
        "stats": {
            "Hp": 175,
            "Attack": 93,
            "Defense": 95,
            "Sp_Atk": 100,
            "Sp_Def": 92,
            "Speed": 110
            
        }
        
    }
    Swoopscar = {
        "name": "Swoopscar",
        "type": [
            "Bug",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 95,
            "Defense": 90,
            "Sp_Atk": 90,
            "Sp_Def": 100,
            "Speed": 102
            
        }
        
    }
    Sandove = {
        "name": "Sandove",
        "type": [
            "Ground",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 165,
            "Attack": 98,
            "Defense": 88,
            "Sp_Atk": 92,
            "Sp_Def": 93,
            "Speed": 105
            
        }
        
    }
    Dunebeak = {
        "name": "Dunebeak",
        "type": [
            "Ground",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 180,
            "Attack": 105,
            "Defense": 95,
            "Sp_Atk": 107,
            "Sp_Def": 99,
            "Speed": 112
            
        }
        
    }
    Coyol = {
        "name" : "Coyol",
        "type" : [
            "Normal",
            "Ground"
            ],
        "level": [],
        "stats": {
            "Hp": 165,
            "Attack": 75,
            "Defense": ,
            "Sp_Atk": ,
            "Sp_Def": ,
            "Speed": 
            
        }
    }
    Coyoba = {
        "name" : "Coyoba",
        "type" : [
            "Dark",
            "Ground"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Coyestro = {
        "name" : "Coyestro",
        "type" : [
            "Dark",
            "Ground"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Mossclaw = {
        "name": "Mossclaw",
        "type": "Grass",
        "level": [],
        "stats": {
            "Hp": 168,
            "Attack": 83,
            "Defense": 85,
            "Sp_Atk": 83,
            "Sp_Def": 92,
            "Speed": 102
            
        }
        
    }
    Thornpaw = {
        "name": "Thornpaw",
        "type": "Grass",
        "level": [],
            "stats": {
            "Hp": 183,
            "Attack": 110,
            "Defense": 90,
            "Sp_Atk": 98,
            "Sp_Def": 102,
            "Speed": 112
            
        }
        
    }
    Spectrora = {
        "name": "Spectrora",
        "type": [
            "Ghost",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 187,
            "Attack": 91,
            "Defense": 90,
            "Sp_Atk": 105,
            "Sp_Def": 102,
            "Speed": 112
            
        }
        
    }
    Tucaro = {
        "name" : "Tucaro",
        "type" : [
            "Normal",
            "Flying"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Tucanor = {
        "name" : "Tucanor",
        "type" : [
            "Normal",
            "Flying"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Tucanix = {
        "name" : "Tucanix",
        "type" : [
            "Normal",
            "Flying"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Tulehag = {
        "name": "Tulehag",
        "type": [
            "Ghost",
            "Grass"
            ],
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 100,
            "Defense": 88,
            "Sp_Atk": 90,
            "Sp_Def": 90,
            "Speed": 98
            
        }
        
    }
    Mistlion = {
        "name": "Mistlion",
        "type": "Ice",
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 80,
            "Defense": 90,
            "Sp_Atk": 85,
            "Sp_Def": 90,
            "Speed": 90
            
        }
        
    }
    Hazeleo = {
        "name": "Hazeleo",
        "type": [
            "Ice",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp": 188,
            "Attack" : 98,
            "Defense" : 100,
            "Sp_Atk" : 100,
            "Sp_Def" : 103,
            "Speed" : 100
            
        }
        
    }
    Stormlion = {
        "name": "Stormlion"
        "type": "Electric",
        "level": [],
        "stats": {
            "Hp": 172,
            "Attack" : 83,
            "Defense" : 88,
            "Sp_Atk" : 90,
            "Sp_Def" : 88,
            "Speed" : 95
            
        }
        
    }
    Roarstom  = {
        "name": "Roarstom",
        "type": [
            "Electric",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp": 185,
            "Attack": 95,
            "Defense": 100,
            "Sp_Atk": 103,
            "Sp_Def": 98,
            "Speed": 106
            
        }
        
    }
    Floracorn = {
        "name": "Floracorn",
        "type": [
            "Fairy",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 188,
            "Attack": 85,
            "Defense": 90,
            "Sp_Atk": 98,
            "Sp_Def": 100,
            "Speed": 99
            
        }
        
    }
    Verdantus = {
        "name": "Verdantus",
        "type": [
            "Grass",
            "Poison"
            ],
        "level": [],
        "stats": {
            "Hp": 190,
            "Attack" : 105,
            "Defense" : 100,
            "Sp_Atk": 105,
            "Sp_Def": 100,
            "Speed": 110
            
        }
        
    }
    Iguar = {
        "name" : "Iguar",
        "type" : [
            "Normal",
            "Grass"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Igualis = {
        "name" : "Igualis",
        "type" : [
            "Normal",
            "Grass"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Iguarex = {
        "name" : "Iguarex",
        "type" : [
            "Normal",
            "Dragon"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Camix = {
        "name" : "Camix",
        "type" : [
            "Normal",
            "Bug"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Camillo = {
        "name" : "Camillo",
        "type" : [
            "Normal",
            "Bug"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Camaximo = {
        "name" : "Camaximo",
        "type" : [
            "Normal",
            "Bug"
            ],
        "level": [],
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
        "name": "Electray",
        "type": [
            "Electric",
            "Water"
            ],
        "level": [],
        "stats":{
            "Hp": 195,
            "Attack": 80,
            "Defense": 95,
            "Sp_Atk": 110,
            "Sp_Def": 100,
            "Speed": 109
            
        }
        
    }
    Frostpaw = {
        "name": "Frostpaw",
        "type": "Ice",
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack" : 75,
            "Defense" : 85,
            "Sp_Atk" : 83,
            "Sp_Def" : 88,
            "Speed" : 90
            
        }
        
    }
    Hailclaw = {
        "name" : "Hailclaw",
        "type" : "Ice",
        "level": [],
        "stats" : {
            "Hp" : 185,
            "Attack" : 85,
            "Defense" : 98,
            "Sp_Atk" : 100,
            "Sp_Def" : 100,
            "Speed" : 105
            
        }
        
    }
    Frostcub = {
        "name" : "Frostcub",
        "type" : [
            "Ice",
            "Water"
            ],
        "level": [],
        "stats" : {
            "Hp" : 168,
            "Attack" : 73,
            "Defense" : 72,
            "Sp_Atk" : 75,
            "Sp_Def" : 74,
            "Speed" : 85
            
        }
        
    }
    Chillber = {
        "name" : "Chillber",
        "type" : [
            "Ice",
            "Water"
            ],
        "level": [],
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
        "level": [],
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
        "level": [],
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
        "level": [],
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
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Brawlion = {
        "name" : "Brawlion",
        "type" : [
            "Fighting",
            "Fire"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Scorpinch = {
        "name" : "Scorpinch",
        "type" : [
            "Fire",
            "Poison"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Toxinip = {
        "name" : "Toxinip",
        "type" : [
            "Fire",
            "Poison"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Pyrotox = {
        "name" : "Pyrotox",
        "type" : [
            "Fire",
            "Poison"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Tlacota = {
        "name" : "Tlacota",
        "type" : "Normal",
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Tlacotor = {
        "name" : "Tlacotor",
        "type" : "Normal",
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Tlacoguard = {
        "name" : "Tlacoguard",
        "type" : [
            "Normal",
            "Fighting"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Fangrend = {
        "name" : "Fangrend",
        "type" : [
            "Fighting",
            "Ice"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Effigy = {
        "name" : "Effigy",
        "type" : "Ghost",
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Vexdoll = {
        "name" : "Vexdoll",
        "type" : [
            "Ghost",
            "Psychic"
            ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Vexweav = {
        "name" : "Vexweav",
        "type" : [
        "Ghost",
        "Dark"
        ],
        "level": [],
        "stats" : {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Aqualith = {
        "name": "Aqualith",
        "type": "Water",
        "level": [],
        "stats": {
            "Hp": ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Aquadon = {
        "name": "Aquadon",
        "type": [
            "Water",
            "Beast"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Plesyodrake =  {
        "name": "Plesyodrake",
        "type": [
            "Dragon",
            "Beast"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Veloscale = {
        "name" : "Veloscale",
        "type" : "Grass",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Predaptor = {
        "name": "Predaptor",
        "type": [
            "Grass",
            "Beast"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Velocydrake = {
        "name": "Velocydrake",
        "type": [
            "Dragon",
            "Beast"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Sprinkleaf = {
        "name": "Sprinkleaf",
        "type": "Fairy",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Glitterose = {
        "name": "Glitterose",
        "type": [
            "Fairy",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Pebbleon = {
        "name": "Pebbleon",
        "type": "Rock",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Granitear = {
        "name": "Granitear",
        "type": [
            "Rock",
            "Ground"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Vena = {
        "name": "Vena",
        "type": [
            "Normal",
            "Grass"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Venatus = {
        "name": "Venatus",
        "type": [
            "Normal",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Venomalo = {
        "name": "Venomalo",
        "type": [
            "Normal",
            "Dark"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Ratil = {
        "name": "Ratil",
        "type": "Normal",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Ratal = {
        "name": "Ratal",
        "type": "Normal",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Ratonar = {
        "name": "raton",
        "type": "Normal",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Crysantis = {
        "name": "Crysantis",
        "type": [
            "Ice",
            "Bug"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Slapshling = {
        "name": "Slapshling",
        "type": "Water",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Wavelet = {
        "name": "Wavelet",
        "type": [
            "Water",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Venofang = {
        "name": "Venofang",
        "type": "Poison",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Serpentide = {
        "name": "Serpentide",
        "type": [
            "Poison",
            "Dragon"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Colibin = {
        "name": "Colibin",
        "type": [
            "Normal",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Colibra = {
        "name": "Colibra",
        "type": [
            "Normal",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Colibrio = {
        "name": "Colibrio",
        "type": [
            "Normal",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
    }
    Zyephblade = {
        "name": "Zyephblade",
        "type": [
            "Steel",
            "Rock"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Aurostride = {
        "name": "Aurostride",
        "type": [
            "Ice",
            "Rock"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Embstrike = {
        "name": "Embstrike",
        "type": [
            "Fire",
            "Rock"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Webbing = {
        "name": "Webbing",
        "type": [
            "Poison",
            "Dark"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Plaguefly = {
        "name": "Plaguefly",
        "type": [
            "Poison",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Whimsiren = {
        "name": "Whimsiren",
        "type": [
            "Fairy",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Glailhorn = {
        "name": "Glailhorn",
        "type": "Ice",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Frosthorn = {
        "name": "Frosthorn",
        "type": [
            "Ice",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Duskbat = {
        "name": "Duskbat",
        "type": [
            "Dark",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Eclipsbat = {
        "name": "Eclipsbat",
        "type": [
            "Dark",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Xtabay = {
        "name": "Xtabay",
        "type": [
            "Fairy",
            "Grass"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Spectrabane = {
        "name": "Spectrabane",
        "type": [
            "Ghost",
            "Fairy"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Nightmane = {
        "name": "Nightmane",
        "type": [
            "Ghost",
            "Fire"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Tuskdrill = {
        "name": "Tuskdrill",
        "type": [
            "Ground",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Sylphora = {
        "name": "Sylphora",
        "type": "Fairy",
        "level": [],
        "stats": {
            "Hp" : ,
            "Attack" : ,
            "Defense" : ,
            "Sp_Atk" : ,
            "Sp_Def" : ,
            "Speed" :
            
        }
        
    }
    Galepetal = {
        "name": "Galepetal",
        "type": [
            "Fairy",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp": ,
            "Attack": ,
            "Defense": ,
            "Sp_Atk": ,
            "Sp_Def": ,
            "Speed": 105
            
        }
        
    }
    Sylvantrix = {
        "name": "Sylvantrix",
        "type": [
            "Fairy",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp": 205,
            "Attack": 100,
            "Defense": 130,
            "Sp_Atk": 145,
            "Sp_Def": 135,
            "Speed": 115
            
        }
        
    }
    Teratot = {
        "name": "Teratot",
        "type": [
            "Ground",
            "Rock"
            ],
        "level": [],
        "stats": {
            "Hp": 175,
            "Attack": 85,
            "Defense": 90,
            "Sp_Atk": 80,
            "Sp_Def": 85,
            "Speed": 80
            
        }
        
    }
    Terraforge = {
        "name": "Terraforge",
        "type": [
            "Ground",
            "Grass"
            ],
        "level": [],
        "stats": {
            "Hp": 190,
            "Attack": 95,
            "Defense": 100,
            "Sp_Atk": 90,
            "Sp_Def": 98,
            "Speed": 94
            
        }
        
    }
    Gaialith = {
        "name": "Gaialith",
        "type": [
            "Ground",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp": 210,
            "Attack": 110,
            "Defense": 120,
            "Sp_Atk": 125,
            "Sp_Def": 115,
            "Speed": 115
            
        }
        
    }
    Teraguard = {
        "name": "Teraguard",
        "type": "Ground",
        "level": [],
        "stats": {
            "Hp": 170,
            "Attack": 85,
            "Defense": 88,
            "Sp_Atk": 85,
            "Sp_Def": 88,
            "Speed": 90
            
        }
        
    }
    Fistquake = {
        "name": "Fistquake",
        "type": [
            "Ground",
            "Fighting"
            ],
        "level": [],
        "stats": {
            "Hp": 193,
            "Attack": 125,
            "Defense": 110,
            "Sp_Atk": 90,
            "Sp_Def": 95,
            "Speed": 100
            
        }
        
    }
    Tectoknight = {
        "name": "Tectoknight",
        "type": [
            "Fighting",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp": 205,
            "Attack": 140,
            "Defense": 135,
            "Sp_Atk": 100,
            "Sp_Def": 110,
            "Speed": 115
            
        }
        
    }
    Earthrend = {
        "name": "Earthrend",
        "type": [
            "Ground",
            "Dragon"
            ],
        "level": [],
        "stats": {
            "Hp": 185,
            "Attack": 125,
            "Defense": 125,
            "Sp_Atk": 90,
            "Sp_Def": 90,
            "Speed":95
            
        }
        
    }
    Terrascale = {
        "name": "Terrascale",
        "type": [
            "Dragon",
            "Steel"
            ],
        "level": [],
        "stats": {
            "Hp": 200,
            "Attack": 135,
            "Defense": 145,
            "Sp_Atk": 100,
            "Sp_Def": 100,
            "Speed": 105
            
        }
        
    }
    Astralynx = {
        "name": "Astralynx",
        "type": [
            "Psychic",
            "Fighting"
            ],
        "level": [],
        "stats": {
            "Hp": 235,
            "Attack": 145,
            "Defense": 135,
            "Sp_Atk": 145,
            "Sp_Def": 140,
            "Speed": 140
            
        }
        
    }
    Novastrike = {
        "name": "Novastrike",
        "type": [
            "Fire",
            "Flying"
            ],
        "level": [],
        "stats": {
            "Hp": 230,
            "Attack" : 138,
            "Defense" : 145,
            "Sp_Atk" : 140,
            "Sp_Def" : 145,
            "Speed" : 140
            
        }
        
    }
    Feralstorm = {
        "name": "Feralstorm",
        "type": [
            "Beast",
            "Electric"
            ],
        "level": [],
        "stats": {
            "Hp": 200,
            "Attack": 145,
            "Defense": 140,
            "Sp_Atk": 145,
            "Sp_Def": 142,
            "Speed": 160
            
        }
        
    }
    Lunaryx {
        "name": "Lunaryx",
        "type": [
            "Ice",
            "Dark"
            ],
        "level": [],
        "stats" : {
            "Hp" : 240,
            "Attack" : 155,
            "Defense" : 135,
            "Sp_Atk" : 150,
            "Sp_Def" : 140,
            "Speed" : 145
            
        }
        
    }
    Solaris = {
        "name": "Solaris",
        "type": [
            "Fire",
            "Psychic"
            ],
        "level": [],
        "stats": {
            "Hp": 240,
            "Attack": 130,
            "Defense": 140,
            "Sp_Atk": 155,
            "Sp_Def": 140,
            "Speed": 145
      
    }
    
  }
    Serpentix = {
        "name": "Serpentix",
        "type": [
            "Dragon",
            "Fairy"
            ],
        "level": [],
        "stats": {
            "Hp": 245,
            "Attack": 145,
            "Defense" : 140,
            "Sp_Atk" : 150,
            "Sp_Def" : 145,
            "Speed" : 150
            
        }
        
    }
    Shadow = {
        "name": "Shadow",
        "type": "Ghost",
        "level": [],
        "stats": {
            "Hp": 235,
            "Attack": 140,
            "Defense": 130,
            "Sp_Atk": 145,
            "Sp_Def": 135,
            "Speed": 135
            
        }
        
    }