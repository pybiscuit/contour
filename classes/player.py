
class Player:

    def __init__(self, pg_shape):
        self.id = 42
        self.x = 0
        self.y = 0
        self.coords = (self.x,self.y)
        self.shape = pg_shape

    def update(self, events):
        self.x = events[0]
        self.y = events[1]
        self.shape[1] = (self.shape[1][0] + self.x, self.shape[1][1] + self.y)