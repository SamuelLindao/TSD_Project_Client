import customtkinter as ctk
import random
import datetime

initial_date = datetime.datetime.now()


def update_label(label):
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
    app.mainloop()
