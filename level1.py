import random
import string
import base64
import hashlib
from cryptography.fernet import Fernet


#level 1: just 4 digits
def generate_password_1(length=4):
    characters = string.digits
    password = "".join(random.choices(characters, k=length))
    return password



def decrypt_flag():
    password = input("Enter the password.")
    filename = "flag1.txt"

    key_bytes = hashlib.sha256(password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    cipher = Fernet(fernet_key)

    #to decrypt:

    with open(filename, "rb") as f:
        decrypted = cipher.decrypt(f.read())
    with open (filename,"wb") as f:
        f.write(decrypted)






while True:
    print("Welcome to Level 1 of this Insecure Cryptography CTF. Your goal is to use your cryptography and programming knowledge to crack the password and decrypt the .txt files to get the flag.\n")
    print("You are allowed to inspect the source code, but do not think the flag will just be sitting there in plain sight! You may have to write your own script to reverse the encryption algorithm, or brute-force your way through the challenges. Either way, I wish you the best of luck. Go forth and hack stuff. \n")
    print("A hint: The flag file was encrypted using the hashlib library. It takes a password, hashes it with sha256, then uses that key to encrypt the file. \n")
    print("The password was also randomly generated. If you would like to see the function operate in real time, type '1'. Type '0' to quit the challenge. Type '2' to attempt to decrypt the file. \n")

    words = input("What will you do?\n")
    choice = int(words)

    if choice == 0:
          break
    elif choice == 1:
          print("\n========================================")
          print("Your password is:", generate_password_1())
          print("========================================\n")
          
          # this pause keeps the password on screen until you press Enter
          input("Press Enter to return to the main menu...") 
          
    elif choice == 2:
          decrypt_flag()
          print("flag1.txt has been decrypted with the provided password. Check and see if you succeeded.")
          break
  

