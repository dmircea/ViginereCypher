'''This is the cript containing the main function for the cypher program.'''
import cypher as ciph

def main():
    '''Main file for the cypher program.'''
    print('Welcome to the Viginere Cypher Program!')

    cypher = ciph.Cypher()

    while True:
        print('Please choose an option: ')

        #   Options --> open to change in future versions
        print(' 1. Type a text to encrypt.')
        print(' 2. Type the name of a file to encrypt.')
        print(' 3. Type an encrypted text to decrypt.')
        print(' 4. Type the name of a file to decrypt.')
        print(' 5. Utilize special encryptions.')
        print(' 0. See help.')
        print('-1. Exit the program.')

        choice = int(input('Choice: '))

        if   choice == -1:
            #   Sentinel option for quitting the program
            print('Thank you for using the Viginere Cypher Program.')
            break

        if   choice == 0:
            #   HELP option for what each option does.
            pass

        if   choice == 1:
            #   Utilize the basic functions to encrypt the text
            input_text = input('Please type a text here: ')
            input_key = input('Please type the keyword that will be used here: ')
            print('Computing encryption...')

            cypher.change_text(input_text.upper())
            cypher.change_key_word(input_key.upper())
            cypher.encrypt()

            print('Done!')
            print('Here is the encrypted text: ' + cypher.get_encrypted_text())
            print()

        elif choice == 2:
            #   Utilize the basic functions, then choose a file to encrypt
            #   Does nothing if file by the given name does not exist
            input_file = input('Please enter the name of the file you wish to encrypt: ')
            input_key = input('Please type the keyword that will be used here: ')
            result_file = input('Please enter the name of the resulting file: ')
            print('Computing encryption...')

            cypher.change_key_word(input_key.upper())
            successful = cypher.encrypt_file(input_file, result_file)

            print('Done!') if successful else print('Error occured. Please try again!')
            print()

        elif choice == 3:
            #   Utilize the basic functions to decrypt an already encrypted text.
            input_text = input('Please type an encrypted text here: ')
            input_key = input('Please type the keyword that will be used here: ')
            print('Computing decryption...')

            cypher.change_encrypted_text(input_text.upper())
            cypher.change_key_word(input_key.upper())
            cypher.decrypt()

            print('Done!')
            print('Here is the actual text: ' + cypher.get_text())
            print()

        elif choice == 4:
            #   Utilize the basic functions to decrypt an already encrypted file.
            input_file = input('Please enter the name of the file you wish to decrypt: ')
            input_key = input('Please type the keyword that will be used here: ')
            result_file = input('Please enter the name of the resulting file: ')
            print('Computing decryption...')

            cypher.change_key_word(input_key.upper())
            successful = cypher.decrypt_file(input_file, result_file)

            print('Done!') if successful else print('Error occured. Please try again!')
            print()

        elif choice == 5:
            #   Makes use of the special encryptions using multiple keywords and a partition length.
            pass


if __name__ == '__main__':
    main()
