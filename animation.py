import time

f = 2
j = 0.09

#while True:
for o in range(f):
    for i in range(16):
        print("[]" * i + ">" + "[]" * (15 - i))
        time.sleep(j)
    for e in range(16):
        print("[]" * (15 - e) + "<" + "[]" * e)
        time.sleep(j)
