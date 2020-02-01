class Game(object):
    top_score = 0

    def __init__(self, name):
        self.name = name
        print("玩家：%s 进入游戏" % name)

    @staticmethod
    def show_help():
        print("show help")

    @classmethod
    def show_top_score(cls):
        print("top score: %.2f" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏" % self.name)


Game.show_help()
Game.show_top_score()

player1 = Game("小王")
player2 = Game("小李")

player1.start_game()
player2.start_game()
