import sys
import pygame
from enum import Enum

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

class Types(Enum):
    Grass = {
        "Type": "Grass",
        "Weakness": [
            "Fire",
            "Flying",
            "Bug",
            "Ice"],
        "Strong": [
            "Rock",
            "Ground",
            "Water"],
        "Weak": []
        "Nuetral": []
        
    }
    Fire = {
        "Type": "Fire",
        "Weakness": [
            "Water",
            "Rock",
            "Ground"],
        "Strong": [
            "Grass",
            "Bug",
            "Ice",
            "Steel",
            "Beast"],
        "Weak": []
        "Neutral": []
        
    }
    Water = {
        "Type": "Water",
        "Weakness": [
            "Grass",
            "Electric"
            ],
        "Strong": [
            "Fire",
            "Rock",
            "Ground"],
        "Weak": [],
        "Neutral": []
        
    }
    Bug = {
        "Type": "Bug",
        "Weakness": [
            "Fire",
            "Flying",
            "Rock"],
        "Strong": [
            "Grass",
            "Psychic",
            "Dark"],
        "Weak": [],
        "Neutral": []
        
    }
    Flying = {
        "Type": "Flying",
        "Weakness": [
            "Electric",
            "Ice",
            "Rock"
            ],
        "Strong": [
            "Grass",
            "Bug",
            "Fighting"
            ],
        "Weak": [],
        "Neutral": [],
        "Imune": [
            "Ground"
            ]
        
    }
    Poison = {
        "Type": "Poison",
        "Weakness": [
            "Ground",
            "Psychic"
            ],
        "Strong": [
            "Grass",
            "Fairy"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Electric = {
        "Type": "Electric",
        "Weakness": [
            "Ground"],
        "Strong": [
            "Water",
            "Flying",
            "Beast"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Rock = {
        "Type":"Rock",
        "Weakness": [
            "Grass",
            "Water",
            "Ground",
            "Fighting",
            "Steel"
            ],
        "Strong": [
            "Fire",
            "Bug",
            "Flying",
            "Ice"],
        "Weak": [],
        "Neutral": []
        
    }
    Normal = {
        "Type": "Normal",
        "Weakness": [
            "Fighting"
            ],
        "Strong": [],
        "Weak": [
            "Rock",
            "Steel"
            ],
        "Neutral": []
        "Imune": [
            "Ghost"
            ]
        
    }
    Ground = {
        "Type": "Ground",
        "Weakness": [
            "Grass",
            "Water",
            "Ice"
            ],
        "Strong": [
            "Fire",
            "Electric",
            "Rock",
            "Steel"
            ],
        "Weak": [],
        "Neutral": [],
        "Imune": [
            "Electric"
            ]
        
    }
    Psychic = {
        "Type":"Psychic",
        "Weakness": [
            "Bug",
            "Ghost",
            "Dark",
            "Beast"
            ],
        "Strong": [
            "Poison",
            "Fighting"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Ice = {
        "Type": "Ice",
        "Weakness": [
            "Fire",
            "Rock",
            "Fighting",
            "Steel"
            ],
        "Strong": [
            "Grass",
            "Flying",
            "Ground",
            "Dragon"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Fighting = {
        "Type": "Fighting",
        "Weakness": [
            "Psychic",
            "Flying",
            "Fairy"],
        "Strong": [
            "Normal",
            "Rock",
            "Ice",
            "Dark"
            ],
        "Weak": [],
        "Neutral": []
        
    }
    Dragon = {
        "Type": "Dragon",
        "Weakness": [
            "Dragon",
            "Ice",
            "Fairy"
            ],
        "Strong": [
            "Dragon"
            ],
        "Weak": [],
        "Neutral": []
        
    }
        "Ghost",
        "Dark",
        "Steel",
        "Fairy",
        "Beast"
        ]
    def __init__(self, type_name):
        self.type = pymon_type
        self.strong = []
        self.weakness = []
        self.weak = []
        self.neutral = []

    def set_relations(self, strong, weak, neutral, weakness):
        self.strong = strong
        self.weak = weak
        self.neutral = neutral
        self.weakness = weakness

class Hold:
    def hold(self, hold):
        self.hold = hold

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