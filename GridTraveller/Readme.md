
Consideing a traveller of 2D grid, begining from top left corner moving to reach the bottom right corner. Traveller only have choice to move either down or right.  This code helps to find the total number of Possible pathways can be found using the following code.

a is the number of rows and b is the number of column.

When a is 0, the traveller is on the top row of the grid and when b is 0, the traveller is on the leftmost column.

When there is only one grid, traveller is already on the destination.

When there is the larger number of grid size, 
When traveller moves, the size of grid it can move is reduced.
eg. When there is a grid of 3*3,
when traveller moves down, grid size shrink to 2*3 grid
when traveller moves right, grid size shrink to 3*2 grid



1. just calculate the grid traveller count

2. using dynamic programming (Tree Approch)

3. Using Tabular approch 