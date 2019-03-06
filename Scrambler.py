from random import shuffle
class Scrambler():
    '''
    A class for scrambling text input.
    ...
    Attributes
    -----------
    sentences : list of str
    
    Methods
    -------
    scramble_word(word)
        Scrambles a single word
        
    scramble_it()
        Scrambles all sentences in sentences list
         '''
    def __init__(self):

        self.sentences = []
        sentence = input("Enter sentence: ")
        while sentence is not '':
            self.sentences.append(sentence)
            sentence = input()

    def scramble_word(self, word):
        '''
        Parameters
        ----------
        word: str
            A word from sentences list
        '''
        word = list(word)
        shuffle(word)
        return ''.join(word)

    def scramble_it(self):
        for sentence in self.sentences:
            for word in sentence.split():
                print(self.scramble_word(word), end=' ')
            print()
temp = Scrambler()
temp.scramble_it()

    