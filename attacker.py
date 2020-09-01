from utilities import decimal_to_binary
from encryptor import transform

DECRYPTION = "decryption"

def brute_force(file):
	# Open the file specified by the user and read all the records.
	fhandler = open(file, "r")

	# Try to find the correct key for all the pairs of ciphertext and plaintext.
	first_pt = fhandler.readline()[:8]
	possible_keys = []
	for x in range(pow(2,10)):
		key = decimal_to_binary(x)[-10:]
		key = ''.join([str(elem) for elem in key])
		output = transform(DECRYPTION, key, first_pt, False)

		if fhandler.readline()[9:17] == output:
			possible_keys.append(key)
	
	print(possible_keys)


	# If the key was not the correct, try the next one.