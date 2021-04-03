import datetime


class GameOver(Exception):
    """
    The GameOver class is used by "decrease_lives" method. It is called when the player loses.
    this class has oly one method  - "write_score".
    Write_score is used for write game result (player name, score, date and type to .txt file"
    """

    time = datetime.datetime.today()

    def write_score(self, player_obj):
        with open('score.txt', 'a') as scores_list:
            scores_list.write(f"{player_obj.name}: {player_obj.score} | {self.time} \n")
            scores_list.close()


class EnemyDown(Exception):

    """"
    This class is empty and called when enemy lives equal to "0"
    """
