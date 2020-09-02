from utilities import decimal_to_binary
from encryptor import transform

ENCRYPTION = "encryption"

def brute_force(file):
	# Open the file specified by the user and read all the records.
	fhandler = open(file, "r")

	# Find the correct keys for the first pair of ciphertext and plaintext.
	first_line = fhandler.readline()
	first_pt = first_line[:8]
	first_ct = first_line[9:17]
	possible_keys = []
	for x in range(pow(2,10)):
		key = decimal_to_binary(x)[-10:]
		key = ''.join([str(elem) for elem in key])
		output = transform(ENCRYPTION, key, first_pt, False)

		if first_ct == output:
			possible_keys.append(key)

	print(possible_keys)
	
	key_found = False
	final_key = ""
	for key in possible_keys:
		for line in fhandler:
			plaintext = line[:8]
			real_ciphertext = line[9:17]
			ciphertext = transform(ENCRYPTION, key, plaintext, False)
			# print(line)
			# print("Real cipher {} and cipher {}".format(real_ciphertext,ciphertext))

			if real_ciphertext != ciphertext:
				key_found = False
				final_key = ""
				break
			elif real_ciphertext == ciphertext and key_found is False:
				key_found = True
				final_key = key
				continue
		if key_found is True:
			break
	
	print("The perfect key is {}".format(final_key))