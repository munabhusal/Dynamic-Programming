def countWordConstruct(string, wordslist):
    if(string==''):return 1
    wordcount = 0
    for word in wordslist:
        if(string.find(word) == 0):
            remaining = string.removeprefix(word)
            count = countWordConstruct(remaining , wordslist)
            wordcount = wordcount+ count
    return wordcount

def countWordConstructdp(string, wordslist, dict = {}):
    if(string in dict):
        return dict[string]
    if(string==''):return 1
    wordcount = 0
    for word in wordslist:
        if(string.find(word) == 0):
            remaining = string.removeprefix(word)
            count = countWordConstructdp(remaining , wordslist)
            wordcount = wordcount+ count
            dict[string] = wordcount
    return wordcount

def countwordconstructdp_tabular(string, wordlist):
    table = [0] * (len(string)+1)
    table[0] =  1

    for i in range(len(string)):
        if table[i] == 1:
            for word in wordlist:
                if(string[slice(i,len(word)+i)] == word):
                    table[i + len(word)] += table[i]        
    return table[len(string)]

string = 'abcdefgh'
wordlist = ['ab','abc', 'de', 'fgh', 'cdefgh']



print(countwordconstructdp_tabular(string, wordlist))
print(countWordConstructdp(string, wordlist))
# print(countWordConstruct(string, wordlist))