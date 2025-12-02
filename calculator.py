class Math:
    def __init__(self,*args):
        self.numbers=args

    def lifemadeeasy(self):
        pass

class Basics(Math):
    def sum(self):
        __total=0
        for num in self.numbers:
            __total+=num
        return __total
    
    def sub(self):
        __sub=self.numbers[0]
        for num in self.numbers[1:]:
            __sub-=num
        return __sub
    
    def mul(self):
        __mul=1
        for num in self.numbers:
            __mul*=num
        return __mul
    
    def div(self):
        __div=self.numbers[0]
        for num in self.numbers[1:]:
            if num==0:
                return 'Cannot Divide by Zero'
            __div/=num
        return __div
    
    def floor(self):
        __mod=self.numbers[0]
        for num in self.numbers[1:]:
            if num==0:
                return 'Cannot Divide by Zero'
            __mod//=num
        return  __mod
    
    def ceil(self):
        result=self.div()
        if isinstance(result,str):
            return result
        if result==int(result):
            return result
        if result==int(result):
            return int(result)
        if result>0:
            return int(result)+1
        else:
            return int(result)
    
import math

class Intermediate(Math):
    
    def log(self, base, number):
        if base <= 0 or base == 1:
            return "Base must be > 0 and not equal to 1"
        if number <= 0:
            return "Number must be > 0"
        return math.log(number, base)
    
    def sqrt(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        if number < 0:
            return "Square root of negative number not possible"
        return math.sqrt(number)
    
    def nth_root(self, number=None, n=2):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        if n == 0:
            return "Root cannot be zero"
        if number < 0 and n % 2 == 0:
            return "Even root of negative number not possible"
        return number ** (1/n)
    
    def factorial(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        if not isinstance(number, int):
            return "Factorial is only defined for integers"
        if number < 0:
            return "Factorial of negative number not possible"
        return math.factorial(number)
    
    def natural_log(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        if number <= 0:
            return "Number must be > 0"
        return math.log(number)  
    def antilog(self, number=None, base=10):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        return base ** number
    
class Advanced(Intermediate):

    def power(self, base=None, exponent=None):
        if base is None or exponent is None:
            if len(self.numbers) < 2:
                return "Provide base and exponent"
            base, exponent = self.numbers[:2]
        return math.pow(base, exponent)

    def sin(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        return math.sin(math.radians(number))

    def cos(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        return math.cos(math.radians(number))

    def tan(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        return math.tan(math.radians(number))

    def exponential(self, number=None):
        if number is None:
            if len(self.numbers) == 0:
                return "No number provided"
            number = self.numbers[0]
        return math.exp(number)
    






def get_numbers():
    """Helper to take multiple numbers from user."""
    n = int(input("How many numbers? : "))
    nums = []
    for i in range(n):
        val = float(input(f"Enter number {i+1}: "))
        nums.append(val)
    return nums

def basics_menu():
    print("\n--- BASICS MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Ceil of Division")

    choice = int(input("Enter your choice : "))

    nums = get_numbers()
    obj = Basics(*nums)

    if choice == 1:
        print("Result =", obj.sum())
    elif choice == 2:
        print("Result =", obj.sub())
    elif choice == 3:
        print("Result =", obj.mul())
    elif choice == 4:
        print("Result =", obj.div())
    elif choice == 5:
        print("Result =", obj.floor())
    elif choice == 6:
        print("Result =", obj.ceil())
    else:
        print("Invalid choice in Basics")


def intermediate_menu():
    print("\n--- INTERMEDIATE MENU ---")
    print("1. Log (any base)")
    print("2. Natural Log (ln)")
    print("3. Antilog")
    print("4. Square Root")
    print("5. Nth Root")
    print("6. Factorial")

    choice = int(input("Enter your choice : "))

    obj = Intermediate()   # we can pass numbers later directly to functions

    if choice == 1:
        base = float(input("Enter base : "))
        num = float(input("Enter number : "))
        print("Result =", obj.log(base, num))

    elif choice == 2:
        num = float(input("Enter number : "))
        print("Result =", obj.natural_log(num))

    elif choice == 3:
        base = float(input("Enter base (default 10, press Enter to skip): ") or 10)
        power = float(input("Enter power : "))
        print("Result =", obj.antilog(power, base))

    elif choice == 4:
        num = float(input("Enter number : "))
        print("Result =", obj.sqrt(num))

    elif choice == 5:
        num = float(input("Enter number : "))
        n = int(input("Enter n (for nth root) : "))
        print("Result =", obj.nth_root(num, n))

    elif choice == 6:
        num = int(input("Enter integer number : "))
        print("Result =", obj.factorial(num))

    else:
        print("Invalid choice in Intermediate")


def advanced_menu():
    print("\n--- ADVANCED MENU ---")
    print("1. Power (a^b)")
    print("2. Sine (in degrees)")
    print("3. Cosine (in degrees)")
    print("4. Tangent (in degrees)")
    print("5. Exponential (e^x)")

    choice = int(input("Enter your choice : "))

    obj = Advanced()   # we’ll pass numbers directly to functions

    if choice == 1:
        base = float(input("Enter base : "))
        exp = float(input("Enter exponent : "))
        print("Result =", obj.power(base, exp))

    elif choice == 2:
        angle = float(input("Enter angle in degrees : "))
        print("Result =", obj.sin(angle))

    elif choice == 3:
        angle = float(input("Enter angle in degrees : "))
        print("Result =", obj.cos(angle))

    elif choice == 4:
        angle = float(input("Enter angle in degrees : "))
        print("Result =", obj.tan(angle))

    elif choice == 5:
        num = float(input("Enter number : "))
        print("Result =", obj.exponential(num))

    else:
        print("Invalid choice in Advanced")


def main():
    while True:
        print("\n=======================")
        print("    PYTHON CALCULATOR  ")
        print("=======================")
        print("1. Basics")
        print("2. Intermediate")
        print("3. Advanced")
        print("4. Exit")

        try:
            choice = int(input("Select Level (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            basics_menu()
        elif choice == 2:
            intermediate_menu()
        elif choice == 3:
            advanced_menu()
        elif choice == 4:
            print("Exiting Calculator... Bye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()

























