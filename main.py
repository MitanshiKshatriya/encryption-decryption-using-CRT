import sys
import time
import crt
import rsa_crt
global enc,p,q,d
def main():
    done = False
    while done == False:
        print(""" ======ENCRYPTION AND DECRYPTION USING CRT=======
                1. Encryption using CRT
                2. Decryption using CRT
                3. Encryption using RSA and CRT
                4. Decryption using RSA and CRT
                5. Exit
                """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            M1 = input("enter the message to be encrypted: ")
            crt.encrypt_crt(M1,3)
            main()
        elif choice == 2:
            C1 = input("enter the message to be decrpted: ")
            key = int(input("enter your private key: "))
            crt.decrypt_crt(C1,key)

            main()
        elif choice == 3:
            globals()["enc"],globals()["p"],globals()["q"],globals()["d"] = rsa_crt.RSA_encrypt()
            main()
        elif choice == 4:
            rsa_crt.RSA_decrypt(enc,p,q,d)
            main()

        elif choice == 5:
            sys.exit()

main()
