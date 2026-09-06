def columnar():
    key = list(map(int, input("Enter key: ").split()))
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ").replace(" ", "").upper()

    cols = len(key)

    if sorted(key) != list(range(1, cols + 1)):
        print("Key must contain numbers from 1 to", cols)
        return

    if choice == "e":

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

    elif choice == "d":

        if len(text) % cols != 0:
            print("Invalid ciphertext.")
            return

        rows_count = len(text) // cols
        matrix = [[""] * cols for _ in range(rows_count)]

        index = 0

        for number in sorted(key):
            col = key.index(number)

            for row in range(rows_count):
                matrix[row][col] = text[index]
                index += 1

        result = ""

        for row in matrix:
            result += "".join(row)

    else:
        print("Invalid choice")
        return

    print("Result:", result)