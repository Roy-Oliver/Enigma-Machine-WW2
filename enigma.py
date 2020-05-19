from alphabet_represent import represent
from plugboard import Plugboard
from reflector_types import ReflectorA, ReflectorB, ReflectorC, ReflectorBThin, ReflectorCThin
from rotor_set import RotorSet


class EnigmaMachine:
    """Creates an Enigma Machine with a Rotor Set, Reflector and Plugboard"""

    def __init__(self, rotor_settings, plugboard_settings, reflector):
        # Initialize the Enigma Machine Rotors and Plugboards
        self.rotor_set = RotorSet(rotor_settings)
        self.plugboard = Plugboard(plugboard_settings)

        # Initialize the reflector object
        if reflector == "A":
            self.reflector = ReflectorA()
        elif reflector == "B":
            self.reflector = ReflectorB()
        elif reflector == "C":
            self.reflector = ReflectorC()
        elif reflector == "BThin":
            self.reflector = ReflectorBThin()
        else:
            self.reflector = ReflectorCThin()

    def encrypt_decrypt(self, letter: int):
        # Encrypt or decrypts a letter

        # Feed the letter to the plugboard:
        if letter in self.plugboard.letter_pairs:
            plugboard_output_1 = self.plugboard.plug(letter)
        else:
            plugboard_output_1 = letter  # If there is no connection in plugboard, return the letter

        # Feed plugboard output to Rotor Set(First pass from right to left):
        rotor_output_1 = self.rotor_set.right_to_left(plugboard_output_1)

        # Feed rotor output to reflector
        reflector_output = self.reflector.reflect(rotor_output_1)

        # Feed reflector output back to rotor:
        rotor_output_2 = self.rotor_set.left_to_right(reflector_output)

        # Feed rotor output to plugboard again
        if rotor_output_2 in self.plugboard.letter_pairs:
            plugboard_output_2 = self.plugboard.plug(rotor_output_2)
        else:
            plugboard_output_2 = rotor_output_2  # If there is no connection in plugboard, return the letter

        # return the result as letter
        return represent(plugboard_output_2)  # Represent is added to Output the letter as an alphabetic letter
