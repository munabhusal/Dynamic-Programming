  # Computing Fibonacci Number using Dynamic Programming
def fibonacci_tree(n, dict = {}):
    if n in dict:
        return dict[n]
    if(n<0):
        print('Not valid number  to calculate.')
        return False
    else:
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n>=2):
            result = fibonacci_tree(n-1, dict) + fibonacci_tree(n-2, dict)
            dict[n] = result       
    return result

print(fibonacci_tree(100))