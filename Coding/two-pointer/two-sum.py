input = [3,5,6,4,8,2,1]

def twosum(input:list,target:int):
    input.sort()
    left = 0
    right = len(input)-1
    while(left < right):
        currsum = input[left] + input[right]
        if currsum == target:
            return [input[left],input[right]]
        elif currsum < target:
            left +=1
        else:
            right -=1
    
    return f"No elements found for two sum of {target}"

print(twosum(input=input,target=7))