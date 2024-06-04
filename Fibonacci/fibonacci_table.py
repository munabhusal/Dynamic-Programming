def fiboncci_table(n):
    table = [0] * (n+1)
    table[1] = 1

    for i in range(n):
        table[i+1] = table[i+1] + table[i]
        if(i != n-1):
            table[i+2] = table[i+2] + table[i]
    
    return(table[n])

print(fiboncci_table(8))