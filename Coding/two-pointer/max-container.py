height = [1,8,6,2,5,4,8,3,7]

def container(height:list):
    left = 0
    right = len(height)-1
    maxarea = 0
    while(left<right):
        area = (right-left) * min(height[left],height[right])
        if area > maxarea:
            maxarea = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxarea

print(container(height))