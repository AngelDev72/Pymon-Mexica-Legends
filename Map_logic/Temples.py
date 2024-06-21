import sys
import pygame as pg
from enum import Enum
from Mons_logic.Mons_base import Mons

class Temple(Enum):
    # Tenochtitlan
    Sun_Temple = {
        "name": "Sun Temple",
        "Type": [
            "Fire",
            "Fighting"
            ],
        "Leader": "Tonatiuh",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Kickora,
            Scorpinch,
            Brawlion
            ]
    }
    # Tlalocan
    Rain_Temple = {
        "name": "Rain Temple", 
        "Type": [
            "Water", 
            "Electric"
            ], 
        "Leader": "Atl",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Aqualith,
            Frostcub,
            Electray
            ]
    }
    # Teotihuacan
    Pyramid_Temple = {
        "name": "Pyramid Temple",
        "Type": [
            "Rock",
            "Ground"
            ], 
        "Leader": "Itzpapalotl",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Shadeimp,
            Granitear,
            Tuskdrill,
            Terraforge
            ]
    }
    #Xochimilco
    Gardens_Temple = {
        "name": "Gardens Temple", 
        "Type": [
            "Grass", 
            "Poison"
            ],
        "Leader": "Xochiquetzal",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Plaguefly,
            Veloscale,
            Terrathorn,
            Verdantus
            ]
    }
    # Chichen Itza
    Snake_Temple = {
        "name": "Snake Temple", 
        "Type": [
            "Dragon", 
            "Steel"
            ], 
        "Leader": "Quetzalcoatl",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Hazeleo,
            Roarstom,
            Zyephblade,
            Plesyodrake,
            Velocydrake,
            Terrascale
            ]
    }
    #Tlatelolco
    Plazas_Temple = {
        "name": "Plazas Temple", 
        "Type": [
            "Fairy", 
            "Psychic"
            ], 
        "Leader": "Cihuacoatl",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Thundhoof,
            Whimsiren,
            Wavelet,
            Xtabay,
            Glitterose
            ]
    }
    #Cuzco
    Mountain_Temple = {
        "name": "Mountain Temple", 
        "Type": [
            "Beast", 
            "Ice"
            ],
        "Leader": "Inti",
        "Temple Diciple": [
            ],
        "Leaders team": [
            Aquadon,
            Essenfest,
            Chillber,
            Crysantis,
            Fangrend
            ]
    }
    #Tenayuca
    Ruins_Temple = {
        "name": "Ruins Temple", 
        "Type": [
            "Dark",
            "Ghost"
            ], 
        "Leader": "Tlalocatl"
        "Temple Diciple": [
            ]
        "Leaders team": [
            Webbing,
            Nightmane,
            Souldevoir,
            Spectrora,
            Vexweav,
            Beheroach
            ]
    }