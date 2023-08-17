contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

name = input()
found = False  # Bulunduğunda True olarak işaretlenecek

for x in contacts:
    if name in x:
        print(str(x[0]) + " is " + str(x[1]))
        found = True
        break

if not found:
    print("Not Found")