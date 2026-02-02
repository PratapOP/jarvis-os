from voice.listener import listen

while True:
    text = listen()
    print("You said:", text)
