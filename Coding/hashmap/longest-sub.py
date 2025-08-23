# Longest substring without repeating characters
# Sliding Window : left starts at 0 while right is the iterator of loops
# window size = r-l+1
input = "dvdf"

def longest(input:list):
    charset = set()
    left = 0
    result = 0
    for right in range(len(input)):
        while input[right] in charset:
            # Removing the chars behind the first dup value if present
            charset.remove(input[left])
            left +=1
        # Add the rightmost char
        charset.add(input[right])
        result = max(result,right-left+1)
    return result

print(longest(input=input))
    
        




