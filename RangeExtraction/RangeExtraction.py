def solution(args):
    result=[]
    i=0
    while i<len(args):
        start=i
        while i+1<len(args) and args[i+1]==args[i]+1:
            i+=1
        if i-start>=2:
            result.append(f"{args[start]}-{args[i]}")
        else:
            result.extend(map(str,args[start:i+1]))
        i+=1
        
    return ",".join(result)
        