import sys
import pygame
from enum import Enum

#Team Monsters
class Team (Enum):
    Team_Slot = {
        "Slot_1: ",
        "Slot_2: "
        "Slot_3: "
        "Slot_4: "
        "Slot_5: "
        "Slot_6: "
        "Slot_7: "
    }
    def Members(self):
        

#Player
class Player:
    def __init__(self, player_1, player_2, npc):
        self.player_1 = Player_1
        self.player_2 = Player_2
        self.npc = NPC

#Trainers
class Trainers:
    Route_Trainer = [
        "Worker",
        "Chandler",
        "Astronomer",
        "Preist",
        "Scribe",
        "Camper",
        "Infant",
        "Farmer"
        ]
    Temple_Trainer= [
        "Temple Diciple "
        ]
    Temple_Leader =[
        "Tonatiuh",
        "Atl",
        "Itzpapalotl",
        "Xochiquetzal",
        "Quetzalcoatl",
        "Cihuacoatl",
        "Inti",
        "Tlalocatl"
        ]
    Team_Grunt = [
        "Sect Grunt",
        "Sect Admin",
        "Sect Admin"
        ]
    Team_Leader = [
        "Sect Leader Mictla"
    ]
    Heralds = [
        "Wind Herald ",
        "Water Herald ",
        "Fire Herald ",
        "Earth Herald"
        ]
    female_t = [
        "Citlali",
        "Xochitl",
        "Itzel",
        "Mayahuel",
        "Tlalli",
        "Malinalli",
        "Coatl",
        "Atlacoya",
        "Izel",
        "Xilonen",
        "Xiloxoch",
        "Xiuhtonal",
        "Xiuhcoatl",
        "Citlalmina",
        "Chimalma",
        "Tzitzilin",
        "Nochtli",
        "Atlatonin",
        "Ayauhcihuatl",
        "Cuetlaxochitl",
        "Chicahua",
        "Nenetl",
        "Ohtli",
        "Tecuichpo",
        "Tenoch",
        "Tizoc",
        "Xochipilli",
        "Cipactli",
        "Tlaloc",
        "Ichtaca"
        ]
    male_t = [
        "Cuauhtémoc",
        "Moctezuma",
        "Huitzilopochtli",
        "Tlatoani",
        "Tlacaelel",
        "Xipe Totec",
        "Tezcatlipoca",
        "Cuitláhuac",
        "Netzahualcóyotl",
        "Iztaccíhuatl",
        "Tlahuicole",
        "Cacamatzin",
        "Xolotl",
        "Ixtlilxochitl",
        "Tizoc",
        "Tlaloc",
        "Tlalpan",
        "Nezahualpilli",
        "Axayacatl",
        "Cuauhtli",
        "Quetzalcoatl",
        "Chalchiuhtlicue",
        "Tzitzimitl",
        "Tepoztecatl",
        "Xochiquetzal",
        "Tecpatl",
        "Xiuhtecuhtli",
        "Mictlantecuhtli",
        "Tlachinolli",
        "Tzompantli"
        ]
    def Trainer_name(self):
        