# first_module.py

def addition(x, y):
    print("Add")
    c = x + y
    print("{} + {} = {}".format(x, y, c))
    return

def subtract(x, y):
    print("Subtract")
    c = x - y
    print("{} - {} = {}".format(x, y, c))
    return

def addsubtract(x, y, symbol):
    if symbol == "+":
        c = x+y
    elif symbol == "-":
        c = x-y
    else:
        c = "Unrecognized"
    return c

if __name__ == "__main__": # tell python this is where to start the code
    x = input("Input a command: ")
    print("You entered {}.".format(x))
    a = int(input("a = "))
    b = int(input("b = "))
    if x == 'add' or x == 'a':
        symbol = "+"
        answer = addsubtract(a,b,symbol)
    elif x == 'sub' or x == 's':
        symbol = "-"
        answer = addsubtract(a,b,symbol)
    else:
        print("{} is not an active command.".format(x))
        print("Enter a new command.")
    print("c = {}".format(answer))
    print ("Done")
