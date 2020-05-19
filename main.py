from enigma import EnigmaMachine
from user_inputs import set_rotor, set_reflector, set_plugboard, encode_decode
from alphabet_represent import represent

if __name__ == '__main__':

    # Rotor Settings
    # Format: [[rotor type: str, start position: str, ring setting: str]...]
    # Rotor types available : I, II, III, IV, V
    # Uncomment the following line if you want command line interaction
    # rotors_settings = set_rotor()
    rotors_settings = [["I", "E", "E"], ["III", "Q", "F"], ["IV", "P", "I"]]

    # Choose a reflector
    # Format: reflector type = str
    # Reflectors available: A, B, C, BThin, CThin
    # Uncomment the following line if you want command line interaction
    # reflector_type = set_reflector()
    reflector_type = "B"

    # Plugboard settings
    # Format: "AB CD EF GH IJ"
    # Type None if there are no plugboard pairs
    # Uncomment the following line if you want command line interaction
    # plugboard_settings = set_plugboard()
    plugboard_settings = "bq cr di ej kw mt os px uz gh"


    # Create an Enigma Machine Object
    enigma_machine = EnigmaMachine(rotors_settings, plugboard_settings, reflector_type)

    # Encode or Decode the message
    # Uncomment the following line if you want command line interaction
    # encode_decode(enigma_machine)
    message = "zpbisehkwmfoqasflctixnaawwxjsufhzwtfzheybbkswxgnpmqwoqehbgpkdyuqjtmzzhzewvbvfhjjbhykgcfuceayzhlhwkuamdgtkaqummretdkplleszkikanfqvpoitcunpfoqlwvxzpxrllftssazgcmrxnreccnmuvmfvfgxpkoeealmvpvysriyfuubnpkttdgvdrwhnlfcyhczxhwpczduhpzlwscmfnnwaiezwmwtyafvytuhnfpflpdlcpsrimdpilmqaeabfvropbhxnynbefstqkdyzesyu"
    converted_text = [enigma_machine.encrypt_decrypt(represent(i))for i in message]
    print("".join(converted_text))
