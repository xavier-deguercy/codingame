import sys
import math


n = int(input())
result = []
ans = 100
for i in range(n):
    pi = int(input())
    result.append(pi)
   
result = sorted(result)

for j in range(0,len(result)-1):
    if (result[j+1] - result[j]) < ans:
        ans = result[j+1] - result[j]
        if ans == 1:
            break
        

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(ans)