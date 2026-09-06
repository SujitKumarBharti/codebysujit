def railfence():
    rails = int(input("Enter number of rails: "))
    choice = input("Enter e for Encrypt or d for Decrypt: ").lower()
    text = input("Enter text: ")

    if rails < 2:
        print("Number of rails must be at least 2.")
        return

    if choice == "e":

        fence = [""] * rails
        row = 0
        direction = 1

        for ch in text:
            fence[row] += ch

            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1

            row += direction

        result = "".join(fence)

    elif choice == "d":

        pattern = []

        row = 0
        direction = 1

        for i in range(len(text)):
            pattern.append(row)

            if row == 0:
                direction = 1
            elif row == rails - 1:
                direction = -1

            row += direction

        counts = [pattern.count(i) for i in range(rails)]

        fence = []
        index = 0

        for count in counts:
            fence.append(list(text[index:index + count]))
            index += count

        positions = [0] * rails
        result = ""

        for r in pattern:
            result += fence[r][positions[r]]
            positions[r] += 1

    else:
        print("Invalid choice")
        return

    print("Result:", result)