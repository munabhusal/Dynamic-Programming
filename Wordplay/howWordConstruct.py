def allConstruct(target, words):
    if target == '':
        return [[]]
    
    result =[]
    for word in words:
        if target.find(word)==0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, words)
            targetWays = list(map(lambda way: [word, *way],suffixWays))
            # result.append(*targetWays)
            result.extend(targetWays)
            
    return result


print(allConstruct('dsfds', ['ds','f','d', 's']))


