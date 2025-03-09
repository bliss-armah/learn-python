# names = ['ama','cofia','jane']

# print(names[0:2])


duplicate = [1,5,4,2,8,7,1,4,1,2,3,6,5,8]

unique_values = []

for item in duplicate:
    if item not in unique_values:
        unique_values.append(item)
print(unique_values)