from cProfile import label
from tkinter import *
import tkinter.font as tkFont
import random
import time

students = {
    1:"강민철",
    2:"강우빈",
    3:"김도균",
    4:"김시환",
    5:"김의태",
    6:"김하준",
    7:"노우진",
    8:"박준상",
    9:"박현욱",
    10:"오형택",
    11:"이강민",
    12:"이건우",
    13:"이동현",
    14:"이원대",
    15:"이장원",
    16:"이찬빈",
    17:"이충민",
    18:"정민혁",
    19:"정세헌",
    20:"정찬웅",
    21:"조계헌",
    22:"최우혁",
    23:"홍수호",
    24:"황유빈"
}

student_num = list(students.keys())

root = Tk()
root.title("Nado GUI")
#root.geometry("1920x1080")
root.attributes("-fullscreen", True)
root.resizable(False, False) 
fontStyle = tkFont.Font(family="Lucida Grande", size=32)

wall = PhotoImage(file="wall.png")
wall_label = Label(image=wall).place(x = 0, y = 0)

label1 = Label(root, text="1", font=fontStyle, bg="white")
label1.place(x = 307, y = 205)
label2 = Label(root, text="2", font=fontStyle, bg="white")
label2.place(x = 587, y = 205)
label3 = Label(root, text="3", font=fontStyle, bg="white")
label3.place(x = 860, y = 205)
label4 = Label(root, text="4", font=fontStyle, bg="white")
label4.place(x = 1130, y = 205)
label5 = Label(root, text="5", font=fontStyle, bg="white")
label5.place(x = 1400, y = 205)

label6 = Label(root, text="6", font=fontStyle, bg="white")
label6.place(x = 307, y = 355)
label7 = Label(root, text="7", font=fontStyle, bg="white")
label7.place(x = 587, y = 355)
label8 = Label(root, text="8", font=fontStyle, bg="white")
label8.place(x = 860, y = 355)
label9 = Label(root, text="9", font=fontStyle, bg="white")
label9.place(x = 1130, y = 355)
label10 = Label(root, text="10", font=fontStyle, bg="white")
label10.place(x = 1400, y = 355)

label11 = Label(root, text="11", font=fontStyle, bg="white")
label11.place(x = 307, y = 513)
label12 = Label(root, text="12", font=fontStyle, bg="white")
label12.place(x = 587, y = 513)
label13 = Label(root, text="13", font=fontStyle, bg="white")
label13.place(x = 860, y = 513)
label14 = Label(root, text="14", font=fontStyle, bg="white")
label14.place(x = 1130, y = 513)
label15 = Label(root, text="15", font=fontStyle, bg="white")
label15.place(x = 1400, y = 513)

label16 = Label(root, text="16", font=fontStyle, bg="white")
label16.place(x = 307, y = 670)
label17 = Label(root, text="17", font=fontStyle, bg="white")
label17.place(x = 587, y = 670)
label18 = Label(root, text="18", font=fontStyle, bg="white")
label18.place(x = 860, y = 670)
label19 = Label(root, text="19", font=fontStyle, bg="white")
label19.place(x = 1130, y = 670)
label20 = Label(root, text="20", font=fontStyle, bg="white")
label20.place(x = 1400, y = 670)

label21 = Label(root, text="21", font=fontStyle, bg="white")
label21.place(x = 307, y = 840)
label22 = Label(root, text="22", font=fontStyle, bg="white")
label22.place(x = 587, y = 840)
label23 = Label(root, text="23", font=fontStyle, bg="white")
label23.place(x = 860, y = 840)
label24 = Label(root, text="24", font=fontStyle, bg="white")
label24.place(x = 1130, y = 840)



def btn_start_cmd():
    random.shuffle(student_num)
    print(student_num)

    label1.config(text=str(students[student_num[0]]) + "(" + str(student_num[0]) +")")
    label2.config(text=str(students[student_num[1]]) + "(" + str(student_num[1]) +")")
    label3.config(text=str(students[student_num[2]]) + "(" + str(student_num[2]) +")")
    label4.config(text=str(students[student_num[3]]) + "(" + str(student_num[3]) +")")
    label5.config(text=str(students[student_num[4]]) + "(" + str(student_num[4]) +")")
    label6.config(text=str(students[student_num[5]]) + "(" + str(student_num[5]) +")")
    label7.config(text=str(students[student_num[6]]) + "(" + str(student_num[6]) +")")
    label8.config(text=str(students[student_num[7]]) + "(" + str(student_num[7]) +")")
    label9.config(text=str(students[student_num[8]]) + "(" + str(student_num[8]) +")")
    label10.config(text=str(students[student_num[9]]) + "(" + str(student_num[9]) +")")
    label11.config(text=str(students[student_num[10]]) + "(" + str(student_num[10]) +")")
    label12.config(text=str(students[student_num[11]]) + "(" + str(student_num[11]) +")")
    label13.config(text=str(students[student_num[12]]) + "(" + str(student_num[12]) +")")
    label14.config(text=str(students[student_num[13]]) + "(" + str(student_num[13]) +")")
    label15.config(text=str(students[student_num[14]]) + "(" + str(student_num[14]) +")")
    label16.config(text=str(students[student_num[15]]) + "(" + str(student_num[15]) +")")
    label17.config(text=str(students[student_num[16]]) + "(" + str(student_num[16]) +")")
    label18.config(text=str(students[student_num[17]]) + "(" + str(student_num[17]) +")")
    label19.config(text=str(students[student_num[18]]) + "(" + str(student_num[18]) +")")
    label20.config(text=str(students[student_num[19]]) + "(" + str(student_num[19]) +")")
    label21.config(text=str(students[student_num[20]]) + "(" + str(student_num[20]) +")")
    label22.config(text=str(students[student_num[21]]) + "(" + str(student_num[21]) +")")
    label23.config(text=str(students[student_num[22]]) + "(" + str(student_num[22]) +")")
    label24.config(text=str(students[student_num[23]]) + "(" + str(student_num[23]) +")")

btn_start_photo = PhotoImage(file="button_start_image.png")
btn_start = Button(root, image=btn_start_photo, command=btn_start_cmd).place(x=760, y=950)

btn_exit_photo = PhotoImage(file="button_exit_image.png")
btn_exit = Button(root, image=btn_exit_photo, command=root.quit).place(x=980, y=950) 



root.mainloop()

