def jumpingOnClouds(c):
    current_idx = 0 
    count_jumps = 1
    while current_idx < len(c) - 3:
        if c[current_idx + 1] == 0 and c[current_idx + 2] == 1:
            current_idx += 1 
        else: 
            current_idx += 2 
        count_jumps += 1 
    return count_jumps
    
    
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)

 
