# AND

has_high_income = False
has_good_credit = True
has_criminal_record = True


if has_high_income and has_good_credit:
    print("Eligible for loan")

# OR

# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# NOT 

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
    


# comparison operators
 
temperature = 30

if temperature == 30:
    print("It's warm")
else:
    print("It's cold")