import string
import random

passlen = int(input("enter the lenght of pass: "))
all_punctuations = string.punctuation
all_chars = string.ascii_letters
total_possibilities = all_punctuations + all_chars
# sample method is used try the permutations 
pass_generated = "".join(random.sample(total_possibilities,passlen))

print(pass_generated)