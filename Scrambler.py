from random import shuffle
class Scrambler():

    def __init__(self):

        self.sentences = []
        sentence = input("Enter sentence: ")
        while sentence is not '':
            self.sentences.append(sentence)
            sentence = input()
    def scramble_word(self, word):
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

    