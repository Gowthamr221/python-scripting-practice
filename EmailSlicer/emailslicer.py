email = input("enter your email: ")
#returns lowest index where the element aapears before
# here the index less than the @ will be returned back
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]

format_data = (f"your username is '{username}' and your domain is '{domain_name}'")

print(format_data)