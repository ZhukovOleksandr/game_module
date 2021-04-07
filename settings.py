"""
The settings.py contains values that are using for set parameters in models.py and game.py

character_for_attack - dictionary that contains allowed attacks for game process

player_hit_points - variable that contains value of player hit points

start_enemy_level - variable that contains value of enemy hit points


"""

character_for_attack = {1: 'wizard',
                        2: 'warrior',
                        3: 'bandit'
                        }
player_hit_points = 5
start_enemy_level = 1

win = ['wizard-warrior', 'warrior-bandit', 'bandit-wizard']
lose = ['warrior-wizard', 'bandit-warrior', 'wizard-bandit']

