from alphabet_represent import represent

class Plugboard:
    def __init__(self, pairs: list):
        self.letter_pairs = {}
        for pair in pairs:
            first_letter = represent(pair[0])
            second_letter = represent(pair[1])
            self.letter_pairs[first_letter] = second_letter
            self.letter_pairs[second_letter] = first_letter
    def plug(self, letter):
        return self.letter_pairs[letter]