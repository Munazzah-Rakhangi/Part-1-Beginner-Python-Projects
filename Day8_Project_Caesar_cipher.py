# Function with inputs
# def greet(name):
#     print(f"Hello {name}")
#     print(f"Hi, {name}")
#     print(f"How are you, {name}?")

# greet("billy")

#------------------------------------------------------------------------------------
# Coding challenge Life in Weeks using function inputs

# current_age = int(input("Please enter your current age: "))

# years = 90
# weeks = 52
# months = 12
# days = 365

# def life_in_weeks(current_age):
#     years_left = years - current _age
#     weeks_left = years_left * weeks
#     days_left = years_left * days
#     months_left = years_left * months

#     print(f"You have {weeks_left} weeks left.")

# life_in_weeks(current_age)

# ----------------------------------------------------------------------------------
# Function with more than 1 inputs
# def greet(name, location):
#     print(f"Hello, {name}")
#     print(f"what is the wheather in {location}")

# greet(name = "Billy", location = "london")
# -----------------------------------------------------------------------------------
# Coding Challenge Love calculator

# print("Welcome to Love Calculator")

# def calculate_love_score(name1, name2):

#     combined_names = name1 + name2
#     lower_names = combined_names.lower()

#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e

#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e

#     score = int(str(first_digit) + str(second_digit))
#     print(f"Your Love score is {score}")
    
# calculate_love_score("Kanye West", "Kim Kardashian")

# -----------------------------------------------------------------------------------------

# Caesar Cipher Part 1
import Day8_Project_Caesar_cipher_art
print(Day8_Project_Caesar_cipher_art.logo)

alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# # hello 2
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift  # h is at position 7 so letter becomes 7 then addinf the shift amount for thr shift
#         shifted_position = shifted_position % len(alphabet)  # makes sure we are always inside the range of 0-25
#         cipher_text += alphabet[shifted_position]
    
#     print(f"Here is the encoded result: {cipher_text}")  
    
# encrypt(original_text=text, shift_amount=shift) 


# def decrypt(original_text, shift_amount):
#     decipher_text = ""
    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift  # h is at position 7 so letter becomes 7 then addinf the shift amount for thr shift
#         shifted_position = shifted_position % len(alphabet)  # makes sure we are always inside the range of 0-25
#         decipher_text += alphabet[shifted_position]
        
#     print(f"Here is the decoded result: {decipher_text}")  
    
# decrypt(original_text=text, shift_amount=shift) 




def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
                shift_amount *= -1
    
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter
        else:        
            shifted_position = alphabet.index(letter) + shift  # h is at position 7 so letter becomes 7 then addinf the shift amount for thr shift
            shifted_position = shifted_position % len(alphabet)  # makes sure we are always inside the range of 0-25
            output_text += alphabet[shifted_position]
        
    print(f"Here is the {encode_or_decode} result: {output_text}")  

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) 

should_continue = True

while should_continue:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction) 
    
    restart = input("Tpe 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == 'no':
        should_continue == False
        print("GOODBYE")
    