# Creating an empty list called my_list.
my_list = []

# Appending the following elements to my_list: 10, 20, 30, 40.
newList = [10, 20, 30, 40]
for i in newList:
    my_list.append(i)

# Inserting the value 15 at the second position in the list.
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70].
newList = [50, 60, 70]
my_list.extend(newList)

# Removing the last element from my_list.
my_list.remove(70)

# Sort my_list in ascending order.
my_list.sort()

# Find and print the index of the value 30 in my_list.
print(my_list.index(30))