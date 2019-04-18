class Game(object):
    def __init__(self):
        self.__rolls__ = [0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0,
                          0]
        self.__currentRoll__ = 0

    # keep track of rolls
    def roll(self, pins):
        self.__rolls__[self.__currentRoll__] = pins
        self.__currentRoll__ += 1

    # calculate score
    def score(self):
        score = 0
        rollIndex = 0
        for frame in range(0, 10):
            if self.is_strike(rollIndex):
                score += 10 + self.strike_bonus(rollIndex)
                rollIndex += 1
            elif self.is_spare(rollIndex):
                score += 10 + self.spare_bonus(rollIndex)
                rollIndex += 2
            else:
                score += self.sum_of_balls_in_frame(rollIndex)
                rollIndex += 2
        return score

    # game rules
    def is_strike(self, rollIndex):
        return self.__rolls__[rollIndex] == 10

    def strike_bonus(self, rollIndex):
        return self.__rolls__[rollIndex + 1] + self.__rolls__[rollIndex + 2]

    def is_spare(self, rollIndex):
        return self.__rolls__[rollIndex] + self.__rolls__[rollIndex + 1] == 10

    def spare_bonus(self, rollIndex):
        return self.__rolls__[rollIndex + 2]

    def sum_of_balls_in_frame(self, rollIndex):
        return self.__rolls__[rollIndex] + self.__rolls__[rollIndex + 1]


# Execute
if __name__ == '__main__':
    g = Game()
    for i in range(0, 12):
        g.roll(10)
    print(g.score())
