def freq(word):
# count frequncies of letter in given word
    freq = {}
    for letter in word:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq


def probability(word):
    frequencies = freq(word)
    frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    lenght = len(word)
    probabilities = [round(freque[1]/lenght, 2) for freque in frequencies]
    return probabilities


if __name__ == '__main__':
    word = input('Enter to string to perform Huffman algorithm: ')

    probability(word)
