def rsa():
    p = int(input("Enter prime p: "))
    q = int(input("Enter prime q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = int(input("Enter public key e: "))

    try:
        d = pow(e, -1, phi)
    except ValueError:
        print("Invalid e.")
        return

    message = int(input("Enter numeric message: "))

    encrypted = pow(message, e, n)
    decrypted = pow(encrypted, d, n)

    print("Public Key :", (e, n))
    print("Private Key:", (d, n))
    print("Encrypted  :", encrypted)
    print("Decrypted  :", decrypted)