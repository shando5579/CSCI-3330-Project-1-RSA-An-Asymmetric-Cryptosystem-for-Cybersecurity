"""
@author: Shandon Probst
@project: Algorithms Project 1
@file: front_end.py
This file is used for processing inputs from a user and giving
correct outputs. This acts as the main driver for the entire
RSA project.
"""
import key_gen
import encrypt_decrypt
import digital_signature

global m


def main():


    '''Main driver'''

    # Step 1: Generate RSA keys
    key_gen.generateKeys(100000,
                         1000000)  # Generates RSA keys, where p and q are prime numbers in range 100,000 - 1,000,000
    print('RSA keys have been generated.')

    signature = []
    enc_signature = []
    enc_msgs = []
    dec_msg = []

    #
    program_exit = False
    while (program_exit == False):

        # Step 2: Selecting user type
        print('Please select your user type:')
        print('\t1. A public user')
        print('\t2. The owner of the keys')
        print('\t3. Exit program')
        user_choice = input("\nEnter your choice: ")

        # A public user
        if (user_choice == '1'):
            public_exit = False

            while (public_exit == False):
                # List of options for public user to do
                print('\nAs a public user, what would you like to do?')
                print('\t1. Send an encrypted message')
                print('\t2. Authenticate a digital signature')
                print('\t3. Exit')
                public_choice = input("\nEnter your choice: ")

                # Send an encrypted message
                if (public_choice == '1'):
                    message = input('\nEnter a message: ')
                    # Encrypts and stores encrypted message
                    print('Message encrypted and sent.')

                # Authenticate a digital signature
                elif (public_choice == '2'):
                    if not signature:  # If no signatures in the signature array
                        print('There are no signatures to authenticate')

                    else:  # If there are signatures to be read
                        auth_exit = False
                        auth_choices = []  # Signatures the public user may choose from
                        while (auth_exit == False):

                            # Displays all available signatures
                            print('\nThe following messages are available:')
                            for i in range(0, len(signature), 1):
                                print(i + 1, '. ', signature[i])
                                auth_choices.append(i + 1)

                            # Prompts for choice
                            auth_choice = input("\nEnter your choice: ")
                            auth_choice = int(auth_choice)

                            if (auth_choice > 0 & auth_choice <= len(
                                    signature)):  # See if the choice was a valid number

                                # If the digital signature can authenticate the encrypted signature with the provided n and e, it is valid
                                if (digital_signature.authenticate(enc_signature[auth_choice - 1], 119, 5)):
                                    print('Signature is valid.')

                                else:
                                    print('Signature is invalid.')

                            auth_exit = True

                # Return to main menu
                elif (public_choice == '3'):
                    public_exit = True
                    print('\n')

        # The owner of the keys
        elif (user_choice == '2'):
            owner_exit = False

            # List of options for owner to do
            while (owner_exit == False):
                print('\nAs the owner of the keys, what would you like to do?')
                print('\t1. Decrypt a received message')
                print('\t2. Digitally sign a message')
                print('\t3. Exit')
                owner_choice = input("\nEnter your choice: ")

                # Decrypt a received message
                if (owner_choice == '1'):
                    if not enc_msgs:  # If no messages in the encrypted messages array
                        print('There are no messages to decrypt')

                    else:
                        # Makes sure user enters a valid choice
                        decrypt_exit = False
                        decrypt_choices = []
                        while (auth_exit == False):

                            print('\nThe following messages are available:')

                            # Displays all currently available encrypted messages
                            for i in range(0, len(enc_msgs), 1):
                                print(i + 1, '. ', enc_msgs[i])
                                decrypt_choices.append(i + 1)

                            decrypt_choice = input("\nEnter your choice: ")
                            # Enter decryption stuff here
                            decrypt_exit = True

                # Digitally sign a message
                elif (owner_choice == '2'):
                    signed_message = input('\nEnter a message: ')
                    signature.append(signed_message)
                    enc_signature.append(digital_signature.sign(19, 119, 77))
                    print('Message signed and sent.')

                # Return to main menu
                elif (owner_choice == '3'):
                    owner_exit = True
                    print('\n')


        # Exit program
        elif (user_choice == '3'):
            program_exit = True

        else:  # Makes sure user enters a proper choice
            print('\nPlease enter a valid choice (1-3).\n')

    print('\nBye for now!')


main()