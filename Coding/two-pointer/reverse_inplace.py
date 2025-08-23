input = "abhishek"

def reverse(input:str):
    input = list(input)
    left = 0
    right = len(input)-1
    while(left<right):
        input[left],input[right] = input[right],input[left]
        left+=1
        right-=1
    return ''.join(input)

print(reverse(input))

