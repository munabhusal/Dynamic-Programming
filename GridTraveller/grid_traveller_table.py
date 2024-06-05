import numpy as np

def grid_traveller__table(a, b):
    table = np.zeros((a+1,b+1))
    #putting 0 everywhere
    # [
    #     [0 ,0 ,0],
    #     [0 ,0 ,0],
    #     [0 ,0 ,0],
    # ]


    table[1][1] = 1
    #  grid traveller of 1,1 return 1
    # [
    #     [0 ,0 ,0, 0],
    #     [0 ,1 ,0, 0],
    #     [0 ,0 ,0, 0],
    #     [0 ,0 ,0, 0],
    # ]

    for i in range(a+1):
        for j in range(b+1):
            curr_pos = table[i][j]
            if(j+1 <= b):table[i][j+1] = table[i][j+1] + curr_pos
            if(i+1 <= a): table[i+1][j] = table[i+1][j] + curr_pos
            # Adding the pivot value to the grid which lies left and below - if grid exist.
           
    return table[a][b] #Returning the value within the final index.

print(grid_traveller__table(30,30))