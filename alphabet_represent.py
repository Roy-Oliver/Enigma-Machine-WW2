def represent(letter):
    """Converts a letter to its index. A -> 0, B -> 1..."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if type(letter) == str:
        return alphabet.index(letter)
    if type(letter) == int:
        return alphabet[letter]