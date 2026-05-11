#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Yaya

def caesar_encrypt(message: str, shift: int) -> str:
    """
    Encrypt a message by shifting each letter a shift amount 
    A-Z
    a-z

    """

    result= []

    for char in message:
        if char.isupper():
            shifted = (ord(char) - ord("A") + shift) % 26 + ord("A")
            result.append(chr(shifted))
        elif char.islower():
            shifted = (ord(char) - ord("a") + shift) % 26 + ord("a")
            result.append(chr(shifted))
        else:
            result.append(char)

    return "".join(result)
        

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypt a caesar cipher message by shifting backwards
    """
    return caesar_encrypt(ciphertext, -shift)
        
def get_shift_value() -> int:
     """
     Prompt the user for a shifts value between 1 and 25.
     """
     while True:
        try: 
            shift = int(input("Enter a value between 1-25: "))
            if 1 <= shift <= 25:
                return shift
            print("Please enter a valid shift.")
        except ValueError:
            print("Please enter a valid number or integer.")

def main():
    print("Caesar Cipher Encrypt and Decrypt")
    message = input("Enter a message: ").strip()
    if not message:
         print("No message entered. Exiting.")
         return
                        
    #get shift value
    shift = get_shift_value()

    #Encrypt
    encrypted = caesar_encrypt(message, shift)
    print(f"Encrypted message: {encrypted}")

    #Ask for decryption
    answer = input("decrypt the message? (yes/no): ").strip().lower()

    if answer in ("yes", "y"):
       decrypted = caesar_decrypt(encrypted, shift)
       print(f"Decrypted message: {decrypted}")
                    
       #Validation
       match = decrypted == message
       print(f"validation of match {match}")
    else: 
        print("Decryption skipped.")
    print()

if __name__ == "__main__":
    main()


    





