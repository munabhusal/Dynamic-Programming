# Fibonacci - Dynamic Programming
 
Learning how dynamic programming improves performance over plain recursion.
 
### Approaches
 
| Approach    | Time    | Space | File                  |
|-------------|---------|-------|-----------------------|
| No DP       | O(2^n)  | O(n)  | just_fibonacci.py     |
| Memoization | O(n)    | O(n)  | fibonacci_tree.py     |
| Tabulation  | O(n)    | O(n)  | fibonacci_table.py    |
 
Run `fibonacci.py` to see all three benchmarked together.
 
### Key Takeaway
 
Without DP, `fib(50)` requires 2^50 calculations. With memoization or tabulation, it takes just 50.