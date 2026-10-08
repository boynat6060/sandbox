print("============ ANGLE SIMPLIFIER 3000 ============")

def angles(x):
    return x % 360

while True:
    y = input("Enter angle measure: ")
    if y == "exit":
        print("Program terminated.")
        break
    else :
        print(angles(int(y)))
