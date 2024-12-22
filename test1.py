import tkinter
import scenic

root = tkinter.Tk()
root.geometry("850x450")
root.title("Test1")

scene1 = scenic.Scene()

scene1["label"] = tkinter.Label(root, text="Hello, World")
scene1["label"].set_mode("pack", anchor="nw")

scene1.load()

root.mainloop()
