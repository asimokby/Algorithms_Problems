def twoStrings(s1, s2):
    dict_s1 = dict.fromkeys(s1,0)
    for char in s2:
        if char in dict_s1:
            return "YES"
    return "NO"  
   

q = int(raw_input())

for q_itr in xrange(q):
  s1 = raw_input()
  s2 = raw_input()
  result = twoStrings(s1, s2)
  print(result)
