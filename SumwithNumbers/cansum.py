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
    
myobj = CanSum()

start = time.time()
res = myobj.check_if_sum_exist_dp(200, [7, 14 ])
end = time.time()
print(str(res) + '::  Using dynamic programming '+str(end-start))


start = time.time()
res = myobj.check_if_sum_exist_wodp(200, [7, 14 ])
end = time.time()
print(str(res) + '::  Without using dynamic programming '+str(end-start))