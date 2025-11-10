

## marios

import time

ArrayHello = ['H', 'E', 'L', 'L', 'O']
ArrayWorld = ['W', 'O', 'R', 'L', 'D']

while 1:
    
    print(ArrayHello)
    time.sleep(4)
    print(ArrayWorld)
    
    break


## AVOID together
print("---------", "\n\n")

for i in range(0,5,1):
    
    print(ArrayHello[i])
    for i in range(1,4,1):
        time.sleep(1)
        print(" ", ArrayHello[i+1])
