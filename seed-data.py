import requests

url = "http://localhost:3000/pokedex/add"

pokedex = [
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 1
  },
  {
    "name": "Ivysaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 2
  },
  {
    "name": "Venusaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 3
  },
  {
    "name": "Charmander",
    "type_1": "Fire",
    "description": "Lizard",
    "pokedex_number": 4
  },
  {
    "name": "Charmeleon",
    "type_1": "Fire",
    "description": "Flame",
    "pokedex_number": 5
  },
  {
    "name": "Charizard",
    "type_1": "Fire",
    "type_2": "Flying",
    "description": "Flame",
    "pokedex_number": 6
  },
  {
    "name": "Squirtle",
    "type_1": "Water",
    "description": "Tiny Turtle",
    "pokedex_number": 7
  },
  {
    "name": "Wartortle",
    "type_1": "Water",
    "description": "Turtle",
    "pokedex_number": 8
  },
  {
    "name": "Blastoise",
    "type_1": "Water",
    "description": "Shellfish",
    "pokedex_number": 9
  },
  {
    "name": "Caterpie",
    "type_1": "Bug",
    "description": "Worm",
    "pokedex_number": 10
  },
  {
    "name": "Metapod",
    "type_1": "Bug",
    "description": "Cocoon",
    "pokedex_number": 11
  },
  {
    "name": "Butterfree",
    "type_1": "Bug",
    "type_2": "Flying",
    "description": "Butterfly",
    "pokedex_number": 12
  },
  {
    "name": "Weedle",
    "type_1": "Bug",
    "type_2": "Poison",
    "description": "Hairy Worm",
    "pokedex_number": 13
  },
  {
    "name": "Kakuna",
    "type_1": "Bug",
    "type_2": "Poison",
    "description": "Cocoon",
    "pokedex_number": 14
  },
  {
    "name": "Beedrill",
    "type_1": "Bug",
    "type_2": "Poison",
    "description": "Poison Bee",
    "pokedex_number": 15
  },
  {
    "name": "Pidgey",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Tiny Bird",
    "pokedex_number": 16
  },
  {
    "name": "Pidgeotto",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Bird",
    "pokedex_number": 17
  },
  {
    "name": "Pidgeot",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Bird",
    "pokedex_number": 18
  },
  {
    "name": "Ratatta",
    "type_1": "Normal",
    "description": "Mouse",
    "pokedex_number": 19
  },
  {
    "name": "Radicate",
    "type_1": "Normal",
    "description": "Mouse",
    "pokedex_number": 20
  },
  {
    "name": "Spearow",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Tiny Bird",
    "pokedex_number": 21
  },
  {
    "name": "Fearow",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Beak",
    "pokedex_number": 22
  },
  {
    "name": "Ekans",
    "type_1": "Poison",
    "description": "Snake",
    "pokedex_number": 23
  },
  {
    "name": "Arbok",
    "type_1": "Poison",
    "description": "Cobra",
    "pokedex_number": 24
  },
  {
    "name": "Pikachu",
    "type_1": "Electric",
    "description": "Mouse",
    "pokedex_number": 25
  },
  {
    "name": "Raichu",
    "type_1": "Electric",
    "description": "Mouse",
    "pokedex_number": 26
  },
  {
    "name": "Sandshrew",
    "type_1": "Mouse",
    "description": "Mouse",
    "pokedex_number": 27
  },
  {
    "name": "Sandslash",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Mouse",
    "pokedex_number": 28
  },
  {
    "name": "Nidoran♀",
    "type_1": "Poison",
    "description": "Poison Pin",
    "pokedex_number": 29
  },
  {
    "name": "Nidorina",
    "type_1": "Poison",
    "description": "Poison Pin",
    "pokedex_number": 30
  },
  {
    "name": "Nidoqueen",
    "type_1": "Poison",
    "type_2": "Ground",
    "description": "Drill",
    "pokedex_number": 31
  },
  {
    "name": "Nidoran♂",
    "type_1": "Poison",
    "description": "Poison Pin",
    "pokedex_number": 32
  },
  {
    "name": "Nidorino",
    "type_1": "Poison",
    "description": "Poison Pin",
    "pokedex_number": 33
  },
  {
    "name": "Nidoking",
    "type_1": "Poison",
    "type_2": "Ground",
    "description": "Drill",
    "pokedex_number": 34
  },
  {
    "name": "Clefairy",
    "type_1": "Fairy",
    "description": "Fairy",
    "pokedex_number": 35
  },
  {
    "name": "Clefable",
    "type_1": "Fairy",
    "description": "Fairy",
    "pokedex_number": 36
  },
  {
    "name": "Vulpix",
    "type_1": "Fire",
    "description": "Fox",
    "pokedex_number": 37
  },
  {
    "name": "Ninetales",
    "type_2": "Fire",
    "description": "Fox",
    "pokedex_number": 38
  },
  {
    "name": "Jigglypuff",
    "type_1": "Normal",
    "type_2": "Fairy",
    "description": "Balloon",
    "pokedex_number": 39
  },
  {
    "name": "Wigglytuff",
    "type_1": "Normal",
    "type_2": "Fairy",
    "description": "Balloon",
    "pokedex_number": 40
  },
  {
    "name": "Zubat",
    "type_1": "Poison",
    "type_2": "Flying",
    "description": "Bat",
    "pokedex_number": 41
  },
  {
    "name": "Golbat",
    "type_1": "Poison",
    "type_2": "Flying",
    "description": "Bat",
    "pokedex_number": 42
  },
  {
    "name": "Oddish",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Weed",
    "pokedex_number": 43
  },
  {
    "name": "Gloom",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Weed",
    "pokedex_number": 44
  },
  {
    "name": "Vileplume",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Flower",
    "pokedex_number": 45
  },
  {
    "name": "Paras",
    "type_1": "Bug",
    "type_2": "Grass",
    "description": "Mushroom",
    "pokedex_number": 46
  },
  {
    "name": "Parasect",
    "type_1": "Bug",
    "type_2": "Grass",
    "description": "Mushroom",
    "pokedex_number": 47
  },
  {
    "name": "Venonat",
    "type_1": "Bug",
    "type_2": "Poison",
    "description": "Insect",
    "pokedex_number": 48
  },
  {
    "name": "Venomoth",
    "type_1": "Bug",
    "type_2": "Poison",
    "description": "Poison Moth",
    "pokedex_number": 49
  },
  {
    "name": "Diglett",
    "type_1": "Ground",
    "description": "Mole",
    "pokedex_number": 50
  },
  {
    "name": "Dugtrio",
    "type_1": "Ground",
    "description": "Mole",
    "pokedex_number": 51
  },
  {
    "name": "Meowth",
    "type_1": "Normal",
    "description": "Scratch Cat",
    "pokedex_number": 52
  },
  {
    "name": "Persian",
    "type_1": "Normal",
    "description": "Classy Cat",
    "pokedex_number": 53
  },
  {
    "name": "Psyduck",
    "type_1": "Water",
    "description": "Duck",
    "pokedex_number": 54
  },
  {
    "name": "Golduck",
    "type_1": "Water",
    "description": "Duck",
    "pokedex_number": 55
  },
  {
    "name": "Mankey",
    "type_1": "Fighting",
    "description": "Pig Monkey",
    "pokedex_number": 56
  },
  {
    "name": "Primape",
    "type_1": "Fighting",
    "description": "Pig Monkey",
    "pokedex_number": 57
  },
  {
    "name": "Growlithe",
    "type_1": "Fire",
    "description": "Puppy",
    "pokedex_number": 58
  },
  {
    "name": "Arcanine",
    "type_1": "Fire",
    "description": "Legendary",
    "pokedex_number": 59
  },
  {
    "name": "Poliwag",
    "type_1": "Water",
    "description": "Tadpole",
    "pokedex_number": 60
  },
  {
    "name": "Poliwhirl",
    "type_1": "Water",
    "description": "Tadpole",
    "pokedex_number": 61
  },
  {
    "name": "Poliwrath",
    "type_1": "Water",
    "type_2": "Fighting",
    "description": "Tadpole",
    "pokedex_number": 62
  },
  {
    "name": "Abra",
    "type_1": "Psychic",
    "description": "Psi",
    "pokedex_number": 63
  },
  {
    "name": "Kadabra",
    "type_1": "Psychic",
    "description": "Psi",
    "pokedex_number": 64
  },
  {
    "name": "Alakazam",
    "type_1": "Psychic",
    "description": "Psi",
    "pokedex_number": 65
  },
  {
    "name": "Machop",
    "type_1": "Fighting",
    "description": "Superpower",
    "pokedex_number": 66
  },
  {
    "name": "Machoke",
    "type_1": "Fighting",
    "description": "Superpower",
    "pokedex_number": 67
  },
  {
    "name": "Machamp",
    "type_1": "Fighting",
    "description": "Superpower",
    "pokedex_number": 68
  },
  {
    "name": "Bellsprout",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Flower",
    "pokedex_number": 69
  },
  {
    "name": "Weepinbell",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Flycatcher",
    "pokedex_number": 70
  },
  {
    "name": "Victreebel",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Flycatcher",
    "pokedex_number": 71
  },
  {
    "name": "Tentacool",
    "type_1": "Water",
    "type_2": "Poison",
    "description": "Jellyfish",
    "pokedex_number": 72
  },
  {
    "name": "Tentacruel",
    "type_1": "Water",
    "type_2": "Poison",
    "description": "Jellyfish",
    "pokedex_number": 73
  },
  {
    "name": "Geodude",
    "type_1": "Rock",
    "type_2": "Ground",
    "description": "Rock",
    "pokedex_number": 74
  },
  {
    "name": "Graveler",
    "type_1": "Rock",
    "type_2": "Ground",
    "description": "Rock",
    "pokedex_number": 75
  },
  {
    "name": "Golem",
    "type_1": "Rock",
    "type_2": "Ground",
    "description": "Megaton",
    "pokedex_number": 76
  },
  {
    "name": "Ponyta",
    "type_1": "Fire",
    "description": "Fire Horse",
    "pokedex_number": 77
  },
  {
    "name": "Rapidash",
    "type_1": "Fire",
    "description": "Fire Horse",
    "pokedex_number": 78
  },
  {
    "name": "Slowpoke",
    "type_1": "Water",
    "type_2": "Psychic",
    "description": "Dopey",
    "pokedex_number": 79
  },
  {
    "name": "Slowbro",
    "type_1": "Water",
    "type_2": "Psychic",
    "description": "Hermit Crab",
    "pokedex_number": 80
  },
  {
    "name": "Magnemite",
    "type_1": "Electric",
    "type_2": "Steel",
    "description": "Magnet",
    "pokedex_number": 81
  },
  {
    "name": "Magneton",
    "type_1": "Electric",
    "type_2": "Steel",
    "description": "Magnet",
    "pokedex_number": 82
  },
  {
    "name": "Farfetch'd",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Wild Duck",
    "pokedex_number": 83
  },
  {
    "name": "Doduo",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Twin Bird",
    "pokedex_number": 84
  },
  {
    "name": "Dotrio",
    "type_1": "Normal",
    "type_2": "Flying",
    "description": "Triple Bird",
    "pokedex_number": 85
  },
  {
    "name": "Seel",
    "type_1": "Water",
    "description": "Sea Lion",
    "pokedex_number": 86
  },
  {
    "name": "Dewgong",
    "type_1": "Water",
    "type_2": "Ice",
    "description": "Sea Lion",
    "pokedex_number": 87
  },
  {
    "name": "Grimer",
    "type_1": "Poison",
    "description": "Sludge",
    "pokedex_number": 88
  },
  {
    "name": "Muk",
    "type_1": "Poison",
    "description": "Sludge",
    "pokedex_number": 89
  },
  {
    "name": "Shellder",
    "type_1": "Water",
    "description": "Bivalve",
    "pokedex_number": 90
  },
  {
    "name": "Cloyster",
    "type_1": "Water",
    "type_2": "Ice",
    "description": "Bivalve",
    "pokedex_number": 91
  },
  {
    "name": "Gastly",
    "type_1": "Ghost",
    "type_2": "Poison",
    "description": "Gas",
    "pokedex_number": 92
  },
  {
    "name": "Haunter",
    "type_1": "Ghost",
    "type_2": "Poison",
    "description": "Gas",
    "pokedex_number": 93
  },
  {
    "name": "Gengar",
    "type_1": "Ghost",
    "type_2": "Poison",
    "description": "Shadow",
    "pokedex_number": 94
  },
  {
    "name": "Onix",
    "type_1": "Rock",
    "type_2": "Ground",
    "description": "Rock Snake",
    "pokedex_number": 95
  },
  {
    "name": "Drowzee",
    "type_1": "Psychic",
    "description": "Hypnosis",
    "pokedex_number": 96
  },
  {
    "name": "Hypno",
    "type_1": "Psychic",
    "description": "Hypnosis",
    "pokedex_number": 97
  },
  {
    "name": "Krabby",
    "type_1": "Water",
    "description": "River Crab",
    "pokedex_number": 98
  },
  {
    "name": "Kingler",
    "type_1": "Water",
    "description": "Pincer",
    "pokedex_number": 99
  },
  {
    "name": "Voltorb",
    "type_1": "Electric",
    "description": "Ball",
    "pokedex_number": 100
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 101
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 102
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 103
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 104
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 105
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 106
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 107
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 108
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 109
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 110
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 111
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 112
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 113
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 114
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 115
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 116
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 117
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 118
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 119
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 120
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 121
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 122
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 123
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 124
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 125
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 126
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 127
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 128
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 129
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 130
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 131
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 132
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 133
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 134
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 135
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 136
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 137
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 138
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 139
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 140
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 141
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 142
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 143
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 144
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 145
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 146
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 147
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 148
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 149
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 150
  },
  {
    "name": "Bulbasaur",
    "type_1": "Grass",
    "type_2": "Poison",
    "description": "Seed",
    "pokedex_number": 151
  }
]

for pokemon in pokedex:
  requests.post(url, json=pokemon)