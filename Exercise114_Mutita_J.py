from currency_converter import CurrencyConverter
from tkinter import *
from tkinter import ttk


mainWindow = Tk()
mainWindow.geometry("1000x300")
mainWindow.title("Currency Converter")
mainWindow.configure(bg="White")
mainWindow.resizable(height=FALSE, width=FALSE)

# Header
header = Frame(mainWindow, width=1000, height=60, bg="Blue")
header.grid(row=0, column=0)
header_text = Label(header, text="Currency Converter", fg="White", bg="Blue", font='Arail 20 bold', height=2, padx=370, pady=0, anchor=CENTER)
header_text.place(x=0, y=0)

# Main
main = Frame(mainWindow, width=1000, height=260, bg="White")
main.grid(row=1, column=0)

currency = ("HUF", "LVL", "RON", "ISK", "SIT", "CHF", "DKK", "MYR", "PHP", "KRW",
            "HKD", "IDR", "HRK", "MTL", "LTL", "CZK", "CYP", "NZD", "ZAR", "NOK",
            "AUD", "SGD", "THB", "CNY", "SKK", "GBP", "TRL", "TRY", "JPY", "BGN",
            "USD", "CAD", "RUB", "SEK", "EUR", "BRL", "ROL", "PLN", "EEK", "ILS",
            "MXN", "INR",)
def calculate():
    result_label.delete(0, END)
    c = CurrencyConverter()
    result = c.convert(amount.get(), from_user_choose.get(), to_user_choose.get())
    result_label.insert(0, result)

# Amount
amount = IntVar()
amount_label = Label(main, text="AMOUNT", bg="White", fg="Black", font='Arial 16 bold')
amount_label.place(x=30, y=30)
amount_text_box = Entry(main, textvariable=amount, width=20, justify=CENTER, relief=SOLID, font='Arial 16 bold')
amount_text_box.place(x=30, y=65)

# From
from_user_choose = StringVar()
from_label = Label(main, text="FROM", fg="Black", bg="White", font='Arial 16 bold')
from_label.place(x=360, y=30)
from_combo_box = ttk.Combobox(main, textvariable=from_user_choose, width=20, justify=CENTER, font='Arial 16 bold')
from_combo_box['values'] = (currency)
from_combo_box.place(x=360, y=65)

# To
to_user_choose = StringVar()
to_label = Label(main, text="TO", fg="Black", bg="White", font='Arial 16 bold')
to_label.place(x=700, y=30)
to_combo_box = ttk.Combobox(main, textvariable=to_user_choose, width=20, justify=CENTER, font='Arial 16 bold')
to_combo_box['values'] = (currency)
to_combo_box.place(x=700, y=65)

# Result
result_label = Label(main, text="RESULT", relief=FLAT, fg="Black", bg="White", font='Arial 16 bold')
result_label.place(x=30, y=115)
result_label = Entry(main, bg="White", fg="Black", font='Arial 16 bold', justify=CENTER)
result_label.place(x=30, y=150)

# Button
button_convert = Button(main, text="Convert", command=calculate, relief=SOLID, width=10, bg="Blue", fg="White", font='Arial 16 bold')
button_convert.place(x=823, y=150)

mainWindow.mainloop()

