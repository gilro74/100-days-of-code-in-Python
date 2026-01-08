# Note - this code does not run here - Go to Reeborg's World Website and 
# The solution down here works for hurdle 1-4
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while not right_is_clear(): 
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left() 
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        