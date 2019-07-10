def checkMagazine(magazine, note):
    mag_dict = {}
    for w in magazine:
        if w in mag_dict:mag_dict[w] += 1
        else: mag_dict[w] = 1
        
    for word in note:
        if word not in mag_dict: 
            print("No")
            return 
        if word in mag_dict:
            if mag_dict[word] > 0:
                mag_dict[word] -= 1
            else: 
                print("No")
                return
    print("Yes")
    
    
magazine = raw_input().rstrip().split()

note = raw_input().rstrip().split()

checkMagazine(magazine, note)
    
    
