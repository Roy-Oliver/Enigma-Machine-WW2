from components.rotor_types import RotorI, RotorII, RotorIII, RotorIV, RotorV
from components.alphabet_represent import represent


class RotorSet:
    """This class models a WW2 Enigma Rotor Set. This includes the order of the 3 rotors, types of rotors
    and settings of the rotors """

    def __init__(self, rotors: list):
        # Make an empty list of rotor objects
        self.rotors = []

        # Populate self.rotors with 3 rotor objects
        for order, rotor in enumerate(rotors):
            if rotor[0] == "I":
                # The Represent Function is enables setting the rotors with letters
                window_position = represent(rotor[1])
                ring_setting = represent(rotor[2])
                self.rotors.append(RotorI(window_position, ring_setting, order))
            elif rotor[0] == "II":
                window_position = represent(rotor[1])
                ring_setting = represent(rotor[2])
                self.rotors.append(RotorII(window_position, ring_setting, order))
            elif rotor[0] == "III":
                window_position = represent(rotor[1])
                ring_setting = represent(rotor[2])
                self.rotors.append(RotorIII(window_position, ring_setting, order))
            elif rotor[0] == "IV":
                window_position = represent(rotor[1])
                ring_setting = represent(rotor[2])
                self.rotors.append(RotorIV(window_position, ring_setting, order))
            elif rotor[0] == "V":
                window_position = represent(rotor[1])
                ring_setting = represent(rotor[2])
                self.rotors.append(RotorV(window_position, ring_setting, order))

    def rotorset_move(self):
        # Turn the third rotor
        self.rotors[2].move()

        # Check if the middle rotor needs to turn
        if self.rotors[2].turnover + 1 == self.rotors[2].window_position:
            self.rotors[1].move()
        # Check for double-step
        elif self.rotors[1].turnover == self.rotors[1].window_position:
            self.rotors[1].move()
            self.rotors[0].move()

    def right_to_left(self, letter):
        # This method encodes a letter wherein the information / letter goes from right to left

        # Move the rotor. Happens only once during typing.
        self.rotorset_move()

        # Encode from right to left on third rotor
        output_third_rotor = self.rotors[2].right_to_left(letter)

        # Encode from right to left on middle rotor
        output_second_rotor = self.rotors[1].right_to_left(output_third_rotor)

        # Encode from right to left on first rotor
        output_first_rotor = self.rotors[0].right_to_left(output_second_rotor)

        return output_first_rotor

    def left_to_right(self, letter):
        # This method encodes a letter wherein the information / letter goes from right to left

        # Encode from left to right on first rotor
        output_first_rotor = self.rotors[0].left_to_right(letter)

        # Encode from left to right on second rotor
        output_second_rotor = self.rotors[1].left_to_right(output_first_rotor)

        # Encode from left to right on third rotor
        output_third_rotor = self.rotors[2].left_to_right(output_second_rotor)

        # Return the result
        return output_third_rotor
