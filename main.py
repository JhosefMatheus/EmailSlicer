from tkinter import *

window = Tk()

window_width = 600
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

position_x = int(screen_width/2) - int(window_width/2)
position_y = int(screen_height/2) - int(window_height/2)

window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

window["bg"] = "#808080"

email_label = Label(
    window,
    text="Email:",
    font="Arial 12",
    background="#808080"
).place(x=10, y=10)

email_entry = Entry(
    window,
    width=85
).place(x=67, y=13)

password_email_label = Label(
    window,
    text="Senha:",
    font="Arial 12",
    background="#808080"
).place(x=10, y=40)

password_email_entry = Entry(
    window,
    width=85
).place(x=67, y=43)

receiver_email_label = Label(
    window,
    text="Destinatário:",
    font="Arial 12",
    background="#808080"
).place(x=10, y=70)

receiver_email_entry = Entry(
    window,
    width=78
).place(x=107, y=73)

subject_email_label = Label(
    window,
    text="Assunto:",
    font="Arial 12",
    background="#808080"
).place(x=10, y=100)

subject_email_entry = Entry(
    window,
    width=83
).place(x=80, y=103)

body_email_label = Label(
    window,
    text="Mesagem:",
    font="Arial 12",
    background="#808080"
).place(x=10, y=130)

body_email_text = Text(
    window,
    width=60,
    height=26
).place(x=95, y=133)

send_button = Button(
    window,
    text="Enviar",
    font="Arial"
).place(x=521, y=562)

window.mainloop()
