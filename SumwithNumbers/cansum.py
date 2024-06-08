import time

class CanSum:
    def __init__(self):
        self.__mydict = {}
    
    
    def check_if_sum_exist_wodp(self,number, list):
        if(number == 0):
            return True
        if(number < 0):
            return False

        for num in list:
            if(num>0):
                remaining = number - num
                ret_val = self.check_if_sum_exist_wodp(remaining , list)
                if(ret_val == True):
                    return True
        return False
    
    def check_if_sum_exist_dp(self, number, list):
        if(number in self.__mydict):
            return self.__mydict[number]

        if(number == 0):
            return True
        if(number < 0):
            return False

        for num in list:
            if(num>0):
                remaining = number - num
                ret_val = self.check_if_sum_exist_dp(remaining , list)
                self.__mydict[remaining] = ret_val
                if(ret_val == True):
                    return True
        self.__mydict[remaining] = False
        return False
    
    def check_if_sum_exist_dp_tabular(self, number, list):
        table = [False] * (number+1)
        table[0] =  True
        for i in range(len(table)):
            if table[i]== True:
                for j in list:
                    if(i+j <= number):
                        table[i+j] = True        
        return table[number]
    
myobj = CanSum()

start = time.time()
res = myobj.check_if_sum_exist_dp(1500, [7, 14 ])
end = time.time()
print(str(res) + '::  Using dynamic programming '+str(end-start))


start = time.time()
res = myobj.check_if_sum_exist_wodp(200, [7, 14 ])
end = time.time()
print(str(res) + '::  Without using dynamic programming '+str(end-start))


start = time.time()
res = myobj.check_if_sum_exist_dp_tabular(1500, [7, 14 ])
end = time.time()
print(str(res) + ':: Using dynamic programming tabular approch: '+str(end-start))