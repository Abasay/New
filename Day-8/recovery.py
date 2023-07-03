alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                                                         
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: create a function called 'encrypt' that takes the texts and 'shift' as inputs.
        #TODO-2: Inside the 'encrypt function, shift each letter of the word 'text' forwards in the alphabet by the shift amount and print the encrypted text.

def caesar(text, shift, direction):
    textList = list(text)
    outputMessageList = []
    resultType = ''

    if direction == "encode":
        resultType = 'encoded'
        def encrypt(newNumber = 0, shiftedLetter=''):
            """Function to encrypt the text input"""
            for i in textList:
                if ord(i) < 97 or ord(i) > 122:
                    outputMessageList.append(i)
                    continue
                letterNumberEquivalent = ord(i) + shift
                if letterNumberEquivalent > 122:
                    if (ord(i) == 122):
                        newNumber = letterNumberEquivalent - 123
                    else:
                        newNumber = letterNumberEquivalent - 122
                    letterNumberEquivalent = 97 + newNumber
                shiftedLetter = chr(letterNumberEquivalent)
                outputMessageList.append(shiftedLetter)
            outputMessage = "".join(outputMessageList)
            print(f"Here is the {resultType} result: {outputMessage}")
        encrypt()

    elif (direction == 'decode'):
        resultType = 'decoded'
        def decrypt(newNumber = 0, shiftedLetter=""):
            """Function to decrypt the text input"""
            for i in textList:
                if ord(i) < 97 or ord(i) > 122:
                    outputMessageList.append(i)
                    continue
                letterNumberEquivalent = ord(i) - shift
                if letterNumberEquivalent < 97:
                    if (ord(i) == 97):
                        newNumber = letterNumberEquivalent - 96
                    else:
                        newNumber = letterNumberEquivalent - 97
                    letterNumberEquivalent = 122 + newNumber
                shiftedLetter = chr(letterNumberEquivalent)
                outputMessageList.append(shiftedLetter)
            outputMessage = "".join(outputMessageList)
            print(f"Here is the {resultType} result: {outputMessage}")
        decrypt()
    else:
        print('Please enter a valid direction!!!')
caesar(text, shift, direction)
