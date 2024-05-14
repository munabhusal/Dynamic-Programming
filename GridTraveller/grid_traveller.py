# Consideing self as a traveller of 2D grid, begining from top left corner moving to reach the 
# bottom right corner. Traveller only have choice to move either down or right. Total number of 
# Possible pathways can be found using the following code.


class Grid_traveller:
    def __init__(self):
        self.__data = {}

    def gridTravellerPathCount(self,a,b):
        grid_size = str(min(a,b)) + '_' + str(max(a,b))
        if grid_size in self.__data:
            return self.__data[grid_size]        
        if(a==0 or b==0):
            return 0
        if(a==1 and b==1):
            return 1
        else:
            result = self.gridTravellerPathCount(a-1,b)+ self.gridTravellerPathCount(a,b-1)
            grid_size = str(min(a,b)) + '_' + str(max(a,b))
            self.__data[grid_size] = result
            return result
        
a = Grid_traveller()
print("Total Available paths on gridTraveller of given grid is " +str(a.gridTravellerPathCount(3,3)) + ".")