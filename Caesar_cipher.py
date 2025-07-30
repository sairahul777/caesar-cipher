logo = """
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
"""                                             
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=="decode":
         shift_amount*=-1
    for letter in original_text:
     if letter not in alphabet:
            output_text+=letter
     else:
       
        shifted_pos=alphabet.index(letter)+shift_amount
        shifted_pos%=len(alphabet)
        output_text+=alphabet[shifted_pos]
    print(f"here is {encode_or_decode}d result: {output_text}")
should_continue=True
while should_continue:

 direction=input("type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
 text=input("enter message: \n").lower()
 shift=int(input("enter shift number: \n"))


 caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
 restart=input("enter 'yes' if u want to go again. or else type 'no'. \n").lower()
 if restart=="no": 
  should_continue=False
  print("Goodbye")

