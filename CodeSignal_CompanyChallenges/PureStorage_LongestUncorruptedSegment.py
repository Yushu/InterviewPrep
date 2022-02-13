from difflib import SequenceMatcher as sm
def solution(sourceArray, destinationArray):
    
    sourceArray = [str(x) for x in sourceArray]
    destinationArray = [str(x) for x in destinationArray]
    len1 = len(sourceArray)
    len2 = len(destinationArray)
    
    seq_match = sm(a=sourceArray, b=destinationArray)
    match = seq_match.find_longest_match(alo=0, ahi=len1, blo=0, bhi=len2)
    
    start = match.a+match.size
    
    if match.size == 0:
        return [match.size, 0]
    else:
        return [match.size, start - match.size]