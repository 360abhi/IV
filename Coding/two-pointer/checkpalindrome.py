input = "Racecar"

def check(input:str) -> bool:
    input = input.strip().lower()
    left = 0
    right = len(input)-1
    while(left<right):
        if input[left] != input[right]:
            return False
        left +=1
        right -=1
    return True

print(check(input=input))