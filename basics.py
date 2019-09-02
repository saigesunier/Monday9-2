# basics.py
x = input("Input a command: ")
print("You entered {}.".format(x))
if x == 'add' or x == 'a':
    print("Add")
    a = 1
    b = 2
    c = a + b
    print("{} + {} = {}".format(a, b, c))
elif x == 'sub' or x == 's':
    print("subtract")
    a = 1
    b = 2
    c = a - b
    print("{} - {} = {}".format(a, b, c))
else:
    print("{} is not an active command.".format(x))
print ("Done")
