import customtkinter as ctk
import datetime
initial_date = datetime.datetime.now()

WeNeedYou = True


def track_start():
    global WeNeedYou
    WeNeedYou = not WeNeedYou


def update_label(label):
    if WeNeedYou:
        new_time = datetime.datetime.now().replace(microsecond=0) - initial_date.replace(microsecond=0)
        label.configure(text=str(new_time))
        label.after(1000, update_label, label)


def create_screen():
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("380x500")
    app.title("TSD Client")
    label = ctk.CTkLabel(app, text="CTkLabel", font=("Inter", 54))
    label.pack()
    update_label(label)
    track_button = ctk.CTkButton(app, text="Track", command=track_start)
    track_button.pack()
    app.mainloop()
