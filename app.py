# Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Dude,car is already started.")
        else:
            started = True
            print("Car started! Let's go!")

    elif command == "stop":
        if not started:
            print("Car's already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - starts the car
stop - stops the car
quit - exits the game
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
