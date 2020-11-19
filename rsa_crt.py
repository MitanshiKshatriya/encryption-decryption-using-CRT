


import sympy
import time


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def convert_to_int(text):
    converted = []
    for letter in text:
        converted.append(ord(letter) - 96)
    print("converted to int: ",converted)
    return converted


def convert_to_ascii(text):
    converted = ''
    for number in text:
        converted = converted + chr(number + 96)
    print(converted)
    return converted


def choose_e(phi, n):
    print('Choosing e...')
    for e in range(2 ** 31, 2, -1):
        if gcd(e, phi) == 1 and gcd(e, n) == 1:
            return e


def modular_inverse(a, m):  # modular inverse of e modulo phi
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0

    return x


def encrypt(text, public_key):
    key, n = public_key
    ctext = [pow(ord(char), key, n) for char in text]
    return ctext


def decrypt(ctext, private_key):
    key, n = private_key
    text = [chr(pow(char, key, n)) for char in ctext]
    return "".join(text)





# The CRT method of decryption
def TCR(p, q, dP, dQ, c):
    qInv = modular_inverse(q, p)
    m1 = pow(c, dP, p)
    m2 = pow(c, dQ, q)
    h = (qInv * (m1 - m2)) % p
    m = m2 + h * q
    return m


def RSA_encrypt():
    enc = []
    dec = []
    p = sympy.nextprime(2 ** 512)
    q = sympy.nextprime(p)
    print('p = ', p, ' q = ', q)
    n = p * q
    print('n = ', n)
    phi = (p - 1) * (q - 1)

    print('phi = ', phi)
    e = choose_e(phi, n)
    print('e = ', e)
    d = modular_inverse(e, phi)
    print('d = ', d)
    #text = 'encryption'
    text = input('Enter the text you want to encrypt: ')
    print('Plaintext: ', text)
    converted = convert_to_int(text)
    for number in converted:
        enc.append(pow(number, e, n))
    print('Encrypted text: ', enc)
    return enc,p,q,d

def RSA_decrypt(enc,p,q,d):
    # enc = input("enter the encrypted key: ")
    # p = int(input("enter p: "))
    # q = int(input("enter q: "))
    # d = int(input("enter d: "))
    dp = d % (p - 1)
    dq = d % (q - 1)
    text = ''
    for number in enc:
        number=int(number)
        text = text + chr(TCR(p, q, dp, dq, number) + 96)
    print("decrypted text: ",text)




