i = input("Input: ").strip()
ls = [ "a", "e", "i", "o", "u"]

for c in i:
    if not c in ls:
        print(c, end = "")

