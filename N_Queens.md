# Solving N_Queens Problem Using Various Algorithms in Python

The N_Queens problem is a classic problem that lends itself for local search algorithms. In this problem, N queens are placed on an N × N chessboard, one queen per column. We assume that each queen can only move vertically (Up or Down) within her column of residence. 
You can find more information about the problem in this [Wikipedia article](https://en.wikipedia.org/wiki/Eight_queens_puzzle). An example solution for 8 x 8 chessboard is shown:

![image](https://user-images.githubusercontent.com/90617686/159763749-91840b80-e77f-4937-9cbd-0cdfd19f316d.png)


The N_Queens.py file contains python solution codes to several algorithms that try to solve the problem. These algorithms are explained below.


## General Description

To represent the place of all queens, a one-dimensional array with N columns is created. In this array, columns are indexed from 0 to N-1 and each column contains a single number that describes the row location of the residing queen in that column.

To evaluate each state of the board, first, the maximal number of queen pairs in conflict is calculated as follows:

Maximum conflicts = 1 + 2 + ... + N-1 = (N-1 × N) / 2

Since the algorithms are doing ascending search, the evaluation score of each board is thus:

Evaluation Score = Maximum conflicts - Total current conflict pairs

At last, the program ends when the maximum evaluation score (which is just the number of Maximum conflicts) is reached. Since the algorithms might stuck in local optimum, if the global optimum is not found, the program ends after 1000 iterations. Afterwards, the resulting board, evaluation score and a graph demonstrating evaluation score dduring iterations is shown.


## Random Search

In random algorithm, on each iteration, the queen of each column is placed in a random row. The success rate of this algorithm is quite low, specially if N is large.


## Optimised Random Search

In this algorithm, on each iteraion, a new board is copied from the original, in which the queen of each column is placed in a random row. Only if the evaluation score of this new board is higher than the original board, the changes of the new board are applied to the original board.


## Simulated Annealing

This algorithm is an upgrade to the Optimised Random Search algorithm. If the new board created, changes in a way that the evaluation score increases, the changes are applied to the original board. However, if the evaluation score is decreased, with some probability the changes are applied to the original board. Since the algorithm here tries to find the global maximum, this probability is calculated as follows:

<img src='https://user-images.githubusercontent.com/90617686/159782039-d45197cc-1b9b-4a5e-a2c6-72cdb93d59a4.png' width="200" height="50"/>

Here, e is the Euler's number, ∆S is the change in evaluation score (Negative since the evaluation score has decreased) and T is tempreature. Temperature is just a fansy word for a variable that decreases after each iteraition. Thus, in primary iterations, this number is high and the probability of accepting decreasing new boards is high. On the contrary, as T decreases, the probability of accepting decreasing new boards decreases, as if the algorithm stops sudden changes and focuses on reaching the local ahead. Note that in general, worse new boards which drastically decrease the evaluation score are less probable to be accepted.


## Hill Climbing

This algorithm is in a sense hiruistic, as we perform the best move on each iteration. That is, we calculate the evaluation score of all possible new boards in which the location of a single queen has changed. Then, the new board of maximum evaluaiton score is chosen and the changes are applied to the original board. If there exist more than one new board having maximum evaluation score, the first one found is used due to using python built-in max function.

This algorithm is not efficient and has a high order time complexity. Furthermore, it is quite valunrable to local optimums. In general, on each iteration we make the best move (Climb one step up th hill) and we stop whene there is no better move than our current move (Stop at the optimum). This way we are able to easily find an optimum, however, we cannot avoid local optimums.


## Hill Climbing + Constant Random Probability

This algorithm is an add-on to Hill Climbing to decrease the chance of getting stuck in local optimums. On each iteration, with a constant probaility of 23%, instead of following hill climbing, 2 random queens are chosen and are moved to random rows. This subtle change enables the algorithm to "shake" iself once in a while and hopefully avoid some local optimums.

The reason behind 23% probabilty and 2 random queens is discussed in Discussion file.


## Hill Climbing + Changing Random Probability

This algorithm is an add-on to Hill Climbing to decrease the chance of getting stuck in local optimums. By somehow combining the idea of hill climbing with simulated annealing, on each iteration, with a changing probaility, instead of following hill climbing, 2 random queens are chosen and are moved to random rows. This subtle change enables the algorithm to "shake" iself once in a while and hopefully avoid some local optimums. This changing probability is calculated as follows:

<img src='https://user-images.githubusercontent.com/90617686/159782039-d45197cc-1b9b-4a5e-a2c6-72cdb93d59a4.png' width="200" height="50"/>


## Optimised Hill Climbing

In another attempt, the algorithm is changed inorder to avoid local optimums. This algorithm has memory, that is, it stored the evaluation score of the previous board and the current board. If these two scores are equal, it means the algorithm is stuck in local optimum and thus instead of following hill climbing, 4 random queens are chosen and are moved to random rows. This modification enables the algorithm to move randomly to another state hen stuck in local optimim

The reason behing 4 random queens is discussed in Discussion file.


## Genetics Algorithm











