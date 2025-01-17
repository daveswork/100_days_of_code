def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_up():
    turn_left()
    move()
    turn_right()
    
while at_goal() is False:
    if wall_on_right() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif wall_in_front():
        turn_left()