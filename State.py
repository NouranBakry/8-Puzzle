
""""" This class defines the initial positions and moving function in each state.
        It also has the function used to expand each state and generate its children """


class State:

    def __init__(self, initial_values, parent=None):
        self.value = initial_values
        self.parent = parent
        self.hash_value = self.generate_hash()
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    #   expands each state sent to it and generates the list of children
    def generate_neighbours(self):
        # Defines the positions for each state UP,DOWN,LEFT and Right and their corresponding step size
        actions = ((0, 1, 2, -3), (6, 7, 8, 3), (0, 3, 6, -1), (2, 5, 8, 1))
        neighbours = []
        empty_position = self.value.index(0)

        for position in actions:
            if empty_position not in position[:3]:

                temp_list = self.value[:]
                temp_list[empty_position + position[3]], temp_list[empty_position] = \
                    temp_list[empty_position], temp_list[empty_position + position[3]]

                neighbours.append(State(temp_list, self))

        return neighbours

    #   Generates a hash code for each state which is a list sent to it; this helps to speed up the search
    def generate_hash(self):
        hash_val = 0
        for val in self.value:
            hash_val += 101*hash_val + val
        return hash_val

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.depth < other.depth
