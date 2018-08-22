class Table:
    def __init__(self, board=None, size=2, players=None):
        self.board = board
        self.size = size
        self.players = players

    def __str__(self):
        representation = str(self.board)
        return representation
