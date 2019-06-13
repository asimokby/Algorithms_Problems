def hourglassSum(arr):
    list_max = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sm = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            list_max.append(sm)
    return max(list_max)


arr = []
for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))
        
result = hourglassSum(arr)
