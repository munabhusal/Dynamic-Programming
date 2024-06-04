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
    
  # Computing Fibonacci Number using Dynamic Programming memo method
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
    
  # Computing Fibonacci Number using Dynamic Programming table method
  def fib_table(self, n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(n):
        table[i+1] = table[i+1] + table[i]
        if(i != n-1):
            table[i+2] = table[i+2] + table[i]
    
    return(table[n])
        

# Creating Object
obj = Fibonacci()

# Observing Computation Time using Dynamic programming (memo)
start = time.time()
print(obj.fib_wd(30))
end = time.time()
print('Time to calculate the result using tree based memo dynamic programming '+str(end-start))
print('____________________________________________________________________')
print('____________________________________________________________________')

# Observing Computation Time using Dynamic programming (table)
start = time.time()
print(obj.fib_table(30))
end = time.time()
print('Time to calculate the result using tabulaer dynamic programming '+str(end-start))
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

