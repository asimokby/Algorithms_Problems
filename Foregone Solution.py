def contains_4(s):
    for i in str(s): 
        if i == '4':
            return False
    return True

def solve(n, count):
    str_n = str(n)
    a = str_n.replace("4", "3")
    b = ""
    for i in str_n: 
        if i == "4":
            b+= "1"
        else: b+="0"
    idx = b.find("1")
    b = b[idx:]
    return "Case #%g: "%count + a + " " + b 
def take_input():
    t_cases = input()
    N_s = []
    for i in range(t_cases):
        inp = input()
        N_s.append(inp)
    
    for n in range(len(N_s)):
        print solve(N_s[n], n+1)
    
take_input()