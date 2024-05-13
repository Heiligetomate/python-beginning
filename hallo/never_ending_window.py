import tkinter


window = tkinter.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
large = str(width) + "x" + str(height)

tkinter.Label(window, text="Hello World! ", font=('Helvetica bold', 15)).pack(pady=20)

window.geometry(large)

window.attributes('-topmost', True)

window.resizable(False, False)

window.overrideredirect(True)

window.mainloop()

