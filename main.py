#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_chars = nr_letters + nr_numbers + nr_symbols
counter_list = [nr_letters, nr_numbers, nr_symbols]
char_list = [letters, numbers, symbols]
password = ""

while len(password) < total_chars:
  random_select = random.randint(0, 2)
  counter = counter_list[random_select]

  if counter > 0:
    chars = char_list[random_select]
    char_select = random.randint(0, len(chars) - 1)
    password += chars[char_select]
    counter_list[random_select] -= 1
    
print(password)
