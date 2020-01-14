import pytest
from oop_variant import TreasureHunt
from functional_variant import find_way, hunt_treasure


def test_oop_implementation_1():
    matrix = [[55, 14, 25, 52, 21],
              [44, 31, 11, 53, 43],
              [24, 13, 45, 12, 34],
              [42, 22, 43, 32, 41],
              [51, 23, 33, 54, 15]]
    obj = TreasureHunt(matrix)
    clues = obj.calculate()
    obj.print_result(clues)

    assert type(clues) == list
    assert len(clues) == 9
    assert clues == [11, 55, 15, 21, 44, 32, 13, 25, 43]


def test_oop_implementation_2():
    matrix = [[11, 14, 25, 52, 21],
              [44, 31, 11, 53, 43],
              [24, 13, 45, 12, 34],
              [42, 22, 43, 32, 41],
              [51, 23, 33, 54, 15]]
    obj = TreasureHunt(matrix)
    clues = obj.calculate()

    assert clues == [11]
    assert len(clues) == 1
    assert type(clues) == list


def test_oop_implementation_3():
    matrix = [11, 14, 25, 52, 21]
    obj = TreasureHunt(matrix)
    clues = obj.calculate()

    assert obj.matrix is None
    assert clues == "Given false matrix"
    assert type(clues) == str
    assert obj.print_result(clues) == "Given false matrix"


def test_oop_implementation_4():
    matrix = 12
    obj = TreasureHunt(matrix)
    clues = obj.calculate()

    assert obj.matrix is None
    assert clues == "Given false matrix"
    assert type(clues) == str
    assert obj.print_result(clues) == "Given false matrix"


def test_functional_implementation_1():
    matrix = [[55, 14, 25, 52, 21],
              [44, 31, 11, 53, 43],
              [24, 13, 45, 12, 34],
              [42, 22, 43, 32, 41],
              [51, 23, 33, 54, 15]]
    res_data = find_way(matrix)

    assert type(res_data) == list
    assert len(res_data) == 9
    assert res_data == [11, 55, 15, 21, 44, 32, 13, 25, 43]


def test_functional_implementation_2():
    matrix = [[11, 14, 25, 52, 21],
              [44, 31, 11, 53, 43],
              [24, 13, 45, 12, 34],
              [42, 22, 43, 32, 41],
              [51, 23, 33, 54, 15]]
    res_data = find_way(matrix)
    hunt_treasure(matrix)

    assert res_data == [11]
    assert len(res_data) == 1
    assert type(res_data) == list


def test_functional_implementation_3():
    matrix = [11, 14, 25, 52, 21]
    res_data = find_way(matrix)

    assert res_data == "Invalid data received"
    assert type(res_data) == str
    assert hunt_treasure(matrix) == "Invalid data received"


def test_functional_implementation_4():
    matrix = 12
    res_data = find_way(matrix)

    assert res_data == "Invalid data received"
    assert type(res_data) == str
    assert hunt_treasure(matrix) == "Invalid data received"
