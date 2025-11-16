

import re

#from re import 

regeString = "Hello World!, A laptop"


regMatch0 = re.search("A" , regeString)
regMatch1 = re.search("laptop", regeString)


print(regMatch0.group(0) + " hello")
print("A " + regMatch1.group(0) + " hello")