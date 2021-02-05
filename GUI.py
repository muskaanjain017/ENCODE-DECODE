from tkinter import *
import base64

root = Tk()
root.geometry("1545x800")
root.title("Message Encode and Decode")
root.resizable(0,0)
root.configure(background="Plum")

Label(root, text="ENCRYPTION AND DECRYPTION", font = "arial 50 bold", bg="Plum").pack()
Label(root, text="MESSAGE", font = "arial 50 bold", bg="Plum").pack()
Label(root, text="MUSKAAN JAIN", font = "helvetica 30 bold", bg="Plum").pack(side=BOTTOM)

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

def Exit():
    root.destroy()

def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

Label(root, text="MESSAGE", font="arial 20 bold", bg="Plum").place(x=400, y=200)
Entry(root, textvariable = Text, font = "arial 18", width=25, bg="Snow").place(x=800, y=200)

Label(root, text="KEY", font="arial 20 bold", bg="Plum").place(x=400, y=280)
Entry(root, textvariable = private_key, font = "arial 18", width=25, bg="Snow").place(x=800, y=280)

Label(root, text="Mode (e-Encode/d-Decode)", font="arial 20 bold", bg="Plum").place(x=400, y=360)
Entry(root, textvariable = mode, font = "arial 18", width=25, bg="Snow").place(x=800, y=360)

Label(root, text="Result", font="arial 20 bold", bg="Plum").place(x=400, y=440)
Entry(root, textvariable = Result, font = "arial 18", width=25, bg="Snow").place(x=800, y=440)

Button(root, text="Check Result", font="arial 20 bold", bg="Light Green", bd=16, command=Mode).place(x=500, y=550)

Button(root, text="Reset", font="arial 20 bold", bg="Yellow", command=Reset, bd=16 ).place(x=800, y=550)

Button(root, text="Exit", font="arial 20 bold", bg="Red", command=Exit, bd=16 ).place(x=985, y=550)

root.mainloop()