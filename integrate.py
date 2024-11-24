from sympy import Symbol, integrate, sympify

def integral():
    expression = input("Enter the expression to integrate (in terms of x): ")
    x = Symbol('x')
    try:
        f = sympify(expression)
        result = integrate(f, x)
        print("The integral is: ", result)
    except:
        print("Invalid input, try again.")

if __name__ == "__main__":
    integral()
