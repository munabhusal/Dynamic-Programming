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

string = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
wordlist = ['ee','ee','eeeee']

print(countWordConstructdp(string, wordlist))
print(countWordConstruct(string, wordlist))

