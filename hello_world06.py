


import string
import re

print();print()
## THE LETTERS
AL = string.ascii_lowercase
AU = string.ascii_uppercase


## THE NUMBERS
Dgs = string.digits
HDgs = string.hexdigits
Odgs = string.octdigits


## THE SYMBOLS
PCtn = string.punctuation


## "HELLO"
StringRegAL = re.search("h", AL)
StringRegAU = re.search("E", AU)
StringRegPCtn0 = re.search("\|", PCtn)
StringRegPCtn1 = re.search("\|", PCtn)
StringRegDgs = re.search("0", Dgs)

## "WORLD"
StringRegAL_ = re.search("w", AL)
StringRegAU_ = re.search("O", AU)
StringRegPCtn_0 = re.search("\~", PCtn)
StringRegPCtn_1 = re.search("\!", PCtn)
StringRegPCtn_2 = re.search("\_", PCtn)
StringRegHDgs = re.search("d", HDgs)

print(StringRegAL.group(0) + StringRegAU.group(0) + \
      StringRegPCtn0.group(0) + StringRegPCtn1.group(0) + \
      StringRegDgs.group(0))
    
print(StringRegAL_.group(0) + StringRegAU_.group(0) + \
      StringRegPCtn_0.group(0) + StringRegPCtn_1.group(0) + \
      StringRegHDgs.group(0))
    


print();print()
