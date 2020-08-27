from utilities import decimal_to_binary
from encryptor import transform

DECRYPTION = "decryption"

def brute_force():

	# Ask the user to enter the name of the file to process.
	file = input("Enter the name of the file with the pairs of plain and ciphertexts: ")

	# Open the file specified by the user and read all the records.
	fhandler = open(file, "r")

	# Try to find the correct key for all the pairs of ciphertext and plaintext.
	for line in fhandler:
		for x in range(pow(2,10)):
			key = decimal_to_binary(x)[-10:]
			key = ''.join([str(elem) for elem in key])
			output = transform(DECRYPTION, key, line[:8], False)

			if line[9:] == output:
				print("Cipher: {} and attack {} and key {}\n".format(line[9:], output, key))


	# If the key was not the correct, try the next one.