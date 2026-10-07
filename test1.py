#file maker

#with open("bomb.txt", "w") as file:
#   file.write("eeeeeeee")

for i in range(100):
    if i % 2 == 0:
        print("even" + str(i))
    else:
        print("odd" + str(i))

for j in range(5):
    with open("test.txt" + str(j), "w") as file:
        file.write("test" + str(j))