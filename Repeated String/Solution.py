def repeatedString(s, n):
    num_whole_str = n / len(s)
    part_of_the_str = n % len(s)
    count_a_in_one_s = 0 
    count_a_in_part_s = 0
    final_count_a = 0 
    for char in s:
        if char == "a":
            count_a_in_one_s += 1 
    for i in range(part_of_the_str):
        if s[i] == "a":
            count_a_in_part_s += 1
    final_count_a = (count_a_in_one_s * num_whole_str) + count_a_in_part_s
    return final_count_a
    
s = raw_input()
n = int(raw_input())
result = repeatedString(s, n)
print(result)
