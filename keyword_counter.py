'''This module takes a word and will give the next letter of the word or the
first if the word ended'''

class KeyWordGen:
    '''This class creates a stateful keyword letter generator given a word
    It is used in the cypher mainly for readability purposes. Please use only a
    string when constructing this object.'''
    def __init__(self, key):
        self.key = key
        self.current_index = 0
        self.current_letter = self.key[self.current_index]

    def next(self):
        '''This will give you the next letter in the key_word or the first if at the end of the key_word'''
        letter = self.current_letter

        self.current_index += 1

        # print(len(self.key) + "      " + self.cur)

        if(self.current_index is len(self.key)):
            self.current_index = 0

        self.current_letter = self.key[self.current_index]

        return letter
