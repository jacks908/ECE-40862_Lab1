bdays = {
    "Tim Cook": "11/01/1960",
    "Avinash Kak": "01/17/1944",
    "Mung Chiang": "02/02/1977",
    "Lu Su": "09/17/2025",
    "Steve Jobs": "02/24/1955",
}
print("Welcome to the birthday dictionary. We know the birthdays of:")

for k in bdays:
    print(k)
    
name = input("Whose birthday do you want to look up?\n")

if name in bdays:
    print(f"{name}'s birthday is {bdays[name]}.")
else:
    print("Sorry, not found.")