
def calculate_love_score(name_1,name_2):
    count1 = 0
    count2 = 0
    for i in name_1:
        if i == "T":
            count1 += 1 
        elif i == "R":
            count1 += 1
        elif i == "U":
            count1 += 1  
        elif i == "E":
            count1 += 1 
        else:
            count1 += 0
    for i in name_2:
        if i == "T":
            count1 += 1 
        elif i == "R":
            count1 += 1
        elif i == "U":
            count1 += 1  
        elif i == "E":
            count1 += 1 
        else:
            count1 += 0
    for i in name_1:
        if i == "L":
            count2 += 1 
        elif i == "O":
            count2 += 1
        elif i == "V":
            count2 += 1  
        elif i == "E":
            count2 += 1 
        else:
            count2 += 0
    for i in name_2:
        if i == "L":
            count2 += 1 
        elif i == "O":
            count2 += 1
        elif i == "V":
            count2 += 1  
        elif i == "E":
            count2 += 1 
        else:
            count2 += 0
    print(f"{count1}{count2}")
    
            
calculate_love_score("Angela Yu".upper(), "Jack Bauer".upper())

