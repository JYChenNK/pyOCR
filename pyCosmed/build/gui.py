
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("600x300")
window.configure(bg = "#E8EAF6")


canvas = Canvas(
    window,
    bg = "#E8EAF6",
    height = 300,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    23.0,
    11.0,
    374.0,
    79.0,
    fill="#C5CAE9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    198.5,
    225.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#C5CAE9",
    highlightthickness=0
)
entry_1.place(
    x=28.0,
    y=161.0,
    width=341.0,
    height=126.0
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
    x=311.0,
    y=35.0,
    width=20.0,
    height=20.0
)

canvas.create_text(
    339.0,
    35.0,
    anchor="nw",
    text="HR",
    fill="#111111",
    font=("Ubuntu Regular", 16 * -1)
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
    x=230.0,
    y=35.0,
    width=20.0,
    height=20.0
)

canvas.create_text(
    258.0,
    35.0,
    anchor="nw",
    text="VE",
    fill="#111111",
    font=("Ubuntu Regular", 16 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=128.0,
    y=35.0,
    width=20.0,
    height=20.0
)

canvas.create_text(
    156.0,
    35.0,
    anchor="nw",
    text="VCO2",
    fill="#111111",
    font=("Ubuntu Regular", 16 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=35.0,
    y=35.0,
    width=20.0,
    height=20.0
)

canvas.create_text(
    63.0,
    35.0,
    anchor="nw",
    text="VO2",
    fill="#111111",
    font=("Ubuntu Regular", 16 * -1)
)

canvas.create_text(
    403.0,
    55.0,
    anchor="nw",
    text="Cosmed RT-OCR",
    fill="#064EE8",
    font=("Ubuntu Regular", 24 * -1)
)

canvas.create_text(
    433.0,
    25.0,
    anchor="nw",
    text="102Lab",
    fill="#064EE8",
    font=("Ubuntu Regular", 36 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=403.0,
    y=91.0,
    width=175.0,
    height=58.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=403.0,
    y=161.0,
    width=175.0,
    height=58.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=403.0,
    y=231.0,
    width=175.0,
    height=58.0
)

canvas.create_rectangle(
    31.0,
    90.0,
    101.0,
    120.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    120.0,
    90.0,
    190.0,
    120.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    205.0,
    91.0,
    275.0,
    121.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    294.0,
    90.0,
    364.0,
    120.0,
    fill="#FFFFFF",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    66.0,
    139.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E8EAF6",
    highlightthickness=0
)
entry_2.place(
    x=31.0,
    y=127.0,
    width=70.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    155.0,
    140.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#E8EAF6",
    highlightthickness=0
)
entry_3.place(
    x=120.0,
    y=128.0,
    width=70.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    240.0,
    139.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#E8EAF6",
    highlightthickness=0
)
entry_4.place(
    x=205.0,
    y=127.0,
    width=70.0,
    height=23.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    329.0,
    139.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E8EAF6",
    highlightthickness=0
)
entry_5.place(
    x=294.0,
    y=127.0,
    width=70.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()
