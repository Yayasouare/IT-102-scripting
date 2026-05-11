#!/usr/bin/env python3
# Script that encodes and decodes text using Base64
# By Yaya Souare
"""
This script is to take an input and encode and decode BASE64
"""

#Imported libaries
import base64


def encode_to_base64(plaintext: str) -> str:
    """
Encoding plaintext to Base64.
We will do the following steps
1. Convert string to bytes (UTF-8)
2. Pass the bytes into a function called b64.encode
3.Resulted bytes and return
    """
    text_as_bytes = plaintext.encode("utf-8") # "Hello" -1> b"Hello" -> 0x48 0x65 0x6c
    encoded_bytes = base64.b64encode(text_as_bytes) # b"Hello" -> b"SGVsbG8="
    return encoded_bytes.decode("utf-8") # b"SGVsbG8=" -> "SGVsbG"


def decode_from_base64(encoded_text: str) -> str:
    """
    Decode Base64 back to plaintext.
    1. Taking base64 string back to original plaintext
    2. Convert base64 string to get original bytes
    3. decode those bytes back to utf-8 string
    """
    encoded_as_bytes = encoded_text.encode("utf-8") #SGVsbG" -> b"SGVsbG8
    decoded_bytes = base64.b64decode(encoded_as_bytes) # b"SGVsbG8 -> b"hello"
    return decoded_bytes.decode("utf-8")

#DEFINE main what we want to call and how

def main():
    print("Base64 Encoder / Decoder")
    print(" This IS NOT ENCRYPTION")

    # User input of what to encode
    message = input("Enter your message to encode: ").strip()

    if not message:
        print("No message entered. Exiting.")
        return

    #Encode
    encoded = encode_to_base64(message)
    print(f"Base64 : {encoded}")

    # Decode
    decoded = decode_from_base64(encoded)
    print(f"Decoded message: {decoded}")

    #Validation
    match = decoded == message
    print("Confirmation matched")
    print()


if __name__ == "__main__":
    main()