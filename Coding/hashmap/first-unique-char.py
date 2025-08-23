input = "leetcode"
input2 = "loveleetcode"
input3 = "aabbb"

def first(input:str):
    map = {}
    for s in input:
        map[s] = map.get(s,0) + 1

    for i,ch in enumerate(input):
        if map[ch] == 1:
            return [i,ch]
        
    return -1

print(first(input=input2))