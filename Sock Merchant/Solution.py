def sockMerchant(n, ar):
    dic = {}
    count = 0
    for i in range(n):
        if ar[i] in dic: dic[ar[i]] +=1
        else: dic[ar[i]] = 1
    for key in dic:
        if dic[key] >= 2: 
            r = dic[key]/2
            count +=r
    return count
    
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
result = sockMerchant(n, ar)
