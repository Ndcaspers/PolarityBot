# Nick Caspers
# Jan 1, 2018
#####################################################################################

# KeyBank class
# Maintains the keys for the program

class KeyBank:

    # Data Members (Keys)
    key1 = 'AAAAAAAAAAAAAAAAAAAAAPAh2AAAAAAAoInuXrJ%2BcqfgfR5PlJGnQsOniNY%3Dn9galDg4iUr7KyRAU47JGDbQz2q7sdwXRTkonzBX2uLxXRgNv0'
    key2 = 'AAAAAAAAAAAAAAAAAAAAALFf3wAAAAAAtv5xXx99oZExN2l8rfaEqn0Zm7w%3Dkv3KeZWGJI01UojOzLb9wgY2FT5RxGDw2NKIRA3cxht7GVN7Pe'
    key3 = 'AAAAAAAAAAAAAAAAAAAAAOlf3wAAAAAAz5KqWIIoL6%2FYdAgGJFa%2FzUjOHvA%3DEYDKQz79SUJo28tSVBKkSrKA9Ku3vsZonuceHr2Y1ythHwXqUo'
    key4 = 'AAAAAAAAAAAAAAAAAAAAAPVf3wAAAAAAj505smvCTftNV%2BIj4IWux7DBUHA%3DvhNJ28zUQwGKUQ7yqakq6cHEU0sKyDTatGNvoUhvYEk4GXKVNA'
    key5 = 'AAAAAAAAAAAAAAAAAAAAAARg3wAAAAAAdjOC4CljaQKZ00rmgex3Hv3f6N0%3D5cAIslZRfst2pnE74E3CQ8pVWcfp33bsY7gMIluxHmeiWWdv31'

    bank = []
    bankIndex = 0


    ###########################################################
    # Constructor (should just leave it as a default constructor)

    # Setting the key bank up
    @staticmethod
    def setup():
        
        # Setting up the key bank list
        KeyBank.bank = [KeyBank.key1, KeyBank.key2, KeyBank.key3, KeyBank.key4, KeyBank.key5]
        bankIndex = 0

    ###########################################################
    # Bank Operations

    @ staticmethod
    def changeKeys():

        # switch the key one grabs
        KeyBank.bankIndex += 1

        if(KeyBank.bankIndex >= len(KeyBank.bank)):
            KeyBank.bankIndex = 0


    @staticmethod
    def getKey():

        # get the current key of use
        return KeyBank.bank[KeyBank.bankIndex]

        
        
