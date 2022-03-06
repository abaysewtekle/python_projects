## import libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound


window = Tk()
window.geometry('350x300')
window.resizable(0,0)
window.config(bg = 'coral')
window.title('Text To Speech')


##heading
Label(window, text = 'Text To Speech' , font='arial 20 bold' , bg ='coral').pack()


#label
Label(window, text ='Enter Text', font ='arial 15 bold', bg ='coral').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(window,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('sound.mp3')
    playsound('sound.mp3')

def Exit():
    window.destroy()

def Reset():
    Msg.set("")

#Button
Button(window, text = "Play" , font = 'arial 15 bold', command = Text_to_speech, width =4).place(x=25, y=140)
Button(window,text = 'Exit',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(window, text = 'Reset', font='arial 15 bold', command = Reset).place(x=175 , y =140)


#infinite loop to run program
root.mainloop()

