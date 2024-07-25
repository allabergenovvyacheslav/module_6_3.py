class Horse:

    def __init__(self, x_distance, sound):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.dx = self.x_distance + dx
        return dx

h1 = Horse(0, 'Frrr')
h1.run(12)
print(h1)
