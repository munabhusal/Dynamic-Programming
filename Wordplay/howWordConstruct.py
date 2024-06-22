def allConstruct(target, words, memo = {}):
    if(target in memo):
        return memo[target]
    
    if target == '':
        return [[]]
    
    result =[]
    for word in words:
        if target.find(word)==0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, words, memo)
            targetWays = list(map(lambda way: [word, *way],suffixWays))
            result.extend(targetWays)
            
    memo[target] = result
    return result

def allConstruct_tabular(target, wordlist):
    table  = [ [] for _ in range(len(target)+1) ]
    table[0] = [[]]
    for i in range(len(target)): 
    
        for word in wordlist:
            if(len(table[i])> 0):
                if(target[slice(i,len(word)+i)] == word): 
                    add_me = list(filter(None, table[i][0] + [word]))
                    table[i+len(word)].extend([add_me])     

    return table[len(target)]
print(allConstruct_tabular('abaaab', ['ab','aa', 'a', 'b']))