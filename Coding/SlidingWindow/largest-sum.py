# largest sum of k size subarray
nums = [2, 1, 5, 1, 3, 2]

def largest(nums:list):
    k = 3
    curr_sum = sum(nums[:k])
    result = curr_sum
    for i in range(k,len(nums)):
        curr_sum += nums[i] - nums[i-k] # removing the left element from the window
        result = max(curr_sum,result)
    return result


print(largest(nums))
        