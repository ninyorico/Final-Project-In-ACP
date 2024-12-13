import tkinter as tk
from tkinter import messagebox
import mysql.connector  # type: ignore
from tkinter import ttk

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'bus_management1'  # Change to your database name
DB_USER = 'root'  # Your database username
DB_PASSWORD = 'bancoro6'  # Your database password

class TourGuideLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tour Guide Login")
        self.geometry("400x400")
        self.configure(bg="#F3F3E0")
        self.center_window()
        self.create_widgets()
        
    def center_window(self):
        # Get the dimensions of the window
        width = 400
        height = 400

        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the geometry of the window
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Title Bar
        title_frame = tk.Frame(self, bg="#193E87")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Log In", bg="#193E87", fg="white", font=("Tahoma", 18))
        title_label.pack(side=tk.LEFT, padx=10)

        # Login Frame
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

        # New User Link
        signup_label = tk.Label(self, text="New User? Click Here", fg="blue", cursor="hand2", bg="#F3F3E0", font=("Tahoma", 10))
        signup_label.pack(pady=10)
        signup_label.bind("<Button-1>", self.open_signup)

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
                cursor.execute("SELECT id FROM adminuser WHERE username=%s AND password=%s", (username, password))
                result = cursor.fetchone()
                conn.close()

                if result:
                    messagebox.showinfo("Login Successful", "Welcome!")
                    self.destroy()  # Close the login window
                    bus_passenger_info_window = BusPassengerInfos()  # Create an instance of BusPassengerInfos
                    bus_passenger_info_window.mainloop()  # Open the BusPassengerInfos window
                else:
                    messagebox.showerror("Login Failed", "Account does not exist.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def open_signup(self, event):
        self.destroy()
        signup_window = TourGuideSignup()  # Create a new instance of the sign-up window
        signup_window.mainloop()  # Open the sign-up window


class TourGuideSignup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tour Guide Sign Up")
        self.geometry("400x400")
        self.configure(bg="#F3F3E0")
        self.center_window()
        self.create_widgets()
    def center_window(self):
        # Get the dimensions of the window
        width = 400
        height = 400

        # Get the screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the geometry of the window
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_widgets(self):
        # Title Bar
        title_frame = tk.Frame(self, bg="#193E87")
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text="Sign Up", bg="#193E87", fg="white", font=("Tahoma", 18))
        title_label.pack(side=tk.LEFT, padx=10)

        # Sign Up Frame
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

        # Already have an account link
        login_label = tk.Label(self, text="Already have an account? Click Here", fg="blue", cursor="hand2", bg="#F3F3E0", font=("Tahoma", 10))
        login_label.pack(pady=10)
        login_label.bind("<Button-1>", self.open_login)

    def signup(self):
        username = self.signup_username_entry.get()
        password = self.signup_password_entry.get()

        if username and password:
            try:
                conn = mysql.connector.connect(
                    host=DB_HOST,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO adminuser (username, password) VALUES (%s, %s)", (username, password))
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
        login_window = TourGuideLogin()  # Create a new instance of the login window
        login_window.mainloop()  # Open the login window


class BusPassengerInfos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bus Passenger Information")
        self.attributes('-fullscreen', True)
        self.geometry("1200x600")
        self.configure(bg="#F3F3E0")
        self.create_widgets()
        self.set_location()
        
        self.bind("<Escape>", self.exit_fullscreen)

    def create_widgets(self):
        
        title_label = tk.Label(self, text="Bus Passenger Information", bg="#F3F3E0", font=("Tahoma", 24))
        title_label.pack(pady=20)
        close_button = tk.Button(self, text="Close", command=self.close_app, bg="#608BC1", fg="white", font=("Tahoma", 12))
        close_button.pack(pady=20)

    def exit_fullscreen(self, event=None):
        self.attributes('-fullscreen', False)  
        
    def create_widgets(self):
        
        title_label = tk.Label(self, text="Passenger Information", font=("Tahoma", 22), bg="#F3F3E0")
        title_label.pack(pady=10)

        # Input Bus ID
        input_frame = tk.Frame(self, bg="#F3F3E0")
        input_frame.pack(pady=10)

        self.bus_id_label = tk.Label(input_frame, text="Input the Bus ID:", font=("Tahoma", 14), bg="#F3F3E0")
        self.bus_id_label.pack(side=tk.LEFT, padx=5)

        self.bus_id_entry = tk.Entry(input_frame, font=("Tahoma", 14))
        self.bus_id_entry.pack(side=tk.LEFT, padx=5)

        self.search_button = tk.Button(input_frame, text="Search", command=self.search_passengers, bg="#608BC1", fg="white", font=("Tahoma", 12))
        self.search_button.pack(side=tk.LEFT, padx=5)

        # Table for displaying passenger information
        self.columns = ("Name", "Age", "Contact Number", "Parent Name", "Parent Contact", "OnBoard", "Seat No.")
        self.passenger_table = ttk.Treeview(self, columns=self.columns, show='headings', height=30)  # Set height to 20
        self.passenger_table.pack(pady=20)

        for col in self.columns:
            self.passenger_table.heading(col, text=col)
            self.passenger_table.column(col, anchor="center")

        # Buttons for actions
        button_frame = tk.Frame(self, bg="#F3F3E0")
        button_frame.pack(pady=10)

        self.onboard_button = tk.Button(button_frame , text="OnBoard", command=self.onboard_passenger, bg="#608BC1", fg="white", font=("Tahoma", 12))
        self.onboard_button.pack(side=tk.LEFT, padx=5)

        self.offboard_button = tk.Button(button_frame, text="Off Board", command=self.offboard_passenger, bg="#608BC1", fg="white", font=("Tahoma", 12))
        self.offboard_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete", command=self.delete_passenger, bg="#FA4032", fg="white", font=("Tahoma", 12))
        self.delete_button.pack(side=tk.LEFT, padx=5)


    def set_location(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def search_passengers(self):
        bus_id = self.bus_id_entry.get()
        if not bus_id:
            messagebox.showerror("Input Error", "Please enter a Bus ID to search.")
            return

        # Clear the table before updating
        for row in self.passenger_table.get_children():
            self.passenger_table.delete(row)

        query = """
            SELECT p.name, p.age, p.contactNumber, p.parentName, p.parentContact, p.attendance, p.seatNo
            FROM passengerinfo p
            JOIN bus1 b ON p.id = b.passengerID
            WHERE b.busID = %s
        """

        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute(query, (bus_id,))
            rows = cursor.fetchall()
            conn.close()

            if not rows:
                messagebox.showinfo("No Results", f"No passengers found for Bus ID {bus_id}.")
                return

            for row in rows:
                onboard_status = "On Board" if row[5] else "Off Board"
                self.passenger_table.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], onboard_status, row[6]))

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error retrieving data: {e}")

    def onboard_passenger(self):
        selected_items = self.passenger_table.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "Please select at least one passenger.")
            return

        for item in selected_items:
            name = self.passenger_table.item(item, 'values')[0]
            contact_number = self.passenger_table.item(item, 'values')[2]

            try:
                conn = mysql.connector.connect(
                    host=DB_HOST,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD
                )
                cursor = conn.cursor()
                cursor.execute("UPDATE passengerinfo SET attendance = 1 WHERE name = %s AND contactNumber = %s", (name, contact_number))
                conn.commit()
                conn.close()
                self.passenger_table.item(item, values=(name, self.passenger_table.item(item, 'values')[1], contact_number, self.passenger_table.item(item, 'values')[3], self.passenger_table.item(item, 'values')[4], "On Board", self.passenger_table.item(item, 'values')[6]))
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error updating attendance: {e}")

    def offboard_passenger(self):
        selected_items = self.passenger_table.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "Please select at least one passenger.")
            return

        for item in selected_items:
            name = self.passenger_table.item(item, 'values')[0]
            contact_number = self.passenger_table.item(item, 'values')[2]

            try:
                conn = mysql.connector.connect(
 host=DB_HOST,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD
                )
                cursor = conn.cursor()
                cursor.execute("UPDATE passengerinfo SET attendance = 0 WHERE name = %s AND contactNumber = %s", (name, contact_number))
                conn.commit()
                conn.close()
                self.passenger_table.item(item, values=(name, self.passenger_table.item(item, 'values')[1], contact_number, self.passenger_table.item(item, 'values')[3], self.passenger_table.item(item, 'values')[4], "Off Board", self.passenger_table.item(item, 'values')[6]))
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error updating attendance: {e}")

    def delete_passenger(self):
        selected_items = self.passenger_table.selection()
        if not selected_items:
            messagebox.showwarning("Selection Error", "Please select a passenger to delete.")
            return

        for item in selected_items:
            contact_number = self.passenger_table.item(item, 'values')[2]

            try:
                conn = mysql.connector.connect(
                    host=DB_HOST,
                    database=DB_NAME,
                    user=DB_USER,
                    password=DB_PASSWORD
                )
                cursor = conn.cursor()
                cursor.execute("DELETE FROM passengerinfo WHERE contactNumber = %s", (contact_number,))
                conn.commit()
                conn.close()
                self.passenger_table.delete(item)
                messagebox.showinfo("Success", "Passenger deleted successfully.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error deleting passenger: {e}")

if __name__ == "__main__":
    app = TourGuideLogin()
    app.mainloop()