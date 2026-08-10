import random
import string
import base64
import hashlib
from cryptography.fernet import Fernet
import time


# to do: add a way to check passwords based on timestamps

#level 3: digits, punctuation, and letters, determined by timestamp seed
def generate_password_3(length=8):
  
    now = int(time.time())
    random.seed(now)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters, k=length))    
    return password
   





def decrypt_flag():
    password = input("Enter the password.")
    filename = "flag3.txt"

    # Deterministically recreate the exact same key
    key_bytes = hashlib.sha256(password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_bytes)
    cipher = Fernet(fernet_key)

    # Read the encrypted data
    with open(filename, "rb") as f:
        encrypted_data = f.read()

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write the decrypted data back to the file (or a new file)
    with open(filename, "wb") as f:
        f.write(decrypted_data)


generate_password_3()

while True:
    print("Welcome to Level 3 of this Insecure Cryptography CTF. Your goal is to use your cryptography and programming knowledge to crack the password and decrypt the .txt files to get the flag.\n")
    print("You are allowed to inspect the source code, but do not think the flag will just be sitting there in plain sight! You may have to write your own script to reverse the encryption algorithm, or brute-force your way through the challenges. Either way, I wish you the best of luck. Go forth and hack stuff. \n")
    print("A hint: The flag file was encrypted using a password that was randomly generated (with Python's random library) using a timestamp as a seed value. The program then takes that password, hashes it with sha256, then uses that key to encrypt the file. \n")
    print("Decrypting the file works in reverse: You provide your password, the program hashes it, then tries to use that hash as a key to decrypt the file.\n")
    print("Sources say that the password was generated on Saturday, July 25, 2026 at 2:27:55 AM\n")
    print("If you would like to see the random password generator operate in real time, type '1'. Type '0' to quit the challenge. Type '2' to attempt to decrypt the file. \n")
    words = input("What will you do?")
    choice = int(words)

    if choice == 0:
        break
    elif choice == 1:
        print("\n========================================")
        print("Your password is:", generate_password_3())
        print("========================================\n")
        
        # this pause keeps the password on screen until you press Enter
        input("Press Enter to return to the main menu...") 
        
    elif choice == 2:
        decrypt_flag()
        print("flag3.txt has been decrypted with the provided password. Check and see if you succeeded.")
        break
