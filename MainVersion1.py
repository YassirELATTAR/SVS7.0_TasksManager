import os
import tkinter
import tkinter.messagebox
import customtkinter
import tkinter as tk
from tkinter import filedialog

#Setting the appearance:
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class MyApp(customtkinter.CTk):

    username ="default"
    password = ""
    selected_file =""
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

        self.login_frame = LoginFrame(master=self.home_frame)
        self.login_frame.grid(row=2, column=0, sticky="nsew")
        

        # Directories and Files Manager Frame:
        self.dir_and_files_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.dir_and_files_frame.rowconfigure(2,weight=1)
        self.dir_and_files_frame.columnconfigure(0,weight=1)

        self.dir_and_files_frame_label = customtkinter.CTkLabel(self.dir_and_files_frame,corner_radius=0,fg_color="transparent",text="Welcome to the Directories and Files Manager",font=("Times",16,"bold"))
        self.dir_and_files_frame_label.grid(row=1,column=0,pady=(20,0),sticky="nsew")
        # create tabview
        self.files_dir_tabview = customtkinter.CTkTabview(self.dir_and_files_frame,fg_color="transparent")
        self.files_dir_tabview.columnconfigure(1,weight=1)
        self.files_dir_tabview.grid(row=2, column=0, padx=0, pady=(20, 0), sticky="nsew")
        self.files_dir_tabview.add("Create Folders")
        self.files_dir_tabview.add("Remove Dublicates")
        self.files_dir_tabview.add("Sort by ISP")
        self.files_dir_tabview.add("Files Combiner")

        #Frame for folders creation manager:
        self.create_folders_frame = customtkinter.CTkFrame(self.files_dir_tabview.tab("Create Folders"),fg_color="transparent")
        self.create_folders_frame.rowconfigure(4,weight=1)
        self.create_folders_frame.pack(expand=True)

        self.create_folders_labl = customtkinter.CTkLabel(self.create_folders_frame,text="Enter the names of the folders",font=('Arial',14,"bold"))
        self.create_folders_labl.grid(row=0,pady=(20,10),padx=20,sticky="nw")
        self.folders_names_texbox = customtkinter.CTkTextbox(self.create_folders_frame,width=500)
        self.folders_names_texbox.grid(row=1, padx=20, pady=(20, 0), sticky="nsew")
        self.folders_creation_result_label = customtkinter.CTkLabel(self.create_folders_frame, text="", font=("Arial",12,"italic"))
        self.folders_creation_result_label.grid(row=3,padx=20,pady=(20,10),sticky="nsew")

        self.create_folders_button = customtkinter.CTkButton(self.create_folders_frame, text="Create Folders",width=500,command=self.createFolders)
        self.create_folders_button.grid(row=2, padx=20, pady=(20, 10))

        #Frame for deleting dublicates of lines from a file:
        self.remove_dublicates_frame = customtkinter.CTkFrame(self.files_dir_tabview.tab("Remove Dublicates"),fg_color="transparent")
        self.remove_dublicates_frame.rowconfigure(4,weight=1)
        self.remove_dublicates_frame.columnconfigure(3,weight=1)
        self.remove_dublicates_frame.pack(expand=True)
        self.remove_dubs_title_label = customtkinter.CTkLabel(self.remove_dublicates_frame,text="Enter lines (emails or otherwise) or/and select a file to remove its content:",font=("Arial",12))
        self.remove_dubs_title_label.grid(row=0,columnspan=3, padx=20,pady=(20,0),sticky="nw")
        self.remove_dublicate_textbox = customtkinter.CTkTextbox(self.remove_dublicates_frame,width=600)
        self.remove_dublicate_textbox.grid(row=1, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

        self.select_origin_file_button= customtkinter.CTkButton(self.remove_dublicates_frame, text="Select Original File",width=150,command=self.select_file)
        self.select_origin_file_button.grid(row=2, column=0, padx=0, pady=(20, 10))
        self.select_second_file_button = customtkinter.CTkButton(self.remove_dublicates_frame, text="Select Second File",width=150,command=self.select_file)
        self.select_second_file_button.grid(row=2,column=1,  padx=0, pady=(20, 10))
        self.process_dublicates_button = customtkinter.CTkButton(self.remove_dublicates_frame, text="Remove Dublicates",width=150,command=self.removeDublicates)
        self.process_dublicates_button.grid(row=2,column=2,  padx=0, pady=(20, 10))

        #Frame for sorting list of emails by ISP:
        self.sortby_isp_frame = customtkinter.CTkFrame(self.files_dir_tabview.tab("Sort by ISP"),fg_color="transparent")
        self.sortby_isp_frame.rowconfigure(2,weight=1)
        self.sortby_isp_frame.columnconfigure(2,weight=1)
        self.sortby_isp_frame.pack(expand=True)

        self.sortby_isp_title_label = customtkinter.CTkLabel(self.sortby_isp_frame,text="select a file to split into others according to the ISP",fg_color="transparent",font=("Arial",14,"italic"))
        self.sortby_isp_title_label.grid(row=0,column=0,columnspan=2, padx=10, pady=10, sticky="nw")
        self.sortby_isp_button = customtkinter.CTkButton(self.sortby_isp_frame, text="Remove Dublicates",width=150,command=self.sortbyisp)
        self.sortby_isp_button.grid(row=2,column=1, padx=10, pady=10,sticky="nsew")

        ###GOT TIRED HERE... TO BE FINISHED LATER (review the two options on tabview: remove dubs and sort by isp)
        


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

    # Function to sort a file by ISP:
    def sortbyisp(self):
        pass
    
    # Function to create the folders from a list of names:
    def createFolders(self):
        folder_names = self.folders_names_texbox.get("0.0",customtkinter.END).strip().split('\n')
        folder_to_save = self.getOutputDirectory()
        result = ""
        if folder_to_save != "":
            for fname in folder_names:
                if fname != "":
                    subfolder_path = os.path.join(folder_to_save, f"{fname}")
                    os.makedirs(subfolder_path, exist_ok=True)
                    result = result + " - " + fname
            self.folders_creation_result_label.configure(text=f"Folders '{result}' were created successfully :) ")
        
            
    #Function to reemove dublicates from a file using another file or a list:
    def removeDublicates(self):
        pass

    #Function to get the output directory path:
    def getOutputDirectory(self):
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(title="Select output folder")
        return folder_path
    
    #Function to select a txt file:
    def select_file(self):
        root = tk.Tk()
        root.withdraw()
        #folder_path = filedialog.askdirectory(title="Select Folder Where your emails are saved")
        self.selected_file = filedialog.askopenfilename(title="Select file to process",filetypes=[("Text Files","*.txt"),("All Files","*")])
        return self.selected_file


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



#Class to make the LoginFrame easier and more responsive:
class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color="transparent")

        # Placeholder for login credentials (replace with your authentication logic)

        self.initialize()
    

    def initialize (self):
        self.valid_credentials = {"username": "u", "password": "p"}

        self.username_label = customtkinter.CTkLabel(master=self, text="Username:", font=("Arial", 12))
        self.username_entry = customtkinter.CTkEntry(master=self, width=200)

        self.password_label = customtkinter.CTkLabel(master=self, text="Password:", font=("Arial", 12))
        self.password_entry = customtkinter.CTkEntry(master=self, width=200, show="*")

        self.login_button = customtkinter.CTkButton(master=self, text="Login", command=self.login)

        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=5)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)

        #self.logout_button = customtkinter.CTkButton(master=self, text="Logout", command=self.logout)
        #self.logout_button.pack(pady=10)

        self.tasks_frame = None  # Initialize task frame for later

    def login(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()

        if entered_username == self.valid_credentials["username"] and entered_password == self.valid_credentials["password"]:
            self.show_task_list(tasks= [
            {"name": "Add users", "completed": True},
            {"name": "Clean Bounce", "completed": False},
            {"name": "Create New SMTPs", "completed": True},
            {"name": "Add records", "completed": True},
            {"name": "Initialize domains", "completed": True},
        ])
            self.username_label.configure(text=f"Welcome {entered_username} - Below are your tasks",font=("Times",16))
            self.username_entry.pack_forget()
            self.password_label.pack_forget()
            self.password_entry.pack_forget()
            self.login_button.pack_forget()
            self.logout_button = customtkinter.CTkButton(master=self, text="Logout", command=self.logout)
            self.logout_button.pack(pady=10)
            
        else:
            tkinter.messagebox.showerror("Login Error", "Invalid username or password.")

    def show_task_list(self,tasks):
        if self.tasks_frame is None:
            self.tasks_frame = TaskListFrame(master=self,tasks=tasks)
            self.tasks_frame.tasks=tasks
            self.tasks_frame.pack(padx=(40,20), pady=20,anchor="w")
        else:
            self.tasks_frame.lift()  # Bring task frame to front
    
    def logout(self):
        # Clear existing task frame reference
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()
        self.logout_button.pack_forget()
        self.tasks_frame.pack_forget()
        self.initialize()

#Class to create a frame for the list of tasks:
class TaskListFrame(customtkinter.CTkFrame):
    def __init__(self,tasks, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color="transparent")

        # Placeholder for task list (replace with your task data and display preferences)
        self.tasks = tasks

        self.task_checkboxes = []
        for task in self.tasks:
            task_checkbox = customtkinter.CTkCheckBox(master=self, text=task["name"], font=("Arial", 12))
            task_checkbox.grid(padx=20,pady=(0,20),sticky="nw")
            #task_checkbox.pack()
            self.task_checkboxes.append(task_checkbox)

        # Add checkboxes or other interactive elements as needed



if __name__ == "__main__":
    app = MyApp()
    app.mainloop()