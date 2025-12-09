import sys
import math

#variables.

n = int(input())
max = 0
pertemax = 0


for i in input().split():
    v = int(i)

#si la valeur donnée v est superieur au maximun, alors elle deviens le nouveau max
    if v > max :
        max = v 
    else :
        max
    

#si la difference entre le max et la valeur donnée v est supperieur a la pertemax, alors c'est max-v
    if max - v > pertemax :
        pertemax = max - v


print(-pertemax)
