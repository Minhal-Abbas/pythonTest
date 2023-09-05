
def add(x,y):
    return int(x) + int(y)

def sub(x,y):
    return int(x) - int(y)

def multi(x,y):
    return int(x) * int(y)

def divide(x,y):
    return int(x) / int(y)


while True:

    choice = input("Select Operation: 1 to add, 2 for subs, 3 for multiply, 4 for division and 0 to exit: ")
    
    if False == choice.isnumeric():
        print("You entered invalid DataType!")
        continue

    choice = int(choice)

    if choice == 0:
        print("Thankyou for using my calculator!")
        break

    
    x = input("Enter Number 1: ")
    y = input("Enter number 2: ")

    match choice:
        case 1:
            result = add(x, y)
            print(result)
            
        case 2:
            result = sub(x, y)
            print(result)
        case 3:
            result = multi(x, y)
            print(result)
        case 4:
            result = divide(x, y)
            print(result)

        case _:
            print("Invalid Value!")



