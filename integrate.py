from sympy import Symbol, integrate, sympify

def integral():
    expression = input("Enter the expression to integrate (in terms of x): ")
    x = Symbol('x')
    try:
        f = sympify(expression)
        result = integrate(f, x)
        print("The integral is: ", result)
    except Exception as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    integral()
