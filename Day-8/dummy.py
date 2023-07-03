alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e']
                                                         
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: create a function called 'encrypt' that takes the texts and 'shift' as inputs.
        #TODO-2: Inside the 'encrypt function, shift each letter of the word 'text' forwards in the alphabet by the shift amount and print the encrypted text.


def encrypt(text, shift):
    """Function to encrypt the text input"""
    textList = list(text)
    encryptedMesssageList = []
    shiftedLetter = ""
    for i in textList:
        if ord(i) < 97 or ord(i) > 122:
            encryptedMesssageList.append(i)
            continue
        letterNumberEquivalent = ord(i) + shift
        if letterNumberEquivalent > 122:
            if (ord(i) == 122):
                newNumber = letterNumberEquivalent - 123
            else:
                newNumber = letterNumberEquivalent - 122
            letterNumberEquivalent = 97 + newNumber
        shiftedLetter = chr(letterNumberEquivalent)
        encryptedMesssageList.append(shiftedLetter)
    encryptedMessage = "".join(encryptedMesssageList)
    print(f"Here is the encoded result: {encryptedMessage}")
     
def decrypt(text, shift):
    """Function to decrypt the text input"""
    textList = list(text)
    encryptedMesssageList = []
    shiftedLetter = ""
    newNumber = 0
    for i in textList:
        if ord(i) < 97 or ord(i) > 122:
            encryptedMesssageList.append(i)
            continue
        letterNumberEquivalent = ord(i) + shift
        if letterNumberEquivalent > 122:
            newNumber = letterNumberEquivalent - 122
            letterNumberEquivalent = 96 + newNumber
        shiftedLetter = chr(letterNumberEquivalent)
        encryptedMesssageList.append(shiftedLetter)
    encryptedMessage = "".join(encryptedMesssageList)
    print(f"Here is the encoded result: {encryptedMessage}")

if __name__ == "__main__":
    encrypt(text, shift)