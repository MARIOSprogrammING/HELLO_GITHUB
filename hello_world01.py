import requests
import time

from requests import get as GETget
from requests import put as PUTput
from requests import put as POSTpost

from time import sleep

i = 0;

try:
    while i < 10:
        
        ++i
        sleep(1)
        getterValue = GETget("www.geeksforgeeks.org", timeout=2)
        print("HELLO i got it!")

    KeyboardInterrupt()
    
except KeyboardInterrupt:
    
    theHELLO_worldPUT = {str(getterValue) : str(getterValue), str(getterValue) : str(getterValue)}
    IgotIT = POSTpost("https://www.geeksforgeeks.org/problems/java-hello-world4004/1", data = theHELLO_worldPUT)

except:
    print("HELLO WORLD OF ERRORS\n")

sleep(10)
numTOif = int(input("Hey Five (num): "))
sleep(2)
numTOelif = int(input("Hey FIve (num): "))
sleep(3)

if numTOif < 11:
    print("HELLO MAN ITS AN ERROR")
    print()
    print("HELLO why???\n\nreturn 1;")
       
elif numTOelif < 9:
    print("Hello its anz errorz")
    print()
    print("HELLO why???\n\nreturn 1;")
       
else:
    print("HELLO why???\n\nreturn 1;")
        
        