from alphabet_represent import represent

class ReflectorA:
    def reflect(self, letter: int):
        wiring = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        return represent(wiring[letter])