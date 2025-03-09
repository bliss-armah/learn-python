# i=1

# while i <=5:
#     print('*'*i)
#     i+=1
# print("Done")

# Guessing game

secret_number =  9
guess_count = 0 
guess_limit = 3

while guess_count < guess_limit:
    guessed_number = int(input('Guess number? '))
    guess_count+=1
    if guessed_number == secret_number:
        print('You win!')
        break
else:
    print('Sorry, you failed? ')