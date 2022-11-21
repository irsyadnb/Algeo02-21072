
from pathlib import Path

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import time
import main

window = Tk()

window.configure(bg = "#000000")
window.geometry("1920x1080")
window.resizable(False, False)
window.title("Face Recognition")

running = False
# time variables initially set to 0
hours, minutes, seconds, ms = 0, 0, 0, 0

def start():
    global running
    pause()
    if not running:
        reset()
        update()
        running = True
        #ada prosedur eigen
        imgoutputmmain=main.mainprog(img1txt.get(),path1.get())
        imgoutput.set(imgoutputmmain)
        img_fotooutput=Image.open(imgoutput.get()).resize((500,500))
        img_fotooutput=ImageTk.PhotoImage(img_fotooutput)
        img_label2.configure(image=img_fotooutput)
        img_label2.image=img_fotooutput
        print(imgoutput.get())
        pause()

def pause():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # set variables back to zero
    global hours, minutes, seconds, ms
    hours, minutes, seconds,ms = 0, 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='0.000')
    

def update():
    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds, ms
    ms+=1
    if ms == 1000:
        seconds += 1
        ms=0
    if seconds == 60:
        minutes += 1
        seconds = 0
    # if minutes == 60:
    #     hours += 1
    #     minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}'
    ms_string = f'{ms}' if ms > 99 else f'0{ms}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text= seconds_string + '.' + ms_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1, update)




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(".\\assets\\frame0")

img1= StringVar()
img1.set("")

img1txt= StringVar()
img1txt.set("")

path1=StringVar()
path1.set("")

imgoutput=StringVar()
imgoutput.set("")

img1input=StringVar()
img1input.set("")

path1main=StringVar()
img1input.set("")

img1inputtxt=StringVar()
img1input.set("")

img_label2=StringVar()
img_label2.set("")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open():
    img1filename=filedialog.askopenfilename(initialdir=".\\Algeo02-21072",title="Choose file",filetypes=(("jpg files","*.jpg"),("all files","*.*")))

    if (img1filename):
        img1txt.set(img1filename)
        img1inputtxt.set(img1filename)
        img1.set(img1filename)
        img_foto=Image.open(img1.get()).resize((500,500))
        img_foto=ImageTk.PhotoImage(img_foto)
        img_label.configure(image=img_foto)
        img_label.image=img_foto
        
        img1txtlabel=img1txt.get()
        
        img1labeltxt.configure(text=img1txtlabel)
        img1labeltxt.text=img1txtlabel
        
    
        # img1input.configure(text=img1inputtxt.get())
        # img1input.text=img1inputtxt.get()
    
     

def opendir():
    path1name=filedialog.askdirectory(initialdir=".\\Algeo02-21072",title="Choose file")

    if (path1name):
        path1.set(path1name)
        
        temp=path1.get()
        
        path1label.configure(text= temp)
        path1label.text=temp
        
        # path1main.configure(text= temp)
        # path1main.text=temp
        
        
        
def get_time():
    timeVar=time.strftime("%I : %M : %S %p")
    clock.config(text=timeVar)
    clock.after(500,get_time)
    
    
    
# img_fotooutput=Image.open(imgoutput.get()).resize((500,500))
# img_fotooutput=ImageTk.PhotoImage(img_fotooutput)
# img_label2.configure(image=img_fotooutput)
# img_label2.image=img_fotooutput

canvas = Canvas(
    window,
    bg = "#000000",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

img1labeltxt=Label(canvas, font=("Arial",14),fg="white" ,bg="#181818",width=400,anchor="e")
img1labeltxt.place( x=75.0, y=660.0,width=400) 

img_label=Label(canvas,width=500,height=500)
img_label.place(x=611,y=385,width=512,height=512)

img_label2=Label(canvas,width=500,height=500)
img_label2.place(x=1011,y=385,width=512,height=512)

stopwatch_label = Label(text='', font=('Audiowide Regular', 25), fg="white" , bg="#181818" ,width=300,anchor='center')
stopwatch_label.place( x=122.0, y=838.0,width=300)    

clock=Label(canvas,font=("Arial",18),bg="#181818" , fg="white")
clock.place( x=1684.0, y=1000.0)

path1label=Label(canvas,font=("Arial",14),fg="white" ,bg="#181818",width=400,anchor="e")
path1label.place(x=75.0, y=420.0,width=400)


get_time()
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    540.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1165.0,
    599.0,
    image=image_image_2
)

# canvas.create_text(
#     611.0,
#     319.0,
#     anchor="nw",
#     text="Test Image",
#     fill="#000000",
#     font=("Audiowide Regular", 32 * -1)
# )

# canvas.create_text(
#     654.0,
#     84.0,
#     anchor="nw",
#     text="Face Recognition",
#     fill="#FFFFFF",
#     font=("Audiowide Regular", 72 * -1,"bold","underline")
# )

Ti = PhotoImage(
    file=relative_to_assets("Test_Image.png"))
image_6 = canvas.create_image(
    704.0,
    349.0,
    image=Ti
)


Fr = PhotoImage(
    file=relative_to_assets("Face_Recognition.png"))
image_5 = canvas.create_image(
    954.0,
    140.0,
    image=Fr
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= opendir,
    relief="flat"
)
button_1.place(
    x=172.0,
    y=350.0,
    width=187.0,
    height=59.0
)

canvas.create_text(
    87.0,
    298.0,
    anchor="nw",
    text="INSERT YOUR DATASET",
    fill="#FFFFFF",
    font=("Armata Regular", 31 * -1)
)

canvas.create_text(
    110.0,
    535.0,
    anchor="nw",
    text="INSERT YOUR IMAGE",
    fill="#FFFFFF",
    font=("Armata Regular", 31 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open,
    relief="flat"
)
button_2.place(
    x=172.0,
    y=588.0,
    width=187.0,
    height=59.0
)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command= start,
    relief="flat"
)
button_3.place(
    x=612.0,
    y=914.0,
    width=109.0,
    height=27.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command= pause,
    relief="flat"
)
button_4.place(
    x=742.0,
    y=914.0,
    width=109.0,
    height=27.0
)

# canvas.create_text(
#     1222.0,
#     319.0,
#     anchor="nw",
#     text="Closest Result",
#     fill="#000000",
#     font=("Audiowide Regular", 32 * -1)
# )

Cr = PhotoImage(
    file=relative_to_assets("Closest_Result.png"))
image_7 = canvas.create_image(
    1354.0,
    344.0,
    image=Cr
)

# canvas.create_text(
#     164.0,
#     775.0,
#     anchor="nw",
#     text="Execution Time",
#     fill="#FFFFFF",
#     font=("Arsenal Regular", 31 * -1)
# )

Et = PhotoImage(
    file=relative_to_assets("Execution_Time.png"))
image_8 = canvas.create_image(
    270.0,
    790.0,
    image=Et
)

canvas.create_rectangle(
    183.0,
    887.0,
    356.0,
    897.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    867.0,
    641.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1478.0,
    641.0,
    image=image_image_4
)

window.mainloop()
