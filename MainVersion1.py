import tkinter
import tkinter.messagebox
import customtkinter

#Setting the appearance:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class MyApp(customtkinter.CTk):

    username ="default"
    password = ""
    def __init__(self):
        super().__init__()

        self.title("SVS7 Tasks Manger")
        self.geometry("1000x650")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Navigation Frame",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.dir_files_manger_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Files & Dir Manager",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.dir_files_manger_button_event)
        self.dir_files_manger_button.grid(row=2, column=0, sticky="ew")

        self.bounce_management_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Bounce Manager",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.bounce_management_button_event)
        self.bounce_management_button.grid(row=3, column=0, sticky="ew")

        self.smtps_manager_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="SMTPs Manager",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.smtps_manager_button_event)
        self.smtps_manager_button.grid(row=4, column=0, sticky="ew")

        self.add_namecheap_records_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add Records to NC",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.add_namecheap_records_button_event)
        self.add_namecheap_records_button.grid(row=5, column=0, sticky="ew")

        self.ms_accounts_manager_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="MS Accounts (PS)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                       anchor="w", command=self.ms_accounts_manager_button_event)
        self.ms_accounts_manager_button.grid(row=6, column=0, sticky="ew")

        #Creating Home Frame:
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(2, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="Home Sweet Home")
        self.home_frame_large_image_label.grid(row=1, column=0, padx=20, pady=10)

        self.login_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0,fg_color="white")
        self.login_frame.grid(row=2,column=0,sticky="nsew")

        # Directories and Files Manager Frame:
        self.dir_and_files_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="yellow")

        # Bounce Manager Frame:
        self.bounce_management_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="red")

        # Bounce Manager Frame:
        self.smtp_manager_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="blue")

        # Add records to namecheap Frame:
        self.add_namecheap_records_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="purple")

        # Microsoft Accounts Manager
        self.ms_accounts_manager_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="green")

        #Select default frame: Home
        self.select_frame_by_name("home")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.dir_files_manger_button.configure(fg_color=("gray75", "gray25") if name == "dir_and_files_frame" else "transparent")
        self.bounce_management_button.configure(fg_color=("gray75", "gray25") if name == "bounce_management_frame" else "transparent")
        self.smtps_manager_button.configure(fg_color=("gray75", "gray25") if name == "smtp_manager_frame" else "transparent")
        self.add_namecheap_records_button.configure(fg_color=("gray75", "gray25") if name == "add_namecheap_records_frame" else "transparent")
        self.ms_accounts_manager_button.configure(fg_color=("gray75", "gray25") if name == "ms_accounts_manager_frame" else "transparent")

        #Show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "dir_and_files_frame":
            self.dir_and_files_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.dir_and_files_frame.grid_forget()
        if name == "bounce_management_frame":
            self.bounce_management_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.bounce_management_frame.grid_forget()
        if name == "smtp_manager_frame":
            self.smtp_manager_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.smtp_manager_frame.grid_forget()
        if name == "add_namecheap_records_frame":
            self.add_namecheap_records_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.add_namecheap_records_frame.grid_forget()
        if name == "ms_accounts_manager_frame":
            self.ms_accounts_manager_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ms_accounts_manager_frame.grid_forget()

    #Navigation Functions for the buttons:
    def home_button_event(self):
        self.select_frame_by_name("home")

    def dir_files_manger_button_event(self):
        self.select_frame_by_name("dir_and_files_frame")

    def bounce_management_button_event(self):
        self.select_frame_by_name("bounce_management_frame")

    def smtps_manager_button_event(self):
        self.select_frame_by_name("smtp_manager_frame")
    def add_namecheap_records_button_event(self):
        self.select_frame_by_name("add_namecheap_records_frame")
    def ms_accounts_manager_button_event(self):
        self.select_frame_by_name("ms_accounts_manager_frame")


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()