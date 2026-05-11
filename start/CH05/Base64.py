#!/usr/bin/env python3
# Script that encodes and decodes text using Base64
# By Yaya Souare

import base64


def encode_to_base64(plaintext: str) -> str:
    """
    Encode plaintext to Base64.
    Steps:
    1. Convert string to bytes (UTF-8)
    2. Encode using base64
    3. Convert result back to string
    """
    text_as_bytes = plaintext.encode("utf-8")
    encoded_bytes = base64.b64encode(text_as_bytes)
    return encoded_bytes.decode("utf-8")


def decode_from_base64(encoded_text: str) -> str:
    """
    Decode Base64 back to plaintext.
    Steps:
    1. Convert string to bytes
    2. Decode Base64 bytes
    3. Convert back to UTF-8 string
    """
    encoded_as_bytes = encoded_text.encode("utf-8")
    decoded_bytes = base64.b64decode(encoded_as_bytes)
    return decoded_bytes.decode("utf-8")


def main():
    print("Base64 Encoder / Decoder")
    print("NOTE: This is NOT encryption, only encoding.\n")

    # User input
    message = input("Enter your message to encode: ").strip()

    if not message:
        print("No message entered. Exiting.")
        return

    # Encode
    encoded = encode_to_base64(message)
    print(f"Base64 encoded : {encoded}")

    # Decode
    decoded = decode_from_base64(encoded)
    print(f"Decoded message: {decoded}")

    # Confirmation
    confirmation = decoded == message
    print(f"Confirmation   : {confirmation}")


if __name__ == "__main__":
    main()