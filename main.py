"""
A program that simulates the Wehrmacht Enigma used by the Nazi Army and Air Force during World War 2
Rotor types available : I, II, III, IV, V
Reflectors available: A, B, C, BThin, CThin

Edit out code below and/or run this file. An example is pre-filled
"""

from components.enigma import EnigmaMachine
from components.user_inputs import set_rotor, set_reflector, set_plugboard, encode_decode

# Rotor Settings
# Format from left to right: [[rotor type: str, start position: str, ring setting: str]...]
# Rotor types available : I, II, III, IV, V
# Type rotor settings in capital letters, otherwise there may be an error
# Uncomment the following line if you want command line interaction
# rotors_settings = set_rotor()
rotors_settings = [["I", "E", "E"], ["III", "Q", "F"], ["IV", "P", "I"]]

# Choose a reflector
# Format: reflector: str
# Reflectors available: A, B, C, BThin, CThin
# Type reflector settings in capital letters, otherwise there may be an error
# Uncomment the following line if you want command line interaction
# reflector_type = set_reflector()
reflector_type = "B"

# Plugboard settings
# Format: "AB CD EF GH IJ"
# Plugboard pairs my be in lowercase
# Type None if there are no plugboard pairs
# Uncomment the following line if you want command line interaction
# plugboard_settings = set_plugboard()
plugboard_settings = "bq cr di ej kw mt os px uz gh"

# Create an Enigma Machine Object
enigma_machine = EnigmaMachine(rotors_settings, plugboard_settings, reflector_type)

# Encode or Decode the message
# Accepts lowercase letters and removes the spaces from the string. Non alphabetic characters are not allowed.
message = "zpbisehkwmfoqasflctixnaawwxjsufhzwtfzheybbkswxgnpmqwoqehbgpkdyuqjtmzzhzewvbv"
decoded_message = encode_decode(enigma_machine, message)
print(decoded_message)
