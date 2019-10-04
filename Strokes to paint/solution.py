# Algorithm: 
    # iterate through the rows.
    #scan an element, say x, of a row.
    #get all adjacent elements' indexes of x, and store them in a list.
    #remove negative indexes, that we get we x is an edge, from the list.
    #if any of the adjacent indexes exists in idx_letter, a dict containing scanned elements
    #in the form of (index:element or letter), add it to idx_letter.
    #if none of the adjacent indexes exists in idx_letter, add it to idx_letter,
    #then increment the number of strokes. 
    #repeat untill all elements are scanned. 



def get_adjacents_list(current_idx, columns_num):
    up = current_idx #the djacent's index above the element 
    down = current_idx #the djacent's index below the element  
    if current_idx == 0: #if the element is the first of the list(it will have no left adjacent)
        right = current_idx + 1
        left = -1
    elif current_idx == (columns_num - 1): #if the element is the last of the list(it will have no right adjacent)
        left = current_idx - 1 
        right = -1 
    else: #if the element is not an edge
        left = current_idx - 1
        right = current_idx + 1
    list_adjacents = [up, down, right, left] #a list of all adjacents 
    list_adjacents = [i for i in list_adjacents if i >= 0] #removing the negative adjacents' indexes added earlier. 
    return list_adjacents 

def strokes_num(input_pic, columns_num):
    idx_letter = {} #a dict for saving all scanned elements and their indexes in the form {idx:element}
    strokes = 0 #number of strokes: to be incremented.
    for row in input_pic: #iterating through the rows.
        for current_idx in range(len(row)): #scanning every elemet.
            list_adjacents = get_adjacents_list(current_idx, columns_num) #getting the list of adjacents' indexes.
            adj_doesnt_exist = True #in case none of the adjacents' indexes exists. (will be false if it does exist).
            for adj in list_adjacents: #iterating through the list of adjacents' indexes.
                if adj in idx_letter: #checking if the adj's index exist in idx_letter.
                    let_val = idx_letter[adj] #getting the value of the index in idx_letter.
                    if row[current_idx] == let_val: #checking if the letter in idx_letter equals the current letter(element).
                        idx_letter[current_idx] = row[current_idx] #adding the scanned element to idx_letter.
                        adj_doesnt_exist = False #setting this to False because it does exist.
                        break
            if adj_doesnt_exist: #if adj's index does not index.
                idx_letter[current_idx] = row[current_idx] #add scanned element to idx_letter.
                strokes += 1 #increment the number of strokes by one. 
    return strokes




#Testing: 
input_pic1_columns_num = 5
input_pic1 = [["a", "a", "a", "b", "a"], ["a", "b", "a", "b", "a"], ["a", "a", "a", "c", "a"]]
input_pic2_columns_num = 5
input_pic2 = [["a", "a", "b", "b", "a"], ["a", "a", "b", "b", "a"], ["a", "a", "a", "c", "b"]]
input_pic3_columns_num = 3
input_pic3 = [["a", "a"], ["b", "c"]]

def display_picture(input_pic):
    for i in range(len(input_pic)):
        print("".join(input_pic[i])) 

display_picture(input_pic1)
print("Number of strokes: " + str(strokes_num(input_pic1, input_pic1_columns_num)))
display_picture(input_pic2)
print("Number of strokes: " + str(strokes_num(input_pic2, input_pic2_columns_num)))
display_picture(input_pic3)
print("Number of strokes: " + str(strokes_num(input_pic3, input_pic3_columns_num)))


#Output: 

#aaaba
#ababa
#aaaca
#Number of strokes: 5

#aabba
#aabba
#aaacb
#Number of strokes: 5

#aa
#bc
#Number of strokes: 3


        



