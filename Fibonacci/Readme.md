# Fibonacci Number

The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …


formula: fib(n) = fib(n-1) + fib(n-2)



## Without using Any Dynamic Programming
code: 

So, while calculating fib(6),

fib(6) = fib(5) + fib(4)
fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(2) = fib(1) + fib(0)

We can see that to get the value of fib(6), we must have to calculte fib(5), fib(4), fib(3), fib(2), fib(1) in a recursive manner

While calculating fib(3), we have to find the value of fib(2) and fib(1)
Again while calculating the fib(4), we have to find the value of fib(3) and fib(2) from beginning to get the result.



here comes diagram

1. for time complexity

2. for space complexity



time complexity is O(2^n)

Meaning to calulate fib(50), 2^50 steps needs to be calculated.

space complexity is O(n)


We can see that we are repetedly calculating for the same result back to back. 

Is there any solution??

- Using Dynamic Programming, if we have larger problem we can decompose it to a smaller ones.

-if any duplicate work- We can work on optimality of the solution.

## Using Memoization to solve Fibonacci Series
code: 

In this approch, we use dictonary to store the data so that we can fetch the data from there rather then doing calculation.

When fib(6) is to be calculated, every return is stored in the dictonary.

first fib(2) is stored.
then fib(3) is stored.

When fib(4) needs to be calculated, we just grab the value of fib(3) and fib(2) from dictonary and store the value to dict.

When fib(5) needs to be calculated, we just grab the value of fib(4) and fib(3) from dictonary,
and so on.



diagram comes here!


time complexity is O(n)
space complexity is O(n)

## Using Tabular Method to solve Fibonacci Series
code: 


In tabular approch, we solve the things iteratively insted of doing it recursively or storing values in dictonary

Step1: create a array (table) of length (n+1)

Step2: Initialize zero value to everywhere and set the initial values as it should be in respective index. In this fib case, set index 0 to 0 ans index 1 to 1 .

images!


Step 3:
Iteration : Add the value of pivot to its next 2 element. Pivot index moves from 0 to nth index.

diagram!!

time complexity is O(n)
space complexity is O(n)