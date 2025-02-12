import tkinter as tk
from tkinter import ttk, messagebox
from fpdf import FPDF

# Menu items and prices
MENU = {
    "Pizza": 12,
    "Soda": 2,
    "Chicken Nuggets": 5,
    "Breadsticks": 3,
    "Pasta": 8,
    "Burger": 7,
    "Fries": 4,
    "Milkshake": 6
}

# Coupon Codes
COUPONS = {
    "DISCOUNT10": 0.10,  # 10% off
    "FREESODA": "Soda",   # Free soda
}

# Order Storage
order = {}

# Function to update receipt and calculate total
def calculate_total():
    total = 0
    order_details = ""
    order.clear()  # Reset order storage
    
    for item, price in MENU.items():
        qty = quantity_vars[item].get()
        if qty > 0:
            item_total = qty * price
            total += item_total
            order[item] = qty
            order_details += f"{item}: {qty} x ${price} = ${item_total}\n"
    
    # Apply Coupon Code
    discount_text = ""
    coupon_code = coupon_entry.get().strip().upper()
    if coupon_code in COUPONS:
        if isinstance(COUPONS[coupon_code], float):
            discount = total * COUPONS[coupon_code]
            total -= discount
            discount_text = f"Discount Applied ({coupon_code}): -${discount:.2f}\n"
        elif isinstance(COUPONS[coupon_code], str):
            free_item = COUPONS[coupon_code]
            if free_item in MENU:
                order_details += f"Free {free_item} (Coupon Applied)\n"
                discount_text = f"Free {free_item} added!\n"
    
    # Total calculation
    total_with_tax = total * 1.08  # Applying 8% tax

    if total == 0:
        show_custom_error("Please select at least one item.")
        return

    # Update receipt
    receipt_text.set(f"Order Summary:\n{order_details}{discount_text}\nTotal (with tax): ${total_with_tax:.2f}")

# Function to generate PDF receipt
def export_receipt():
    if not order:
        show_custom_error("No order to export!")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, "Pizza Palace Receipt", ln=True, align="C")
    pdf.ln(10)
    
    for item, qty in order.items():
        pdf.cell(200, 10, f"{item}: {qty} x ${MENU[item]}", ln=True)
    
    pdf.cell(200, 10, f"Total (including tax): ${receipt_text.get().split('$')[-1]}", ln=True)
    
    pdf.output("receipt.pdf")
    show_custom_success("Receipt saved as receipt.pdf!")

# Function to show custom error message box
def show_custom_error(message):
    error_window = tk.Toplevel(root)
    error_window.title("Error")
    error_window.geometry("250x100")  # Larger error window
    error_window.configure(bg="#2e2e2e")
    
    label = tk.Label(error_window, text=message, font=("Arial", 10), fg="white", bg="#2e2e2e")
    label.pack(pady=10)
    
    button = tk.Button(error_window, text="OK", command=error_window.destroy, font=("Arial", 10), bg="#ff4d4d", fg="white", relief="solid", bd=1)
    button.pack(pady=5)

# Function to show custom success message box
def show_custom_success(message):
    success_window = tk.Toplevel(root)
    success_window.title("Success")
    success_window.geometry("250x100")  # Larger success window
    success_window.configure(bg="#2e2e2e")
    
    label = tk.Label(success_window, text=message, font=("Arial", 10), fg="white", bg="#2e2e2e")
    label.pack(pady=10)
    
    button = tk.Button(success_window, text="OK", command=success_window.destroy, font=("Arial", 10), bg="#4CAF50", fg="white", relief="solid", bd=1)
    button.pack(pady=5)

# Create main window
root = tk.Tk()
root.title("🍕 Pizza Palace Ordering System 🍕")
root.geometry("900x600")  # Increased width for more space (same height)
root.configure(bg="#2e2e2e")  # Dark background for the whole window

# Header Section with Title
header_frame = tk.Frame(root, bg="#333333", bd=0, relief="solid")
header_frame.pack(fill="x")

title_label = tk.Label(header_frame, text="Pizza Palace Ordering", font=("Arial", 16, "bold"), fg="white", bg="#333333")
title_label.pack(pady=5)

# Menu Frame (Compact and smaller)
menu_frame = tk.Frame(root, bg="#333333", padx=0, pady=0, bd=0, relief="solid")
menu_frame.pack(pady=10, padx=20)

quantity_vars = {}

for item, price in MENU.items():
    frame = tk.Frame(menu_frame, bg="#333333", bd=0, relief="solid")
    frame.pack(fill="x", pady=5)

    tk.Label(frame, text=f"{item} (${price}):", font=("Arial", 10), fg="white", bg="#333333").pack(side="left", padx=5)
    
    quantity_vars[item] = tk.IntVar(value=0)
    qty_dropdown = ttk.Combobox(frame, textvariable=quantity_vars[item], values=list(range(11)), width=5, state="readonly", font=("Arial", 10))
    qty_dropdown.pack(side="right", padx=5)

# Coupon Entry
coupon_frame = tk.Frame(root, bg="#333333", bd=0, relief="solid")
coupon_frame.pack(pady=10)

tk.Label(coupon_frame, text="Coupon Code:", font=("Arial", 10), fg="white", bg="#333333").pack(side="left", padx=10)
coupon_entry = tk.Entry(coupon_frame, width=12, font=("Arial", 10), bd=0)
coupon_entry.pack(side="left", padx=5)

# Place Order Button
order_button = tk.Button(root, text="Place Order", command=calculate_total, width=15, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="solid", bd=1)
order_button.pack(pady=10)

# Receipt Section
receipt_text = tk.StringVar(value="Order Summary:\n\n")
receipt_label = tk.Label(root, textvariable=receipt_text, font=("Arial", 10), justify="left", bg="#2e2e2e", fg="white")
receipt_label.pack(pady=10)

# Export Button (Export to PDF)
export_button = tk.Button(root, text="Export Receipt", command=export_receipt, width=15, font=("Arial", 12, "bold"), bg="#2196F3", fg="white", relief="solid", bd=1)
export_button.pack(pady=10)

# Run the application
root.mainloop()
