from Crypto.Cipher import DES

def des():
    key = input("Enter 8-character key: ").encode()
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ")

    if len(key) != 8:
        print("Key must be exactly 8 characters.")
        return

    cipher = DES.new(key, DES.MODE_ECB)

    if choice == "e":
        data = text.encode()

        padding = 8 - (len(data) % 8)
        data += bytes([padding]) * padding

        encrypted = cipher.encrypt(data)

        print("Encrypted:", encrypted.hex())

    elif choice == "d":
        try:
            data = bytes.fromhex(text)

            decrypted = cipher.decrypt(data)

            padding = decrypted[-1]

            if padding < 1 or padding > 8:
                print("Invalid ciphertext.")
                return

            decrypted = decrypted[:-padding]

            print("Decrypted:", decrypted.decode())

        except Exception:
            print("Invalid ciphertext.")

    else:
        print("Invalid choice")