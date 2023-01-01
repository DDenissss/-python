import os
import random
import time
from tkinter import *
from tkinter import messagebox
import keyboard

root = Tk()

def Quit():
    pass

def destroy_text():
    text_1_line.place_forget()
    text_2_line.place_forget()
    text_3_line.place_forget()
    text1.place_forget()
    text2.place_forget()
    text3.place_forget()
    text4.place_forget()

def one():
    destroy_text()
    replace_text1 = Label(text="Молодец правильно!", font=("Arial", 50),
                         bg="black",
                         fg="red")
    replace_text1.place(relx=0.22,
                       rely=0.15)
    time.sleep(1)
    replace_text1.place_forget()
    replace_text2 = Label(text="Но этот комп", font=("Arial", 50),
                         bg="black",
                         fg="red")
    replace_text2.place(relx=0.05,
                       rely=0.15)

    replace_text3 = Label(text="Все равно уничтожится", font=("Arial", 50),
                         bg="black",
                         fg="red")
    replace_text3.place(relx=0.05,
                       rely=0.19)
    time.sleep(2)
    replace_text3.place_forget()
    replace_text2.place_forget()

    timer1 = Label(text="5", font=("Arial", 50, "bold"),
                  bg="black",
                  fg="red")
    timer1.place(relx=0.3,
                rely=0.15)
    time.sleep(1)
    timer1.place_forget()
    timer2 = Label(text="4", font=("Arial", 50, "bold"),
                  bg="black",
                  fg="red")
    timer2.place(relx=0.3,
                rely=0.15)
    time.sleep(1)
    timer2.place_forget()
    timer3 = Label(text="3", font=("Arial", 50, "bold"),
                  bg="black",
                  fg="red")
    timer3.place(relx=0.3,
                rely=0.15)
    time.sleep(1)
    timer3.place_forget()
    timer4 = Label(text="2", font=("Arial", 50, "bold"),
                  bg="black",
                  fg="red")
    timer4.place(relx=0.3,
                rely=0.15)
    time.sleep(1)
    timer4.place_forget()
    timer5 = Label(text="1", font=("Arial", 50, "bold"),
                  bg="black",
                  fg="red")
    timer5.place(relx=0.3,
                rely=0.15)
    time.sleep(1)
    timer5.place_forget()
    timer6 = Label(text="0", font=("Arial", 50, "bold"),
                  bg="black",
                  fg="red")
    timer6.place(relx=0.3,
                rely=0.15)
    
    os.system("shutdown /r /t 0")


def two():
    one()

def three():
    one()
    
def four():
    one()

root.protocol("WM_DELETE_WINDOW", Quit)
root["bg"] = "black"
root.title("One programm")
root.wm_attributes("-alpha", 2)
root.overrideredirect(1)
root.geometry("2000x2000")
root.attributes("-topmost", True)

keyboard.add_hotkey("1", lambda: one())
keyboard.add_hotkey("2", lambda: two())
keyboard.add_hotkey("3", lambda: three())
keyboard.add_hotkey("4", lambda: four())


text_1_line = Label(text="В чем смысл жизни?", font=("Arial", 60),
             bg="black",
             fg="red")
text_1_line.place(relx=0.06)

text_2_line = Label(text="Неправельный ответ приведет", font=("Arial", 60),
             bg="black",
             fg="red")
text_2_line.place(relx=0.03,
           rely=0.04)

text_3_line = Label(text="к уничтожению", font=("Arial", 60),
             bg="black",
             fg="red")
text_3_line.place(relx=0.03,
           rely=0.08)

text1 = Label(text="1: Коты", font=("Arial", 50),
             bg="black",
             fg="red")
text1.place(relx=0.06,
           rely=0.14)

text2 = Label(text="2: Кушать", font=("Arial", 50),
             bg="black",
             fg="red")
text2.place(relx=0.06,
           rely=0.18)

text3 = Label(text="3: Спать", font=("Arial", 50),
             bg="black",
             fg="red")
text3.place(relx=0.06,
           rely=0.22)

text4 = Label(text="4: Ни один из перечисленных", font=("Arial", 50),
             bg="black",
             fg="red")
text4.place(relx=0.06,
           rely=0.26)


root.mainloop()
