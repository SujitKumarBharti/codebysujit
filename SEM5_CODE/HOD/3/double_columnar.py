def double_columnar():
    key1 = list(map(int, input("Enter first key: ").split()))
    key2 = list(map(int, input("Enter second key: ").split()))
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").replace(" ", "").upper()

    def encrypt(text, key):
        cols = len(key)

        while len(text) % cols != 0:
            text += "X"

        rows = [
            text[i:i + cols]
            for i in range(0, len(text), cols)
        ]

        result = ""

        for number in sorted(key):
            col = key.index(number)

            for row in rows:
                result += row[col]

        return result

    def decrypt(text, key):
        cols = len(key)
        rows_count = len(text) // cols

        matrix = [[""] * cols for _ in range(rows_count)]

        index = 0

        for number in sorted(key):
            col = key.index(number)

            for row in range(rows_count):
                matrix[row][col] = text[index]
                index += 1

        return "".join("".join(row) for row in matrix)

    if choice == "e":

        first = encrypt(text, key1)
        result = encrypt(first, key2)

    elif choice == "d":

        first = decrypt(text, key2)
        result = decrypt(first, key1)

    else:
        print("Invalid choice")
        return

    print("Result:", result)