def represent(letter):
    """ -Converts a letter to its index. A -> 0, B -> 1...
       -Converts an index to its letter
       -if string is not a letter, return the letter
    """

    alphabet_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_small = "abcdefghijklmnopqrstuvwxyz"
    if type(letter) == str:
        if letter.isupper():
            return alphabet_capital.index(letter)
        elif letter.islower():
            return alphabet_small.index(letter)
        else:
            return letter
    if type(letter) == int:
        return alphabet_capital[letter]