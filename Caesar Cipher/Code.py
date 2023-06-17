logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
user_choice = "yes"
plain_text = []
cipher_text = []
text = ""
shift = ""
def encrypt(plain_text,shift):
  for n in plain_text:
    if n in alphabet:
      position = alphabet.index(n)
      cipher_text.append(alphabet[(position+shift)%26])
    else:
      cipher_text.append(n)
  print(f"The encoded text is {''.join(cipher_text)}")
def decrypt(d,s):
  for n in d:
    if n in alphabet:
      position = alphabet.index(n)
      plain_text.append(alphabet[(position-s)%26])
    else:
      plain_text.append(n)
  print(f"The decoded text is {''.join(plain_text)}")
while user_choice=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text,shift)
  elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(cipher_text,shift)
  else:
    print("Wrong input")
  user_choice = input("Want to run again, type yes or no? ").lower()
