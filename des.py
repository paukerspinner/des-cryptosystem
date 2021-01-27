from constants import *
from lib import *
from key import *

def des(block, originalKey, method, presentation=None):
    key = Key(originalKey)
    key.createKeys(presentation)
    leftBlock = [permute(IP[:32], convertToBin(block))]
    rightBlock = [permute(IP[32:], convertToBin(block))]
    if presentation == 1:
        print('\nINPUT BLOCK:\t\t%s' % convertToBin(block))
        print('Initial Permutation:\t%s' % (''.join(leftBlock+rightBlock)))
    for i in range(1, 17, 1):
        if presentation == 1:
            print('\nRound %d' % i)
        if method == 'ENCRYPT':
            currentKey = key.binOf(i)
        elif method == 'DECRYPT':
            currentKey = key.binOf(16-i+1)
        currentFunc = createFunctionF(rightBlock[i-1], currentKey, presentation)
        leftBlock.append(rightBlock[i-1])
        rightBlock.append(xor(leftBlock[i-1], currentFunc))
        if presentation == 1:
            print('L[%d] R[%d]:\t%s %s' % (i, i, leftBlock[i], rightBlock[i]))
    res = permute(FP, rightBlock[16] + leftBlock[16])
    if presentation == 1:
        print('\nCIPHER:\t%s' % res)
    return convertToHex(res)

def encryptDES(inputBlock, inputKey, presentation=None):
    return des(inputBlock, inputKey, 'ENCRYPT', presentation)

def deCryptDES(outputBlock, inputKey):
    return des(outputBlock, inputKey, 'DECRYPT')
