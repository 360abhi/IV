# Sub array with max sum
input = [2,4,-5,-2,3]

def kadane(input:list):
    maxsum = -100
    currsum = -100
    for num in input:
        currsum = max(num,currsum+num)
        if currsum > maxsum:
            maxsum = currsum
    return maxsum


print(kadane(input))