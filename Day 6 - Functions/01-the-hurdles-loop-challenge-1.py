# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdle 1 Challenge

# Solution:
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
 
for _ in range(6):
    one_jump()