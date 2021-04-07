from termcolor import colored as clrd
from exceptions import EnemyDown, GameOver
from models import Player, Enemy
from settings import start_enemy_level


def play():
    """
    play method contains logic of game process
    """
    # start_button = str(input("Please type 'start' to begin the game:\n").lower())
    while True:
        start_button = str(input("Please type 'start' to begin the game:\n").lower())
        if start_button == 'start':
            break
        else:
            print(f"{clrd('Incorrect command', 'red')}")
            continue

    win_count = 0
    round_count = 1
    # Name input
    player_name = str(input("Who are you? Say your name?\n"))

    # Инициализация игрока и врага
    player = Player(player_name)
    enemy_object = Enemy(start_enemy_level)
    print(f"Your hit points: {clrd(player.lives, 'red')}")
    print(f"Enemy hit points: {clrd(enemy_object.lives, 'red')}")
    print(f"\n------Round {round_count}------")
    # Ход игры
    while player.lives != 0:
        try:
            player.attack(enemy_object)
            print(f"Your hit points: {clrd(player.lives, 'red')}\n"
                  f"Enemy hit points: {clrd(enemy_object.lives, 'red')}")
            player.defence(enemy_object)
            print(f"Your hit points: {clrd(player.lives, 'red')}\n"
                  f"Enemy hit points: {clrd(enemy_object.lives, 'red')}")
        except EnemyDown:
            round_count += 1
            win_count += 1
            print(clrd("Enemy down!", 'green'))
            player.lives += 1
            player.score += 5
            print(f"\n------Round {round_count}------")
            enemy_object = Enemy(win_count + start_enemy_level)
            print(f"New enemy was created, he has {clrd(enemy_object.lives, 'red')} hit points")
            print(f"You have {clrd(player.lives, 'red')} hit points")

        except GameOver as err:
            print(clrd("You lose!", 'red'))
            err.write_score(player)


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print("The game was interrupted")
    finally:
        print("Good bye!")
