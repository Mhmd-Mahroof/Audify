from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import askokcancel as oc
from tkinter.messagebox import showinfo as showinfo
from PIL import ImageTk,Image
from pytesseract import pytesseract
import pyttsx3
from gtts import gTTS
import io 
from playsound import playsound

w=Tk()
w.state('zoomed')

w.title('Audify')
w.iconbitmap('img\ico3.ico')
w.resizable(False,False)
w.bind('<Escape>', lambda e: w.destroy())
def on_closing():
    if oc(title='Exit!!!',message="Do you Want to Quit"):
        w.destroy()


w.protocol("WM_DELETE_WINDOW",on_closing)
# p1 = PhotoImage(file = 'ico2.png')   
# w.iconphoto(False,p1)
showinfo(title='About',message='This application Used to Pick the Text Content from An Image and Convert it into Audio')

def open():
    global img
    global filename
    f_types = [('Jpg Files', '*.jpg'),('Png Files','*.png')]
    filename = fd.askopenfilename(filetypes=f_types)
    showinfo(title='Opened File',message=filename)
    img=Image.open(filename)
    img_resized=img.resize((400,200))
    img = ImageTk.PhotoImage(img_resized)     #file=filename
 
    l=Label(w,image=img)
    l.place(x=500,y=200)
    # b2 =Button(w,image=img) # using Button 
    # b2.grid(row=3,column=1)
   
def audify():
    #We can Implement Audio Playing By Two Methods Either By pyttsx3 (Offline Method)
    #Or gtts module Created By Google (Online Method) 
    #Inorder to Playsound in Addition to gtts we should use playsound Module
    #in gtts module Malayalam Is supported
    pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(filename)
    ob=gTTS(text)
    ob.save("aud.mp3")
    playsound("aud.mp3")
    
    # engine=pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
def sel():
    if(str(v.get())=='1'):
        showinfo(title='Info',message='')
    if(str(v.get())=='2'):
        showinfo(title='Info',message='English Supports Offline Mode')
def resize_bg(event):
    global bg_image, bg_photo
    new_width = event.width
    new_height = event.height
    bg_image = bg_image.resize((new_width, new_height),Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label.config(image=bg_photo)

# Bind the resize event to the resize_bg function
w.bind('<Configure>', resize_bg)    


bg_image = Image.open("img\i1.jpg")
bg_image = bg_image.resize((500, 500), Image.LANCZOS)

# Create a PhotoImage object from the resized image
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget with the PhotoImage as its background image
bg_label = Label(w, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
label=Label(w,text='Select Language Of Image Text:')
label.place(x=500,y=30)
label3=Label(w,text='Select a image File to convert Audio')
label3.place(x=500,y=80)
v = IntVar()
rd1=Radiobutton(w,text="malayalam",variable=v,value='1',command=sel)
rd1.place(x=560,y=55)
rd2=Radiobutton(w,text="English",variable=v,value='2',command=sel)
rd2.place(x=650,y=55)
b=Button(w,text='Open File',command=open)
b.place(x=600,y=120)
label2=Label(w,text='Preview of Image:')
label2.place(x=500,y=170)
b1=Button(w,text='Audify',command=audify)
b1.place(x=680,y=400)
w.mainloop()