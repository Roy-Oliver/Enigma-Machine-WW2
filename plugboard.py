class Plugboard:
    def __init__(self, pairs: list):
        self.letter_pairs = {}
        for pair in pairs:
            self.letter_pairs[pair[0]] = pair[1]
            self.letter_pairs[pair[1]] = pair[0]
    def plug(self, letter):
        return self.letter_pairs[letter]