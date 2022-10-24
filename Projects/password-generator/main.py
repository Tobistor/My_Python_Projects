#Password Generator Project
import random
from random import choice
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

nr_letters
nr_symbols
nr_numbers

#letters[]
#numbers[]
#symbols[]

get_letters = []
for i in range (1,nr_letters+1):
  letter = random.randint(1, nr_letters)
  get_letters.append(letters[letter])
  
get_numbers = []
for i in range (1,nr_numbers+1):
  number = random.randint(1, nr_numbers)
  get_numbers.append(numbers[number])

get_symbols = []
for i in range (1,nr_symbols+1):
  symbol = random.randint(1, nr_symbols)
  get_symbols.append(symbols[symbol])

password = get_letters + get_symbols + get_numbers

randomized = random.sample(password, len(password))

str_upper_lower = ''.join(choice((str.upper, str.lower))(c) for c in randomized)

print(f'\n This is your newly generated password 😉: {str_upper_lower}')


