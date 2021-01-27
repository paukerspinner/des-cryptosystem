from constants import *
import random

def permute(permuted_choice, bits):
    return ''.join([bits[pos-1] for pos in permuted_choice])

def leftShift(bits, number_shifts):
    number_shifts %= len(bits)
    return bits[number_shifts:] + bits[0:number_shifts]

def expand(expansionTable, bits):
    res = [0] * len(expansionTable)
    return ''.join([bits[pos-1] for pos in expansionTable])

''' Luu y zfill de xu ly truong hop so 0 dung dau '''
def convertToHex(bits):
    return hex(int(bits, 2))[2:].zfill(int(len(bits)/4))

def convertToBin(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex) * 4)

def xor(bits_1, bits_2):
    res = ''
    for i in range(len(bits_1)):
        if bits_1[i] == bits_2[i]:
            res += '0'
        else:
            res += '1'
    return res

def selectByfunctionS(block_6_bits, selectionFunction):
    row = int(block_6_bits[0] + block_6_bits[5], 2)
    col = int(block_6_bits[1:5], 2)
    return bin(selectionFunction[row][col])[2:].zfill(4)

def createFunctionF(rightBlock, roundKey, presentation=None):
    afterExpand = expand(E, rightBlock)
    
    afterXor = xor(afterExpand, roundKey)
    
    block_6_bits = [afterXor[i:i+6] for i in range(0, 48, 6)]
    afterS = ''.join([selectByfunctionS(block_6_bits[i], S[i]) for i in range(8)])
    
    res = permute(P, afterS)
    
    if presentation == 1:
        print('Expand:\t\t%s' % afterExpand)
        print('XOR:\t\t%s' % afterXor)
        print('S-Boxes:\t%s' % afterS)
        print('Feistel:\t%s' % res)
    return res

def generateRandomBlock(numberBits = 64):
    block = ''.join([str(random.randint(0, 1)) for i in range(numberBits)])
    return hex(int(block, 2))[2:].zfill(int(numberBits/4))
