def caesar_cipher_decrypt(ciphertext: str) -> str:
    decrypted = []

    for char in ciphertext:
        if 'a' <= char <= 'z':
            shifted = chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
            decrypted.append(shifted)
        else:
            raise ValueError(f"Invalid character '{char}' in ciphertext. Only lowercase letters are allowed.")

    return ''.join(decrypted)
