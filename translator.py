from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def conversion(txt="type",fromConvert="English",toConvert="Hindi"):
    trans = Translator()
    Result = trans.translate(txt,src=fromConvert,dest=toConvert)
    return Result.text

def data():
    s = comb_source1.get()
    d = comb_source2.get()
    msg = Sor_txt.get(1.0,END)
    main = conversion(msg.lower(),s,d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,main)


window = Tk()
window.title("Translator")

window.geometry('800x600')
window.config()

Label_txt = Label(window,text="Translator",font=("Time New Roman",30)).pack()

frame = Frame(window,height=100,).pack(side=BOTTOM)

Sor_txt = Text(frame,font=("Time New Roman",16),wrap=WORD,spacing1=10,spacing3=10)
Sor_txt.place(height=80,y=80,width=500,x=125)

List_txt = list(LANGUAGES.values())

comb_source1 = ttk.Combobox(frame,value=List_txt)
comb_source1.place(x=150,y=200,height=25,width=80)
comb_source1.set("English")

comb_source2 = ttk.Combobox(frame,value=List_txt)
comb_source2.place(x=500,y=200,height=25,width=80)
comb_source2.set("Japanese")

dest_txt = Text(frame,font=("Time New Roman",16),wrap=WORD,spacing1=10,spacing3=10)
dest_txt.place(height=100,y=300,width=500,x=125)

button = Button(frame,text="Translate",relief=RAISED,bg="white",command=data)
button.place(height=30,width=80,x=330,y=200)





window.mainloop()