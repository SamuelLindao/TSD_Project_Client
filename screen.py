import customtkinter as ctk
import datetime
from tkinter import PhotoImage
track_time = 0
WeNeedYou = False


def track_start(button):
    global WeNeedYou
    WeNeedYou = not WeNeedYou
    button.configure(fg_color=("#E0211C" if WeNeedYou == True else "#5CE090"), text=("Stop Track" if WeNeedYou == True else "Track"), hover_color=("#E0211C" if WeNeedYou == True else "#5CE090"))

    print(WeNeedYou)


def update_label(label):
    global track_time
    if WeNeedYou:
        track_time += 1
        hours = track_time // 3600
        minutes = (track_time % 3600)//60
        seconds = track_time % 60
        label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
    label.after(1000, update_label, label)


def create_screen():
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    width_sc = int(app.winfo_screenwidth() * 0.25)
    height_sc = int(app.winfo_screenheight() * 0.70)
    app.geometry(f"{width_sc}x{height_sc}")
    app.title("TSD Client")
    app.configure(bg="#121417")

    print(f"{width_sc}x{height_sc}")

    time_container = ctk.CTkFrame(app)
    time_container.pack(side="top", fill="both", expand=True)
    bottom_container = ctk.CTkFrame(app)
    bottom_container.pack(side="bottom", fill="both", expand=True)
    name_label = ctk.CTkLabel(time_container, text="Tracker", font=("Manrope", 18, "bold"))
    name_label.pack(side="top", pady = 10)
    label = ctk.CTkLabel(time_container, text="00:00:00", font=("Manrope", 54, "bold"))
    label.pack(side="top")
    update_label(label)
    track_button = ctk.CTkButton(bottom_container, text="Track", font=("Manrope", 16), fg_color="#5CE090",width=int(width_sc * 0.55), height=int(height_sc * 0.1),corner_radius=35,  command=lambda: track_start(track_button))
    track_button.pack( side="bottom", pady=15)

    config_button = ctk.CTkButton(time_container, text="", width=25, height=25)
    config_button.place( x=width_sc * 0.05, y=height_sc * 0.05)

    app.resizable(False,False)
    app.mainloop()

