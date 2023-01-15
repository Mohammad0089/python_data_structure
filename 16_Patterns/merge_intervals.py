def merge_intervals(intervals):
    if not intervals: # given list is empty
        return None
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])
    # Initialize an empty list to store the merged intervals
    merged = []
    # Iterate through the intervals
    for interval in intervals:
        # If the list of merged intervals is empty, add the current interval
        if not merged:
            merged.append(interval)
        else:
            # Get the last interval in the list of merged intervals
            last_interval = merged[-1]
            # If the current interval overlaps or abuts the last interval, merge them
            if interval[0] <= last_interval[1]:
                merged[-1] = last_interval[0], max(last_interval[1], interval[1])
            else:
                # If the current interval does not overlap or abut the last interval, add it to the list of merged intervals
                merged.append(interval)
    return merged
print(merge_intervals([[1,5],[3,7],[4,6]]))
print(merge_intervals([[1,5],[4,6],[6,8],[11,15]]))
print(merge_intervals([[3,7],[6,8],[10,12],[11,15]]))
print(merge_intervals([[1,5]]))
print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[0,1],[1,4],[7,10],[12,13],[18,20],[22,23]]))