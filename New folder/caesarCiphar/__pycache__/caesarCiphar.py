alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for item in start_text:
    if item in alphabet:
        position = alphabet.index(item)
        end_text+=alphabet[position+shift_amount]
  print(f"Here's the {cipher_direction}d result: {end_text}")

import art
print(art.Logo)
answer = 'yes'
while answer == 'yes':
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift%=26
	caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
	answer = input("Do you want to  restart the program?? type 'yes' or 'no'")
print("Thank you for your time!!")