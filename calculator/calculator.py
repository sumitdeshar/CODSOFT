import math

def calculator(operator, value1, value2):
    try:
        value = eval("{}{}{}".format(value1, operator, value2))
    except ZeroDivisionError:
        return f"Divided by zero"
    return f"{value1} {operator} {value2} = {value}"
print(calculator('/', 5.34, 1.23))


def main():
    print("These are the operation that you can perform in this calculator")
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Remainder\n6.Power\n7.Square Root\n8.Triginometric calculation\nLog")

    while True:
        choice = input("Enter choice: ")

        if choice in [str(num) for num in range(1,9)]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Please note that you second number is 1 so that its does affect the operation when it is not required.\nEnter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                calculator('+',num1,num2)

            elif choice == '2':
                calculator('-',num1,num2)

            elif choice == '3':
                calculator('*',num1,num2)

            elif choice == '4':
                calculator('/',num1,num2)

            elif choice == '5':
                calculator('%',num1,num2)

            elif choice == '6':
                calculator('**',num1,num2)

            elif choice == '7':
                return eval("math.sqrt(num1)")

            elif choice == '8':
                trigno_choice = input("Choose trigonometric function: sin, cos, tan: ").lower()
                if trigno_choice == 'sin':
                    print(f"sin({num1}) = {math.sin(math.radians(num1))}")
                elif trigno_choice == 'cos':
                    print(f"cos({num1}) = {math.cos(math.radians(num1))}")
                elif trigno_choice == 'tan':
                    print(f"tan({num1}) = {math.tan(math.radians(num1))}")
                else:
                    print("Invalid trigonometric function.")
            elif choice == '9':
                base = float(input("Enter base for log (default is e fo now): ") or math.e)
                print(f"log({num1}, {base}) = {math.log(num1, base)}")
                
            else:
                return f'Your choices doesnot match with any given choices.'
            
        else:
            return ("Invalid choice")

if __name__ == "__main__":
    main()