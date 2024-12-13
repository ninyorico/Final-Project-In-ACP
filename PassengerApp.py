from binascii import Error
import tkinter as tk
from tkinter import PhotoImage, messagebox
import mysql.connector  # type: ignore

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'bus_management1'  # Change to your database name
DB_USER = 'root'  # Your database username
DB_PASSWORD = 'bancoro6'  # Your database password

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x400")
        self.configure(bg="#F3F3E0")
        self.center_window()
        self.create_widgets()
        
    def center_window(self):
        width = 400
        height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        title_frame = tk.Frame(self, bg="#193E87")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Log In", bg="#193E87", fg="white", font=("Tahoma", 18))
        title_label.pack(side=tk.LEFT, padx=10)

        login_frame = tk.Frame(self, bg="#F3F3E0")
        login_frame.pack(pady=20)

        tk.Label(login_frame, text="Username:", bg="#F3F3E0", font=("Tahoma", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(login_frame, bg="#CBDCEB", font=("Tahoma", 12))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(login_frame, text="Password:", bg="#F3F3E0", font=("Tahoma", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(login_frame, show='*', bg="#CBDCEB", font=("Tahoma", 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = tk.Button(login_frame, text="Login", command=self.login, bg="#608BC1", fg="white", font=("Tahoma", 12))
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        signup_label = tk.Label(self, text="New User? Click Here", fg="blue", cursor="hand2", bg="#F3F3E0", font=("Tahoma", 10))
        signup_label.pack(pady=10)
        signup_label.bind("<Button-1>", self.open_signup)

    def is_user_on_board(self, user_id):
        """Check if the user is currently onboard based on attendance."""
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            cursor = conn.cursor()
            # Query to check the attendance status of the user
            cursor.execute("SELECT attendance FROM passengerinfo WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            if result:
                attendance_status = result[0]
                return attendance_status == 0  # Return True if the user is onboard (attendance = 0)
            else:
                return False  # User not found
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            try:
                conn = mysql.connector.connect(
                    host=DB_HOST,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD
                )
                cursor = conn.cursor()
                cursor.execute("SELECT id FROM user WHERE username=%s AND pass=%s", (username, password))
                result = cursor.fetchone()
                conn.close()

                if result:
                    loggedinid = result[0]  # Get the user ID
                    # Check if user is onboard
                    if self.is_user_on_board(loggedinid):
                        messagebox.showinfo("Login Successful", "You are currently onboard.")
                    else:
                        messagebox.showinfo("Login Successful", "You are not onboard.")

                    messagebox.showinfo("Login Successful", "Welcome!")
                    self.destroy()  # Close the login window
                    passenger_form_window = PassengerFormApp()  # Create an instance of PassengerFormApp
                    passenger_form_window.mainloop()  # Open the CompanyInfos window
                else:
                    messagebox.showerror("Login Failed", "Account does not exist.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            
    def open_signup(self, event):
        self.destroy()
        signup_window = SignupForm()  # Create a new instance of the sign-up window
        signup_window.mainloop()  # Open the sign-up window

class SignupForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign Up")
        self.geometry("400x400")
        self.configure(bg="#F3F3E0")
        self.center_window()
        self.create_widgets()

    def center_window(self):
        width = 400
        height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        title_frame = tk.Frame(self, bg="#193E87")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Sign Up", bg="#193E87", fg="white", font=("Tahoma", 18))
        title_label.pack(side=tk.LEFT, padx=10)

        signup_frame = tk.Frame(self, bg="#F3F3E0")
        signup_frame.pack(pady=20)

        tk.Label(signup_frame, text="Username:", bg="#F3F3E0", font=("Tahoma", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.signup_username_entry = tk.Entry(signup_frame, bg="#CBDCEB", font=("Tahoma", 12))
        self.signup_username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(signup_frame, text="Password:", bg="#F3F3E0", font=("Tahoma", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.signup_password_entry = tk.Entry(signup_frame, show='*', bg="#CBDCEB", font=("Tahoma", 12))
        self.signup_password_entry.grid(row=1, column=1, padx=10, pady=10)

        signup_button = tk.Button(signup_frame, text="Sign Up", command=self.signup, bg="#608BC1", fg="white", font=("Tahoma", 12))
        signup_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        login_label = tk.Label(self, text="Already have an account? Click Here", fg="blue", cursor="hand2", bg="#F3F3E0", font=("Tahoma", 10))
        login_label.pack(pady=10)
        login_label.bind("<Button-1>", self.open_login)

    def signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()

        if username and password:
            try:
                conn = mysql.connector.connect(
                host='localhost',
                database='bus_management1',  # Change to your database name
                user='root',  # Your database username
                password='bancoro6'
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO user (username, pass) VALUES (%s, %s)", (username, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sign Up Successful", "You can now log in.")
                self.open_login(None)  # Redirect to login after successful sign-up
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def open_login(self, event):
        self.destroy()  # Close the sign-up window
        login_window = LoginForm()  # Create a new instance of the login window
        login_window.mainloop()  # Open the login window


class PassengerFormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Passenger Information")
        self.geometry("1541x868")
        self.configure(bg="#F3F3E0")
        self.center_window()
        self.create_widgets()

    def center_window(self):
        width = 1541
        height = 868
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
         # Header Panel
        header_frame = tk.Frame(self, bg="#133E87")
        header_frame.pack(fill=tk.X)

        # Information Label
        info_label = tk.Label(header_frame, text="Kindly input your information below", bg="#133E87", fg="white", font=("Tahoma", 24))
        info_label.pack(pady=10)

        # Main Panel
        main_frame = tk.Frame(self, bg="#F3F3E0")
        main_frame.pack(pady=20)

        # Labels and Entry Fields
        labels = [
            ("Full Name:", "name"),
            ("Age:", "age"),
            ("Personal Contact No.:", "personal_contact"),
            ("Parent's Name:", "parents_name"),
            ("Parents Contact No.:", "parents_contact"),
            ("Bus ID:", "bus_id"),
            ("Seat No.:", "seat_no")
        ]

        self.entries = {}
        for i, (text, key) in enumerate(labels):
            label = tk.Label(main_frame, text=text, bg="#F3F3E0", font=("Tahoma", 18))
            label.grid(row=i, column=0, padx=20, pady=10, sticky="e")  # Align labels to the right

            entry = tk.Entry(main_frame, bg="#CBDCEB", font=("Tahoma", 18))
            entry.grid(row=i, column=1, padx=20, pady=10)  # Align fields to the left
            self.entries[key] = entry  # Store entry in a dictionary for easy access

        # Submit Button
        submit_button = tk.Button(main_frame, text="SUBMIT", command=self.submit_passenger_info, bg="#608BC1", fg="white", font=("Tahoma", 12))
        submit_button.grid(row=len(labels), columnspan=2, pady=20)  # Place below the last input field

        
    def exit_application(self, event):
        self.destroy()

    def minimize_window(self, event):
        self.iconify()

    def submit_passenger_info(self):
        name = self.name_field.get()
        age = self.age_field.get()
        personal_contact = self.personal_contact_field.get()
        parent_name = self.parents_name_field.get()
        parent_contact = self.parents_contact_field.get()
        bus_id = self.bus_id_field.get()
        seat_no = self.seat_number_field.get()

        # Insert passenger data into the SQL database
        try:
            conn = mysql.connector.connect(
                host='localhost',
                database='bus_management1',  # Change to your database name
                user='root',  # Your database username
                password='bancoro6'
                # Your database password
            )
            if conn.is_connected():
                cursor = conn.cursor()
                sql = "INSERT INTO passengerinfo (name, age, contactNumber, parentName, parentContact, seatNo) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (name, age, personal_contact, parent_name, parent_contact, seat_no))
                conn.commit()

                passenger_id = cursor.lastrowid  # Get the generated passenger ID

                if bus_id:
                    bus_sql = "INSERT INTO bus1 (busID, passengerID) VALUES (%s, %s)"
                    cursor.execute(bus_sql, (bus_id, passenger_id))
                    conn.commit()

                messagebox.showinfo("Success", "Passenger added successfully!")
                self.clear_fields()
                # Optionally, open the login form here
                # from login_form import LoginForm
                # login_window = LoginForm()
                # login_window.mainloop()

        except Error as e:
            messagebox.showerror("Error", f"Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def clear_fields(self):
        self.name_field.delete(0, tk.END)
        self.age_field.delete(0, tk.END)
        self.personal_contact_field.delete(0, tk.END)
        self.parents_name_field.delete(0, tk.END)
        self.parents_contact_field.delete(0, tk.END)
        self.bus_id_field.delete(0, tk.END)
        self.seat_number_field.delete(0, tk.END)
        
        
class CompanyInfos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Company Information")
        self.geometry("1540x868")
        self.configure(bg="#F3F3E0")
        self.center_window()
        self.create_widgets()

    def center_window(self):
        width = 1540
        height = 868
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Main Frame
        main_frame = tk.Frame(self, bg="#F3F3E0")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header_frame = tk.Frame(main_frame, bg="#82B4A8")
        header_frame.pack(fill=tk.X)

        # Exit and Minimize Buttons
        exit_button = tk.Label(header_frame, text="X", bg="#FF0000", fg="white", font=("Tahoma", 24))
        exit_button.pack(side=tk.RIGHT, padx=10)
        exit_button.bind("<Button-1>", self.exit_application)

        minimize_button = tk.Label(header_frame, text="-", bg="#FFCC00", fg="white", font=("Tahoma", 24))
        minimize_button.pack(side=tk.RIGHT)
        minimize_button.bind("<Button-1>", self.minimize_window)

        # Company Info Panel
        info_frame = tk.Frame(main_frame, bg="#82B4A8")
        info_frame.pack(pady=20)

        # Company Logo
        try:
            logo_image = PhotoImage(file="C:/Users/banco/Desktop/acp/ACP/bus.png")  # Use absolute path
            logo_label = tk.Label(info_frame, image=logo_image, bg="#82B4A8")
            logo_label.image = logo_image  # Keep a reference to avoid garbage collection
            logo_label.grid(row=0, column=0, padx=10, pady=10)
        except Exception as e:
            print(f"Error loading image: {e}")
            # Optionally, you can show a placeholder image or a message

        # Company Name
        company_name = tk.Label(info_frame, text="Lavera Educations Tours Co.", font=("Calibri", 24), bg="#82B4A8", fg="white")
        company_name.grid(row=0, column=1, padx=10, pady=10)

        # Contact Information
        contact_label = tk.Label(info_frame, text="Contact Us:", font=("Tahoma", 14), bg="#82B4A8", fg="white")
        contact_label.grid(row=1, column=0, columnspan=2, pady=10)

        email_label = tk.Label(info_frame, text="laveratours2006@gmail.com", font=("Calibri", 18), bg="#82B4A8", fg="white")
        email_label.grid(row=2, column=0, columnspan=2)

        phone_label = tk.Label(info_frame, text="09178913571 / 09171555358 / 09665272931", font=("Calibri", 18), bg="#82B4A8", fg="white")
        phone_label.grid(row=3, column=0, columnspan=2)

        # Booking Information
        booking_label = tk.Label(info_frame, text="BOOK NOW!", font=("STHupo", 40), bg="#82B4A8", fg="white")
        booking_label.grid(row=4, column=0, columnspan=2, pady=20)

        address_label = tk.Label(info_frame, text="POBLACION 1, CALACA CITY, BATANGAS", font=("SimSun-ExtB", 26), bg="#82B4A8", fg="white")
        address_label.grid(row=5, column=0, columnspan=2)

        visit_label = tk.Label(info_frame, text="OR VISIT US AT:", font=("STXihei", 26), bg="#82B4A8", fg="white")
        visit_label.grid(row=6, column=0, columnspan=2)

        # Button to go to the login form
        booking_button = tk.Button(info_frame, text="CLICK HERE", command=self.open_login_form, bg="#C2FFC7", fg="#526E48", font=("Tahoma", 14))
        booking_button.grid(row=7, column=0, columnspan=2, pady=20)

        already_booked_label = tk.Label(info_frame, text="Already Booked?", font=("Rockwell", 24), bg="#82B4A8", fg="white")
        already_booked_label.grid(row=8, column=0, columnspan=2)
    def exit_application(self, event):
        self.destroy()

    def minimize_window(self, event):
        self.iconify()

    def open_login_form(self):
        # Assuming loginForm1 is another class you have defined
        login_window = LoginForm()
        login_window.set_location_relative_to(self)
        login_window.mainloop()
        self.destroy()
        
        

if __name__ == "__main__":
    app = LoginForm()
    app.mainloop()