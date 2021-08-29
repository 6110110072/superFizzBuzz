
def superFizzBuzzFunction(n):
    if(n % 9 == 0 and n % 25 == 0):
        FizzBuzzPrinter("FizzFizzBuzzBuzz")
        return "FizzFizzBuzzBuzz"
    elif(n % 3 == 0 and n % 5 == 0):
        FizzBuzzPrinter("FizzBuzz")
        return "FizzBuzz"
    elif(n % 9 == 0):
        FizzBuzzPrinter("FizzFizz")
        return "FizzFizz"
    elif(n % 25 == 0):
        FizzBuzzPrinter("BuzzBuzz")
        return "BuzzBuzz"
    elif(n % 3 == 0):
        FizzBuzzPrinter("Fizz")
        return "Fizz"
    elif(n % 5 == 0):
        FizzBuzzPrinter("Buzz")
        return "Buzz"
    else:
        FizzBuzzPrinter("NoFizzBuzz")
        return "NoFizzBuzz"

def FizzBuzzPrinter(str):
    print(str)

def check(n):
    if(n > 1 and n <= 10000):
        return True
    return False


def main():
    n = int(input("Please enter number (1 - 10,000) : "))
    if(check(n)):
        superFizzBuzzFunction(n)
    else:
        print("Please enter number in range (1 - 10,000) !!")

if __name__ == "__main__":
    main()