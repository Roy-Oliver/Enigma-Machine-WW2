"""Functions that ask for user input"""

from alphabet_represent import represent


def set_rotor():
    # Populate rotor setting
    rotors_settings = []
    for i in range(1, 4):
        # Ask for rotor type, initial position and ring setting
        rotor_type = input(f"\nInput rotor type (available: I, II, III, IV, IV) for rotor {i}: ")
        rotor_start_position = input(f"Input rotor start position (e.g. A, B, C, ...) for rotor {i}: ")
        rotor_ring_setting = input(f"Input ring setting (e.g. A, B, C, ...) for rotor {i}: ")

        # Add to settings
        rotors_settings.append([rotor_type, rotor_start_position, rotor_ring_setting])

    return rotors_settings


def set_reflector():
    # Choose a reflector
    reflector_type = input("\nChoose reflector(available: A, B, C, BThin, CThin): ")

    return reflector_type


def set_plugboard():
    # Ask for letters
    letters = input(f"\nType the plugboard letter pairs (e.g. AB CD EF). Type 'None' for blank plugboard: ")
    if letters == "None":
        return ""
    return letters


def encode_decode(enigma_machine):
    # Encode or Decode the message
    while True:
        message = input("\nType your message. Type 'exit' to exit: ")
        message = message.replace(" ", "")  # Remove spaces in message
        if message == 'exit':
            break
        else:
            # Print the message
            converted_text = [enigma_machine.encrypt_decrypt(represent(i)) for i in message]
            print("".join(converted_text))
