def encode(password):
    encoded = ""
    for i in password:
        num = int(i)
        num2 = (num + 3) % 10
        encoded += str(num2)
    return encoded
