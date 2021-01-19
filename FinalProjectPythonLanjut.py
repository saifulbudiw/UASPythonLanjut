from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.resizable(width=False, height=False)

HEIGHT = 100
WIDTH = 300

canvas = Canvas(root, bg='grey', height=HEIGHT, width=WIDTH)
canvas.pack()

def proses():
    x = float(numInput.get())
    
    if suhuInput.get()=='Celsius':
        if suhuOutput.get()=='Celsius':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x))
        elif suhuOutput.get()=='Reaumur':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x*0.8))
        elif suhuOutput.get()=='Fahrenheit':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x*1.8)+32))
        elif suhuOutput.get()=='Kelvin':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x+273.15))
        elif suhuOutput.get()=='Rankine':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x*1.8)+32+459.67))
            
    elif suhuInput.get()=='Reaumur':
        if suhuOutput.get()=='Celsius':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x*1.25))
        elif suhuOutput.get()=='Reaumur':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x))
        elif suhuOutput.get()=='Fahrenheit':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x*2.25)+32))
        elif suhuOutput.get()=='Kelvin':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x*1.25)+273.15))
        elif suhuOutput.get()=='Rankine':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x*2.25)+32+459.67))

    elif suhuInput.get()=='Fahrenheit':
        if suhuOutput.get()=='Celsius':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x-32)/1.8))
        elif suhuOutput.get()=='Reaumur':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x-32)/2.25))
        elif suhuOutput.get()=='Fahrenheit':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x))
        elif suhuOutput.get()=='Kelvin':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x+459.67)/1.8))
        elif suhuOutput.get()=='Rankine':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x+459.67))

    elif suhuInput.get()=='Kelvin':
        if suhuOutput.get()=='Celsius':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x-273.15))
        elif suhuOutput.get()=='Reaumur':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x-273.15)*1.8))
        elif suhuOutput.get()=='Fahrenheit':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x*1.8)-459.67))
        elif suhuOutput.get()=='Kelvin':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x))
        elif suhuOutput.get()=='Rankine':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x*1.8))

    elif suhuInput.get()=='Rankine':
        if suhuOutput.get()=='Celsius':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x-32-459.67)/1.8))
        elif suhuOutput.get()=='Reaumur':
            numOutput.delete(0, END)
            numOutput.insert(0,str((x-32-459.67)/2.25))
        elif suhuOutput.get()=='Fahrenheit':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x-459.67))
        elif suhuOutput.get()=='Kelvin':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x/1.8))
        elif suhuOutput.get()=='Rankine':
            numOutput.delete(0, END)
            numOutput.insert(0,str(x))

frameInput = Frame(root, bg='silver')
frameInput.place(relx=0.5,rely=0.4,relwidth=0.9,relheight=0.4,anchor='center')

suhu = ("Celsius","Reaumur","Fahrenheit","Kelvin","Rankine")

suhuInput = Spinbox(frameInput, bg='white', values=suhu)
suhuInput.place(relx=0.03,rely=0.5,relwidth=0.26,relheight=0.8,anchor='w')
suhuInput.get()
numInput = Entry(frameInput)
numInput.place(relx=0.3,rely=0.5,relwidth=0.15,relheight=0.8,anchor='w')
numInput.insert(0,0)
numInput.get()

tolabel = Label(frameInput, text='to', fg='white', bg='silver')
tolabel.place(relx=0.5,rely=0.5,relwidth=0.1,relheight=0.8,anchor='center')

suhuOutput = Spinbox(frameInput, bg='white', values=suhu)
suhuOutput.place(relx=0.81,rely=0.5,relwidth=0.26,relheight=0.8,anchor='e')
suhuOutput.get()
numOutput = Entry(frameInput, text=0)
numOutput.place(relx=0.95,rely=0.5,relwidth=0.15,relheight=0.8,anchor='e')
numOutput.get()


enter_button = Button(root, text='enter', command=proses)
enter_button.place(relx=0.5,rely=0.8,relwidth=0.2,relheight=0.2,anchor='center')

root.mainloop()
