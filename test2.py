import customtkinter as ttk
import scenic

root = ttk.CTk()
root.geometry("850x450")
root.title("Test2")


def next_scene() -> None:
    scene1.unload()
    scene2.load()


def reset(_event) -> None:
    scene1["label"].widget.configure(True, text=scene1["entry"].widget.get())


scene1 = scenic.Scene()
scene1["label"] = ttk.CTkLabel(root, text="Hello, World!")
scene1["label"].set_mode("pack", padx=5, pady=5, anchor="nw")

scene1["entry"] = ttk.CTkEntry(root)
scene1["entry"].set_mode("pack", anchor="nw", fill="x", expand=True)
scene1["entry"].widget.bind("<Return>", reset)

scene1["button"] = ttk.CTkButton(root, text="Next", command=next_scene)
scene1["button"].set_mode("pack")

scene2 = scenic.Scene()
scene2["label"] = ttk.CTkLabel(root, text="Thanks for the input!")
scene2["label"].set_mode("pack", fill="both", expand=True)

scene1.load()

root.mainloop()
