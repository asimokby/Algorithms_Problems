def minimumBribes(q):
   count = 0 
   if isChatotic(q):
      print "Too chaotic"
      return
   while not issorted(q): 
      for i in range(1, len(q)):
         if q[i] < q[i-1]:
            item = q[i-1]
            q[i-1] = q[i]
            q[i] = item 
            count+=1 
   print(count)  

def issorted(l):
   return all(l[i] <= l[i+1] for i in xrange(len(l)-1))
   
def isChatotic(q):
    i = 0 
    while i < len(q):
        if (q[i] - 2) > i + 1: 
            return True
        i+=1

        
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
