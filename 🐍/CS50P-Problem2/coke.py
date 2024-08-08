c = int(50)
print(f"Amount due: {c}")
ls = [50 , 25, 5]
while c > 0:
    coin = int(input("Insert coin: "))
    if coin in ls:
        c -= coin
        print(f"Amout due: {c}")
    else:
        coin = int(input("Insert coin: "))
    

        


    



    


    
