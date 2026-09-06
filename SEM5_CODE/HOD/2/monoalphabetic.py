def monoalphabetic():
    key = input("Enter 26-letter key: ").upper()
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").upper()

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if len(key) != 26 or len(set(key)) != 26 or not key.isalpha():
        print("Invalid key. Enter 26 unique letters.")
        return

    if choice == "e":
        source = alphabet
        target = key

    elif choice == "d":
        source = key
        target = alphabet

    else:
        print("Invalid choice")
        return

    result = ""

    for ch in text:
        if ch.isalpha():
            result += target[source.index(ch)]
        else:
            result += ch

    print("Result:", result)