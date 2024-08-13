def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:    
        if s.isalpha():
            return True
        else:
            if s[0:1].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].startswith("0") or s[i:].isalpha():
                        return False
                    else:
                        return True
            else:
                return False                 
    else:
        return False
    
main()