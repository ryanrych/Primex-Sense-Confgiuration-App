class Hardware:
    def __init__(self):
        self.t101 = 0
        self.t102 = 0
        self.a100 = 0
        self.a120 = 0
        self.e121 = 0
        self.e122 = 0
        self.e123 = 0
        self.totalPoints = 0

    def getPrice(self):
        return (self.t101 * 446) + (self.t102 * 605) + (self.a100 * 315) + (self.a120 * 749) + (self.e121 * 304) + (self.e122 * 338) + (self.e123 * 439)