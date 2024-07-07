# screen.py
import tkinter as tk
import customtkinter as ctk
import datetime


class TSDClientApp:
    def __init__(self, root):
        self.root = root
        self.track_time = 0
        self.WeNeedYou = False
        self.list_box = None
        self.create_screen()

    def track_start(self, button):
        self.WeNeedYou = not self.WeNeedYou
        button.configure(
            fg_color=("#E0211C" if self.WeNeedYou else "#5CE090"),
            text=("Stop Track" if self.WeNeedYou else "Track"),
            hover_color=("#E0211C" if self.WeNeedYou else "#5CE090")
        )

    def update_label(self, label):
        if self.WeNeedYou:
            self.track_time += 1
            hours = self.track_time // 3600
            minutes = (self.track_time % 3600) // 60
            seconds = self.track_time % 60
            label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        label.after(1000, self.update_label, label)

    def font_size(self, width, constant):
        return int(width / constant)

    def create_screen(self):
        ctk.set_default_color_theme("dark-blue")
        width_sc = int(self.root.winfo_screenwidth() * 0.25)
        height_sc = int(self.root.winfo_screenheight() * 0.70)
        self.root.geometry(f"{width_sc}x{height_sc}")
        self.root.title("TSD Client")
        self.root.configure(fg_color="#121417")

        time_container = ctk.CTkFrame(self.root, fg_color="#121417")
        time_container.pack(side="top", fill="both", expand=True)

        self.list_box = ctk.CTkScrollableFrame(
            self.root, fg_color="#121417", label_text="Last Track",
            label_font=("Manrope", self.font_size(width_sc, 20)),
            label_fg_color="#121417"
        )
        self.list_box.pack(side="top", fill="both", expand=True)

        bottom_container = ctk.CTkFrame(self.root, fg_color="#121417")
        bottom_container.pack(side="bottom", fill="both", expand=True)

        name_label = ctk.CTkLabel(time_container, text="Tracker",
                                  font=("Manrope", self.font_size(width_sc, 16), "bold"))
        name_label.pack(side="top", pady=25)

        label = ctk.CTkLabel(time_container, text="00:00:00", font=("Manrope", self.font_size(width_sc, 7), "bold"))
        label.pack(side="top")
        self.update_label(label)

        track_button = ctk.CTkButton(
            bottom_container, text="Track", font=("Manrope", self.font_size(width_sc, 22), "bold"),
            text_color="#121417", fg_color="#5CE090", width=int(width_sc * 0.55),
            height=int(height_sc * 0.1), corner_radius=35,
            command=lambda: self.track_start(track_button)
        )
        track_button.pack(side="bottom", pady=25)

        config_button = ctk.CTkButton(time_container, text="", width=25, height=25)
        config_button.place(x=width_sc * 0.05, y=height_sc * 0.05)

        self.root.resizable(False, False)

    def track_add(self, text):
        if self.list_box is not None:
            history_frame = ctk.CTkFrame(self.list_box, fg_color="#121417")
            history_frame.pack(fill="x", expand=True)

            history_frame.grid_columnconfigure(0, weight=1)
            history_frame.grid_columnconfigure(1, weight=1)
            history_frame.grid_columnconfigure(2, weight=1)

            hours = self.track_time // 3600
            minutes = (self.track_time % 3600) // 60
            seconds = self.track_time % 60

            text_track = ctk.CTkLabel(history_frame, text="",
                                      font=("Manrope", self.font_size(int(self.root.winfo_screenwidth() * 0.25), 25)))
            text_track.grid(column=2, row=0, sticky="s")
            text_track.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

            text_date = ctk.CTkLabel(history_frame, text="",
                                     font=("Manrope", self.font_size(int(self.root.winfo_screenwidth() * 0.25), 25)))
            text_date.grid(row=0, column=0, sticky="w", padx=30)
            text_date.configure(text=str(datetime.datetime.now().date()).replace("-", "/"))

            text_values = ctk.CTkLabel(history_frame, text=text,
                                       font=("Manrope", self.font_size(int(self.root.winfo_screenwidth() * 0.25), 30)))
            text_values.grid(row=1, column=0, sticky="w", padx=30)


def create_app():
    root = ctk.CTk()
    root.iconbitmap("Icon.ico")
    icon = tk.PhotoImage(file="WorkClockIcon.png")
    root.iconphoto(True, icon, icon)
    app = TSDClientApp(root)
    return app, root
