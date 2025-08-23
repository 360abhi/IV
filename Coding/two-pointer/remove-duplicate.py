nums = [0,0,1,1,1,2,2,3,3,4]

def remove(nums:list) -> int:
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow +=1
            nums[slow] = nums[fast]
    return slow+1

length = remove(nums)
print(nums[:length])
