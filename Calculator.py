import math
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics
from sympy import Symbol, integrate, sympify
import sympy as sp
from scipy.stats import poisson,norm
import scipy.stats as stats


#Scientific Calculator
def evaluate_expression(expr):
    try:
        expr = expr.replace("sin(", "math.sin(")
        expr = expr.replace("cos(", "math.cos(")
        expr = expr.replace("tan(", "math.tan(")
        expr = expr.replace("log(", "math.log10(")
        expr = expr.replace("ln(", "math.log(")
        expr = expr.replace("e(", "math.exp(")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("abs(", "math.fabs(")
        expr = expr.replace("math.sqrt(", "math.sqrt(")
        return eval(expr)
    except Exception as e:
        return "Error"
    
def scientific_calculator():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Scientific Calculator")
    global string, input
    string = ""
    input = StringVar()
    e = Entry(root, width=35, borderwidth=5, textvariable=input)
    e.grid(row=0, column=0, columnspan=5, padx=10)

    def button_click(symbol):
        global string
        string += str(symbol)
        input.set(string)

    def clear():
        global string
        string = ""
        input.set(string)

    def delete():
        global string
        string = string[:-1]
        input.set(string)

    def calculate():
        global string
        result = evaluate_expression(string)
        string = str(result)
        input.set(string)

    Button(root, text="ABS",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("abs(")).grid(row=1, column=0, sticky="nsew")
    Button(root, text="MOD",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("%")).grid(row=1, column=1, sticky="nsew")
    Button(root, text="DIV",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("//")).grid(row=1, column=2, sticky="nsew")
    Button(root, text="x!",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("math.factorial(")).grid(row=1, column=3, sticky="nsew")
    Button(root, text='e', bg="#ee9f27", fg="#ffffff",command=lambda: button_click(str(math.e))).grid(row=1, column=4, sticky="nsew")

    Button(root, text="sin",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("sin(")).grid(row=2, column=0, sticky="nsew")
    Button(root, text="cos",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("cos(")).grid(row=2, column=1, sticky="nsew")
    Button(root, text="tan",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("tan(")).grid(row=2, column=2, sticky="nsew")
    Button(root, text="π", bg="#ee9f27", fg="#ffffff",command=lambda: button_click("π")).grid(row=2, column=3, sticky="nsew")
    Button(root, text='x^n',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('**')).grid(row=2, column=4, sticky="nsew")

    Button(root, text='√',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('math.sqrt(')).grid(row=3, column=0, sticky="nsew")
    Button(root, text='log10',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('log(')).grid(row=3, column=1, sticky="nsew")
    Button(root, text='ln',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('ln(')).grid(row=3, column=2, sticky="nsew")
    Button(root, text="e^x",bg="#ee9f27", fg="#ffffff", command=lambda: button_click('math.exp(')).grid(row=3, column=3, sticky="nsew")
    Button(root, text="\u00B1",bg="#ee9f27", fg="#ffffff", command=lambda: button_click('-')).grid(row=3, column=4, sticky="nsew")

    Button(root, text='(',bg="#505050", fg="#ffffff", command=lambda: button_click('(')).grid(row=4, column=0, sticky="nsew")
    Button(root, text=')',bg="#505050", fg="#ffffff", command=lambda: button_click(')')).grid(row=4, column=1, sticky="nsew")
    Button(root, text="csc",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("1/sin(")).grid(row=4, column=2, sticky="nsew")
    Button(root, text="sec",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("1/cos(")).grid(row=4, column=3, sticky="nsew")
    Button(root, text="cot",bg="#ee9f27", fg="#ffffff", command=lambda: button_click("1/tan(")).grid(row=4, column=4, sticky="nsew")

    Button(root, text='7',bg="#505050", fg="#ffffff", command=lambda: button_click('7')).grid(row=5, column=0, sticky="nsew")
    Button(root, text="8",bg="#505050", fg="#ffffff", command=lambda: button_click('8')).grid(row=5, column=1, sticky="nsew")
    Button(root, text="9",bg="#505050", fg="#ffffff", command=lambda: button_click('9')).grid(row=5, column=2, sticky="nsew")
    Button(root, text='DEL',bg="#2196F3", fg="#ffffff", command=delete).grid(row=5, column=3, sticky="nsew")
    Button(root, text='CLR',bg="#2196F3", fg="#ffffff", command=clear).grid(row=5, column=4, sticky="nsew")

    Button(root, text='4',bg="#505050", fg="#ffffff", command=lambda: button_click('4')).grid(row=6, column=0, sticky="nsew")
    Button(root, text="5",bg="#505050", fg="#ffffff", command=lambda: button_click('5')).grid(row=6, column=1, sticky="nsew")
    Button(root, text="6",bg="#505050", fg="#ffffff", command=lambda: button_click('6')).grid(row=6, column=2, sticky="nsew")
    Button(root, text='*',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('*')).grid(row=6, column=3, sticky="nsew")
    Button(root, text='/',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('/')).grid(row=6, column=4, sticky="nsew")

    Button(root, text='1',bg="#505050", fg="#ffffff", command=lambda: button_click('1')).grid(row=7, column=0, sticky="nsew")
    Button(root, text="2",bg="#505050", fg="#ffffff", command=lambda: button_click('2')).grid(row=7, column=1, sticky="nsew")
    Button(root, text="3",bg="#505050", fg="#ffffff", command=lambda: button_click('3')).grid(row=7, column=2, sticky="nsew")
    Button(root, text='+',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('+')).grid(row=7, column=3, sticky="nsew")
    Button(root, text='-',bg="#ee9f27", fg="#ffffff", command=lambda: button_click('-')).grid(row=7, column=4, sticky="nsew")

    Button(root, text='0',bg="#505050", fg="#ffffff", command=lambda: button_click('0')).grid(row=8, column=0, sticky="nsew")
    Button(root, text=".",bg="#505050", fg="#ffffff", command=lambda: button_click('.')).grid(row=8, column=1, sticky="nsew")
    Button(root, text="=",bg="#ee9f27", fg="#ffffff", command=calculate).grid(row=8, column=2, columnspan=2, sticky="nsew")
    Button(root, text="Back",bg="#2196F3", fg="#ffffff", command=Mainmenu).grid(row=8, column=4, columnspan=1, sticky="nsew")

