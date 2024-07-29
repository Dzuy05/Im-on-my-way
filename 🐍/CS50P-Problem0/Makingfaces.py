def main(n):
    if ":)" in n:
        r = n.replace(":)", "😊")
        return r
    elif ":(" in n:
        r = n.replace(":(", "😢")
        return r
    
    return n

n = input()
print(main(n))
