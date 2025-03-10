try:
    age  = int(input('Enter your age: '))   
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid input")



