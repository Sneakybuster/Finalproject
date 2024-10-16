from tkinter import *
import numpy as np
import math
root= Tk()
root.title("Scientific Calculator")
string=""
input= StringVar()
e= Entry(root, width=35, borderwidth=5, textvariable=input)
e.grid(row=0, column=0, columnspan=5, padx=10)
def button_click(symbol):
    global string
    string += str(symbol)
    input.set(string)

def clear():
    global string
    string=""
    input.set(string)

def delete():
    global string
    tect= string[:-1]
    input.set(tect)


#
abs = Button(root, text="abs", command=lambda:button_click("abs(")).grid(row=1, column=0, sticky="nsew")
mod = Button(root, text="mod", command=lambda:button_click("%")).grid(row=1, column=1, sticky="nsew")
div = Button(root, text="div", command=lambda:button_click("//")).grid(row=1, column=2, sticky="nsew")

factorial = Button(root, text="x!", command=lambda:("fact")).grid(row=1, column=3, sticky="nsew")

euler = Button(root, text='e', command=lambda:button_click(str(math.exp(1)))).grid(row=1, column=4, sticky="nsew")

#
sin=Button(root, text="sin", command=lambda:button_click("sin")).grid(row=2, column=0, sticky="nsew")
cos=Button(root, text="cos", command=lambda:button_click("cos")).grid(row=2, column=1, sticky="nsew")
tan=Button(root, text="tan", command=lambda:button_click("tan")).grid(row=2, column=2, sticky="nsew")

pi=Button(root, text="π", command=lambda:button_click(str(math.pi))).grid(row=2, column=3, sticky="nsew")
x=Button(root, text="x", command=lambda:button_click("x")).grid(row=2, column=4, sticky="nsew")
#
integral=Button(root, text="\u222B", command=lambda:button_click("inte")).grid(row=3, column=0, sticky="nsew")
diffrentiation=Button(root, text="\u0064\u0079\u2044\u0064\u0078", command=lambda:button_click("diff")).grid(row=3, column=1, sticky="nsew")

xpowern = Button(root, text='x^n',command=lambda:button_click('**')).grid(row=3, column=2, sticky="nsew")

equation= Button(root,text="Eq", command=lambda:button_click("eq")).grid(row=3, column=3, sticky="nsew")
simultaneous= Button(root, text="sim", command=lambda:button_click("sim")).grid(row=3, column=4, sticky="nsew")
#
nth_root = Button(root, text='\u221A', command=lambda:button_click('**(1/')).grid(row=4, column=0, sticky="nsew")
log10 = Button(root, text='log\u2081\u2080', command=lambda:button_click('log(')).grid(row=4, column=1, sticky="nsew")
ln = Button(root, text='ln', command=lambda:button_click('ln(')).grid(row=4, column=2, sticky="nsew")
eulerpower = Button(root, text="e^x", command=lambda:button_click('e(')).grid(row=4, column=3, sticky="nsew")
signchange = Button(root, text="\u00B1", command=lambda:button_click('-')).grid(row=4, column=4, sticky="nsew")
#
left = Button(root, text='(', command=lambda:button_click('(')).grid(row=5, column=0, sticky="nsew")
right = Button(root, text=')', command=lambda:button_click(')')).grid(row=5, column=1, sticky="nsew")

csc=Button(root, text="csc", command=lambda:button_click("csc")).grid(row=5, column=2, sticky="nsew")
sec=Button(root, text="sec", command=lambda:button_click("sec")).grid(row=5, column=3, sticky="nsew")
cot=Button(root, text="cot", command=lambda:button_click("cot")).grid(row=5, column=4, sticky="nsew")
#

button7 = Button(root, text='7', command=lambda:button_click('7')).grid(row=6, column=0, sticky="nsew")
button8 = Button(root, text="8", command=lambda:button_click('8')).grid(row=6, column=1, sticky="nsew")
button9 = Button(root, text="9", command=lambda:button_click('9')).grid(row=6, column=2, sticky="nsew")
deletee = Button(root, text='del', command=lambda:button_click('del')).grid(row=6, column=3, sticky="nsew")
clearr = Button(root, text='clr', command=lambda:button_click('clr')).grid(row=6, column=4, sticky="nsew")
#
button4 = Button(root, text='4', command=lambda:button_click('4')).grid(row=7, column=0, sticky="nsew")
button5 = Button(root, text="5", command=lambda:button_click('5')).grid(row=7, column=1, sticky="nsew")
button6 = Button(root, text="6", command=lambda:button_click('6')).grid(row=7, column=2, sticky="nsew")
multipy = Button(root, text='*', command=lambda:button_click('*')).grid(row=7, column=3, sticky="nsew")
div = Button(root, text='/', command=lambda:button_click('/')).grid(row=7, column=4, sticky="nsew")
#
button1 = Button(root, text='1', command=lambda:button_click('1')).grid(row=8, column=0, sticky="nsew")
button2 = Button(root, text="2", command=lambda:button_click('2')).grid(row=8, column=1, sticky="nsew")
button3 = Button(root, text="3", command=lambda:button_click('3')).grid(row=8, column=2, sticky="nsew")
add = Button(root, text='+', command=lambda:button_click('+')).grid(row=8, column=3, sticky="nsew")
sub = Button(root, text='-', command=lambda:button_click('-')).grid(row=8, column=4, sticky="nsew")
#
button0 = Button(root, text='0', command=lambda:button_click('0')).grid(row=9, column=0, sticky="nsew")
deciaml = Button(root, text=".", command=lambda:button_click('.')).grid(row=9, column=1, sticky="nsew")
equal = Button(root, text="=", command=lambda:button_click('=')).grid(row=9, column=2, columnspan=3, sticky="nsew")
#


root.mainloop()