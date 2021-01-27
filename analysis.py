from key import *
from lib import *
from des import *
from constants import *

def presentativeEncrypt(block = '00123456789abcde', originalKey = '0133457799bbcdff'):
    print('Block:   %s' % block)
    print('Key:     %s' % originalKey)
    print('\nRound f(R,K)\tLn\t  Rn')
    key = Key(originalKey)
    leftBlock = [permute(IP[:32], convertToBin(block))]
    rightBlock = [permute(IP[32:], convertToBin(block))]
    print('00\t      %s  %s  %s' % ('', convertToHex(leftBlock[0]), convertToHex(rightBlock[0])))
    for i in range(1, 17, 1):
        currentKey = key.binOf(i)
        currentFunc = createFunctionF(rightBlock[i-1], currentKey)
        leftBlock.append(rightBlock[i-1])
        rightBlock.append(xor(leftBlock[i-1], currentFunc))
        print('%0.2d    %s  %s  %s' % (
                i,
                convertToHex(currentFunc),
                convertToHex(leftBlock[i]),
                convertToHex(rightBlock[i])
            ))
    res = permute(FP, rightBlock[16] + leftBlock[16])
    print('\nCipherBlock: %s' % convertToHex(res))

presentativeEncrypt()
