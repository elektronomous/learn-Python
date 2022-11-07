def add(n1:float|int, n2:float|int):
    return n1 + n2;

def substract(n1:float|int, n2:float|int):
    return n1 - n2;

def multiply(n1:float|int, n2:float|int):
    return n1 * n2;

def divide(n1:float|int, n2:float|int):
    return n1 / n2;

def main():
    operations = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
    };
    
        
    
    calculating = True;

    number1 = float(input("What's the first number: "));

    while calculating:
        for operation in operations:
            print(operation);
        operator = input("pick an operation: ");
        number2 = float(input("What's the next number: "));
        
        if operator in operations:
            total = operations[operator](number1, number2);
            print(f"{number1} {operator} {number2} = {total}");
            number1 = total;
        else:
            print("Invalid operations");
            number1 = 0;
                    
        promptUser = input(f"Type 'y' to continue to count {total}, 'q' to quit, 'n' to calculate new number: ").lower()[0];
        
        if promptUser == 'n':
            number1 =  float(input("What's the first number: "));
        elif promptUser != 'y':
            calculating = False;

if __name__ == '__main__':
    main();