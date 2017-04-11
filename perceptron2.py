import sys
import numpy as np

argvs = sys.argv
argc  = len(argvs)

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y  = AND(s1, s2)
    return y

a1 = float(argvs[1])
b1 = float(argvs[2])
Aans = AND(a1, b1)
Nans = NAND(a1, b1)
Oans = OR(a1, b1)
Xans = XOR(a1, b1)
print("AND  = " + str(Aans) )
print("NAND = " + str(Nans) )
print("OR   = " + str(Oans) )
print("XOR  = " + str(Xans) )