#Graphic Calculator
def graphic_calculator():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Graphic Calculator")

    def plot_graph():
        try:
            degree = int(degree_entry.get())
            coeffs = list(map(float, coeff_entry.get().split()))
            left = float(left_entry.get())
            right = float(right_entry.get())
            points = int(points_entry.get())

            if len(coeffs) != degree + 1:
                raise ValueError("Number of coefficients must match the degree + 1.")
            p = np.poly1d(coeffs)
            x = np.linspace(left, right, points)
            y = p(x)

            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(x, y, label="Polynomial Curve", color="blue")
            ax.axhline(0, color="black", linewidth=0.8, linestyle="--")  # X-axis
            ax.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Y-axis
            ax.set_xlabel("X-Axis")
            ax.set_ylabel("Y-Axis")
            ax.grid(True)
            ax.set_xlim(left, right)
            ax.set_ylim(min(y)-1, max(y)+1)

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()

        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Degree of Polynomial:").pack()
    degree_entry = Entry(root)
    degree_entry.pack()

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Coefficients (space-separated):").pack()
    coeff_entry = Entry(root)
    coeff_entry.pack()

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Left Bound:").pack()
    left_entry = Entry(root)
    left_entry.pack()

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Right Bound:").pack()
    right_entry = Entry(root)
    right_entry.pack()

    Label(root, bg="#2c2c2c", fg="#ffffff",text="How Many Points Should Be Plotted Within The Bounds:").pack()
    points_entry = Entry(root)
    points_entry.pack()

    Button(root,bg="#505050", fg="#ffffff", text="Plot Graph", command=plot_graph).pack(pady=10)

    error_label = Label(root, bg="#2c2c2c",text="", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()

#Statistics Calculator
def statistics_calculator():
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Statistics Calculator")

    def mean():
        numbers = list(map(float, number_entry.get().split()))
        mean = statistics.mean(numbers)
        result_label.config(text=f"Mean: {mean}")

    def median():
        numbers = list(map(float, number_entry.get().split()))
        median = statistics.median(numbers)
        result_label.config(text=f"Median: {median}")

    def mode():
        numbers = list(map(float, number_entry.get().split()))
        mode = statistics.mode(numbers)
        result_label.config(text=f"Mode: {mode}")
        
    def stdev():
        numbers = list(map(float, number_entry.get().split()))
        stdev = statistics.stdev(numbers)
        stdev= round(stdev,3)
        result_label.config(text=f"Standard Deviation: {stdev}")


    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, bg="#2c2c2c", fg="#ffffff",text="Enter Numbers(space seperated):").pack()
    number_entry = Entry(root)
    number_entry.pack()

    Button(root, text="Mean",bg="#505050", fg="#ffffff", command=mean).pack(pady=10)

    Button(root, text="Median", bg="#505050", fg="#ffffff",command=median).pack(pady=10)

    Button(root, text="Mode",bg="#505050", fg="#ffffff", command=mode).pack(pady=10)

    Button(root, text="Standard Deviation",bg="#505050", fg="#ffffff", command=stdev).pack(pady=10)

    result_label = Label(root,bg="#2c2c2c", text="", font=("Helvetica", 14))
    result_label.pack(pady=20)

