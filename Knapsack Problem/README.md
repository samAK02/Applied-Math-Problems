# Knapsack Problem

The knapsack problem is a combinatorial optimization problem. It can be formulated in various ways, but one of the most common versions is the 0/1 knapsack problem.

In this problem, it is assumed that there is a knapsack with a given maximum capacity, and there is a set of objects, each with associated weight and value. The objective is to determine which objects to include in the knapsack in order to maximize the total value, while respecting the constraint of the knapsack's maximum weight.

And this program offers a solution based on the greedy method to solve it.



# Code Overview


- Take the number of items (N), the space limit (L), the utility of each item (stored in an array A), as well as their weights (stored in an array B).

- Calculate the utility/price ratio for each item.

- Initialize the total weight and total utility to 0, and the boolean "limitReached" to false.

- While the weight limit is not reached:
  - the code select the item with the highest utility/price ratio.
  - it adds the weight (respectively, utility) of the item to the total weight (respectively, total utility).

- Once the limit is reached, set "limitReached" to true

- The result displays the taken objects with their utility and the remaining space.


# Example of use

let us have this table of items with their utilities.
Let's consider tht our limit will be 60 and we have:

| Items             | Utility  | Weight |
| :---------------- | :------: | ----:  |
| item 01           |   8      | 10     |
| item 02           |   10     | 26     |
| item 03           |   7      | 39     |
| item 04           |   10     | 34     |
| item 05           |   6      | 18     |



The output will be:

![output](https://github.com/samAK02/Applied-Math-Problems/assets/131418700/78f0f405-9ccc-4bd9-83a0-20f4a93845d3)
