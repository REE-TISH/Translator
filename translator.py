from tkinter import *
from tkinter import ttk
import gtts,pygame,random
from googletrans import Translator,LANGUAGES

#this dictionary contain the shortform that gtts use for converting to languange
language_codes = {
    "Afrikaans": "af",
    "Arabic": "ar",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Catalan": "ca",
    "Chinese (Mandarin)": "zh-CN",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Filipino": "fil",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Kannada": "kn",
    "Khmer": "km",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Nepali": "ne",
    "Norwegian": "no",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Sinhala": "si",
    "Slovak": "sk",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Welsh": "cy"
}

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
    
    speech(dest_txt.get(1.0,END),language_codes[d.title()])


def speech(line,d):
    tts = gtts.gTTS(text=line,lang=d)
    k = str(random.random()) 
    tts.save("output"+k+".mp3")  # here random function is used to generate a unique mp3 file everytime a new audio is generated 
    playSound(k)

def playSound(a):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("output"+a+".mp3")
    pygame.mixer.music.play()
    

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
comb_source2.set("French")

dest_txt = Text(frame,font=("Time New Roman",16),wrap=WORD,spacing1=10,spacing3=10)
dest_txt.place(height=100,y=300,width=500,x=125)

button = Button(frame,text="Translate",relief=RAISED,bg="white",command=data)
button.place(height=30,width=80,x=330,y=200)





window.mainloop()
