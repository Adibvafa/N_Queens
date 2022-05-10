"""
File: N_Queens.py
-----------------
Solving N_Queens Using Various Algorithms in Python!
You can find detailed explanations for each algorithm in README.md file.
"""

import math
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

MAXQ = 100
MAX_ITER = 1000


def in_conflict(column, row, other_column, other_row):
    """
    Checks if two locations are in conflict with each other.
    :param column: Column of queen 1.
    :param row: Row of queen 1.
    :param other_column: Column of queen 2.
    :param other_row: Row of queen 2.
    :return: True if the queens are in conflict, else False.
    """
    if column == other_column:
        return True  # Same column
    if row == other_row:
        return True  # Same row
    if abs(column - other_column) == abs(row - other_row):
        return True  # Diagonal

    return False


def in_conflict_with_another_queen(row, column, board):
    """
    Checks if the given row and column correspond to a queen that is in conflict with another queen.
    :param row: Row of the queen to be checked.
    :param column: Column of the queen to be checked.
    :param board: Board with all the queens.
    :return: True if the queen is in conflict, else False.
    """
    for other_column, other_row in enumerate(board):
        if in_conflict(column, row, other_column, other_row):
            if row != other_row or column != other_column:
                return True
    return False


def count_conflicts(board):
    """
    Counts the number of queens in conflict with each other.
    :param board: The board with all the queens on it.
    :return: The number of conflicts.
    """
    cnt = 0

    for queen in range(0, len(board)):
        for other_queen in range(queen + 1, len(board)):
            if in_conflict(queen, board[queen], other_queen, board[other_queen]):
                cnt += 1

    return cnt


def evaluate_state(board):
    """
    Evaluation function. The maximal number of queens in conflict can be:
    1 + 2 + 3 + 4 + ... + (nqueens-1) = ((nqueens-1) * nqueens) / 2
    Since we want to do ascending local searches, the evaluation function returns
    (((nqueens-1) * nqueens) / 2) - countConflicts().
    :param board: list/array representation of columns and the row of the queen on that column
    :return: evaluation score
    """
    return (len(board) - 1) * len(board) / 2 - count_conflicts(board)


def print_board(board):
    """
    Prints the board in a human-readable format in the terminal.
    :param board: The board with all the queens.
    """
    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += 'Q' if in_conflict_with_another_queen(row, column, board) else 'q'
            else:
                line += '.'
        print(line)
    print("")


def init_board(nqueens):
    """
    :param nqueens integer for the number of queens on the board
    :returns list/array representation of columns and the row of the queen on that column
    """
    board = []

    for column in range(nqueens):
        board.append(random.randint(0, nqueens - 1))

    return board


"""
------------------------------------------------------ ALGORITHMS ------------------------------------------------------
"""


