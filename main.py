import numpy as np
import matplotlib.pyplot as plt
import math


def create_board(size):
    """

    :param size:
    :return: a two-dimensional numpy array of size 2**n x 2**n populated by zero values.
    """
    return np.zeros([2 ** size, 2 ** size])


def four_quadrants(board):

    result = []

    return result

def return_middle_squares(board):
    """

    :param board:
    :return: a list of tuples containing the coordinates of the centre values of the board.
    """

    result = []

    result.append(( 2**(math.log(len(board), 2) - 1) - 1, 2**(math.log(len(board), 2) - 1) - 1))
    result.append((2 ** (math.log(len(board), 2) - 1) - 1, 2 ** (math.log(len(board), 2) - 1)))
    result.append((2 ** (math.log(len(board), 2) - 1), 2 ** (math.log(len(board), 2) - 1) - 1))
    result.append((2 ** (math.log(len(board), 2) - 1), 2 ** (math.log(len(board), 2) - 1)))
    return result


def paint(board):
    """

    :param board:
    :return: nil
    """
    plt.imshow(board, interpolation="nearest")


def paint_two_boards(first_board, second_board):
    """


    :param first_board:
    :param second_board:
    :return: nil
    """
    f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=True)
    ax1.imshow(first_board)
    ax2.imshow(second_board)

if __name__ == '__main__':
    my_board = create_board(3)
    # my_board[0][0] = 1
    # my_board[1][1] = 2
    # my_board[2][2] = 33

    middle = return_middle_squares(my_board)

    print(math.log(8, 2))

    for i in range(len(middle)):
        my_board[middle[i]] = i + 5

    second_board = create_board(2)

    #paint_two_boards(my_board, second_board)
    paint(my_board)


    plt.title("Paving algorithm")
    plt.show()
