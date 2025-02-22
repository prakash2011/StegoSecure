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
    filename = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.jpg;*.png")])
    if filename:
        img = cv2.imread(filename)
        messagebox.showinfo("Success", "Encrypted Image Loaded Successfully!")


def extract_and_decrypt():
    global img
    if img is None:
        messagebox.showerror("Error", "Please load an encrypted image first!")
        return

    password = simpledialog.askstring("Password", "Enter the decryption password:", show='*')
    if not password:
        messagebox.showerror("Error", "Password required!")
        return

    cipher = generate_key(password)

    extracted_chars = []
    n, m, z = 0, 0, 0
    while True:
        char = chr(img[n, m, z])
        if char == '\x00': 
            break
        extracted_chars.append(char)
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3  

    encrypted_message = "".join(extracted_chars)

    try:
        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
        messagebox.showinfo("Decrypted Message", decrypted_message)
    except:
        messagebox.showerror("Error", "Incorrect password or corrupted image!")

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("🔓 Extract & Decrypt")
root.geometry("400x300")

ctk.CTkButton(root, text="📂 Load Encrypted Image", command=open_image).pack(pady=10)
ctk.CTkButton(root, text="🔓 Extract & Decrypt", command=extract_and_decrypt).pack(pady=10)

root.mainloop()
