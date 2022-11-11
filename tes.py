import tkinter as tk

window=tk.Tk()
greeting = label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
    )
greeting.pack()
window.mainloop()