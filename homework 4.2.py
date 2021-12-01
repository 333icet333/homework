


a = int(input("Enter a:"))
for i in range(0, a):
    print("*"*i)

    if i == 5:
        break
i = "******"
for x in range(6):
    print(i)
    for y in range(1):
        i = i.replace("*","",1)