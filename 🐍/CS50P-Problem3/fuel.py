def get_fraction(promt):
    while True:
        try:
            x, y = input(promt).split("/")
            if 0 <= float(x)/float(y) <= 0.1:
                return ("E")
            elif 0.9 <= float(x)/float(y) <= 1:
                return ("F")
            elif 0.1 < float(x)/float(y) < 0.9:
                return str(round(float(x)/float(y)*100)) + "%"
        except (ValueError, ZeroDivisionError):
            pass

def main():
    i = get_fraction("Fraction: ")
    print(i)
main()

            
            