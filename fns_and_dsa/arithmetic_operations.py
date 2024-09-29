def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if (num2 == 0):
                print("you can't apply division by zero")
                return 0
            else:
                return num1 / num2
        case _:
                print("Invalid operation; shoose one of these (add, subtract, multiply, divide)")
                return 0


    