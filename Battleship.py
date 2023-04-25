# SEA BATTLE
import numpy as np

field = input("Enter field:")


def validate_battlefield(field):
    ships = {2: 3,
             3: 2,
             4: 1
             }

    ships_counter = {2: 0,
                     3: 0,
                     4: 0
                     }

    np_field = np.array(field)
    np_transp = np.transpose(np_field)

    # check total number of cells with ships
    if np.sum(np_field) != 20:
        return False

    # check collisions
    for i in range(1, 10):
        for j in range(9):
            if np_field[i, j] == np_field[i - 1, j + 1] == 1:
                return False

    for i in range(9):
        for j in range(9):
            if np_field[i, j] == np_field[i + 1, j + 1] == 1:
                return False

    # verify the correctness of long ships (> 1 dock length)
    for i in range(10):
        lenship = 0
        for j in range(10):
            if np_field[i, j] == 1:
                lenship += 1
                if j == 9 and lenship > 1:
                    ships_counter[lenship] += 1
            else:
                if lenship > 1:
                    ships_counter[lenship] += 1
                lenship = 0

    for i in range(10):
        lenship = 0
        for j in range(10):
            if np_transp[i, j] == 1:
                lenship += 1
                if j == 9 and lenship > 1:
                    ships_counter[lenship] += 1
            else:
                if lenship > 1:
                    ships_counter[lenship] += 1
                lenship = 0

    return True if ships_counter == ships else False


# field = [
#     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
#     [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
#     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
# ]

print(validate_battlefield(field))


