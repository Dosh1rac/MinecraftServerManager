class Player:
    def __init__(self, nickname, uuid):
        self.nickname = nickname
        self.uuid = uuid

    def __str__(self):
        return self.nickname