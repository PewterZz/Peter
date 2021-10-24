userinput = int(input("Please enter a value: "))
for x in range(userinput):
    print(" " * (userinput - x - 1), end="");print("#"*(x+1))
