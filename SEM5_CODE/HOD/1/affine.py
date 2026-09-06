def affine():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ")

    try:
        inverse = pow(a, -1, 26)
    except ValueError:
        print("Invalid value of a.")
        return

    result = ""

    for ch in text.upper():
        if ch.isalpha():
            x = ord(ch) - 65

            if choice == "e":
                y = (a * x + b) % 26
            elif choice == "d":
                y = (inverse * (x - b)) % 26
            else:
                print("Invalid choice")
                return

            result += chr(y + 65)
        else:
            result += ch

    print("Result:", result)