def vernam():
    key = input("Enter key: ").upper()
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").upper()

    if not key.isalpha():
        print("Invalid key.")
        return

    result = ""

    for i, ch in enumerate(text):
        if ch.isalpha():
            p = ord(ch) - 65
            k = ord(key[i % len(key)]) - 65

            result += chr((p ^ k) + 65)
        else:
            result += ch

    print("Result:", result)