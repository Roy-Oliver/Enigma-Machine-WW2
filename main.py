from enigma import EnigmaMachine
from alphabet_represent import represent
from enigma import EnigmaMachine

if True:

    # Populate rotor setting
    rotors_settings = []
    for i in range(1, 4):
        # Ask for rotor type, initial position and ring setting
        rotor_type = input(f"Input rotor type (available: I, II, III, IV, IV) for rotor {i}: ")
        rotor_start_position = input(f"Input rotor start position (e.g. A, B, C, ...) for rotor {i}: ")
        rotor_ring_setting = input(f"Input ring setting (e.g. A, B, C, ...) for rotor {i}: ")

        # Add to settings
        rotors_settings.append([rotor_type, int(rotor_start_position), represent(rotor_ring_setting)])

    # Choose a reflector
    reflector_type = input("Choose reflector(available: A, B, C, BThin, CThin): ")

    # Plugboard settings
    count = 1
    letter_1 = ""
    plugboard_settings = []
    while True:
        # Ask for first letter
        letter_1 = input(f"Type the first letter in pair {count}. Type exit to end selection: ")

        # Ask if user wants to exit
        if letter_1 == 'exit':
            break

        # Ask for second letter
        letter_2 = input(f"Type the second letter in pair {count}.")

        # Populate plugboard settings
        plugboard_settings.append(represent(letter_1), represent(letter_2))

        # Increment counter by 1
        count += 1

    # Create an Enigma Machine Object
    enigma_machine = EnigmaMachine(rotors_settings,plugboard_settings, reflector_type)

    # Encode or Decode the message
    while True:
        message = input("Type your message. Type 'exit' to exit: ")

        if message == 'exit':
            break
        else:
            # Print the message
            print("".join([enigma_machine.encrypt_decrypt(letter) for letter in message]))


