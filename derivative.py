import sympy as sp

function = input("Enter a function in terms of x ")
x = sp.symbols('x')

try:
    value = sp.parse_expr(function)
except:
    print("Invalid Input. Try Again.")
    exit()

derivative = sp.diff(value, x)
print("The derivative is: ", derivative)
