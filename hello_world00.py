from matplotlib import pyplot as PLM
from numpy import array as NAP

import time


arrPLOT = NAP([1,0,0,1])

arrHELLO = arrPLOT
arrWORLD = arrPLOT * 2

PLM.plot(arrHELLO, arrWORLD)

time.sleep(2)
print("FRIEND GET READY")
PLM.xlabel("arrHELLO")

time.sleep(2)
print("FRIEND GET READY")
PLM.ylabel("arrWORLD")

time.sleep(2)
print("GET FRIEND MAN")
PLM.title("MY FRIEND!, remember me?")

while 1:
    
    try:
        PLM.show()
    except KeyboardInterrupt:
        break;


