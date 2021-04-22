# Encryption Module

def encrypt(plain_text, shift_amount, alphabet):

	cipher_text = ""
	for char in plain_text:
		if char not in alphabet:
			cipher_text += char
		elif char in alphabet:
			position = alphabet.index(char)
			new_position = position + shift_amount
			if new_position > len(alphabet):
				remainder = new_position % len(alphabet)
				adjusted_position = int(remainder)
				new_letter = alphabet[adjusted_position]
				cipher_text += new_letter
			else:
				new_letter = alphabet[new_position]
				cipher_text += new_letter
	return cipher_text