# Importing time so that we can efficiently calculate the time taken for computation
import time


#Creating Fibonacci class which can get the Fibonacci series, get Fibonacci number by using and without using dynamic programming
class Fibonacci:
  def __init__(self):
    self.dict = {}
  
  # Computing Fibonacci Number without using Dynamic Programming
  def fib_wod(self, n):
    if(n<0):
        print('Not valid number  to calculate.')
        return False
    else:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n>=2):
            return self.fib_wod(n-1)+self.fib_wod(n-2)
    
  # Computing Fibonacci Number using Dynamic Programming
  def fib_wd(self, n):
    if n in self.dict:
        return self.dict[n]
    if(n<0):
        print('Not valid number  to calculate.')
        return False
    else:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n>=2):
            result = self.fib_wd(n-1) + self.fib_wd(n-2)
            self.dict[n] = result       
    return result
  
  # Computing Fibonacci Series using Dynamic Programming
  def get_fib_series(self,n):
    self.fib_wd(n)
    return self.dict
        

# Creating Object
obj = Fibonacci()

# Observing Computation Time using Dynamic programming 
start = time.time()
print(obj.fib_wd(30))
end = time.time()
print('Time to calculate the result using dynamic programming '+str(end-start))
print('____________________________________________________________________')
print('____________________________________________________________________')

# Observing Computation Time without using Dynamic programming 
start = time.time()
print(obj.fib_wod(30))
end = time.time()
print('Time to calculate the result without using dynamic programming '+str(end-start))
print('____________________________________________________________________')
print('____________________________________________________________________')

# Getting the  Fibonacci Series
print('Printing the Fibonacci Series')
print(obj.get_fib_series(30))