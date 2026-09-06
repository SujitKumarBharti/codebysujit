def diffie_hellman():
    p = int(input("Enter prime p: "))
    g = int(input("Enter primitive root g: "))

    a = int(input("Enter Alice private key: "))
    b = int(input("Enter Bob private key: "))

    A = pow(g, a, p)
    B = pow(g, b, p)

    alice_key = pow(B, a, p)
    bob_key = pow(A, b, p)

    print("Alice Public Key :", A)
    print("Bob Public Key   :", B)
    print("Alice Shared Key :", alice_key)
    print("Bob Shared Key   :", bob_key)