x, y, z = input().split()
x = int(x)
z = int(z)
match y:
    case "+":
        print(f"{x + z:.1f}")
    case "-":
        print(f"{x - z:.1f}")
    case "*":
        print(f"{x * z}.1f")
    case "/":
        print(f"{x / z:.1f}")
        
