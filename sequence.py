def seq(num):
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = (num * 3) + 1
        print(num)
    if num == 1:
        num = (num * 3) + 1
        print(num)
        num = num / 2
        print(num)
        num = num / 2
        print(num)
    print("Final number: 1.")
    print("Program complete.")
    runAgain()

def runAgain():
    while True:
        askForAgain = str(input("Would you like to run the program again?  (y/n):  ")).lower()
        if askForAgain == "y":
            enterNum = int(input("Enter Number:  "))
            seq(enterNum)
            break
        elif askForAgain == "n":
            print("Program exited.")
            break
        else:
            print("Invalid Response")

ask = int(input("Enter Number:  "))
seq(ask)