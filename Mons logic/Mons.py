import sys
import pygame

	Pymons =	{
	1: {
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
	2: {
	  "name" : "Floraleaf",
	  "type" : "Grass",
	  "stats" : {
	    "Hp" : 160,
	    "Attack" 73: ,
	    "Defense" 75: ,
	    "Sp_Atk" : 93,
	    "Sp_Def" : 88,
	    "Speed" : 125
	  }
	  }
	3: {
	  "name" : "Vinyldra",
	  "type" : ["Grass", "Dragon"],
	  "stats" : {
	    "Hp" : 170,
	    "Attack" : 88,
	    "Defense" : 88,
	    "Sp_Atk" : 110,
	    "Sp_Def" : 98,
	    "Speed" : 130
	  }
	  }
	4: {
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
	5: {
	  "name" : "Blazejaw",
	  "type" : "Fire",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	6: {
	  "name" : "Inferchomp",
	  "type" : ["Fire", "Beast"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	7: {
	  "name" : "Mudlope",
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
	8: {
	  "name" : "Mudskipper",
	  "type" : "Water",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : }
	  }
	9: {
	  "name" : "Quakelotl",
	  "type" : ["Water", "Ground"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	10: {
	  "name" : "Breezowl",
	  "type" : "Flying",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	11: {
	  "name" : "Gustwing",
	  "type" : "Flying",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	12: {
	  "name" : "Cyclohawk",
	  "type" : ["Flying", "Electric"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	13: {
	  "name" : "Rochling",
	  "type" : "Bug",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	14: {
	  "name" : "Scaracral",
	  "type" : "Bug",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	15: {
	  "name" : "Beheroch",
	  "type" : ["Bug", "Dark"],
	  "stats" : {
		    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	16: {
	  "name" : "Kickora",
	  "type" : ["Fighting,Flying"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	17: {
	  "name" : "Siphonbite",
	  "type" : "Dark",
	  "stats" : {
		    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	18: {
	  "name" : "Souldevoir",
	  "type" : ["Dark, Beast"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	19: {
	  "name" : "Essenfest",
	  "type" : ["Dark, Beast"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	20: {
	  "name" : "Sparkitt",
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
	21: {
	  "name" : "Joltflash",
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
	22: {
	  "name" : "Luminara",
	  "type" : ["Water, Dark"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	23: {
	  "name" : "Thundhoof",
	  "type" : ["Electric, Fairy"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	24: {
	  "name" : "Swoopscar",
	  "type" : ["Bug, Flying"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	25: {
	  "name" : "Sandove",
	  "type" : ["Ground, Flying"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	26: {
	  "name" : "Dunebeak",
	  "type" : ["Ground,Flying"],
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	27: {
	  "name" : "Mossclaw",
	  "type" : "Grass",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	28: {
	  "name" : "Thornpaw",
	  "type" : "Grass",
	  "stats" : {
	    "Hp" : ,
	    "Attack" : ,
	    "Defense" : ,
	    "Sp_Atk" : ,
	    "Sp_Def" : ,
	    "Speed" : 
	  }
	  }
	29: {
	  "name" : "Spectrora",
	  "type" : ["Ghost, Flying"],
	  "stats" : {

	  }
	  }
	30: {
	  "name" : "Tulehag",
	  "type" : ["Ghost, Grass"],
	  "stats" : {}
	  }
	31: {
	  "name" : "Mistlion",
	  "type" : "Ice",
	  "stats" : {}
	  }
	32: {
	  "name" : "Hazeleo",
	  "type" : ["Ice, Steel"[,
	  "stats" : {}
	  }
	33: {
	  "name" : "Stormlion"
	  "type" : "Electric",
	  "stats" : {}
	  }
	34: {
	  "name" : "Roarstom",
	  "type" : ["Electric, Steel"],
	  "stats" : {}
	  }
	35: {
	  "name" : "Floracorn",
	  "type" : "Fairy",
	  "stats" : {}
	    }
	36: {
	  "name" : "Verdantus",
	  "type" : ["Grass, Poison"],
	  "stats" : {}
	  }
	37: {
	  "name" : "Electray",
	  "type" : ["Electric, Water"],
	  "stats" :{}
	  }
	38: {
	  "name" : "Frostpaw",
	  "type" : "Ice",
	  "stats" : {}
	  }
	39: {
	  "name" : "Hailclaw",
	  "type" : "Ice",
	  "stats" : {}
	  }
	40: {
	  "name" : "Frostcub",
	  "type" : ["Ice, Water"],
	  "stats" : {}
	  }
	41: {
	  "name" : "Chillber",
	  "type" : ["Ice, Water"],
	  "stats" : {}
	  }
	42: {
	  "name" : "Polarclaw",
	  "type" : ["Ice, Water"],
	  "stats" : {}
	  }
	43: {
	  "name" : "Terrathorn",
	  "type" : ["Grass, Ground"],
	  "stats" : {}
	  }
	44: {
	  "name" : "Searageist",
	  "type" : ["Ghost,Fire"],
	  "stats" : {}
	  }
	45: {
	  "name" : "Shadeimp",
	  "type" : ["Ghost, Rock"],
	  "stats" : {}
	  }
	46: {
	  "name" : "Brawlion",
	  "type" : ["Fighting, Grass"],
	  "stats" : {}
	  }
	47: {
	  "name" : "Scorpinch",
	  "type" : ["Fire, Poison"],
	  "stats" : {}
	  }
	48: {
	  "name" : "Toxinip",
	  "type" : ["Fire, Poison"],
	  "stats" : {}
	  }
	49: {
	  "name" : "Pyrotox",
	  "type" : ["Fire, Poison"],
	  "stats" : {}
	  }
	50: {
	  "name" : "Fangrend",
	  "type" : ["Fighting, Ice"],
	  "stats" : {}
	  }
	51: {
	  "name" : "Effigy",
	  "type" : "Ghost",
	  "stats" : {}
	  }
	52: {
	  "name" : "Vexdoll",
	  "type" : ["Ghost, Psychic"],
	  "stats" : {}
	  }
	53: {
	  "name" : "Vexweav",
	  "type" : ["Ghost, Dark"],
	  "stats" : {}
	  }
	54: {
	  "name" : "Aqualith",
	  "type" : "Water",
	  "stats" : {}
	  }
	55: {
	  "name" : "Aquadon",
	  "type" : ["Water, Beast"],
	  "stats" : {}
	  }
	56: {
	  "name" : "Plesyodrake",
	  "type" : ["Dragon, Beast"],
	  "stats" : {}
	  }
	57: {
	  "name" : "Veloscale",
	  "type" : "Grass",
	  "stats" {}
	  }
	58: {
	  "name" : "Predaptor",
	  "type" : ["Grass, Beast"],
	  "stats" : {}
	  }
	59: {
	  "name" : "Velocydrake",
	  "type" : ["Dragon, Beast"],
	  "stats" : {}
	  }
	60: {
	  "name" : "Sprinkleaf",
	  "type" : "Fairy",
	  "stats" : {}
	  }
	61: {
	  "name" : "Glitterose",
	  "type" : ["Fairy, Psychic"],
	  "stats" : {}
	  }
	62: {
	  "name" : "Pebbleon",
	  "type" : "Rock",
	  "stats" : {}
	  }
	63: {
	  "name" : "Granitear",
	  "type" : ["Rock, Ground"],
	  "stats" : {}
	  }
	64: {
	  "name" : "Crysantis",
	  "type" : ["Ice, Bug"],
	  "stats" : {}
	  }
	65: {
	  "name" : "Slapshling",
	  "type" : "Water",
	  "stats" : {}
	  }
	66: {
	  "name" : "Wavelet",
	  "type" : ["Water, Psychic"],
	  "stats" : {
	    }
	  }
	67: {
	  "name" : "Venofang",
	  "type" : "Poison",
	  "stats" : {}
	  }
	68: {
	  "name" : "Serpentide",
	  "type" : ["Poison, Dragon"],
	  "stats" : {}
	  }
	69: {
	  "name" : "Zyephblade",
	  "type" : ["Steel, Rock"],
	  "stats" : {}
	  }
	70: {
	  "name" : "Aurostride",
	  "type" : ["Ice, Rock"],
	  "stats" : {}
	  }
	71: {
	  "name" : "Embstrike",
	  "type" : ["Fire, Rock"],
	  "stats" : {}
	  }
	72: {
	  "name" : "Webbing",
	  "type" : ["Poison, Dark"],
	  "stats" : {}
	  }
	73: {
	  "name" : "Plaguefly",
	  "type" : ["Poison, Flying"[,
	  "stats" : {}
	  }
	74: {
	  "name" : "Whimsiren",
	  "type" : ["Fairy, Steel"],
	  "stats" : {}
	  }
	75: {
	  "name" : "Glailhorn",
	  "type" : "Ice",
	  "stats" : {}
	  }
	76: {
	  "name" : "Frosthorn",
	  "type" : ["Ice, Steel"],
	  "stats" : {}
	  }
	77: {
	  "name" : "Duskbat",
	  "type" : ["Dark, Flying"],
	  "stats" : {}
	  }
	78: {
	  "name" : "Eclipsbat",
	  "type" : ["Dark, Flying"],
	  "stats" : {}
	  }
	79: {
	  "name" : "Xtabay",
	  "type" : ["Fairy, Grass"],
	  "stats" : {}
	  }
	80: {
	  "name" : "Spectrabane",
	  "type" : ["Ghost, Fairy"],
	  "stats" : {}
	  }
	81: {
	  "name" : "Nightmane",
	  "type" : ["Ghost, Fire"],
	  "stats" : {}
	  }
	82: {
	  " name" : "Tuskdrill",
	  "type" : ["Ground, Steel"],
	  "stats" : {}
	  }
	83: {
	  "name" : "Sylphora",
	  "type" : "Fairy",
	  "stats" : {}
	  }
	84: {
	  "name" : "Galepetal",
	  "type" : ["Fairy, Psychic"],
	  "stats" : {}
	  }
	85: {
	  "name" : "Sylvantrix",
	  "type" : ["Fairy, Psychic"],
	  "stats" : {}
	  }
	86: {
	  "name" : "Teratot",
	  "type" : ["Ground, Rock"],
	  "stats" : {}
	  }
	87: {
	  "name" : "Terraforge",
	  "type" : ["Ground, Grass"],
	  "stats" : {}
	  }
	88: {
	  "name" : "Gaialith",
	  "type" : ["Ground, Psychic"],
	  "stats" : {}
	  }
	89: {
	  "name" : "Teraguard",
	  "type" : "Ground",
	  "stats" : {}
	  }
	90: {
	  "name" : "Fistquake",
	  "type" : ["Ground, Fighting"],
	  "stats" : {}
	  }
	91: {
	  "name" : "Tectoknight",
	  "type" : ["Fighting, Steel"],
	  "stats" : {}
	  }
	92: {
	  "name" : "Earthrend",
	  "type" : ["Ground, Dragon"],
	  "stats" : {}
	  }
	93: {
	  "name" : "Terrascale",
	  "type" : ["Dragon, Steel"],
	  "stats" : {}
	  }
	94: {
	  "name : ""Astralynx",
	  "type" : ["Psychic, Fighting"],
	  "stats" : {}
	  }
	95: {
	  "name" : "Novastrike",
	  "type" : ["Fire, Flying"],
	  "stats" : {}
	  }
	96: {
	  "name" : "Feralstorm",
	  "type" : ["Beast, Electric"],
	  "stats" : {}
	  }
	97: {
	  "name" : "Lunaryx",
	  "type" : ["Ice, Dark"],
	  "stats" : {}
	  }
	98: {
	  "name": "Solaris",
	  "type" : ["Fire, Psychic"],
	  "stats" : {}
	  }
	99: {
	  "name" : "Serpentix",
	  "type" : ["Dragon, Fairy"],
	  "stats" : {}
	  }
	100: {
	  "name" : "Shadow",
	  "type" : "Ghost",
	  "stats" : {}
	  }
	}