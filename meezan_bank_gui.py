import tkinter as tk
from tkinter import messagebox
import re

class MeezanBankGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Meezan Bank Account Holder Information")
        self.root.geometry("400x500")
        
        # Labels and Entry Fields
        tk.Label(root, text="Meezan Bank Account Registration", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(root, text="Full Name").pack()
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(pady=5)
        
        tk.Label(root, text="CNIC (xxxxx-xxxxxxx-x)").pack()
        self.cnic_entry = tk.Entry(root, width=30)
        self.cnic_entry.pack(pady=5)
        
        tk.Label(root, text="Mobile Number (+92xxxxxxxxxx)").pack()
        self.mobile_entry = tk.Entry(root, width=30)
        self.mobile_entry.pack(pady=5)
        
        tk.Label(root, text="Email").pack()
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.pack(pady=5)
        
        tk.Label(root, text="Account Type").pack()
        self.account_type = tk.StringVar(value="Asaan Savings")
        account_types = ["Asaan Savings", "Asaan Current", "Roshan Digital", "Bachat Savings"]
        tk.OptionMenu(root, self.account_type, *account_types).pack(pady=5)
        
        tk.Label(root, text="Initial Deposit (PKR)").pack()
        self.deposit_entry = tk.Entry(root, width=30)
        self.deposit_entry.pack(pady=5)
        
        # Submit Button
        tk.Button(root, text="Submit", command=self.submit).pack(pady=20)
        
    def validate_cnic(self, cnic):
        """Validate CNIC format: xxxxx-xxxxxxx-x"""
        pattern = r"^\d{5}-\d{7}-\d{1}$"
        return bool(re.match(pattern, cnic))
    
    def validate_mobile(self, mobile):
        """Validate Pakistani mobile number: +92 followed by 10 digits"""
        pattern = r"^\+92\d{10}$"
        return bool(re.match(pattern, mobile))
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))
    
    def submit(self):
        """Validate input and save to file"""
        name = self.name_entry.get().strip()
        cnic = self.cnic_entry.get().strip()
        mobile = self.mobile_entry.get().strip()
        email = self.email_entry.get().strip()
        account_type = self.account_type.get()
        deposit = self.deposit_entry.get().strip()
        
        # Validation
        if not name:
            messagebox.showerror("Error", "Name is required")
            return
        if not self.validate_cnic(cnic):
            messagebox.showerror("Error", "Invalid CNIC format. Use xxxxx-xxxxxxx-x")
            return
        if not self.validate_mobile(mobile):
            messagebox.showerror("Error", "Invalid mobile number. Use +92xxxxxxxxxx")
            return
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return
        try:
            deposit_amount = float(deposit)
            if account_type == "Asaan Savings" and deposit_amount < 100:
                messagebox.showerror("Error", "Minimum deposit for Asaan Savings is PKR 100")
                return
            if account_type == "Asaan Current" and deposit_amount < 100:
                messagebox.showerror("Error", "Minimum deposit for Asaan Current is PKR 100")
                return
            if account_type == "Bachat Savings" and deposit_amount < 50000:
                messagebox.showerror("Error", "Minimum deposit for Bachat Savings is PKR 50,000")
                return
            if account_type == "Roshan Digital" and deposit_amount < 0:
                messagebox.showerror("Error", "Initial deposit cannot be negative")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid deposit amount")
            return
        
        # Save to file
        with open("meezan_account_holders.txt", "a") as f:
            f.write(f"Name: {name}\n")
            f.write(f"CNIC: {cnic}\n")
            f.write(f"Mobile: {mobile}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Account Type: {account_type}\n")
            f.write(f"Initial Deposit: PKR {deposit_amount}\n")
            f.write("-" * 50 + "\n")
        
        messagebox.showinfo("Success", "Account information saved successfully!")
        self.clear_fields()
    
    def clear_fields(self):
        """Clear all entry fields"""
        self.name_entry.delete(0, tk.END)
        self.cnic_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.deposit_entry.delete(0, tk.END)
        self.account_type.set("Asaan Savings")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeezanBankGUI(root)
    root.mainloop()