def Random_Search(board):
    """
    Random Search algorithm in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        for column, row in enumerate(board):
            board[column] = random.randint(0, len(board) - 1)

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def Optimized_Random_Search(board):
    """
    Optimized Random Search algorithm in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        for column, row in enumerate(board):
            previous_board_score = evaluate_state(board)
            board[column] = random.randint(0, len(board) - 1)
            if evaluate_state(board) < previous_board_score:
                board[column] = row

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def Simulated_Annealing(board):
    """
    Simulated Annealing algorithm in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    temp = 1000
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) < optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        rand_col = random.randint(0, len(board) - 1)
        rand_row = random.randint(0, len(board) - 1)
        new_board = board.copy()
        new_board[rand_col] = rand_row

        board_score = evaluate_state(board)
        new_board_score = evaluate_state(new_board)

        if new_board_score >= board_score:
            board = new_board

        else:
            score_change = new_board_score - board_score
            probability = math.exp(score_change / temp)
            if random.random() < probability:
                board = new_board

        temp *= 0.95
        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def Hill_Climbing(board):
    """
    Hill Climbing algorithm in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        max_score_of_each_column = []
        row_resulting_in_max_score = []

        for col in range(len(board)):
            col_scores = []

            for row in range(len(board)):
                new_board = board.copy()
                new_board[col] = row
                col_scores.append(evaluate_state(new_board))

            if max(col_scores) > evaluate_state(board):
                max_score_of_each_column.append(max(col_scores))
                row_resulting_in_max_score.append(np.argmax(col_scores))
            else:
                max_score_of_each_column.append(False)
                row_resulting_in_max_score.append(False)

        if max(max_score_of_each_column):
            maximizing_col = np.argmax(max_score_of_each_column)
            maximizing_row = row_resulting_in_max_score[maximizing_col]
            board[maximizing_col] = maximizing_row

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def Hill_Climbing_Constant_Random(board):
    """
    Hill Climbing + Constant Random Probability in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        if random.random() <= 0.23:
            rand_col = random.sample(range(len(board)), 2)
            for col in rand_col:
                board[col] = random.randint(0, len(board) - 1)

        else:
            max_score_of_each_column = []
            row_resulting_in_max_score = []

            for col in range(len(board)):
                col_scores = []

                for row in range(len(board)):
                    new_board = board.copy()
                    new_board[col] = row
                    col_scores.append(evaluate_state(new_board))

                if max(col_scores) > evaluate_state(board):
                    max_score_of_each_column.append(max(col_scores))
                    row_resulting_in_max_score.append(np.argmax(col_scores))
                else:
                    max_score_of_each_column.append(False)
                    row_resulting_in_max_score.append(False)

            if max(max_score_of_each_column):
                maximizing_col = np.argmax(max_score_of_each_column)
                maximizing_row = row_resulting_in_max_score[maximizing_col]
                board[maximizing_col] = maximizing_row

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def Hill_Climbing_Changing_Random(board):
    """
    Hill Climbing + Changing Random Probability in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    rand_prob = 0.23
    optimum = (len(board) - 1) * len(board) / 2
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        if random.random() <= rand_prob:
            rand_col = random.sample(range(len(board)), 2)
            for col in rand_col:
                board[col] = random.randint(0, len(board) - 1)

        else:
            max_score_of_each_column = []
            row_resulting_in_max_score = []

            for col in range(len(board)):
                col_scores = []

                for row in range(len(board)):
                    new_board = board.copy()
                    new_board[col] = row
                    col_scores.append(evaluate_state(new_board))

                if max(col_scores) > evaluate_state(board):
                    max_score_of_each_column.append(max(col_scores))
                    row_resulting_in_max_score.append(np.argmax(col_scores))
                else:
                    max_score_of_each_column.append(False)
                    row_resulting_in_max_score.append(False)

            if max(max_score_of_each_column):
                maximizing_col = np.argmax(max_score_of_each_column)
                maximizing_row = row_resulting_in_max_score[maximizing_col]
                board[maximizing_col] = maximizing_row

            rand_prob *= 0.999

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def Optimized_Hill_Climbing(board):
    """
    Optimized Hill Climbing algorithm in Readme file.
    :param board: list/array representation of columns and the row of the queen on that column
    """
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    previous_board_score = 0
    evaluation = [evaluate_state(board)]

    while evaluate_state(board) != optimum:
        i += 1
        print(f"Iteration {i}: Evaluation = {evaluate_state(board)}")

        if i == MAX_ITER:  # Give up after MAX_ITER tries.
            break

        if evaluate_state(board) == previous_board_score:
            previous_board_score = evaluate_state(board)
            rand_col = random.sample(range(len(board)), 4)
            for col in rand_col:
                board[col] = random.randint(0, len(board) - 1)

        else:
            previous_board_score = evaluate_state(board)
            max_score_of_each_column = []
            row_resulting_in_max_score = []

            for col in range(len(board)):
                col_scores = []

                for row in range(len(board)):
                    new_board = board.copy()
                    new_board[col] = row
                    col_scores.append(evaluate_state(new_board))

                if max(col_scores) > evaluate_state(board):
                    max_score_of_each_column.append(max(col_scores))
                    row_resulting_in_max_score.append(np.argmax(col_scores))
                else:
                    max_score_of_each_column.append(False)
                    row_resulting_in_max_score.append(False)

            if max(max_score_of_each_column):
                maximizing_col = np.argmax(max_score_of_each_column)
                maximizing_row = row_resulting_in_max_score[maximizing_col]
                board[maximizing_col] = maximizing_row

        evaluation.append(evaluate_state(board))

    if evaluate_state(board) == optimum:
        print('\nSolved Puzzle!')

    print('\nFinal State:')
    print_board(board)

    plot(i, evaluation, board, optimum)


def plot(i, evaluation, board, optimum):
    """
    Plots the resulting evaluation on each iteration.
    :param i: Total number of iterations
    :param evaluation: List of evaluation score
    :param board: The final board of queens
    :param optimum: The highest possible score
    :return:
    """
    # For results which break the loop in the algorithm
    if i == MAX_ITER:
        evaluation.append(evaluate_state(board))

    plt.plot(range(i + 1), evaluation, 'teal')
    plt.plot(i, optimum, 'ro')

    plt.xlabel("Iterations")
    plt.ylabel("Evaluation Score")
    plt.show()


def main():
    """
    Main function that will parse input and call the appropriate algorithm.
    """
    try:
        if len(sys.argv) != 2:
            raise ValueError

        n_queens = int(sys.argv[1])
        if n_queens < 1 or n_queens > MAXQ:
            raise ValueError

    except ValueError:
        print('Usage: python n_queens.py NUMBER')
        return False

    print('Choose Your Algorithm:')
    algorithm = input('1:Random,  '
                      '2:Optimized Random Search,  '
                      '3:Simulated Annealing,  '
                      '4:Hill Climbing,  '
                      '5:Hill Climbing Constant Random,  '
                      '6:Hill Climbing Changing Random,  '
                      '7:Optimized Hill Climbing\n')

    try:
        algorithm = int(algorithm)
        if algorithm not in range(1, 8):
            raise ValueError

    except ValueError:
        print('Please input a number in the given range!')
        return False

    board = init_board(n_queens)
    print('\nInitial Board:')
    print_board(board)

    algorithms = {1: Random_Search,
                  2: Optimized_Random_Search,
                  3: Simulated_Annealing,
                  4: Hill_Climbing,
                  5: Hill_Climbing_Constant_Random,
                  6: Hill_Climbing_Changing_Random,
                  7: Optimized_Hill_Climbing}

    algorithms[algorithm](board)


# This line is the starting point of the program.
if __name__ == "__main__":
    main()
