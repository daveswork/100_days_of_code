def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_right()

def turn_up():
    turn_left()
    move()
    turn_right()
    
while at_goal() is False:
    if right_is_clear():
        turn_right()
        if right_is_clear():
            move()
            turn_right()
            if not wall_in_front():
                move()
    elif wall_in_front():
        turn_left()
    else:
        move()