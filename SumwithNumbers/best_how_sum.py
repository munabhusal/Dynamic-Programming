#to calculate the time
import time  

#Class to calculate the numbers which adds upto the targated number from the given list in the shortest possible way
class FindBestHowOfSum:
    def __init__(self):
        pass

# Without Using Dynamic Programming
    def best_howsum_wodp(self, target, list ):
        if(target == 0):
            return []
        if(target < 0):
            return None      
        best = None

        for num in list:
            remaining = target - num
            ret_val = self.best_howsum_wodp(remaining , list)
            if(ret_val is not None) :   
                ret_val.append(num)
                if(best is None or len(ret_val) < len(best)):
                    best = ret_val.copy()
        return(best)
    
#Using Dynamic programming Concept(using memo)
    def best_howsum_wdp(self, target, list, mydict = {}):
        if(target in mydict):
            return mydict[target]
        if(target == 0):
            return []
        if(target < 0):
            return None      
        best = None
        for num in list:
            remaining = target - num
            ret_val = self.best_howsum_wdp(remaining , list)
            if(ret_val is not None) :  
                new_node_point = ret_val + [num]

                # What is diffrence between append and "+"?
                # Consider,
                '''
                a = [1,3]
                series = [1,2,3,9]
                '''
                # When using + operator 
                '''
                for num in series:
                    combination = a + [num]
                    print(combination)
                '''
                # Output:
                '''
                [1, 3, 1]
                [1, 3, 2]
                [1, 3, 3]
                [1, 3, 9]
                '''

                #When Using append, value will get appended to the list one after the other
                '''
                for num in series:
                    a.append(num)
                    print(a)
                '''
                #Output
                '''
                [1, 3, 1]
                [1, 3, 1, 2]
                [1, 3, 1, 2, 3]
                [1, 3, 1, 2, 3, 9]
                '''
    
                if(best is None or len(new_node_point) < len(best)):
                    # With respect to the length, output will if determined if sum exist from the given subset
                    best = new_node_point.copy()        
        mydict[target] = best
        return(best)
    
    # Using tabular method Dynamic programming Approch
    def best_howsum_wdp_tabular(self, target, list):
        table = [None] * (target+1)
        table[0] =  []

        for i in range(len(table)):
            if table[i]!= None:
                for j in list:
                    if(i+j <= target):
                        new_comb = table[i] + [j]
                        if(table[i+j] != None):
                            if(len(new_comb) < len(table[i+j])):
                                table[i+j]= new_comb
                        else:
                            table[i+j]= new_comb 
        
        return table[target]
        
obj = FindBestHowOfSum()

start = time.time()
res = obj.best_howsum_wdp(101, [5, 2 , 1])
end = time.time()
print(str(res) + '::  Using dynamic programming Memo Approch '+str(end-start))
print ('____________________')

start = time.time()
res = obj.best_howsum_wdp_tabular(101, [5, 2 , 1])
end = time.time()
print(str(res) + '::  Using dynamic programming Tabular Approch '+str(end-start))
print ('____________________')

start = time.time()
res = obj.best_howsum_wodp(36, [5, 2 ])
end = time.time()
print(str(res) + '::  Without using dynamic programming '+str(end-start))