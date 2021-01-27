from constants import *
from lib import *

class Key:
    def __init__(self, hexkey):
        self.original = bin(int(hexkey, 16))[2:].zfill(64)

    def createKeys(self, presentation=None):
        key = [self.original]
        C = [permute(PC_1_L, self.original)]
        D = [permute(PC_1_R, self.original)]
        for i in range(1, 17):
            C.append(leftShift(C[i-1], NUM_LSHIFTS[i-1]))
            D.append(leftShift(D[i-1], NUM_LSHIFTS[i-1]))
            key.append(permute(PC_2, C[i] + D[i]))

        if presentation == 1:
            print('Key Schedule:')
            print('C[0] D[0]:\t%s %s' % (C[0], D[0]))
            for i in range(16):
                print('Round %d' % (i+1))
                print('C[%d] D[%d]:\t%s %s' % (i+1,i+1,C[i+1], D[i+1]))
                print('Key[%d]\t\t%s' % (i+1, key[i+1]))
        self.roundKeys = key
        return key

    def hexOf(self, ikey):
        return hex(int(self.roundKeys[ikey], 2))[2:]
    
    def binOf(self, ikey):
        return self.roundKeys[ikey]