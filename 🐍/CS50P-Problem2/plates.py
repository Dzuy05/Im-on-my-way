def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:    
        if s[0:1].isalpha():
            i = 0
            while i < len(s[2:5]):
                if not s[i].isalpha():
                    if s[i] == "0":
                        return False
                    elif not s[i:].isdigit():
                        return False
                    else:
                        return True
                i += 1
            else:
                return True

            
main()