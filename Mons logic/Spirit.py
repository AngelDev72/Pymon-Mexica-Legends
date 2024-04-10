import sys
import pygame as pg
from enum import Enum

class Spirits(Enum):
    Tonatiuh = {
      1: "Fire",
    
  }
    Quetzalcoatl = {
      1: "Dragon",
      2: "Psychic"
      
    }
    Tlaloc = {
      1: "Water",
      2: "Electric",
      
    }
    Huitzilopochtli = {
      1: "Fighting",
      2: "Flying"
      
    }
    Xochipilli = {
      1: "Grass"
      
    }
    Chicomecoatl = {
      1: "Bug",
      
    }
    Itzpapalotl = {
      1: "Pioson",
      
    }
    Tlalzolteotl = {
      1: "Ground",
      2: "Fairy"
      
    }
    Mictlantecuhtli = {
      1: "Dark",
      2: "Ghost"
      
    }
    Xipe_Totec = {
      1: "Steel"
      
    }
    Tonantzin = {
      1: "Ice"
      
    }
    Tezcatlipoca = {
      1: "Normal"
      
    }
    Xolotl = {
      1: "Beast"
      
    }
    Tlaltecuhtli = {
      1: "Rock"
      
    }
  
    def Spirit_Sync(self):
      for Spirit in Spirits:
        