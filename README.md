# StegoSecure
🔒 Secure Steganography with AES Encryption – A Python-based project that securely hides encrypted messages inside images using steganography. The project integrates AES-256 encryption with password protection, ensuring only authorized users can extract the hidden data.

Project Overview  
This project implements AES-256 encryption with steganography to securely hide messages within images. The encrypted message is embedded in an image, ensuring confidentiality while remaining visually unnoticeable. A password-based authentication system ensures only authorized users can retrieve the hidden message.  

Features  
- AES-256 Encryption – Strong encryption ensures secure message storage.  
- Steganography – Hides messages within image pixels without altering appearance.  
- Password Protection – Ensures only authorized users can decrypt messages.  
- User-Friendly GUI – Simple and modern graphical interface using CustomTkinter.  
- Cross-Platform Compatibility – Works on Windows, macOS, and Linux.  

 Technologies Used  
- Programming Language: Python  
- Libraries: OpenCV, Cryptography, CustomTkinter  


Installation & Setup  
1. Clone the Repository  
   
   git clone https://github.com/prakash2011/StegoSecure.git

   cd Secure-Steganography

3. Install Dependencies

   pip install -r requirements.txt
   
4. Run the Encryption Script
   
    python encrypt.py

5. Run the Decryption Script

    python decrypt.py




