from tkinter import *

def leftClickButton(event):
    height = float(textBoxHeight.get())
    weight = float(textBoxWeight.get())
    result = ((weight/ ((height/100)**2)))
    if result < 18.50:
        labelResult.configure(text="น้ำหนักน้อย / ผอม")
    elif 18.50 <= result <= 22.90:
        labelResult.configure(text="ปกติ (สุขภาพดี)")
    elif 23 >= result >= 24.90:
        labelResult.configure(text="ท้วม / โรคอ้วนระดับ 1")
    elif 25 <= result <= 29.90:
        labelResult.configure(text="อ้วน / โรคอ้วนระดับ 2")
    elif result >= 30:
        labelResult.configure(text="อ้วนมาก / โรคอ้วนระดับ 3")
    else:
        labelResult.configure(text="Please Enter Again!")

MainWindow = Tk()

labelHeight = Label(MainWindow,text="Height [cm.]")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="Weight [Kg.]")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="Calculate")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="Result")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()