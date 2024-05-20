import sys
import pygame
from Mons import Mons

class Stats:
  def __init__(self, hp, attack, defense, speed, sp_attk, sp_def, accuracy, evasion):
    self.hp = []
    self.attack = []
    self.defense = []
    self.speed = []
    self.sp_attk = []
    self.sp_def = []
    self.accuracy = []
    self.evasion = []

  def set_stats(self, stats):
    self.hp = Hp
    self.attack = Attack
    self.defense = Defense
    self.speed = Speed
    self.sp_attk = Special_Attack
    self.sp_def = Special_Defense
    self.accuracy = Accuracy
    self.evasion = Evasion

class Type:
    Types = [
        "Grass",
        "Fire",
        "Water",
        "Bug",
        "Flying",
        "Poison",
        "Electric",
        "Rock",
        "Normal",
        "Ground",
        "Psychic",
        "Ice",
        "Fighting",
        "Dragon",
        "Ghost",
        "Dark",
        "Steel",
        "Fairy",
        "Beast"
        ]
    def __init__(self, type_name):
        self.type = pymon_type
        self.strong = []
        self.weak = []
        self.neutral = []

    def set_relations(self, strong, weak, neutral):
        self.strong = strong
        self.weak = weak
        self.neutral = neutral

class Hold:
    def hold(self, hold):


class Catch_rate:
    def catch_rate(self, catch):


class Pymmon_stats:
    def __init__(self, name, pymon_type, level, stats, types, hold, experience = 0,):
        self.name = name
        self.type = pymon_type
        self.level = level
        self.stats = stats
        self.types = types
        self.experience = experience
        self.hold = hold
    
    def level_up(self):
        experience_needed = self.level * 100
    if self.experience >= experience_needed:
        self.level += 1
        self.experience -= experience_needed
        print(f" {self.name} grew to level {self.level}":