class TreasureHunt:

    def __init__(self, matrix: list):
        if type(matrix) is list and type(matrix[0]) is list:
            self.matrix = matrix
        else:
            self.matrix = None

    def calculate(self):
        if self.matrix:
            clues = [11]
            while True:
                coordinates = [int(x) for x in str(clues[-1]).strip()]
                current_data = self.matrix[coordinates[0]-1][coordinates[1]-1]
                if current_data == clues[-1]:
                    return clues
                else:
                    clues.append(current_data)
        else:
            return "Given false matrix"

    def print_result(self, clues: list):
        if self.matrix:
            print("Input table")
            for i in range(len(self.matrix)):
                print(" ".join([str(x) for x in self.matrix[i]]))
            print("\nOutput list")
            print(" ".join([str(x) for x in clues]))
        else:
            return "Given false matrix"
