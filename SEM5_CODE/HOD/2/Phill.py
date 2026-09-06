def hill():
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").upper()

    key = [
        [3, 3],
        [2, 5]
    ]

    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26

    try:
        det_inv = pow(det, -1, 26)
    except ValueError:
        print("Invalid key matrix.")
        return

    text = "".join(c for c in text if c.isalpha())

    if choice == "e":

        if len(text) % 2 != 0:
            text += "X"

        result = ""

        for i in range(0, len(text), 2):
            x1 = ord(text[i]) - 65
            x2 = ord(text[i + 1]) - 65

            y1 = (key[0][0] * x1 + key[0][1] * x2) % 26
            y2 = (key[1][0] * x1 + key[1][1] * x2) % 26

            result += chr(y1 + 65)
            result += chr(y2 + 65)

    elif choice == "d":

        if len(text) % 2 != 0:
            print("Invalid ciphertext.")
            return

        a, b = key[0]
        c, d = key[1]

        inverse_key = [
            [(d * det_inv) % 26, (-b * det_inv) % 26],
            [(-c * det_inv) % 26, (a * det_inv) % 26]
        ]

        result = ""

        for i in range(0, len(text), 2):
            x1 = ord(text[i]) - 65
            x2 = ord(text[i + 1]) - 65

            y1 = (inverse_key[0][0] * x1 +
                  inverse_key[0][1] * x2) % 26

            y2 = (inverse_key[1][0] * x1 +
                  inverse_key[1][1] * x2) % 26

            result += chr(y1 + 65)
            result += chr(y2 + 65)

    else:
        print("Invalid choice")
        return

    print("Result:", result)