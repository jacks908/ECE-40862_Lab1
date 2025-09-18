a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(f'a = {a}')
number = int(input("Enter number: "))
print("The new list is", [x for x in a if x < number])