#Calculus Calculator
def calculus_calculator():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Calculus Calculator")

    def integral():
        try:
            express=Calculus_entry.get()
            x = Symbol('x')
            f = sympify(express)
            result = integrate(f, x)
            result_label.config(text=f"Integral: {result}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    def diffrentiate():
        try:
            express=Calculus_entry.get()
            x = sp.symbols('x')
            value = sp.parse_expr(express)
            derivative = sp.diff(value, x)
            result_label.config(text=f"Derivative: {derivative}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    
    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, bg="#2c2c2c", fg="#ffffff",text="Enter the expression to integrate or differentiate (in terms of x): ").pack()
    Calculus_entry = Entry(root)
    Calculus_entry.pack()

    Button(root, text="Integrate",bg="#505050", fg="#ffffff", command=integral).pack(pady=10)

    Button(root, text="Diffrentiate",bg="#505050", fg="#ffffff", command=diffrentiate).pack(pady=10)

    result_label = Label(root, text="",bg="#2c2c2c", fg="#ffffff", font=("Helvetica", 14))
    result_label.pack(pady=20)

#Distributions
def Binomial_Distribution():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Binomial Distribution")
    def binomial():
        try:
            n = int(successes_entry.get())
            p = float(prob_entry.get())

            x = np.arange(0, n + 1)
            pmf = stats.binom.pmf(x, n, p)
            cdf = stats.binom.cdf(x,n,p)
            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(1, 2, figsize=(10, 4))

            ax[0].bar(x, pmf, color='blue', alpha=0.7)
            ax[0].set_title(f"PMF Binomial (n={n}, p={p})")
            ax[0].set_xlabel("Number of Successes")
            ax[0].set_ylabel("Probability")
            ax[0].grid(False)

            ax[1].bar(x, cdf, color='green', alpha=0.7)
            ax[1].set_title(f"CDF Binomial (n={n}, p={p})")
            ax[1].set_xlabel("Number of Successes")
            ax[1].set_ylabel("Cumulative Probability")
            ax[1].grid(False)

            plt.tight_layout()

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()

        except ValueError as e:
            error_label.config(text="Error: " + str(e))


    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, bg="#2c2c2c", fg="#ffffff",text="Enter Number Of Trials:").pack()
    successes_entry = Entry(root)
    successes_entry.pack()

    Label(root, bg="#2c2c2c", fg="#ffffff",text="Enter Probability:").pack()
    prob_entry = Entry(root)
    prob_entry.pack()

    Button(root,bg="#505050", fg="#ffffff", text="Plot Graph", command=binomial).pack(pady=10)

    error_label = Label(root, bg="#2c2c2c",text="", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()


def Normal_Distribution():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Normal Distribution")

    def normal():
        try:
            mean = int(mean_entry.get())
            stdev = int(stdev_entry.get())
            x = np.linspace(mean - 4 * stdev, mean + 4 * stdev, 1000)

            pdf = stats.norm.pdf(x, mean, stdev)
            cdf = stats.norm.cdf(x, mean, stdev)

            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(1,2,figsize=(10, 4))
            ax[0].plot(x, pdf, color="blue")
            ax[0].fill_between(x, pdf, alpha=0.3, color="blue")
            ax[0].set_title("PDF of Normal Distribution")
            ax[0].set_xlabel("Value")
            ax[0].set_ylabel("Probability Density")
            
            ax[1].plot(x, cdf, color="green")
            ax[1].fill_between(x, cdf, alpha=0.3, color="green")
            ax[1].set_title("CDF of Normal Distribution")
            ax[1].set_xlabel("Value")
            ax[1].set_ylabel("Probability Density")

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    

    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root, bg="#2c2c2c", fg="#ffffff",text="Enter Mean:").pack()
    mean_entry = Entry(root)
    mean_entry.pack()

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Standard Deviation:").pack()
    stdev_entry = Entry(root)
    stdev_entry.pack()

    Button(root, text="Plot Graph",bg="#505050", fg="#ffffff", command=normal).pack(pady=10)

    error_label = Label(root, text="",bg="#2c2c2c", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack()


def Poison_Distribution():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Poison Distribution")

    def poison():
        try:
            Lambda = int(Lambda_entry.get())
            Loc = int(loc_entry.get())
            left = float(Left_entry.get())
            right = float(Right_entry.get())

            array = np.arange(left, right, 1)
            pmf = poisson.pmf(array, Lambda, Loc)
            cdf = poisson.cdf(array, mu=Lambda, loc=Loc)


            for widget in plot_frame.winfo_children():
                widget.destroy()

            fig, ax = plt.subplots(1,2,figsize=(5, 4))
            ax[0].plot(array, pmf)
            ax[0].set_title("PMF Poisson Graph")
            ax[0].set_xlabel("X-Axis")
            ax[0].set_ylabel("Probability")
            ax[0].grid(True)

            ax[1].plot(array, cdf, color="green")
            ax[1].set_title("CDF Poisson Graph")
            ax[1].set_xlabel("X-Axis")
            ax[1].set_ylabel("Cumulative Probability")
            ax[1].grid(True)

            canvas = FigureCanvasTkAgg(fig, master=plot_frame)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError as e:
            error_label.config(text="Error: " + str(e))
    

    Button(root, text="Main Menu", command=Mainmenu).pack(pady=10)

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Left Bound:").pack()
    Left_entry = Entry(root)
    Left_entry.pack()

    Label(root, bg="#2c2c2c", fg="#ffffff",text="Enter Right Bound:").pack()
    Right_entry = Entry(root)
    Right_entry.pack()

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Lambda:").pack()
    Lambda_entry = Entry(root)
    Lambda_entry.pack()

    Label(root,bg="#2c2c2c", fg="#ffffff", text="Enter Shift:").pack()
    loc_entry = Entry(root)
    loc_entry.pack()

    Button(root, text="Plot Graph",bg="#505050", fg="#ffffff", command=poison).pack(pady=10)

    error_label = Label(root, text="",bg="#2c2c2c", fg="red")
    error_label.pack()

    plot_frame = Frame(root)
    plot_frame.pack(fill="both", expand=True)



#Main Menu (function)
def Mainmenu():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Calculator Selector")

    menu = Menu(root)
    root.config(menu=menu)

    calc_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Calculator Type", menu=calc_menu)
    calc_menu.add_command(label="Scientific Calculator", command=scientific_calculator)
    calc_menu.add_command(label="Graphic Calculator", command=graphic_calculator)
    calc_menu.add_command(label="Statistics Calculator", command=statistics_calculator)
    calc_menu.add_command(label="Calculus Calculator", command=calculus_calculator)
    calc_menu.add_command(label="Binomial Graphing", command=Binomial_Distribution)
    calc_menu.add_command(label="Normal Graphing", command=Normal_Distribution)
    calc_menu.add_command(label="Poisson Graphing", command=Poison_Distribution)
    calc_menu.add_separator()
    calc_menu.add_command(label="Quit", command=root.quit)

    Label(root, text="Welcome to the Multi-Mode Calculator", font=("Helvetica", 16),bg="#2c2c2c",fg="#ffffff").pack(pady=20)
    Button(root, text="Scientific Calculator",bg="#505050", fg="#ffffff", width=20, anchor='center', command=scientific_calculator).pack(pady=10)
    Button(root, text="Graphic Calculator",bg="#505050", fg="#ffffff", width=20, anchor='center', command=graphic_calculator).pack(pady=10)
    Button(root, text="Statistics Calculator",bg="#505050", fg="#ffffff", width=20, anchor='center', command=statistics_calculator).pack(pady=10)
    Button(root, text="Calculus Calculator",bg="#505050", fg="#ffffff" , width=20, anchor='center',command=calculus_calculator).pack(pady=10)
    Button(root, text="Binomial Distribution",bg="#505050", fg="#ffffff", width=20, anchor='center',command=Binomial_Distribution).pack(pady=10)
    Button(root, text="Normal Distribution", bg="#505050", fg="#ffffff", width=20, anchor='center',command=Normal_Distribution).pack(pady=10)
    Button(root, text="Poisson Distribution",bg="#505050", fg="#ffffff",  width=20, anchor='center',command=Poison_Distribution).pack(pady=10)

#Starting the Main Menu
root = Tk()
root.title("Calculator Selector")
root.configure(bg="#2c2c2c") 
menu = Menu(root)
root.config(menu=menu)

calc_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Calculator Type", menu=calc_menu)
calc_menu.add_command(label="Scientific Calculator", command=scientific_calculator)
calc_menu.add_command(label="Graphic Calculator", command=graphic_calculator)
calc_menu.add_command(label="Statistics Calculator", command=statistics_calculator)
calc_menu.add_command(label="Calculus Calculator", command=calculus_calculator)
calc_menu.add_command(label="Binomial Graphing", command=Binomial_Distribution)
calc_menu.add_command(label="Normal Graphing", command=Normal_Distribution)
calc_menu.add_command(label="Poisson Graphing", command=Poison_Distribution)
calc_menu.add_separator()
calc_menu.add_command(label="Exit", command=root.quit)

Label(root, text="Welcome to the Multi-Mode Calculator", font=("Helvetica", 16),bg="#2c2c2c",fg="#ffffff").pack(pady=20)
Button(root, text="Scientific Calculator",bg="#505050", fg="#ffffff", width=20, anchor='center', command=scientific_calculator).pack(pady=10)
Button(root, text="Graphic Calculator",bg="#505050", fg="#ffffff", width=20, anchor='center', command=graphic_calculator).pack(pady=10)
Button(root, text="Statistics Calculator",bg="#505050", fg="#ffffff", width=20, anchor='center', command=statistics_calculator).pack(pady=10)
Button(root, text="Calculus Calculator",bg="#505050", fg="#ffffff" , width=20, anchor='center',command=calculus_calculator).pack(pady=10)
Button(root, text="Binomial Distribution",bg="#505050", fg="#ffffff", width=20, anchor='center',command=Binomial_Distribution).pack(pady=10)
Button(root, text="Normal Distribution", bg="#505050", fg="#ffffff", width=20, anchor='center',command=Normal_Distribution).pack(pady=10)
Button(root, text="Poisson Distribution",bg="#505050", fg="#ffffff",  width=20, anchor='center',command=Poison_Distribution).pack(pady=10)

root.mainloop()
