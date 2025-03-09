command = ""
previouscomand = ""

while True:
    previouscomand = command
    command  = (input('> ')).lower()
    if command == 'start' and previouscomand != 'start':
        print('Car ready to go...')
    if command == 'start' and previouscomand == 'start':
        print('Car ready to go...')
    elif command == 'stop' and previouscomand != 'stop':
        print('Car stopped')
    elif command == 'stop' and previouscomand == 'stop':
        print('car has stopoed already!')
    elif command == 'help':
        print('''
Start -  to start the car;
Stop - to stop the car;
quit - to exit the game 
''')
    elif command == "quit":
        print('you just terminated the game')
        break
    else:
        print("I don't know about this")
