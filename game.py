from termcolor import colored as clrd
from exceptions import EnemyDown, GameOver
from models import Player, Enemy
from settings import start_enemy_level


def play():
    """
    play method contains logic of game process
    """
    win_count = 0
    raund_count = 1
    # Name input
    player_name = str(input("Who are you? Say your name?\n"))

    # Инициализация игрока и врага
    player = Player(player_name)
    enemy_object = Enemy(start_enemy_level)
    print(f"Your hit points: {clrd(player.lives, 'red')}")
    print(f"Enemy hit points: {clrd(enemy_object.lives, 'red')}")
    print(f"\n------Raund {raund_count}------")
    # Ход игры
    while player.lives != 0:
        try:
            player.attack(enemy_object)
            print(f"Your hit points: {clrd(player.lives, 'red')}")
            print(f"Enemy hit points: {clrd(enemy_object.lives, 'red')}")
            player.defence(enemy_object)
            print(f"Your hit points: {clrd(player.lives, 'red')}")
            print(f"Enemy hit points: {clrd(enemy_object.lives, 'red')}")
        except EnemyDown:
            raund_count += 1
            win_count += 1
            print(clrd("Enemy down!", 'green'))
            player.lives += 1
            player.score += 5
            enemy_object = Enemy(win_count + start_enemy_level)
            print(f"New enemy has {clrd(enemy_object.lives, 'red')} hit points")
            print(f"\n------Raund {raund_count}------")
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
