import customtkinter as ctk
import datetime
track_time = 0
WeNeedYou = False


def track_start():
    global WeNeedYou
    WeNeedYou = not WeNeedYou
    print(WeNeedYou)


def update_label(label):
    global track_time
    if WeNeedYou:
        track_time += 1
        horas = track_time // 3600
        minutos = (track_time % 3600)//60
        segundos = track_time % 60
        label.configure(text=f"{horas:02}:{minutos:02}:{segundos:02}")
    label.after(1000, update_label, label)


def create_screen():
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("380x500")
    app.title("TSD Client")
    label = ctk.CTkLabel(app, text="00:00:00", font=("Inter", 54))
    label.pack()
    update_label(label)
    track_button = ctk.CTkButton(app, text="Track", command=track_start)
    track_button.pack()
    app.mainloop()
