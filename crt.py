import helper_functions
class Message:

    p=0
    q=0

    def __init__(self,M):
        self.M = M


def generateKeys():
    # print("generating key 1 - p ....")
    p = helper_functions.generate_prime_number(10)
    # print("p:/n",p)
    # print("generating key 2 - q ....")
    q = helper_functions.generate_prime_number(10)



    while(p==q):
        # print("p and q were equal regenrating")
        q=helper_functions.generate_prime_number(10)
    # print("q:/n",q)
        # generating key
    n = p * q
    # print("your private key = ", n)
    # print("generating z ...")

    z= helper_functions.generate_prime_number(10)

    while(z==p or z==q or helper_functions.gcd(n,z)!=1):
        # print("z failed conditions, generating again")
        z = helper_functions.generate_prime_number(10)

    # print("z:/n",z)

    # print("calculating mu ...")
    mu = (helper_functions.modInverse(p,q)*p)+(helper_functions.modInverse(q,p)*q)
    # print("mu:/n",mu)
    # print("n:/n",p*q)
    x =   n*z

    # print(p,q,z,mu)
    return p,q,z,mu,x,n


def generating_random_numbers():
    k1=3
    k2=4

    return k1,k2

# keys = generateKeys()



# def encrypt_crt(M1,k1):
#     # generating keys and additional calculations
#     global p
#     global q
#     p, q, z, mu, x,n = generateKeys()
#     print("generating keys finished!")
#     print("your private key = ",n)
#     # phi(n)
#     phin = helper_functions.phi(p*q)
#     # base = M1**((k1*phin)+1)
#     now = ((M1 % x) ** (k1 * phin + 1)) % x
#     print("your encrypted message: ",now)
#     return now

def encrypt_crt(M1,k1):
    # generating keys and additional calculations
    global p
    global q
    p, q, z, mu, x,n = generateKeys()
    print("generating keys finished!")
    print("your private key = ",n)
    # phi(n)
    phin = helper_functions.phi(p*q)
    # base = M1**((k1*phin)+1)
    # now = pow(M1,k1*phin+1,x)

    l = helper_functions.convert_to_int(M1)
    enc=[]
    for i in l:
        # now = ((M1 % x) ** (k1 * phin + 1)) % x
        now = pow(i,k1*phin+1,x)

        enc.append(str(now))

    newenc = ' '.join(enc)
    print(newenc)
    return newenc

# C1 = encrypt_crt(99899,3)
# print("encrypted text=",C1)

# def decrypt_crt(C1,key):
#     #key = int(input("Enter key: "))
#
#     x = C1%(key)
#     print("decypted message: ",x)
#     return x

def decrypt_crt(C1,key):
    C1 = C1.split(' ')
    dec = []
    text = ""
    for i in C1:
        i = int(i)
        dec.append(i%(key))
    # return C1%(p*q)
    for i in dec:
        text = text + chr((i + 96))
    print("decrypted text = ",text)
    return text

# newM1 = decrypt_crt(C1,key)
# print("decrypted text= ",newM1)












