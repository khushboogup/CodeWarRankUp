def sum_dig_pow(a, b): 
    lst=list(range(a,b+1))
    result_list=[]
    for j in lst:
        number=str(j)
        digits = [int(d) for d in str(number)]
        result = [digit**(index+1) for index, digit in enumerate(digits)]
        if sum(result)==j:
            result_list.append(j)
    return result_list
        