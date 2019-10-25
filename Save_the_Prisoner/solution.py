def saveThePrisoner(n, m, s):
    if (m % n) == 0 and s == 1:
        return n
    elif (m%n) > (n-s+1):
        return (m % n) - (n-s+1) 
    else:
         return (m %n) + (s - 1)
