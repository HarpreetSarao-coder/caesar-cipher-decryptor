from caesar_cipher import caesar_cipher_decrypt

if __name__ == "__main__":
    encrypted_input = input("Enter the encrypted message: ").strip()
    try:
        decrypted = caesar_cipher_decrypt(encrypted_input)
        print("Decrypted message:", decrypted)
    except ValueError as e:
        print("Error:", e)
