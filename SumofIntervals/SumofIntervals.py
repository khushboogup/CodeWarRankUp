def sum_of_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort()
    merged=[intervals[0]]
    for current_start,current_end in intervals[1:]:
        last_start,last_end=merged[-1]
        if current_start<=last_end:
            merged[-1]=(last_start,max(last_end,current_end))
        else:
            merged.append((current_start,current_end))
            
    total=0
    for start,end in merged:
        total+=end-start
    return total