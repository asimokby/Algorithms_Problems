def rotLeft(a, d):
    return a[d:] + a[:d]

nd = raw_input().split()

n = int(nd[0])

d = int(nd[1])

a = map(int, raw_input().rstrip().split())

result = rotLeft(a, d)
