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



def check(n): # pragma: no cover
    if(n >= 1 and n <= 10000): # pragma: no cover
        return True # pragma: no cover
    return False # pragma: no cover


def FizzBuzzPrinter(str):
    print(str)




def main():
    n = int(input("Please enter number (1 - 10,000) : ")) # pragma: no cover
    if(check(n)): # pragma: no cover
        superFizzBuzzFunction(n) # pragma: no cover
    else: # pragma: no cover
        print("Please enter number in range (1 - 10,000) !!") # pragma: no cover

if __name__ == "__main__":
    main() # pragma: no cover