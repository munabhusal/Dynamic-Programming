def just_fibonacci(n):
    if(n<0):
        print('Not valid number  to calculate.')
        return False
    else:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n>=2):
            return just_fibonacci(n-1)+just_fibonacci(n-2)
        
print(just_fibonacci(100))