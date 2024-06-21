import pygame as pg
import sys
import secrets
from enum import Enum
from Mons_logic.Mons_base import Mons
from Maps import Map

class Route_Encounters(Enum):
    Starters = [
        "Leaflet",
        "Flamepup", 
        "Mudlope"
        ]
    Static = [
        "Embstrike",
        "Aurostride",
        "Crysantis",
        "Serpentix"
        ]
    Special_Gift = []
    Legendary = [
        "Astralynx",
        "Novastrike", 
        "Feralstorm"
        ]
    Special_condition = [
        "Aqualith",
        "Veloscale",
        "Solaris", 
        "Lunaryx", 
        "Shadow"
        ]

    def __init__(self, starter_index):
        if starter_index < 0 or starter_index >= len(self.starters):
        raise ValueError("Starter index out of range")

        self.starter = self.starters[starter_index]

        self.special_gift = ["", "", ""]

        if self.starter == "Leaflet":
            self.special_gift[0] = "Flamepup"
            self.special_gift[1] = "Mudlope"

        elif self.starter == "Flamepup":
            self.special_gift[0] = "Leaflet"
            self.special_gift[1] = "Mudlope"

        else:
            self.special_gift[0] = "Leaflet"
            self.special_gift[1] = "Flamepup"

    def get_route(self, route_num):
        return self.route[route_num]

