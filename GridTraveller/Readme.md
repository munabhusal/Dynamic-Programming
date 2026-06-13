# Grid Traveler — Dynamic Programming Visualized

We start at the top-left corner of an `a x b` grid and need to get to the bottom-right corner. We can only move right or down. The goal is to figure out exactly how many unique paths exist.

Example: A small `2x3` grid has exactly 3 unique paths.

### Diffrent Approches

I implemented this three different ways to compare how they scale. 

| Approach | Time Complexity | Space Complexity | Source File |
| :--- | :--- | :--- | :--- |
| **No DP** | \(O(2^{n+m})\) | \(O(n+m)\) | `just_grid_traveller.py` |
| **Memoization** | \(O(n \times m)\) | \(O(n \times m)\) | `grid_traveller_memo.py` |
| **Tabulation** | \(O(n \times m)\) | \(O(n \times m)\) | `grid_traveller_table.py` |

Run `grid_traveller.py` to watch all three methods go head-to-head in a  test.


### The Big Shortcut

An easy trick is to cut down on calculations is realizing that a grid's orientation doesn't change the number of paths like (3*2) grid and (2*3) grid
are just mirrors of eachother, which results to same answer.

Instead of standard string concatenation or expensive string allocations, the memoization script speeds things up by storing results in a sorted lookup key using a simple tuple:

Force order so (3, 2) and (2, 3) both look up the exact same cache entry.