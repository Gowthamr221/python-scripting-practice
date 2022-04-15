# this is how we take continuous input until we want to stop it manually

while True:
    reply = input("Enter Text: ")
    if reply == 'stop' : break
    print(reply)

