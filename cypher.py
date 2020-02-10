'''This function contains the capabilities of encrypting or decrypting the text stored in the member variables.
It uses the Viginere Cypher method of encryption: https://en.wikipedia.org/wiki/Vigenère_cipher'''
import keyword_counter as kc

class Cypher:
    '''Contains a cypher 2D-array (representing the Viginere Table Cypher), a cypher legend dictionary, and member functions
    change the text to be encrypted, or keyword.'''
    cypher = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', \
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A'],
        ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', \
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
        ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', \
        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C'],
        ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D'],
        ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', \
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E'],
        ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
        'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F'],
        ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', \
        'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
        ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', \
        'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', \
        'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
        ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', \
        'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', \
        'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
        ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
        ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', \
        'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'],
        ['O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', \
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'],
        ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', \
        'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'],
        ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', \
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
        ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', \
        'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'],
        ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', \
        'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
        ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', \
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
        ['U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', \
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'],
        ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', \
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'],
        ['W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'],
        ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'],
        ['Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', \
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'],
        ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    ]
    cypher_legend = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9,
        'K': 10,
        'L': 11,
        'M': 12,
        'N': 13,
        'O': 14,
        'P': 15,
        'Q': 16,
        'R': 17,
        'S': 18,
        'T': 19,
        'U': 20,
        'V': 21,
        'W': 22,
        'X': 23,
        'Y': 24,
        'Z': 25
    }

    def __init__(self, text="", key_word=""):
        '''Simplified, but neccessary constructor for Cypher.'''
        self.text = text
        self.key_word = key_word
        self.encrypted_text = ""

    def change_text(self, new_text):
        '''Changes the text that is to be encrypted.'''
        self.text = new_text

    def get_text(self):
        '''Get the current text'''
        return self.text

    def change_key_word(self, new_key_word):
        '''Changes thew keyword used to encrypt the text.'''
        self.key_word = new_key_word

    def get_encrypted_text(self):
        '''Get the finalized encypted text.'''
        return self.encrypted_text

    def change_encrypted_text(self, new_encryption):
        '''Set the current encrypted text'''
        self.encrypted_text = new_encryption

    def encrypt(self):
        '''Uses the cypher, legend and given keyword to encrypt the text.
        Keyword and text are supplied using the change functions. See change_text,
        change_key_word.'''
        key_gen = kc.KeyWordGen(self.key_word)

        self.encrypted_text = ""
        intermediary_text = ""

        for letter in self.text:
            if letter == ' ':
                intermediary_text += ' '
                continue
            intermediary_text += key_gen.next()

        for letter, inter_letter in zip(self.text, intermediary_text):
            if letter == ' ':
                self.encrypted_text += ' '
                continue
            letter_index = self.cypher_legend[letter]
            inter_letter_index = self.cypher_legend[inter_letter]
            self.encrypted_text += self.cypher[inter_letter_index][letter_index]

        #   DEBUG
        # print(self.text)
        # print(intermediary_text)
        # print(self.encrypted_text)

    def decrypt(self):
        '''Uses the cypher, legend and given keyword to decrypt an encrypted text.
        Keyword and encryption are supplied using the change functions. See change_encrypted_text,
        change_key_word.'''
        key_gen = kc.KeyWordGen(self.key_word)

        self.text = ""
        intermediary_text = ""

        for letter in self.encrypted_text:
            if letter == ' ':
                intermediary_text += ' '
                continue
            intermediary_text += key_gen.next()

        for letter, inter_letter in zip(self.encrypted_text, intermediary_text):
            if letter == ' ':
                self.text += ' '
                continue
            # letter_index = self.cypher_legend[letter]
            inter_letter_index = self.cypher_legend[inter_letter]

            letter_index = 0

            for character in self.cypher[inter_letter_index]:
                if character == letter:
                    break
                letter_index += 1

            self.text += self.cypher[0][letter_index]

        #   DEBUG
        # print(self.encrypted_text)
        # print(intermediary_text)
        # print(self.text)

    def encrypt_file(self, name_of_file, name_of_result_file):
        '''Uses the cypher, legend and given keyword to encrypt the text of a file and
        stores it into another file. The keyword is supplied using the chenge_key_word function.'''
        #   TODO Complete the function based on the encrypt function but on a file instead

        try:
            with open(name_of_file, 'r') as file, open(name_of_result_file, 'w') as result:
                lines = file.readlines()

                for line in lines:
                    self.text = line.rstrip().upper()
                    self.encrypt()
                    result.write(self.encrypted_text + '\n')

        except IOError:
            print('File not accessible, or does not exist.')
            return False
        except Exception as e:
            print('Some other error occured: ' + print(e))
            return False

        return True

    def decrypt_file(self, name_of_file, name_of_result_file):
        '''Uses the cypher, legend and given keyword to decrypt an encrypted file and stores the result
        in another file. The keyword is supplied using the change_key_word function.'''
        #   TODO Complete the function.

        try:
            with open(name_of_file, 'r') as file, open(name_of_result_file, 'w') as result:
                lines = file.readlines()

                for line in lines:
                    self.encrypted_text = line.rstrip().upper()
                    # print(self.encrypted_text)
                    self.decrypt()
                    # print(self.text)
                    result.write(self.text + '\n')

        except IOError:
            print('File not accessible, or does not exist.')
            return False
        except Exception as e:
            print('Some other error occured: ' + print(e))
            return False

        return True

    def special_encrypt(self, text, keywords, length_of_partition):
        '''Special encryption given the text, a list of keywords, and a length.
        For details on how this encryptions works, see the README document.'''
        #   TODO Complete the special encrypt function
        pass
