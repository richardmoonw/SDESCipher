from utilities import *

def transform(mode, key, message, debug):

    if validate(key, message) == 1:
        print("There was an error with the key or message you entered, try again \n")
        return 1

    # Construct the P10 permutation key.
    p10_positions = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p10 = make_permutation(p10_positions, key)
    
    # Divide the P10 permutation key in 2.
    first_part = p10[:5]
    second_part = p10[5:10]

    # Generate the first key.
    first_part = shift(first_part, 1)
    second_part = shift(second_part, 1)
    first_key = make_p8(first_part, second_part)

    # Generate the second key.
    first_part = shift(first_part, 2)
    second_part = shift(second_part, 2)
    second_key = make_p8(first_part, second_part)

    if debug is True:
        fkey = array_to_string(first_key)
        skey = array_to_string(second_key)
        print("--------------------------------------------------")
        print("| Key 1 and 2    | {} and {}         |".format(fkey, skey))
        print("--------------------------------------------------")

    # Generate the Initial Permutation (IP).
    ip_positions = [2, 6, 3, 1, 4, 8, 5, 7]
    ip = make_permutation(ip_positions, message)

    if debug is True:
        sip = array_to_string(ip)
        print("| IP             | {}                      |".format(sip))
        print("--------------------------------------------------")

    # Divide the IP in 2 parts.
    ip_one = ip[:4]
    ip_two = ip [4:8]

    # Generate the first E/P.
    ep_positions = [4, 1, 2, 3, 2, 3, 4, 1]
    ep = make_permutation(ep_positions, ip_two)

    if debug is True:
        sep = array_to_string(ep)
        print("| First E/P      | {}                      |".format(sep))
        print("--------------------------------------------------")

    # Process the XOR operation between the E/P and the first key.
    if mode == "encryption":
        ep = process_xor(ep, first_key)
    elif  mode == "decryption":
        ep = process_xor(ep, second_key)

    # if debug is True:
    #     print("The new E/P is {}".format(ep))

    # Obtain the values from the S0 matrix.
    s0_section = ep[:4]
    s0_section = obtain_svalue(0, s0_section)
    
    # Obtain the values from the S1 matrix.
    s1_section = ep[4:8]
    s1_section = obtain_svalue(1, s1_section)

    if debug is True:
        ss0 = array_to_string(s0_section)
        ss1 = array_to_string(s1_section)
        print("| S0 and S1      | {} and {}                     |".format(ss0, ss1))
        print("--------------------------------------------------")

    # Generate the P4.
    s_section = s0_section + s1_section
    p4_positions = [2, 4, 3, 1]
    p4 = make_permutation(p4_positions, s_section)

    if debug is True:
        sp4 = array_to_string(p4)
        print("| First P4       | {}                          |".format(sp4))
        print("--------------------------------------------------")

    # Process the XOR operation between the first P4 and the first part of the initial permutation.
    ip_one = process_xor(p4, ip_one)

    # Generate SW.
    sw = ip_two[:] + ip_one[:]

    if debug is True:
        ssw = array_to_string(sw)
        print("| SW             | {}                      |".format(ssw))
        print("--------------------------------------------------")

    # Divide the SW in 2 parts.
    sw_one = sw[:4]
    sw_two = sw[4:8]

    # Generate the second E/P.
    ep = make_permutation(ep_positions, sw_two)

    if debug is True:
        sep = array_to_string(ep)
        print("| Second E/P     | {}                      |".format(sep))
        print("--------------------------------------------------")
    
    # Process the XOR operation between the second E/P and the second key.
    if mode == "encryption":
        ep = process_xor(ep, second_key)
    elif mode == "decryption":
        ep = process_xor(ep, first_key)

    # if debug is True:
    #     print("The new E/P is {}".format(ep))

    # Obtain the values from the S0 matrix.
    s0_section = ep[:4]
    s0_section = obtain_svalue(0, s0_section)
    
    # Obtain the values from the S1 matrix.
    s1_section = ep[4:8]
    s1_section = obtain_svalue(1, s1_section)

    if debug is True:
        ss0 = array_to_string(s0_section)
        ss1 = array_to_string(s1_section)
        print("| S0 and S1      | {} and {}                     |".format(ss0, ss1))
        print("--------------------------------------------------")

    # Generate the P4.
    s_section = s0_section + s1_section
    p4_positions = [2, 4, 3, 1]
    p4 = make_permutation(p4_positions, s_section)

    if debug is True:
        sp4 = array_to_string(p4)
        print("| Second P4      | {}                          |".format(sp4))
        print("--------------------------------------------------")

    # Process the XOR operation between the second P4 and the first part of the SW.
    sw_one = process_xor(p4, sw_one)

    # Generate a final permutation and the ciphertext.
    ciphertext = sw_one + sw_two
    final_positions = [4, 1, 3, 5, 7, 2, 8, 6]
    ciphertext = make_permutation(final_positions, ciphertext)

    ciphertext = ''.join([str(elem) for elem in ciphertext])

    return ciphertext