nums = [1,2,3,4,6,8,9]

def binary(nums:list,target:int):
    left,right = 0,len(nums)-1
    while(left<=right):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1

print(binary(nums,target=2))