# Solving N_Queens Problem Using Various Algorithms in Python

The N_Queens problem is a classic problem that lends itself for local search algorithms. In this problem, N queens are placed on an N × N chessboard, one queen per column. We assume that each queen can only move vertically (Up or Down) within her column of residence. 
You can find more information about the problem in this [wiki article](https://en.wikipedia.org/wiki/Eight_queens_puzzle). An example solution for 8 x 8 chessboard is shown:

![image](https://user-images.githubusercontent.com/90617686/159763749-91840b80-e77f-4937-9cbd-0cdfd19f316d.png)


The N_Queens.py file contains python solution codes to several algorithms that try to solve the problem. These algorithms are explained below.


## General Description

To represent the place of all queens, a one-dimensional array with N columns is created. In this array, columns are indexed from 0 to N-1 and each column contains a single number that describes the row location of the residing queen in that column.

To evaluate each state of the board, first, the maximal number of queen pairs in conflict is calculated as follows:

Maximum conflicts = 1 + 2 + ... + N-1 = (N-1 × N) / 2

Since the algorithms are doing ascending search, the evaluation score of each board is thus: Maximum conflicts - Total current conflict pairs

At last, since the algorithms might stuck in local optimum, after 1000 iterations the program ends and returns the result.


## Random Search

In random algorithm, on each iteration, the queen of each column is placed in a random row. The success rate of this algorithm is quite low, specially if N is large.


## Optimised Random Search

In this algorithm, on each iteraion, a new board is copied from the original, in which the queen of each column is placed in a random row. Only if the evaluation score of this new board is higher than the original board, the changes of the new board are applied to the original board.


## Simulated Annealing

This algorithm is an upgrade to the Optimised Random Search algorithm. If the new board created, changes in a way that the evaluation score increases, the changes are applied to the original board. However, if the evaluation score is decreased, with some probability the changes are applied to the original board. Since the algorithm here tries to find the global maximum, this probability is calculated as follows:

Probabilty = 
