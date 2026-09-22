class FootBallTeam:
    def __init__(self):
        self.ftbltm=["player1","player2","player3","player4","player5","player6","player7","player8","player9","player10","player11"]
    def __len__(self):
        return len(self.ftbltm)
fbt=FootBallTeam()
print(len(fbt))