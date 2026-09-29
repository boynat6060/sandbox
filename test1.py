#file maker

#with open("bomb.txt", "w") as file:
#   file.write("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

for i in range(100):
    if i % 2 == 0:
        print("even" + str(i))
    else:
        print("odd" + str(i))