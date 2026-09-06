def additive():
    key = int(input("Enter key: "))
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ")

    if choice == "e":
        shift = key
    elif choice == "d":
        shift = -key
    else:
        print("Invalid choice")
        return

    result = ""

    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch

    print("Result:", result)