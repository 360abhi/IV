input = [[1,3],[2,6],[8,10],[9,18]]

def mergeIntervals(interval:list):

    # Sorting
    interval.sort(key=lambda x:x[0])
    merged = [interval[0]]

    # Iterating through next intervals
    for curr in interval[1:]:
        prev = merged[-1]

        if curr[0] <= prev[1]: # overlap
            prev[1] = max(curr[1],prev[1]) # extending end element
        else:
            merged.append(curr)

    return merged

print(mergeIntervals(input))
