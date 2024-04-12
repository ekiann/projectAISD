from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from time import sleep

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\annae\OneDrive\Desktop\projectAISD\build\assets\frame0")

def button_clicked(image2, image1):
    button.config(image=image2)
    sleep(0.1)
    button.config(image=image1)


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("360x800")
window.configure(bg="#02315D")

canvas = Canvas(
    window,
    bg="#02315D",
    height=800,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
back = round_rectangle(
    40.0,
    180.0,
    320.0,
    620.0,
    fill="#806592",
    outline="")

lock = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    180.0,
    426.0,
    image=lock
)
Password = Entry(
    bd=0,
    bg="#806592",
    fg="#D1D1D1",
    highlightthickness=0,
    font=font.Font(family='Inter', size=12),
    insertbackground="#D1D1D1",
    show="*"

)
Password.place(
    x=113.0,
    y=408.0,
    width=154.0,
    height=36.0
)

canvas.create_rectangle(
    72.0,
    501.0,
    287.0,
    577.0,
    fill="#806592",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_image_2 = PhotoImage(file=relative_to_assets("down_button.png"))

button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#806592",
    background="#806592",
    command=lambda: button_clicked(button_image_2, button_image_1),
    relief="flat"
)


button.place(
    x=81.0,
    y=517.0,
    width=200.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    180.0,
    346.0,
    image=entry_image_2
)
login = Entry(
    bd=0,
    bg="#806592",
    fg="#D1D1D1",
    highlightthickness=0,
    font=font.Font(family='Inter', size=12),
    insertbackground="#D1D1D1"
)
login.place(
    x=113.0,
    y=328.0,
    width=154.0,
    height=36.0
)

canvas.create_text(
    138.0,
    245.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    80.0,
    301.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    80.0,
    381.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    112.0,
    481.0,
    anchor="nw",
    text="Forgot password?",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    100.0,
    346.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    98.0,
    426.0,
    image=image_image_2
)

canvas.create_text(
    120.0,
    338.0,
    anchor="nw",
    text="Type your username",
    fill="#D1D1D1",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    120.0,
    418.0,
    anchor="nw",
    text="Type your password",
    fill="#D1D1D1",
    font=("Inter", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
