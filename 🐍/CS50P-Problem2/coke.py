c = int(50)
total = 0
print(f"Amount due: {c}")
ls = [10 , 25, 5]
while c > 0:
    coin = int(input("Insert coin: "))
    if coin in ls:
        c -= coin
        total += coin
        if c >= 0:
            print(f"Amout due: {c}")
        elif c < 0:
            print(f"Change owed: {total - 50}")

    

        


    



    


    
