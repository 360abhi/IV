#Given an array of positive integers nums and a target sum target, return the minimum length of a contiguous subarray of which the sum ≥ target. If no such subarray exists, return 0
target = 7
nums = [2,3,1,2,4,3]

def mintarget(nums:list,target:int):
    left =0
    result = float("inf")
    total = 0
    for right in range(len(nums)):
        total += nums[right]

        while(total>=target):
            result = min(result,right-left+1)
            total -= nums[left]
            left +=1
    return 0 if result == float("inf") else result

print(mintarget(nums,target))
