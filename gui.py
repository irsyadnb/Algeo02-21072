
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ASUS\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#000000")


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

canvas.create_text(
    611.0,
    319.0,
    anchor="nw",
    text="Test Image",
    fill="#000000",
    font=("Audiowide Regular", 32 * -1)
)

canvas.create_text(
    654.0,
    84.0,
    anchor="nw",
    text="Face Recognition",
    fill="#FFFFFF",
    font=("Audiowide Regular", 64 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=162.0,
    y=365.0,
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
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=162.0,
    y=608.0,
    width=187.0,
    height=59.0
)

canvas.create_text(
    1222.0,
    319.0,
    anchor="nw",
    text="Closest Result",
    fill="#000000",
    font=("Audiowide Regular", 32 * -1)
)

canvas.create_text(
    164.0,
    775.0,
    anchor="nw",
    text="Execution Time",
    fill="#FFFFFF",
    font=("Arsenal Regular", 31 * -1)
)

canvas.create_rectangle(
    162.0,
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
window.resizable(False, False)
window.mainloop()