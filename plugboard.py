from alphabet_represent import represent

class Plugboard:
    """ Models a plugboard"""
    def __init__(self, pairs: str):
        # Initiate plugboard connections
        self.letter_pairs = {}

        # Populate plugboard settings
        pairs = pairs.split()

        for letter_pair in pairs:
            first_letter = represent(letter_pair[0])
            second_letter = represent(letter_pair[1])
            self.letter_pairs[first_letter] = second_letter
            self.letter_pairs[second_letter] = first_letter

    def plug(self, letter):
        # Returns the letter pair based on the plugboard settings
        return self.letter_pairs[letter]