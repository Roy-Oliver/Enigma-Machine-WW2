from rotor_types import *

class RotorSet:
    """This class models a Rotor Set. This includes the order of rotors, types of rotors and settings of the rotors"""
    def __init__(self, rotors: list):
        # Make a list of rotor objects
        self.rotors = []

        # Populate self.rotors with rotor objects
        for order, rotor in enumerate(rotors):
            if rotor[0] == "I":
                window_position = rotor[1]
                ring_setting = rotor[2]
                self.rotors.append(RotorI(window_position, ring_setting, order))
            elif rotor[0] == "II":
                window_position = rotor[1]
                ring_setting = rotor[2]
                self.rotors.append(RotorII(window_position, ring_setting, order))
            elif rotor[0] == "III":
                window_position = rotor[1]
                ring_setting = rotor[2]
                self.rotors.append(RotorIII(window_position, ring_setting, order))
            elif rotor[0] == "IV":
                window_position = rotor[1]
                ring_setting = rotor[2]
                self.rotors.append(RotorIV(window_position, ring_setting, order))
            elif rotor[0] == "V":
                window_position = rotor[1]
                ring_setting = rotor[2]
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
        # Encode from left to right on first rotor
        output_first_rotor = self.rotors[0].left_to_right(letter)

        # Encode from left to right on second rotor
        output_second_rotor = self.rotors[1].left_to_right(output_first_rotor)

        # Encode from left to right on third rotor
        output_third_rotor = self.rotors[2].left_to_right(output_second_rotor)

        # Return the result
        return output_third_rotor