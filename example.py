import sympy as sp # type: ignore # import sympy library to perform symbolic mathematics

# Here we define the calculator function
def calculator():
    print("Welcome to the Calculator")

    while True:

        # 1. ASK FOR THE OPERATOR FIRST
        operator = input("Operator (+, -, *, /, %, **, //, SR, DER): ").strip()

        if operator not in ["+", "-", "*", "/", "%", "**", "//", "SR", "DER"]:
            print("Error: unsupported operator.")
            continue

        # 2. VALIDATE FIRST NUMBER (Only if it's NOT a derivative)
        if operator != "DER":
            try:
                first = float(input("First number: ").strip())
            except ValueError:
                print("Error: please enter a valid first number.")
                continue

        # 3. VALIDATE SECOND NUMBER (Only for standard binary operations)
        if operator != "SR" and operator != "DER":  
            try:
                second = float(input("Second number: ").strip())
            except ValueError:
                print("Error: please enter a valid second number.")
                continue

        # Perform calculation
        if operator == "+":
            # Add the first number to the second number and round to two decimal places
            result = round(first + second, 2)

        elif operator == "-":
            # Subtract the second number from the first number and round to two decimal places
            result = round(first - second, 2)

        elif operator == "*":
            # Multiply both numbers and round the result to two decimal places
            result = round(first * second, 2)

        elif operator == "/":
            if second == 0:
                print("Error: cannot divide by zero.")
                continue
            # Divide the first number by the second number and round to two decimal places
            result = round(first / second, 2)

        elif operator == "%": 
            if second == 0:
                print("Error: cannot divide by zero.")
                continue
            # Return the remainder of the division between both numbers (Modulo)
            result = (first % second) 

        elif operator == "**": 
            # Raise the first number to the power of the second number (Exponentiation)
            result = (first ** second) 

        elif operator == "//": 
            if second == 0:
                print("Error: cannot divide by zero.")
                continue
            # Perform division and discard decimals, returning only the integer part
            result = (first // second) 

        elif operator == "SR": 
            if first < 0:
                print("Error: cannot calculate square root of a negative number.")
                continue

            # Newton-Raphson method
            # Iterative numerical algorithm to approximate the exact square root without external libraries
            guess = first
            for _ in range(10):
                guess = (guess + first / guess) / 2

            resultSR = round(guess, 2)
            print(f"Square root of {first:g} = {resultSR:g}")

        elif operator == "DER":
            print("You have selected the derivative operator (DER).")
            print("Please enter the function in terms of 'x' when prompted.")
            print("Example: x**2 + 5*x, 3*x**3, sp.sin(x), etc.")
            
            # Create the symbolic mathematical variable 'x'
            x = sp.Symbol('x')

            # Prompt the user for the function input as regular text
            user_input = input("Enter your function f(x): ")

            try:
                # SymPy automatically converts the text string into a mathematical function expression
                function_expr = sp.sympify(user_input)
    
                # Apply analytical calculus rules to find the derivative with respect to x
                derivative_expr = sp.diff(function_expr, x)
    
                print("\n--- RESULT ---")
                print(f"Original function: f(x) = {function_expr}")
                print(f"Its derivative is: f'(x) = {derivative_expr}")

            except Exception as e:
                print("\n[Error]: Could not parse the function. Make sure to use '*' for multiplication (e.g., 2*x) and '**' for powers (e.g., x**2).")

        # Display result (Only for standard binary operations)
        if operator != "SR" and operator != "DER":  
            print(f"Result of {first:g} {operator} {second:g} = {result:g}")
        
        # Ask only after a successful calculation
        option = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()

        if option == "n":
            print("Exiting calculator.")
            break
        elif option != "y":
            print("Wrong input. Exiting calculator.")
            break

# Here we call the calculator function to start the program
calculator()
