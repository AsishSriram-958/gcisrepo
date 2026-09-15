def operand_number(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        return a / b
    raise ValueError("Unsupported operation")


def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    print(operand_number(a, b, operation))


if __name__ == "__main__":
    main()


       
