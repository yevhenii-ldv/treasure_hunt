def find_way(matrix: list, clues=None):
    if type(matrix) is list and type(matrix[0]) is list:
        if clues is None:
            clues = [11]
        coordinates = [int(x) for x in str(clues[-1]).strip()]
        current_data = matrix[coordinates[0] - 1][coordinates[1] - 1]
        if current_data == clues[-1]:
            return clues
        else:
            clues.append(current_data)
            return find_way(matrix, clues=clues)
    else:
        return "Invalid data received"


def hunt_treasure(matrix: list):
    if type(matrix) is list and type(matrix[0]) is list:
        print("Input table")
        for i in range(len(matrix)):
            print(" ".join([str(x) for x in matrix[i]]))
        clues = find_way(matrix)
        print("\nOutput list")
        print(" ".join([str(x) for x in clues]))
    else:
        return "Invalid data received"
