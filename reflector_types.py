from alphabet_represent import represent

class ReflectorA:
    def __init__(self):
        self.wiring = 'EJMZALYXVBWFCRQUONTSPIKHGD'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])


class ReflectorB:
    def __init__(self):
        self.wiring = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])

class ReflectorC:
    def __init__(self):
        self.wiring = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])

class ReflectorBThin:
    def __init__(self):
        self.wiring = 'ENKQAUYWJICOPBLMDXZVFTHRGS'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])

class ReflectorCThin:
    def __init__(self):
        self.wiring = 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'

    def reflect(self, letter: int):
        return represent(self.wiring[letter])