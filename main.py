from alphabet_represent import represent
from enigma import EnigmaMachine

if __name__ == '__main__':

    # Populate rotor setting
    rotors_settings = []
    for i in range(1, 4):
        # Ask for rotor type, initial position and ring setting
        rotor_type = input(f"\nInput rotor type (available: I, II, III, IV, IV) for rotor {i}: ")
        rotor_start_position = input(f"Input rotor start position (e.g. A, B, C, ...) for rotor {i}: ")
        rotor_ring_setting = input(f"Input ring setting (e.g. A, B, C, ...) for rotor {i}: ")

        # Add to settings
        rotors_settings.append([rotor_type, represent(rotor_start_position), represent(rotor_ring_setting)])

    # Choose a reflector
    reflector_type = input("\nChoose reflector(available: A, B, C, BThin, CThin): ")

    ### Plugboard settings
    plugboard_settings = []

    # Ask for first letter
    letters = input(f"\nType the letter pairs (e.g. AB CD EF). Type 'None' for blank plugboard: ")

    # Populate plugboard settings
    letters = letters.split()

    for letter_pair in letters:
        plugboard_settings.append((letter_pair[0], letter_pair[1]))


    # Create an Enigma Machine Object
    enigma_machine = EnigmaMachine(rotors_settings, plugboard_settings, reflector_type)

    # Encode or Decode the message
    while True:
        message = input("\nType your message. Type 'exit' to exit: ")

        if message == 'exit':
            break
        else:
            # Print the message
            print("".join([represent(enigma_machine.encrypt_decrypt(represent(letter))) for letter in message]))
