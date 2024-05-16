# To learn about the tiem taken with and without using dynamic programming
import time

#Consider one have to exchange the money of the given amount
class MoneyChangeSample:
    def __init__(self):
        self.__dict = {}    #for dynamic programming
        self.temp = []      #to store the subset so that it can sum upto the targated amount

    #Without using Dynamic Programming
    def howsum_wdp(self,target, list):
        if(target == 0):
            return []
        if(target < 0):
            return None

        for num in list:
            remaining = target - num
            ret_val = self.howsum_wdp(remaining , list)
            if(ret_val is not None) :   
                self.temp.append(num)
                return self.temp
            
    #Using Dynamic Programming concept
    def howsum_dp(self,target, list):
        #Concept of Dynamic programming used here!
        if(target in self.__dict):
            return self.__dict[target]
        
        if(target == 0): #if it returns empty array, means, the amount is changable 
            return []
        if(target < 0): #When the amount is not changeable
            return None
        
        for num in list:
            remaining = target - num 
            # if 10 is target possible changes will be [2,5,10]
            #remaing will return [10-2, 10-5 , 10-5]=> when [] is returend in the recursion below, the amount is changable
                    
            ret_val = self.howsum_dp(remaining , list)

            self.__dict[remaining]= ret_val

            if(ret_val is not None) :   #returning the changable amount list
                self.temp.append(num)
                return self.temp


myobj = MoneyChangeSample()

start = time.time()
res = myobj.howsum_dp(500, [7, 14])
end = time.time()
print(str(res) + '::  Using dynamic programming '+str(end-start))
print ('____________________')

start = time.time()
res = myobj.howsum_wdp(100, [7, 14])
end = time.time()
print(str(res) + '::  Without using dynamic programming '+str(end-start))