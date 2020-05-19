from alphabet_represent import represent

class Rotor:
    """Models an Enigma rotor"""
    def __init__(self, window_position: int, ring_setting: int, order: int):
        self.window_position = window_position  # Position of the rotor as seen from the window
        self.ring_setting = ring_setting  # Position of the 'notch' in the rotor
        self.order = order  #  Order of the rotor from 1 to 3, where 1 is the leftmost, 2 is the middle and 3 is the rightmost

    def move(self):
        # Moves the window position upwards. For example, A moves to B in the window. Include mod 26 to cycle through letters
        self.window_position = (self.window_position + 1) % 26

    def right_to_left(self, letter: int):
        # The following code encodes a letter from right to left (First run across Rotors)
        # Within a rotor, INFORMATION flow is PlugBoard/Right Rotor  -> Spring Contact -> Wiring ->
        # Window (INFORMATION) -> Flat Contact

        # Plugboard -> Spring Contact
        spring_contact = (letter + self.window_position - self.ring_setting) % 26

        # Spring Contact -> Wiring
        wiring = (represent(self.wiring[spring_contact])) % 26

        # Wiring -> Window (INFORMATION)
        window = (wiring + self.ring_setting) % 26

        # Window (INFORMATION) -> Flat Contact
        flat_contact = (window - self.window_position) % 26

        # Return the letter
        return flat_contact

    def left_to_right(self, letter: int):
        # The following code encodes a letter from right to left (First run across Rotors)
        # Within a rotor, INFORMATION flow is Flat Contact -> Window (INFORMATION) -> Wiring ->
        # Spring Contact ->PlugBoard/Right Rotor

        # Flat Contact -> Window (INFORMATION)
        window = (letter + self.window_position) % 26

        #  Window (INFORMATION) -> Wiring
        wiring = (window - self.ring_setting) % 26

        # Wiring -> Spring Contact
        spring_contact = (self.wiring.index(represent(wiring))) % 26

        # Spring Contact -> Plugboard
        plugboard = (spring_contact - self.window_position + self.ring_setting) % 26

        # Return the letter
        return plugboard

class RotorI(Rotor):
    """Models an Enigma Rotor I"""

    turnover = 16 # The letter 'Q'
    wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

    def __init__(self, window_position, ring_setting, order):
        super().__init__(window_position, ring_setting, order)

class RotorII(Rotor):
    """Models an Enigma Rotor II"""

    turnover = 4 # The Letter 'E'
    wiring = "AJDKSIRUXBLHWTMCQGZNPYFVOE"

    def __init__(self, window_position, ring_setting, order):
        super().__init__(window_position, ring_setting, order)

class RotorIII(Rotor):
    """Models an Enigma Rotor II"""

    turnover = 21 # The letter 'V'
    wiring = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

    def __init__(self, window_position, ring_setting, order):
        super().__init__(window_position, ring_setting, order)

class RotorIV(Rotor):
    """Models an Enigma Rotor IV"""

    turnover = 9 # The letter 'J'
    wiring = "ESOVPZJAYQUIRHXLNFTGKDCMWB"

    def __init__(self, window_position, ring_setting, order):
        super().__init__(window_position, ring_setting, order)

class RotorV(Rotor):
    """Models an Enigma Rotor V"""

    turnover = 25 # The letter 'Z'
    wiring = "VZBRGITYUPSDNHLXAWMJQOFECK"

    def __init__(self, window_position, ring_setting, order):
        super().__init__(window_position, ring_setting, order)