def is_valid_walk(walk):
    n=walk.count('n')
    s=walk.count('s')
    e=walk.count('e')
    w=walk.count('w')
    if len(walk)!=10:
        return False
    elif n==s and e==w:
        return True
    else:
        return False