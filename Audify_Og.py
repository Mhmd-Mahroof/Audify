from datetime import *
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askokcancel as oc
from tkinter.messagebox import showinfo as showinfo
from PIL import ImageTk, Image
from pytesseract import pytesseract
import pyttsx3
from gtts import gTTS
import io
from playsound import playsound


ck = 0
w = Tk()
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

# Set the window geometry to fill the screen
w.geometry(f"{screen_width}x{screen_height}+0+0")

w.title('Audify')
w.iconbitmap('img/ico3.ico')
w.resizable(height=True, width=True)
w.bind('<Escape>', lambda e: w.destroy())


def on_closing():
    if oc(title='Exit!!!', message="Do you Want to Quit"):
        w.destroy()


w.protocol("WM_DELETE_WINDOW", on_closing)
# p1 = PhotoImage(file = 'ico2.png')
# w.iconphoto(False,p1)
showinfo(title='About', message='This application Used to Pick the Text Content from An Image and Convert it into Audio')


def open():
    global img
    global filename

    f_types = [('Jpg Files,png Files', '*.jpg *.png'), ('Png Files', '*.png')]
    filename = fd.askopenfilename(filetypes=f_types)
    if len(filename) != 0:
        showinfo(title='Opened File', message=filename)
        img = Image.open(filename)
        img_resized = img.resize((400, 200))
        img = ImageTk.PhotoImage(img_resized)  # file=filename
        l = Label(w, image=img)
        l.place(x=500, y=290)
        global ck
        ck = ck+1

    # b2 =Button
    # (w,image=img) # using Button
    # b2.grid(row=3,column=1)


def audify():
    # We can Implement Audio Playing By Two Methods Either By pyttsx3 (Offline Method)
    # Or gtts module Created By Google (Online Method)
    # Inorder to Playsound in Addition to gtts we should use playsound Module
    # in gtts module Malayalam is supported
    pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    ch = sel()
    if ck == 0:
        messagebox.showerror("Image Undetected",
                             "Please Select an Image Before Use")
    else:

        txt = Label(
            w, )

        b2.place_forget()
        progress = ttk.Progressbar(
            w, orient=HORIZONTAL, length=400, mode='determinate')
        txt.place(x=650, y=530)
        date_string = datetime.now().strftime("%d%m%Y%H%M%S")

        def play():
            playsound(aud)

        if ch == 'ml':
            progress.place(x=500, y=560)
            progress['value'] = 30
            txt['text'] = 'converting', progress['value'], '%'
            showinfo(
                title='Info', message='This App needs Internet Connectivity Make Sure your connected to Internet Before Uploading Image')

            text = pytesseract.image_to_string(filename, lang='Malayalam')
            progress['value'] = 100
            ob = gTTS(text, lang='ml')
            aud = "voice"+date_string+".mp3"
            ob.save(aud)
            txt['text'] = 'converting', progress['value'], '%'
            b2.config(command=play)
            b2.place(x=650, y=600)
        elif ch == 'eng':
            progress.place(x=500, y=560)
            progress['value'] = 30
            txt['text'] = 'converting', progress['value'], '%'
            showinfo(
                title='Info', message='This App needs Internet Connectivity Make Sure your connected to Internet Before Uploading Image')

            text = pytesseract.image_to_string(filename, lang='Malayalam')
            progress['value'] = 100
            ob = gTTS(text)
            aud = "voice"+date_string+".mp3"
            ob.save(aud)
            txt['text'] = 'converting', progress['value'], '%'
            b2.config(command=play)
            b2.place(x=680, y=600)

        else:
            messagebox.showerror("Language Undetected",
                                 "Please Select The Language Before Use")


def sel():
    if (str(v.get()) == '1'):
        return 'ml'
    if (str(v.get()) == '2'):
        return 'eng'


def resize_bg(event):
    global bg_image, bg_photo
    new_width = event.width
    new_height = event.height
    bg_image = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label.config(image=bg_photo)


bg_image = Image.open("img/i1.jpg")


bg_photo = ImageTk.PhotoImage(bg_image)


bg_label = Label(w, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
w.bind('<Configure>', resize_bg)


label = Label(w, text='Select Language Of Image Text:',
              borderwidth=0, highlightthickness=0, border=0)
label.place(x=500, y=160)
label3 = Label(w, text='Select a image File to convert Audio',
               borderwidth=0, highlightthickness=0, border=0)
label3.place(x=500, y=80)
v = IntVar()
rd1 = Radiobutton(w, text="malayalam", variable=v, value='1',
                  command=sel, borderwidth=0, highlightthickness=0, border=0)
rd1.place(x=560, y=185)
rd2 = Radiobutton(w, text="English", variable=v, value='2',
                  command=sel, borderwidth=0, highlightthickness=0, border=0)
rd2.place(x=650, y=185)
b = Button(w, text='Open File', command=open)
b.place(x=600, y=120)
label2 = Label(w, text='Preview of Image:', borderwidth=0,
               highlightthickness=0, border=0)
label2.place(x=500, y=250)
b1 = Button(w, text='Audify', command=audify)
b1.place(x=680, y=495)
b2 = Button(w, text='Play')
w.mainloop()
