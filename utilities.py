import re

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
BINARY_LEN = 2

def validate(key, message):
    if not re.match(r"^[10]{10}$", key):
        return 1
    elif not re.match(r"^[10]{8}$", message):
        return 1
    else:
        return 0

def shift(word, value):
    old_word = word[:]
    for x in range(5):
        word[x] = old_word[(x+value+5)%5]

    return word

def make_permutation(perm_arr, word):
    permutation = perm_arr[:]
    for x in range(len(permutation)):
        permutation[x] = int(word[permutation[x] - 1])
    
    return permutation

def make_p8(first_part, second_part):
    p8_key = [6, 3, 7, 4, 8, 5, 10, 9]
    key = first_part[:] + second_part[:]

    for x in range(len(p8_key)):
        p8_key[x] = int(key[p8_key[x]-1])

    return p8_key

def process_xor(message, key):
    for x in range(len(message)):
        message[x] = message[x] ^ key[x]
    
    return message

def decimal_to_binary(value):
    binary = [0, 0]
    while value != 0:
        binary.insert(2, value % 2)
        value = value // 2

    return binary

def binary_to_decimal(binary_arr):
    value = 0

    if binary_arr[0] != 0:
        value = value + 2
    if binary_arr[1] != 0:
        value = value + 1
    
    return value

def obtain_svalue(s_matrix, code):
    row = [code[0]] + [code[3]]
    column = [code[1]] + [code[2]]
    row = binary_to_decimal(row)
    column = binary_to_decimal(column)

    if s_matrix == 0:
        code = S0[row][column]
    elif s_matrix == 1:
        code = S1[row][column]
    
    code = decimal_to_binary(code)[-2:]
    return code
    
