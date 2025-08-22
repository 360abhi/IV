input = [2,4,5,3,4,3]

def twosum(input:list,target:int):
    map = {}
    for i,num in enumerate(input):
        if num in map:
            return [map[num],i]
        diff = target-num
        map[diff] = i
        
print(twosum(input=input,target=8))