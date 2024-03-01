import numpy as np

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))
a5 = float(input("a5 = "))
xe = float(input("X = "))
ye = float(input("Y = "))
ze = float(input("Z = "))

# To solve for Theta 1 or Th1
phi2 = np.arctan(ye/xe)
r1 = np.sqrt(ye**2 + xe **2)
phi1 = np.arccos((a4**2 - r1**2 - a2**2) / (-2 * r1 * a2))
if (phi1 > phi2):
    Th1 = (phi1 - phi2) * 180/np.pi
else:
    Th1 = (phi2 - phi1) * 180/np.pi
    
# To solve for Theta 2 or Th2
phi3 = np.arccos((r1**2 - a2**2 - a4**2) / (-2 * a2 * a4))
Th2 = 180 - (phi3*180/np.pi)

# TO solve for D3
D3 = a1 + a3 - a5 - ze

print("D3 = ", np.around(D3,3))

print("Th1 = ", np.around(Th1,3))

print("Th2= ", np.around(Th2,3))
