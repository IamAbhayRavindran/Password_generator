import random
import string

def generate_password():
  
    num_letters = int(input("Enter the number of letters in the password: "))
    num_symbols = int(input("Enter the number of symbols in the password: "))
    num_numbers = int(input("Enter the number of numbers in the password: "))

    letters = string.ascii_letters
    symbols = '!@#$%^&*()'
    numbers = string.digits

   
    password_letters = random.choices(letters, k=num_letters)
    password_symbols = random.choices(symbols, k=num_symbols)
    password_numbers = random.choices(numbers, k=num_numbers)

   
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
   


    password = ''.join(password_list)
    print(f"Generated Password: {password}")

generate_password()


