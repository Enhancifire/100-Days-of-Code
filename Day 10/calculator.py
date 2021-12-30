def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

def selectOperation():
    print("Select your operation:")
    for i in operations:
        print(i)
    operation = input()
    return operation

def myoperation(operation, startNum, secNum):
    function = operations[operation]
    res = function(startNum, secNum)
    return res


def main():
    startNum = float(input("Enter the first number: "))
    secNum = float(input("Enter the second number: "))
    operation = selectOperation()

    res = myoperation(operation, startNum, secNum)
    print(f"{startNum} {operation} {secNum} = {res}")

    while True:
        shouldContinue = input("Do you want to continue? [y/N]: ")

        if shouldContinue == "y":
            nextnum = float(input("Enter the next number: "))
            operation = selectOperation()
            prevRes = res

            res = myoperation(operation, res, nextnum)
            print(f"{prevRes} {operation} {nextnum} = {res}")
            
        else:
            break

    print("Thanks for using my calculator!!")


main()