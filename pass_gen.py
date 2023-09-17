import string
import random

pass_len = int(input("Password length: "))

print('''Choose Password Type:
		1. Letters.
		2. Digits.
		3. Special characters.
		4. To Generate Password.''')

char_list = ""

while(True):
	choice = int(input("Choose Passoword Type: "))
	if(choice == 1):
		char_list += string.ascii_letters
		
	elif(choice == 2):
		char_list += string.digits
		
	elif(choice == 3):
		char_list += string.punctuation
		
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option!")

password = []

for i in range(pass_len):
	rand_char = random.choice(char_list)
	
	password.append(rand_char)
print("The random password is: " + "".join(password))