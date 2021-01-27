from key import *
from constants import *
from lib import *
from des import *

def run(numberTest):
    for i in range(numberTest):
        inputKey = generateRandomBlock(64)
        inputBlock = generateRandomBlock(64)
        print('Block:   %s' % inputBlock)
        print('Key:     %s' % inputKey)

        cipher = encryptDES(inputBlock, inputKey)
        print('Cipher:  %s' % cipher)

        restoreInputBlock = deCryptDES(cipher, inputKey)
        print('Restore: %s' % restoreInputBlock)
        
        status = 'Success' if restoreInputBlock == inputBlock else 'Fail'
        print('Encrypt and Decrypt: %s' % status, end='\n\n')

def presentation():
    inputKey = generateRandomBlock(64)
    inputBlock = generateRandomBlock(64)
    print('KEY:\t%s' % convertToBin(inputKey))

    cipher = encryptDES(inputBlock, inputKey, 1)

presentation()