# Caesar Cipher 

from encrypt import encrypt
from decrypt import decrypt
from ASCII_art import caesar_cipher

alphabet = alphabet = ['q', 'd', '0', '2', 'p', 'h', '7', 'x', 'w', '4', 'i', 'g', 'l', 's', '3', 'r', 'f', 'a', 'o', 'y', 't', '1', 'm', 'k', 'e', '9', 'u', 'b', 'j', '8', 'v', 'c', '6', 'z', 'n', '5', 'q', 'd', '0', '2', 'p', 'h', '7', 'x', 'w', '4', 'i', 'g', 'l', 's', '3', 'r', 'f', 'a', 'o', 'y', 't', '1', 'm', 'k', 'e', '9', 'u', 'b', 'j', '8', 'v', 'c', '6', 'z', 'n', '5']

print("\nWelcome to The : \n")
# Print Caesar Cipher ASCII Art 
print(caesar_cipher)

again = 'again'
while again == 'again':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print("Wrong input!")
        again = input("Type 'again' to encode or decode another message or type 'quit' to quit :\n")
        if again == 'again':
        	continue
        elif again == 'quit':
          print("Thanks for using Caesar Cipher!")
          print("\t\t\tCreated by 4bd3ss4m4d")
          break
        elif again != 'again' and again != 'quit':
          print("Wrong input!")
          break
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > len(alphabet):
            shift = shift % (len(alphabet))
        if direction == 'encode':
            encrypted_text = encrypt(text, shift, alphabet)
            print(encrypted_text)
        elif direction == 'decode':
            decrypted_text = decrypt(text, shift, alphabet)
            print(decrypted_text)
    again = input("Type 'again' to encode or decode another message or type 'quit' to quit :\n")
    if again != 'again' and again != 'quit':
    	print("Wrong input!")
    	break
    elif again == 'again':
    	continue
    else:
      print("Thanks for using Caesar Cipher!")
      print("\t\t\tCreated by 4bd3ss4m4d")
      break