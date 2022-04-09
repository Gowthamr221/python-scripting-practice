user_input = str(input("Enter a Phrase: "))

test_arr = user_input.split(" ")

acronym = " "

for it in test_arr:
    acronym = acronym + str(it[0]).upper()\

print(acronym)