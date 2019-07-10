def sherlockAndAnagrams(s):
    sherlock_dict = {}
    p1 = 0 
    p2 = 1
    pass_n = 1
    while pass_n < len(s): 
        if p2 >= len(s) + 1:
            pass_n += 1
            p1 = 0
            p2 = pass_n
        sub_s = "".join(sorted(s[p1:p2]))
        if sub_s in sherlock_dict:
            sherlock_dict[sub_s] += 1
        else: sherlock_dict[sub_s] = 1
        p1 += 1
        p2 += 1 
    
    sherlock_dict = {k: v for k, v in sherlock_dict.iteritems() if v > 1}
    sherlock_dict = {k: ((v-1)* ((v-1)+1))/2 for k, v in sherlock_dict.items()}
    return sum(sherlock_dict.values())
    
    
q = int(raw_input())

for q_itr in xrange(q):
    s = raw_input()

    result = sherlockAndAnagrams(s)
    print(result)
