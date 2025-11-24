import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
j = 0
mini = 0
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    
    if j == 0 or abs(t) < abs(mini) or abs(t) == abs(mini) and t > mini:
        mini = t
    j = j + 1


    '''if j == 0:
        mini = t
        
    if  abs(t) < abs(mini):
        mini = t

    if abs(t) == abs(mini) and t > mini :
        mini = t
    
    j = j + 1'''
        
        
        


     
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(mini)
