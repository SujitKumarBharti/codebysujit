def otp():
    key = input("Enter key: ").upper()
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").upper()

    if not text.isalpha() or not key.isalpha():
        print("Only alphabets are allowed.")
        return

    if len(key) != len(text):
        print("OTP key length must be equal to text length.")
        return

    result = ""

    for i in range(len(text)):

        if choice == "e":
            value = (
                (ord(text[i]) - 65) +
                (ord(key[i]) - 65)
            ) % 26

        elif choice == "d":
            value = (
                (ord(text[i]) - 65) -
                (ord(key[i]) - 65)
            ) % 26

        else:
            print("Invalid choice")
            return

        result += chr(value + 65)

    print("Result:", result)