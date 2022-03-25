# Discussion

## Hill Climbing + Constant Random Probability

Two parameters needed some experimentation to come up with. One is the probability of acting random (P), and the other is the number of queens changed in a random action (Q). Based on the following results, 23% and 2 were the most useful numbers. Interestingly, as the number of queens (N) increased, the number of queens which should change in a random iteration (Q) stayed the same. The author believes, as N increases, there is a need for more queens to change, but at the same time each queen affects a higher number of relationships with other queens, and thus, there would not be any need to increase Q. In other words, each queen is more valuable and satisfies our need for a more dramatic change to the board.

To test and find the optimum numbers, a board of size 8 (N = 8) was chosen, and with a maximum iteration number of 1000 (Program ends after 1000 tries if not successful), the mean result for 10 independent runs was recorded. In the begging, instead of experimentation with some constant number of queens, a certain percentage (%) of queens were chosen to be relocated randomly on each random iteration. The product of % and N is truncated to reach Q by the program. Prob is the probability of acting randomly (P).

![image](https://user-images.githubusercontent.com/90617686/159960365-d08b1f72-8bfe-40d9-9a7b-22b50fb7c3f4.png)

Surprisingly, when N = 8, even high values of % could give acceptable results, however, high values of P drastically decreased the success rate. To reach more accurate results, the same experiment was repeated with N = 16.

![image](https://user-images.githubusercontent.com/90617686/159958729-39f7f10b-dd55-4201-a787-afd80e7f4339.png)

These new results demonstrated that in addition to a small %, P should also be small. The best results were obtained when P was around 0.1 to mid-way 0.2 - 0.3 and thus, the experiment was repeated with P ranging from 0.02 to 0.24.

![image](https://user-images.githubusercontent.com/90617686/159960440-e8606308-993c-466d-ba73-b000065ec8b6.png)

Based on the results, the optimum range for % was around 0.2 - 0.3. Thus, the experiment was repeated with P ranging from 0.06 - 0.28 and % ranging from 0.125 - 0.45. Note that the product of % and N is truncated to reach an integer number of queens to be relocated randomly. Percentages pointing toward the same number are colored the same. Each result is the mean of 20 runs. The max number of iterations was also decreased to 700.

![image](https://user-images.githubusercontent.com/90617686/159961980-6c3eb7d7-1f74-4a6e-bcbf-2495c713f03f.png)

Based on the above results, a percentage resulting in changing 2 queens is optimum when N = 16. However, the optimum P could not be decided due to noise from success rates obtained from large %. Thus, part of the results where 2 queens changed was sliced and means were calculated specifically for this slice.

![image](https://user-images.githubusercontent.com/90617686/159964927-784aede7-731f-40df-9e78-3624fe9fc389.png)

Finally, the optimum % was chosen to be 23% for N = 16. Although these numbers are optimums for N = 16, further experiments in the next algorithm showed almost no change is needed for further improvement in other N.

## Optimised Hill Climbing

In this algorithm, since acting random is restricted to when the program is stuck in local optimum, only parameter % (Percentage of queens that are randomly relocated in a random iteration) needs to be optimized. Like the previous optimization, it was deducted that % changes according to N so that their product (N * %) which is the number of queens being randomly relocated (Q) is somehow constant. That is, even for various N, a constant number of queens should be relocated. The author believes, as N increases, there is a need for more queens to change, but at the same time each queen affects a higher number of relationships with other queens, and thus, there would not be any need to increase Q. In other words, each queen is more valuable and satisfies our need for a more dramatic change to the board.

To test and find the optimum numbers, a board of size 8 (N = 8) was chosen, and with maximum iteration numbers ranging from 50 to 1000 (Program ends after these number of tries if not successful), the mean result for 20 independent runs was recorded. In the begging, instead of experimentation with some constant number of queens, a certain percentage (%) of queens were chosen to be relocated randomly on each random iteration. The product of % and N is truncated to reach Q by the program.

Note: The following format is used to represent experiment setup: N Repeats MaximumIterations

![image](https://user-images.githubusercontent.com/90617686/160015186-e67dcdae-9bd5-4b70-84e3-ba794783c64b.png)

Since the algorithm is highly successful, N = 8 could not give us intuition about how to optimize %.

In the next experiment, N was increased to 16 and this time Maximum Iterations ranged from 250 to 1000.

![image](https://user-images.githubusercontent.com/90617686/160015523-5749ec45-7641-4a75-9e6e-85f0c088370e.png)

Based on the results, it was concluded that the optimum % lay somewhere between 0.2 - 0.4. Most probably, a % = 0.3 which resulted in Q = 4 seemed like the best option. Q of 3 or 6 were resulting in lower success rates.

Afterward, N was increased to 24 and the experiment was repeated.

![image](https://user-images.githubusercontent.com/90617686/160015739-c75ab661-c062-46b0-a6b9-bf4013c8fce0.png)

The results of this experiment were quite surprising. The optimum % was 0.2 which pointed towards Q = 4! A proof that despite an 8 queen increase in numbers, the optimum algorithms still changed Q = 4 queens on random iterations.

Thus, it was concluded that % is not important, rather Q is the determining factor. These results are in conjunction with the experiments in the "Hill Climbing + Constant Random Probability" section. Finally, to test this idea, a set of 4 experiments with N = 4, 8, 16, and 24 were conducted. To decrease the noise, the repetition of the experiments was substantially increased. It is also noteworthy that MaxIterations was decided based on the N. The following results were obtained:

N = 4, Repeats = 1000, MaxIterations(15, 18, 20)

![image](https://user-images.githubusercontent.com/90617686/160016551-5c67468f-76c0-4cd3-a744-fa014844ba57.png)

N = 8, Repeats = 500, MaxIterations(65, 70, 75)

![image](https://user-images.githubusercontent.com/90617686/160016655-17345454-a9ff-4a98-a88e-5820c597992c.png)

N = 16, Repeats = 500, MaxIterations(250, 300, 350, 400)

![image](https://user-images.githubusercontent.com/90617686/160016808-27f51118-f017-4b62-9b6c-dd727682aa82.png)

N = 24, Repeats = 50, MaxIterations(300, 400, 450, 500)

![image](https://user-images.githubusercontent.com/90617686/160017084-c4314c19-7174-4af0-95b5-56b7ffb4ed48.png)

Based on the above results, it was confirmed that indeed Q is the determining factor regardless of how large N is. Also, There was not quite much difference between Q = 3 and Q = 4, however, Q = 4 stood for a higher success rate each time. It is also noteworthy that the difference between success rate when Q = 3 and Q = 4 got smaller as N increased, pointing towards a possible hypothesis that in very large N, Q = 3 might become the better option. Unfortunately, this hypothesis remains untested as of today.

## Comparison

To fully compare the success rates of these two algorithms, 5 experiments were conducted, that is, N = 4, 8, 16, 24, 32. The number of Repeats and MaxIterations were both set to 1000. The result took quite a long to come out, as the time complexity of both these algorithms is quite high. Interestingly, the second algorithm solved the problem quicker and ended in lower Iterations. 

First Algorithm (Hill Climbing + Constant Random Probability) ran with P = 23% and Q = 2. The mean success rate of over 1000 repeats is shown.

The second Algorithm (Optimised Hill Climbing) ran with Q = 4. The mean success rate of over 1000 repeats is shown.

![image](https://user-images.githubusercontent.com/90617686/160018632-ed4c0f68-fec7-4950-8acc-6960288b49f2.png)

Unfortunately, the results of the first algorithm in N = 32 took too long and eventually did not come out. However, the dominant victory of the second algorithm is apparent from lower N. The graph below represents the above numbers:

![image](https://user-images.githubusercontent.com/90617686/160018804-b42d6fc6-c952-431a-92e7-824029b6a5a7.png)

In the end, the second algorithm (Optimised Hill Climbing) showed quite high success rates even in large N. A success rate of more than 97% when N = 32 is quite mind-blowing. The only problem, however, is the low efficiency of the algorithm. As a final note, the author believes, since the first algorithm plays randomly in 23% of iterations, a lower Q (Q = 2) optimized it compared with the second algorithm that only acted randomly when stuck at local optimums and needed a higher Q (Q = 4) to be optimized. In other words, if P increases, Q is decreased so they can somehow neutralize each other's effect for the algorithm to remain optimized.
