import time

def seq(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        elif num % 2 == 1:
            num = (num * 3) + 1
        print(num)
        time.sleep(0.001)
    if num == 1:
        num = (num * 3) + 1
        print(num)
        num = num // 2
        print(num)
        num = num // 2
        print(num)
    print("Final number: 1.")

while True:
    ask = int(input("Enter Number:  "))
    seq(ask)

