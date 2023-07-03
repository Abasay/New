alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabet[25 + 2])
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if(direction != 'encode' and direction != 'decode'):
    print('Please enter a valid cipher direction command!\n')
    exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

while shift > 26:
    shift = shift % 26

def caesar(start_text, shift_number, cipher_directions):
    textList = start_text
    outputMessage = ""
 
    if (cipher_directions == 'encode'):
        for i in textList:
            try:
                textIndex = alphabet.index(i)
                outputMessage += alphabet[textIndex + shift_number]
            except ValueError:
                outputMessage += i
                
    elif(cipher_directions == 'decode'):
        for i in textList:
            try:
                textIndex = alphabet.index(i)
                outputMessage += alphabet[textIndex - shift_number]
            except ValueError:
                outputMessage += i
                
    print(f"This is the {cipher_directions}d output: {outputMessage}")


def is_continue(start_text, shift_number, cipher_direction):
    caesar(start_text, shift_number, cipher_direction)
    continue_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    while continue_input == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if(direction != 'encode' and direction != 'decode'):
            print('Please enter a valid cipher direction command!\n')
            continue
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        while shift > 26:
            shift = shift % 26
        caesar(text, shift, direction)
        continue_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    print('Goodbye\n')

is_continue(text, shift, direction)