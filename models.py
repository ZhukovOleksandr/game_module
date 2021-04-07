import random
from termcolor import colored as clrd
from exceptions import EnemyDown, GameOver
from settings import character_for_attack, player_hit_points, win, lose


class Enemy:
    """
    Class include methods:
        select_attack - @staticmethod that selects enemy attack using random module,

        decrease_lives - decreasing hit points of enemy object, if the enemy object has "0" hit points
        raise EnemyDown error,

    The class has constructor, which takes only one value - "level" from settings.py
    """

    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        attack_list = (list(character_for_attack.values()))
        attack = random.choice(attack_list)
        return attack

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    Class include methods:
        fight - @staticmethod that using in "attack" method; contains two attributes: "attack" and "defence",

        decrease_lives - decreasing hit points of player object, if the player object has "0" hit points
        raise GameOver error,

        attack and defence methods use "fight" method for calculating result of event.

    The class has constructor, which takes 4 attributes:
        name - input name from user,
        allowed_attacks  - attribute equal to "character_for_attack" by default and takes data from settings.py,
        lives  - attribute equal to "player_hit_points" by default and takes data from settings.py

    """

    def __init__(self, name, allowed_attacks=character_for_attack, lives=player_hit_points, score=0):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver(self.name, self.score)

    def attack(self, enemy_object):
        print(f"I love the smell of napalm in the morning! Time to attack!\n "
              f"Please, chose attack option:\n "
              f"{clrd(self.allowed_attacks, 'green')}")
        while True:
            try:
                user_attack = self.allowed_attacks.get(int(input()))
                if user_attack is None:
                    print("It is incorrect value, try again:")
                    continue
            except ValueError:
                print("It is incorrect value, try again:")
                continue
            else:
                break

        fight_result = str(user_attack) + '-' + str(enemy_object.select_attack())
        enemy_attack = fight_result.split('-')
        print(f"Enemy chose: {clrd(enemy_attack[1], 'green')}")
        if fight_result in win:
            print(clrd("Your attack was successfully", 'green'))
            enemy_object.decrease_lives()
        elif fight_result in lose:
            print(clrd("You missed!", 'red'))
        else:
            print(clrd("It's a draw!", 'white'))

    def defence(self, enemy_object):
        print(f"\nBe careful, {self.name}, they are in the trees!\n "
              f"Please, choose defence option:\n"
              f"{clrd(self.allowed_attacks, 'green')}")
        while True:
            try:
                user_attack = self.allowed_attacks.get(int(input()))
                if user_attack is None:
                    print("It is incorrect value, try again:")
                    continue
            except ValueError:
                print("It is incorrect value, try again:")
                continue
            else:
                break

        fight_result = str(enemy_object.select_attack()) + '-' + str(user_attack)
        enemy_attack = fight_result.split('-')
        print(f"Enemy chose: {clrd(enemy_attack[0], 'green')}")
        if fight_result in win:
            print(clrd("you took that punch!", 'red'))
            return self.decrease_lives()
        elif fight_result in lose:
            print(clrd("Your defence was successfully", 'green'))
        else:
            print(clrd("It's a draw!", 'white'))
