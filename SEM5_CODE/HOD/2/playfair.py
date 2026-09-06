def playfair():
    key = input("Enter key: ").upper().replace("J", "I")
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").upper().replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    key = "".join(dict.fromkeys(c for c in key if c.isalpha()))
    letters = key + "".join(c for c in alphabet if c not in key)

    matrix = [letters[i:i+5] for i in range(0, 25, 5)]

    print("\nPlayfair Matrix:")

    for row in matrix:
        print(" ".join(row))

    text = "".join(c for c in text if c.isalpha())

    if choice == "e":
        pairs = []
        i = 0

        while i < len(text):
            a = text[i]

            if i + 1 >= len(text):
                b = "X"
                i += 1
            elif text[i + 1] == a:
                b = "X"
                i += 1
            else:
                b = text[i + 1]
                i += 2

            pairs.append((a, b))

        shift = 1

    elif choice == "d":
        if len(text) % 2 != 0:
            print("Invalid ciphertext.")
            return

        pairs = [(text[i], text[i + 1]) for i in range(0, len(text), 2)]
        shift = -1

    else:
        print("Invalid choice")
        return

    result = ""

    for a, b in pairs:

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    ra, ca = r, c
                if matrix[r][c] == b:
                    rb, cb = r, c

        if ra == rb:
            result += matrix[ra][(ca + shift) % 5]
            result += matrix[rb][(cb + shift) % 5]

        elif ca == cb:
            result += matrix[(ra + shift) % 5][ca]
            result += matrix[(rb + shift) % 5][cb]

        else:
            result += matrix[ra][cb]
            result += matrix[rb][ca]

    print("Result:", result)