#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Yaya Souare

'''
This script is to take an input and encode and decode BASE64
'''

#Imported libaries
import base64



def encode_to_base64(plaintext: str) -> str:
   '''
encoding plaintext to base64
we will do the following steps 
1.) Convert the string using UTF-8
2.) Pass the bytes into a function called b64.encode
4.) Resulted bytes and return
   '''
   text_as_bytes = plaintext.encode("utf-8") # "Hello" -1> b"Hello" -> 0x48 0x65 0x6c
   encoded_bytes = base64.b64encode(text_as_bytes) # b 'Hello" -> b"SGVsbG8="
   return encoded_bytes.decode("utf-8") # b"SGVsbG8=" -> "SGVsbG"


def decode_to_base_64(encoded_text: str) -> str:
    '''
1.) Taking base64 string back to original plaintext
2.) Convert base64 string to get original byes
3.) decode those bytes back to utf-8 string  
    '''
    encode_as_bytes = encoded_text.encode("utf-8") #SGVsbG" -> b"SGVsbG8
    decoded_bytes = base64.b64decode(encode_as_bytes) # b"SGVsbG8 -> b"hello"
    return decoded_bytes.decode("utf-8")

#DEFINE main what we want to call and how

def main():
    print("Base64 Encode / Decoder")
    print(" THIS IS NOT ENCRYPTION")
    #User input of what to encode
    message = input("Enter your message to encode: ").strip()
    if not message:
        print("No message entered. Exiting")
        return
    #Encode
    encoded = encode_to_base64(message)
    print(f"Base encoded: {encoded}")


    #Decode
    decoded = decode_to_base_64(encoded)
    print(f"Decoded message: {decoded}")
    #Validation
    if decoded == message:
        print("Confirmation matched")
    else:
        print("Confirmation: Message do not match.")



    if __name__ == "__main__":
        main()
