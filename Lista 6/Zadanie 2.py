import re
from collections.abc import Iterable
from collections.abc import Sequence
from typing import Union

from prettytable import PrettyTable

class HuffmanCode:
    def __init__(self,probability: Sequence):
        self.probability = probability

    def position(self, value, index: Union[complex, float, int]):
        for j in range(len(self.probability)):
            if(value >= self.probability[j]):
                return j
        return index-1


    def compute_code(self):
        num = len(self.probability)
        huffman_code = ['']*num

        for i in range(num-2):
            val = self.probability[num-i-1] + self.probability[num-i-2]
            if(huffman_code[num-i-1] != '' and huffman_code[num-i-2] != ''):
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            elif(huffman_code[num-i-1] != ''):
                huffman_code[num-i-2] = '0'
                huffman_code[-1] = ['1' + symbol for symbol in huffman_code[-1]]
            elif(huffman_code[num-i-2] != ''):
                huffman_code[num-i-1] = '1'
                huffman_code[-2] = ['0' + symbol for symbol in huffman_code[-2]]
            else:
                huffman_code[num-i-1] = '1'
                huffman_code[num-i-2] = '0'

            position = self.position(val, i)
            probability = self.probability[0:(len(self.probability) - 2)]
            probability.insert(position, val)
            if(isinstance(huffman_code[num-i-2], list) and isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + huffman_code[num-i-2]
            elif(isinstance(huffman_code[num-i-2], list)):
                complete_code = huffman_code[num-i-2] + [huffman_code[num-i-1]]
            elif(isinstance(huffman_code[num-i-1], list)):
                complete_code = huffman_code[num-i-1] + [huffman_code[num-i-2]]
            else:
                complete_code = [huffman_code[num-i-2], huffman_code[num-i-1]]

            huffman_code = huffman_code[0:(len(huffman_code)-2)]
            huffman_code.insert(position, complete_code)

        huffman_code[0] = ['0' + symbol for symbol in huffman_code[0]]
        huffman_code[1] = ['1' + symbol for symbol in huffman_code[1]]

        if(len(huffman_code[1]) == 0):
            huffman_code[1] = '1'

        count = 0
        final_code = ['']*num

        for i in range(2):
            for j in range(len(huffman_code[i])):
                final_code[count] = huffman_code[i][j]
                count += 1

        final_code = sorted(final_code, key=len)
        return final_code

def freq(word: Iterable):
# count frequncies of letter in given word
    freq = {}
    for letter in word:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq


def probability(word):
#count probability, return freq and probability
    frequencies = freq(word)
    frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    lenght = len(word)
    probabilities = [round(freque[1]/lenght, 2) for freque in frequencies]
    probabilities = sorted(probabilities, reverse=True)
    return frequencies, probabilities


def clear(word):
# clear non alphanumeric charakters
    return re.sub(r'\W+', '', word)


if __name__ == '__main__':
    word = input('Enter to string to perform Huffman algorithm: ')
    word = clear(word)

    frequencies, probabilities = probability(word)

    huffmanClassObject = HuffmanCode(probabilities)
    P = probabilities

    huffman_code = huffmanClassObject.compute_code()

    x = PrettyTable()
    x.field_names = ["Char", "Huffman Code"]


    for i in range(len(frequencies)):
        letter = frequencies[i][0]
        code = str(huffman_code[i])
        x.add_row([letter, code])

    print(' Char | Huffman code ')
    print('----------------------')

    for id, char in enumerate(frequencies):
        if huffman_code[id] == '':
            print(' %-4r |%12s' % (char[0], 1))
            continue
        print(' %-4r |%12s' % (char[0], huffman_code[id]))
