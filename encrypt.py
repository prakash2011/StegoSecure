import cv2
import os
import base64
import customtkinter as ctk
from tkinter import filedialog, messagebox, simpledialog
from cryptography.fernet import Fernet

img = None
filename = ""


def generate_key(password: str):
    key = base64.urlsafe_b64encode(password.ljust(32).encode()[:32])  # Ensure 32 bytes
    return Fernet(key)


def open_image():
    global img, filename
    filename = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if filename:
        img = cv2.imread(filename)
        messagebox.showinfo("Success", "Image Loaded Successfully!")


def encrypt_and_hide():
    global img
    if img is None:
        messagebox.showerror("Error", "Please load an image first!")
        return
    
    message = msg_entry.get()
    if not message:
        messagebox.showerror("Error", "Enter a message!")
        return
    
    password = simpledialog.askstring("Password", "Enter a password:", show='*')
    confirm_password = simpledialog.askstring("Confirm Password", "Re-enter password:", show='*')
    
    if not password or not confirm_password:
        messagebox.showerror("Error", "Password fields cannot be empty!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    cipher = generate_key(password)
    encrypted_message = cipher.encrypt(message.encode()).decode()


    n, m, z = 0, 0, 0
    for i in range(len(encrypted_message)):
        img[n, m, z] = ord(encrypted_message[i])
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3  # Cycle RGB

    save_path = "encryptedImage.png"
    cv2.imwrite(save_path, img)
    os.system(f"start {save_path}")  

    messagebox.showinfo("Success", "Message Encrypted and Hidden!")


ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("🔒 Encrypt & Hide")
root.geometry("400x350")

ctk.CTkLabel(root, text="Enter Secret Message:").pack(pady=10)
msg_entry = ctk.CTkEntry(root, width=300)
msg_entry.pack(pady=5)

ctk.CTkButton(root, text="📂 Load Image", command=open_image).pack(pady=5)
ctk.CTkButton(root, text="🔒 Encrypt & Hide", command=encrypt_and_hide).pack(pady=5)

root.mainloop()
