"""These classes model different types of reflectors"""

from components.alphabet_represent import represent


class ReflectorA:
    """A class that models an Enigma Reflector A"""

    def __init__(self):
        # Add the wiring
        self.wiring = 'EJMZALYXVBWFCRQUONTSPIKHGD'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])


class ReflectorB:
    """A class that models an Enigma Reflector B"""

    def __init__(self):
        self.wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])


class ReflectorC:
    """A class that models an Enigma Reflector C"""

    def __init__(self):
        self.wiring = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])


class ReflectorBThin:
    """A class that models an Enigma Reflector B Thin"""

    def __init__(self):
        self.wiring = 'ENKQAUYWJICOPBLMDXZVFTHRGS'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])


class ReflectorCThin:
    """A class that models an Enigma Reflector C Thin"""

    def __init__(self):
        self.wiring = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])


class ModifiedReflector:
    """A class that models a reflector which can reflect letters to itself"""

    def __init__(self):
        self.wiring = "AVKDEFYSZOCLWNJUQRHTPBMXGI"

    def reflect(self, letter: int):
        return represent(self.wiring[letter])
