import tkinter as tk
from tkinter import ttk

users = {
    "pal": {"pin": "1234", "balance": 5000},
    "Jay": {"pin": "4321", "balance": 3000}
}
current_user = None

# -----------------------
# Helper Functions
# -----------------------
def calculate_notes(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    result = {}
    for note in notes:
        if amount >= note:
            count = amount // note
            amount = amount % note
            result[note] = count
    return result

def show_popup(title, message, color="#222831"):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("400x300")
    popup.config(bg=color)

    # Drop shadow effect
    popup.attributes("-topmost", True)
    popup.lift()

    frame = tk.Frame(popup, bg=color, bd=8, relief="groove")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    label = tk.Label(frame, text=title, font=("Arial", 18, "bold"), bg=color, fg="cyan")
    label.pack(pady=10)

    msg = tk.Label(frame, text=message, font=("Arial", 13), bg=color, fg="white", justify="left")
    msg.pack(pady=10)

    ttk.Button(frame, text="OK ✅", command=popup.destroy).pack(pady=15)

def login():
    global current_user
    username = entry_username.get()
    pin = entry_pin.get()

    if username in users and users[username]["pin"] == pin:
        current_user = username
        login_frame.pack_forget()
        main_menu()
    else:
        show_popup("Login Failed ❌", "Invalid Username or PIN", "#9a031e")

def withdraw():
    global current_user
    try:
        amount = int(entry_withdraw.get())
        balance = users[current_user]["balance"]

        if amount > balance:
            show_popup("Error ⚠️", "Insufficient Balance", "#9a031e")
        elif amount <= 0:
            show_popup("Error ⚠️", "Enter a valid positive amount", "#9a031e")
        else:
            users[current_user]["balance"] -= amount
            notes = calculate_notes(amount)
            result_text = f"Withdrawn: ₹{amount}\n\nNotes:\n"
            for note, cnt in notes.items():
                result_text += f"₹{note} x {cnt}\n"
            result_text += f"\nRemaining Balance: ₹{users[current_user]['balance']}"
            show_popup("Success 🎉", result_text, "#004d40")
    except ValueError:
        show_popup("Error ⚠️", "Enter a valid number", "#9a031e")

def check_balance():
    global current_user
    balance = users[current_user]["balance"]
    show_popup("Balance 📊", f"Available Balance: ₹{balance}", "#1b4332")

def main_menu():
    main_frame.pack(fill="both", expand=True)

# -----------------------
# Root Setup
# -----------------------
root = tk.Tk()
root.title("💳 ATM Simulator")
root.geometry("600x500")
root.config(bg="#1e1e2e")

# -----------------------
# Style
# -----------------------
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 14, "bold"),
                padding=10)
style.configure("TLabel",
                font=("Arial", 12),
                background="#1e1e2e",
                foreground="white")
style.configure("Header.TLabel",
                font=("Arial", 20, "bold"),
                background="#1e1e2e",
                foreground="cyan")

# -----------------------
# Login Frame
# -----------------------
login_frame = tk.Frame(root, bg="#1e1e2e")
login_frame.pack(fill="both", expand=True)

ttk.Label(login_frame, text="🏦 ATM LOGIN", style="Header.TLabel").pack(pady=30)

ttk.Label(login_frame, text="Username:").pack(pady=5)
entry_username = ttk.Entry(login_frame, font=("Arial", 14))
entry_username.pack(pady=5)

ttk.Label(login_frame, text="PIN:").pack(pady=5)
entry_pin = ttk.Entry(login_frame, show="*", font=("Arial", 14))
entry_pin.pack(pady=5)

ttk.Button(login_frame, text="Login ✅", command=login).pack(pady=30)

# -----------------------
# Main ATM Frame
# -----------------------
main_frame = tk.Frame(root, bg="#2e2e3e")

ttk.Label(main_frame, text="💰 Welcome to Smart ATM", style="Header.TLabel").pack(pady=20)

entry_withdraw = ttk.Entry(main_frame, font=("Arial", 14))
entry_withdraw.pack(pady=15)

ttk.Button(main_frame, text="Withdraw 💸", command=withdraw).pack(pady=10)
ttk.Button(main_frame, text="Check Balance 📊", command=check_balance).pack(pady=10)

# -----------------------
# Run ATM
# -----------------------
root.mainloop()