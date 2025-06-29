names = []
while True:
    name = input("ism kiriting: ")
    if name == "":
        break

    names.append(name)

print(len(names))