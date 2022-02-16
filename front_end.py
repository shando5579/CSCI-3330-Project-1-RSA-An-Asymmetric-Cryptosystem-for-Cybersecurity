"""
@author: Shandon Probst
@project: Algorithms Project 1
@file: front_end.py

This file is used for processing inputs from a user and giving
correct outputs. This acts as the main driver for the entire
RSA project.

"""
from operator import truediv
import key_gen

# Main driver
def main():
    # Step 1: Generate RSA keys
    key_gen.generateKeys(100000,1000000) # Generates RSA keys, where p and q are prime numbers in range 100,000 - 1,000,000
    print('RSA keys have been generated.')

    # 
    program_exit = False
    while (program_exit == False):

        # Step 2: Selecting user type
        print ('Please select your user type:')
        print ('\t1. A public user')
        print ('\t2. The owner of the keys')
        print ('\t3. Exit program')
        user_choice = input("\nEnter your choice: ")

        # Public user choices
        if (user_choice == '1'):
            public_exit = False

            while (public_exit == False):
                print ('\nAs a public user, what would you like to do?')
                print ('\t1. Send an encrypted message')
                print ('\t2. Authenticate a digital signature')
                print ('\t3. Exit')
                public_choice = input("\nEnter your choice: ")

                if (public_choice == '1'):
                    message = input('\nEnter a message: ') 
                    # enter encrypt function here
                    print ('Message encrypted and sent.')

                # write if digital signatures exist

                elif (public_choice == '3'):
                    public_exit = True
                    print ('\n')

        # Owner of keys choices
        elif (user_choice == '2'):
            owner_exit = False

            while (owner_exit == False):
                print ('\nAs the owner of the keys, what would you like to do?')
                print ('\t1. Decrypt a received message')
                print ('\t2. Digitally sign a message')
                print ('\t3. Exit')
                owner_choice = input("\nEnter your choice: ")

                """
                if (owner_choice == '1'):
                    # enter stuff here for viewing decrypted messages

                elif (owner_choice == '2'):
                    signed_message = input('\nEnter a message: ')
                    # enter function to sign message
                    print ('Message signed and sent.')


                elif (owner_choice == '3'):
                    #owner_exit = True
                    #print ('\n')
                """

        # Exit program
        elif (user_choice == '3'):
            program_exit = True

    print ('\nBye for now!')

main()
