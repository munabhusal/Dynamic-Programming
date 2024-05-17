def canconstruct(string, wordslist):
    if(string==''):
        return True
    
    for word in wordslist:
        if(string.find(word) == 0):
            remaining = string.removeprefix(word)
            if(canconstruct(remaining , wordslist)): return True
    
    return False


def canconstructdp(string,wordlist, memo ={}):
    print(memo)
    if(string in memo):return memo[string]

    if(string==''):
        return True
    
    for word in wordlist:
        if(string.find(word) == 0):
            remaining = string.removeprefix(word)
            if(canconstructdp(remaining , wordlist, memo) ==  True):
                # print('hello')
                memo[string] = True
                print(memo)
                return True
    
    memo[string] = False
    return False


string = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeet'
wordlist = ['e','ee','eeeee']

print(canconstructdp(string, wordlist))
