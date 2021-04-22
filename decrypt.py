# Decryption Module

def decrypt(cypher_text, shift_amount, alphabet):
	plain_text = ""
	for char in cypher_text:
		if char not in alphabet:
			plain_text += char
		elif char in alphabet:
			position = alphabet.index(char)
			old_position = position - shift_amount
			if old_position < 0:
				adjusted_position = (-1) * (position - shift_amount)
				old_letter = alphabet[(-1) * (adjusted_position)]
				plain_text += old_letter
			else:
				old_letter = alphabet[old_position]
				plain_text += old_letter
	return plain_text

