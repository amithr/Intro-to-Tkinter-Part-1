from tkinter import *

window = Tk()

# Set font size to appear correctly on a Mac
label_1=Label(window, text='First Number:', font=("Arial", 12))
label_2=Label(window, text='Second Number:', font=("Arial", 12))
field_1=Entry()
field_2=Entry()
label_1.place(x=100, y=50)
field_1.place(x=200, y=50)
label_2.place(x=100, y=100)
field_2.place(x=200, y=100)

label_3=Label(window, text='Result:', font=("Arial", 12))
field_3=Entry()
label_3.place(x=100, y=200)
field_3.place(x=200, y=200)

btn1 = Button(window, text='Add', command=lambda :add(field_1.get(), field_2.get(), field_3), font=("Arial", 12))
btn2 = Button(window, text='Subtract', command=lambda :sub(field_1.get(), field_2.get(), field_3), font=("Arial", 12))

btn1.place(x=100, y=150)
btn2.place(x=200, y=150)

def add(num_1, num_2, field_3):
    print(num_1)
    field_3.delete(0, 'end')
    result = int(num_1) + int(num_2)
    field_3.insert(END, str(result))

def sub(num_1, num_2, field_3):
    field_3.delete(0, 'end')
    result = int(num_1) - int(num_2)
    field_3.insert(END, str(result))


window.title("Intro to Python")
window.resizable(False,False)
window.geometry("400x300")
# Size is weird on a Mac
window.mainloop()