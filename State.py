class State:

    def __init__(self, initial_values, parent=None):
        self.value = initial_values
        self.parent = parent
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    def generate_neighbours(self):  # creates a list of neighbouring states

        actions = ((0, 1, 2, -3), (6, 7, 8, 3), (0, 3, 6, -1), (2, 5, 8, 1))  # up,down,left and right
        neighbours = []
        empty_position = self.value.index(0)

        for position in actions:
            if empty_position not in position[:3]:
                temp_list = self.value[:]
                temp_list[empty_position + position[3]], temp_list[empty_position] = temp_list[empty_position], temp_list[empty_position + position[3]]
                neighbours.append(State(temp_list, self))

        return neighbours

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()