# Consideing self as a traveller of 2D grid, begining from top left corner moving to reach the 
# bottom right corner. Traveller only have choice to move either down or right. Total number of 
# Possible pathways can be found using the following code.

import time
import numpy as np
class Grid_traveller:
    def __init__(self):
        self.__data = {}

# Without using Dynamic Programming 
    def gridTravellerPathCountno_dp(self,a,b):   
        if(a==0 or b==0):
            return 0
        if(a==1 and b==1):
            return 1
        else:
            result = self.gridTravellerPathCountno_dp(a-1,b)+ self.gridTravellerPathCountno_dp(a,b-1)
            return result
        

# Using Dynamic Programming (Memodrum Approch)
    def gridTravellerPathCountMemo(self,a,b):
        grid_size = str(min(a,b)) + '_' + str(max(a,b))
        if grid_size in self.__data:
            return self.__data[grid_size]        
        if(a==0 or b==0):
            return 0
        if(a==1 and b==1):
            return 1
        else:
            result = self.gridTravellerPathCountMemo(a-1,b)+ self.gridTravellerPathCountMemo(a,b-1)
            grid_size = str(min(a,b)) + '_' + str(max(a,b))
            self.__data[grid_size] = result
            return result
        

# Using Dynamic Programming (Tabular Approch)
    def gridTravellerPathCountTable(self,a,b):
        table = np.zeros((a+1,b+1))
        table[1][1] = 1
        for i in range(a+1):
            for j in range(b+1):
                curr_pos = table[i][j]
                if(j+1 <= b):table[i][j+1] = table[i][j+1] + curr_pos
                if(i+1 <= a): table[i+1][j] = table[i+1][j] + curr_pos
        
        return table[a][b]

# Creating Object
obj = Grid_traveller()

# Observing Computation Time using Dynamic programming (memo)
start = time.time()
print(obj.gridTravellerPathCountMemo(8,30))
end = time.time()
print('Total Available paths on gridTraveller of given grid using emo dynamic programming '+str(end-start))
print('____________________________________________________________________')
print('____________________________________________________________________')

# Observing Computation Time using Dynamic programming (table)
start = time.time()
print(obj.gridTravellerPathCountTable(8,30))
end = time.time()
print('Time to calculate the result using tabuler dynamic programming '+str(end-start))
print('____________________________________________________________________')
print('____________________________________________________________________')

# Observing Computation Time without using Dynamic programming 
start = time.time()
print(obj.gridTravellerPathCountno_dp(8,3))
end = time.time()
print('Time to calculate the result without using dynamic programming '+str(end-start))
print('____________________________________________________________________')
print('____________________________________________________________________')
