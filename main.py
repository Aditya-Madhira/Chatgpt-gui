import openai
import config
openai.api_key=config.mykey

import webbrowser

import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is the function called when the button is clicked
def Imbut():


    def genimage():
        userInput = imprompt.get()
        image_resp = openai.Image.create(prompt=userInput, n=4, size="512x512")
        webbrowser.open(image_resp["data"][0]["url"])



    secroot = Tk()

    # This is the section of code which creates the main window
    secroot.geometry('384x134')
    secroot.configure(background='#F0F8FF')
    secroot.title('Hello, I\'m the main window')

    # This is the section of code which creates a text input box
    imprompt = Entry(secroot)
    imprompt.place(x=117, y=45)

    # This is the section of code which creates a button
    Button(secroot, text='Done!', bg='#8B8378', font=('arial', 12, 'normal'), command=genimage).place(x=142, y=85)

    secroot.mainloop()


# this is the function called when the button is clicked
def comptext():
    def genprompt():
        userInput = imprompt.get()
        prompt_resp = openai.Completion.create(
            engine="text-davinci-002",
            stop=None,
            prompt= userInput,
            temperature=0.7,
            max_tokens=4000,

        )
        finalresp=prompt_resp.choices[0]["text"]
        mini = Tk()

        # This is the section of code which creates the main window
        mini.geometry('1280x720')
        mini.configure(background='#F0F8FF')
        mini.title('Hello, I\'m the main window')
        Label(mini, text=finalresp, bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=344, y=106)
        mini.mainloop()



    secroot = Tk()

    # This is the section of code which creates the main window
    secroot.geometry('384x134')
    secroot.configure(background='#F0F8FF')
    secroot.title('Hello, I\'m the main window')

    # This is the section of code which creates a text input box
    imprompt = Entry(secroot)
    imprompt.place(x=117, y=45)

    # This is the section of code which creates a button
    Button(secroot, text='Done!', bg='#8B8378', font=('arial', 12, 'normal'), command=genprompt).place(x=142, y=85)

    secroot.mainloop()




root = Tk()

# This is the section of code which creates the main window
root.geometry('722x355')
root.configure(background='#F0F8FF')
root.title('main')


# This is the section of code which creates the a label
Label(root, text='Click on a button', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=344, y=106)


# This is the section of code which creates the a label
Label(root, text='CHATGPT GUI', bg='#F0F8FF', font=('arial', 20, 'normal')).place(x=289, y=15)


# This is the section of code which creates a button
Button(root, text='Image creator', bg='#F0F8FF', font=('arial', 12, 'normal'), command=Imbut).place(x=91, y=229)


# This is the section of code which creates a button
Button(root, text='Story writer', bg='#F0F8FF', font=('arial', 12, 'normal'), command=comptext).place(x=478, y=223)


root.mainloop()
