from enigma import EnigmaMachine
from alphabet_represent import represent

if __name__ =='__main__':

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
    reflector_type = input(f"Choose reflector(available: A, B, C, BThin, CThin): ")

    # Make