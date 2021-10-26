choice = int(input('1. Addition 2. Subtraction 3.Multiply 4.Division 5.Modulus: '))
# I put all the other inputs inside because i want it to print invalid if the first choice's value is invalid
# Pes and to = Pesto
if choice == 1:
    Pes = eval(input('Input your first Number: '))
    to = eval(input('Input your second Number: '))
    pesto = Pes + to
    print(pesto)
elif choice == 2:
    Pes = eval(input('Input your first Number: '))
    to = eval(input('Input your second Number: '))
    pesto = Pes - to
    print(pesto)
elif choice == 3:
    Pes = eval(input('Input your first Number: '))
    to = eval(input('Input your second Number: '))
    pesto = Pes * to
    print(pesto)
elif choice == 4:
    Pes = eval(input('Input your first Number: '))
    to = eval(input('Input your second Number: '))
    pesto = Pes / to
    print(pesto)
elif choice == 5:
    Pes = eval(input('Input your first Number: '))
    to = eval(input('Input your second Number: '))
    pesto = Pes % to
    print(pesto)
else:
    print('Invalid')

#Made by Peter Nelson Subrata
