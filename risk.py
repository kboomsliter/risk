# RISK classes

class Player:
    def __init__(self, name):
        self.name = name
        # order and color to be assigned during init phase of game play
        
class PlayerColors:
    def __init__(self):
        self.colors = ['red', 'blue', 'green', 'yellow']

    def assign(self, color, player):
        player.color = color
        self.colors.remove(color)
    
class Continent:
    def __init__(self, name, color, bonus):
        self.name = name
        self.color = color
        self.bonus = bonus
        # TODO how to define relationship to children (territories)?

class Territory:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        color = self.continent.color  # TODO does this work?
        borders = [] # assign other territory objects or names


