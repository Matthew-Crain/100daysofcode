alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypter (plain_text, shift_amount, encode):

    coded_text = ''
    if encode != 'encode':
        shift_amount = -1 * shift_amount
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = int(position) + shift_amount
        new_letter = alphabet[new_position]
        coded_text += new_letter
    print(coded_text)

    #print output: "The encoded text is mjqqt"
encrypter(plain_text=text,shift_amount=shift,encode=direction)

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

