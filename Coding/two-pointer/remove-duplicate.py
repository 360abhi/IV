nums = [0,0,1,1,1,2,2,3,3,4]
output = 5

def remove(nums:input):
    slow = 0
    for fast,num in enumerate(nums):
        if nums[slow] != nums[fast]:
            slow +=1
            nums[slow] = nums[fast]
    return slow+1

print(remove(nums))
