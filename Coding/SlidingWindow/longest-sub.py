input = "abcaabbcde"

def longest(input:str):
    left = 0
    result =0
    charset = set()
    for right in range(len(input)):
        while input[right] in charset:
            charset.remove(input[left])
            left +=1
        charset.add(input[right])
        result = max(result,right-left+1)
    return result

print(longest(input))