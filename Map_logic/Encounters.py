import pygame as pg
import sys

class Encounters:
  
  starters = [
    "Leaflet",
    "Flamepup", 
    "Mudlope"
    ]  

  routes = {
    0: [
      "",
      ""
      ],
    1: [
      "",
      ""
      ],
    2: [
      "",
      ""
      ],
    3: [
      "",
      ""
      ],
    4: [
      "",
      ""
      ],
    5: [
      "",
      ""
      ], 
    6: [
      "",
      ""
      ],
    7: [
      "",
      ""
      ],  
    8: [
      "",
      ""
      ],
    9: [
      "",
      ""
      ],
    #Static: 
    10: [
      "Embstrike",
      "Aurostride",
      "Crysantis"
      ],
    #Special_Gift
    11: ["", "", ""],
    #Legendary
    12: [
      "Astralynx",
      "Novastrike", 
      "Feralstorm"
      ],
    #Special_condition
    13: [
      "Aqualith",
      "Veloscale",
      "Solaris", 
      "Lunaryx", 
      "Shadow"
      ]
  }

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

