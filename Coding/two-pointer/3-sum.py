input = [1,4,45,6,10,8]

def threesum(input:list,target:int):
    input.sort()
    print(input)
    for i,num in enumerate(input):
        left = i+1
        right = len(input)-1
        while(left<right):
            currsum = input[i] + input[left] + input[right]
            if currsum == target:
                return [input[i], input[left], input[right]]
            elif currsum < target:
                left +=1
            else:
                right -=1
        return "No subset found"
    

print(threesum(input,target=17))