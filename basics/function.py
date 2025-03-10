def greet_user():
    print('Hi there!')
    print('Welcome aboard')


# function with paramaeters

def greet_user(username):
    print(f'Hi there {username}')
    print('Welcome aboard')

greet_user('John') 

def emoji_generator(words):
    splited_words = words.split(' ')
    emojis = {
        ":)" : "😊",
        ":(" : "😞"
    }
    output = ''
    for word in splited_words:
        output += emojis.get(word,word) + " "
    return output

message = input("> ")
print(emoji_generator(message))