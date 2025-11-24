import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

X, Y = initial_tx, initial_ty #j'assigne X et  Y pour les coordonnée actuelle de thor

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    direction_en_x = ""
    direction_en_y = "" # deux chaine de caractaires


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if Y > light_y :
        direction_en_y = "N"
        Y -=1 #nouvelle position en y
    elif Y == light_y :
        direction_en_y = ""
        Y = Y
    
   # else Y < light_y :
    else :
        direction_en_y = "S"
        Y += 1
    
    
    if X > light_x :
        direction_en_x = "W"
        X -=1 #nouvelle position en X

    elif X == light_x:
        direction_en_x = ""
        X = X
    #else X < light_x:
    else :
        direction_en_x = "E"
        X += 1
    



    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction_en_y + direction_en_x) # celà m'imprime la direction a prendre
