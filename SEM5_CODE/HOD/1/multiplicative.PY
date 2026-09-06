def multiplicative():
    key = int(input("Enter key: "))
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ")

    if choice == "e":
        multiplier = key
    elif choice == "d":
        try:
            multiplier = pow(key, -1, 26)
        except ValueError:
            print("Invalid key. Key must have inverse modulo 26.")
            return
    else:
        print("Invalid choice")
        return

    result = ""

    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - 65
            result += chr((x * multiplier) % 26 + 65)
        else:
            result += ch

    print("Result:", result)