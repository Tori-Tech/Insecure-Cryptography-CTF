import random
import string
import base64
import hashlib
from cryptography.fernet import Fernet
import time

#level 2: digits and letters, with fixed seed
def generate_password_2(length=8):
    number = input("Enter a seed value.")
    num = int(number)
    random.seed(num)
    characters = string.ascii_letters + string.digits
    password = "".join(random.choices(characters, k=length))
    print(password)



def decrypt_flag():
    password = input("Enter the password.")
    filename = "flag2.txt"

    key_bytes = hashlib.sha256(password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    cipher = Fernet(fernet_key)

    #to decrypt:

    with open(filename, "rb") as f:
        decrypted = cipher.decrypt(f.read())
    with open (filename,"wb") as f:
        f.write(decrypted)



while True:
    print("Welcome to Level 2 of this Insecure Cryptography CTF. Your goal is to use your cryptography and programming knowledge to crack the password and decrypt the .txt files to get the flag.\n")
    print("You are allowed to inspect the source code, but do not think the flag will just be sitting there in plain sight! You may have to write your own script to reverse the encryption algorithm, or brute-force your way through the challenges. Either way, I wish you the best of luck. Go forth and hack stuff. \n")
    print("A hint: The flag file was encrypted using a password that was randomly generated (with Python's random library) using a specific seed value that is greater than 20, but lower than 60. The program then takes that password, hashes it with sha256, then uses that key to encrypt the file. \n")
    print("Decrypting the file works in reverse: You provide your password, the program hashes it, then tries to use that hash as a key to decrypt the file.\n")
    print("If you would like to see the random password generator operate in real time, type '1'. Type '0' to quit the challenge. Type '2' to attempt to decrypt the file. \n")

    words = input("What will you do?\n")
    choice = int(words)

    if choice == 0:
          break
    elif choice == 1:
          print("\n========================================")
          generate_password_2()
          print("========================================\n")
          
          # this pause keeps the password on screen until you press Enter
          input("Press Enter to return to the main menu...") 
          
    elif choice == 2:
          decrypt_flag()
          print("flag2.txt has been decrypted with the provided password. Check and see if you succeeded.")
          break
  
