# 🔐 Caesar Cipher Project

A simple Python project that performs encryption and decryption using the Caesar Cipher technique. The user can choose to encode or decode any message with a shift value.

---

## 📜 Description

The **Caesar Cipher** is one of the oldest known encryption techniques. It works by shifting each letter in the message by a fixed number of positions in the alphabet. This project allows the user to:
- Encrypt (encode) messages
- Decrypt (decode) messages
- Enter a custom shift value
- Keep using the program until they choose to exit

---

## 🚀 How It Works

1. The user is prompted to choose whether they want to encode or decode a message.
2. They enter their message (text) and a shift number.
3. The program outputs the result based on the Caesar Cipher logic.
4. The user can repeat the process or exit.

---

## 🧠 Caesar Cipher Logic

- Each letter is shifted forward (for encoding) or backward (for decoding) in the alphabet.
- Non-alphabetic characters (like spaces or punctuation) remain unchanged.
- The alphabet is treated as circular (e.g., 'z' shifted by 1 becomes 'a').

---

## 📷 Sample Output
<pre>

 .o88b.  .d8b.  d88888b .d8888.  .d8b.  d8888b. 
d8P  Y8 d8' `8b 88'     88'  YP d8' `8b 88  `8D 
8P      88ooo88 88ooooo `8bo.   88ooo88 88oobY' 
8b      88~~~88 88~~~~~   `Y8b. 88~~~88 88`8b   
Y8b  d8 88   88 88.     db   8D 88   88 88 `88. 
 `Y88P' YP   YP Y88888P `8888Y' YP   YP 88   YD 
                                                
                                                
 .o88b. d888888b d8888b. db   db d88888b d8888b.
d8P  Y8   `88'   88  `8D 88   88 88'     88  `8D
8P         88    88oodD' 88ooo88 88ooooo 88oobY'
8b         88    88~~~   88~~~88 88~~~~~ 88`8b  
Y8b  d8   .88.   88      88   88 88.     88 `88.
 `Y88P' Y888888P 88      YP   YP Y88888P 88   YD

type 'encode' to encrypt, type 'decode' to decrypt: 
encode
enter message: 
hello
enter shift number: 
5
here is encoded result: mjqqt
enter 'yes' if u want to go again. or else type 'no'. 

</pre>



---

## 💡 Example

```python
caesar(original_text="hello", shift_amount=3, encode_or_decode="encode")
# Output: khoor



🛠️ Technologies Used
Python 3

ASCII Art for logo

Basic control flow and string manipulation



📁 File Structure

caesar_cipher.py   # Main Python script with Caesar Cipher logic
README.md          # Project documentation


✅ Features
Encrypt and decrypt text

Handles spaces and punctuation correctly

Loop for continuous use

User-friendly prompts



