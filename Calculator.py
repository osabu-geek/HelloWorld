from tkinter import*
import math
import tkinter.messagebox

root = Tk()
root.title("Osabu Scientific Calculator")
root.configure(background = "powder blue")
root.resizable(width = False, height =False)
root.geometry("480x568+0+0")

Calc = Frame(root)
Calc.grid()

class calculator():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def NumberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "Subtract":
            self.total -= self.current
        if self.op == "Multiplication":
            self.total *= self.current
        if self.op == "Division":
            self.total /= self.current
        if self.op == "Mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = "0"

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def MathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def Squaredroot(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def Cosine(self):
        self.result = False
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)

    def Sine(self):
        self.result = False
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)

    def Tan(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def Sinh(self):
        self.result = False
        self.current = math.sinh(float(txtDisplay.get()))
        self.display(self.current)

    def Cosh(self):
        self.result = False
        self.current = math.cosh(float(txtDisplay.get()))
        self.display(self.current)

    def Tanh(self):
            self.result = False
            self.current = math.tanh(float(txtDisplay.get()))
            self.display(self.current)

    def aSinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def aCosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def aTanh(self):
        self.result = False
        self.current = math.atanh(float(txtDisplay.get()))
        self.display(self.current)

    def Log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def Log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def Log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def Log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def Exponent(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def Expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def Degree(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

added_value = calculator()

# Text display
txtDisplay = Entry(Calc, font =('times new roman', 20, 'bold'), bg = "powder blue", bd = 30, width = 28, justify = RIGHT)
txtDisplay.grid(row =0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(Calc, width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                          text = numberpad[i]))
        btn[i].grid(row = j, column = k, pady = 1)
        btn[i]["command"] = lambda x = numberpad[i] : added_value.NumberEnter(x)
        i += 1

# ========================================#===================================#==========================

btnClear = Button(Calc, text = chr(67) , width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Clear_Entry).grid(row = 1, column = 0, pady = 1)

btnAllClear = Button(Calc, text = chr(67) + chr(69), width = 6, height = 2, font = ('times new roman', 20, 'bold'),
                     bd = 4, bg = "powder blue", command = added_value.All_Clear_Entry).\
                     grid(row = 1, column = 1, pady = 1)

btnSqrt = Button(Calc, text = "√" , width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Squaredroot).grid(row = 1, column = 2, pady = 1)

btnAdd = Button(Calc, text = "+", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("add")).\
                  grid(row = 1, column = 3, pady = 1)

btnSubtract = Button(Calc, text = "-", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("Subtract")).\
                  grid(row = 2, column = 3, pady = 1)

btnMultiplication = Button(Calc, text = "*", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("Multiplication")).\
                  grid(row = 3, column = 3, pady = 1)

btnDivision = Button(Calc, text = "÷", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("Division")).\
                  grid(row = 4, column = 3, pady = 1)

btnZero = Button(Calc, text = "0", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.NumberEnter(0)).grid(row = 5, column = 0, pady = 1)


btnDot = Button(Calc, text = ".", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.NumberEnter(".")).\
                  grid(row = 5, column = 1, pady = 1)

btnPM = Button(Calc, text = chr(177), width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.MathsPM).grid(row = 5, column = 2, pady = 1)

btnEqual = Button(Calc, text = "=", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.sum_of_total).grid(row = 5, column = 3, pady = 1)

# =================================Scientific Calculator=================================================

btnPi = Button(Calc, text = "π" , width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.pi).grid(row = 1, column = 4, pady = 1)

btnSin = Button(Calc, text = "sin" + chr(69), width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Sine).grid(row = 1, column = 5, pady = 1)

btnCos = Button(Calc, text = "cos" , width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Cosine).grid(row = 1, column = 6, pady = 1)

btnTan = Button(Calc, text = "tan", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Tan).grid(row = 1, column = 7, pady = 1)

# ================================Advance sets 1 ==============================================================

btn2Pi = Button(Calc, text = "2π", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.tau).grid(row = 2, column = 4, pady = 1)

btnCosh = Button(Calc, text = "cosh", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Cosh).grid(row = 2, column = 5, pady = 1)

btnTanh = Button(Calc, text = "tanh", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Tanh).grid(row = 2, column = 6, pady = 1)

btnSinh = Button(Calc, text = "sinh", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Sinh).grid(row = 2, column = 7, pady = 1)

# ================================Advance sets 2 ==============================================================

btnlog = Button(Calc, text = "log", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Log).grid(row = 3, column = 4, pady = 1)

btnExponent = Button(Calc, text = "Exp", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Exponent).grid(row = 3, column = 5, pady = 1)

btnMod = Button(Calc, text = "mod", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = lambda: added_value.operation("Mod")).\
                  grid(row = 3, column = 6, pady = 1)

btne = Button(Calc, text = "e", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.e).grid(row = 3, column = 7, pady = 1)

# ================================Advance sets 3 ==============================================================

btnlog2 = Button(Calc, text = "log2", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Log2).grid(row = 4, column = 4, pady = 1)

btnDeg = Button(Calc, text = "deg", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Degree).grid(row = 4, column = 5, pady = 1)

btnaCosh = Button(Calc, text = "acosh", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.aCosh).grid(row = 4, column = 6, pady = 1)

btnasinh = Button(Calc, text = "asinh", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.aSinh).grid(row = 4, column = 7, pady = 1)

# ================================Advance sets 4 ==============================================================

btnlog10 = Button(Calc, text = "log10", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Log10).grid(row = 5, column = 4, pady = 1)

btnlog1p = Button(Calc, text = "log1p", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Log1p).grid(row = 5, column = 5, pady = 1)

btnexpm1 = Button(Calc, text = "expm1", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.Expm1).grid(row = 5, column = 6, pady = 1)

btnlgamma = Button(Calc, text = "lgamma", width = 6, height = 2, font = ('times new roman', 20, 'bold'), bd = 4,
                  bg = "powder blue", command = added_value.lgamma).grid(row = 5, column = 7, pady = 1)

# ================================================================================================================

lblDisplay = Label(Calc, text = "Scientific Calculator", font = ('times new roman', 30, 'bold'), justify = CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan = 4)

# ====================================Menu=======================================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Osabu Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")


def standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(Calc)
# Creating The files required to specify which calculator to use or exit the program
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Scientific", command = scientific)
filemenu.add_command(label = "Standard", command = standard)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)


# Creating the edit function of the calculator to copy, cut or paste
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

# Creating the Help menu
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help")

# Configure the Menubar
root.config(menu = menubar)
root.mainloop()

