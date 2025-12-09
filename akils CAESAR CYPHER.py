import tkinter as tk
from tkinter import scrolledtext


def caesar(key,text):
    fullalphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;[]{}@~!£$%^&*()123456789-=+_/`¬')
    
    direction = key[0]
    direction = direction.upper()


    magnitude = int(key[1::])
    
    text = list(text)

    new_alphabet = alphabet(direction,magnitude)

    cypher = ""

    for i in text:
        index = fullalphabet.index(i)
        letter = new_alphabet[index]
        cypher = f"{cypher}{letter}"

    return cypher      
def alphabet(direction,magnitude):
    fullalphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;[]{}@~!£$%^&*()123456789-=+_/`¬')
    magnitude = magnitude%88

    
    temp = []
    if direction == 'L':
        temp.extend(fullalphabet)
        temp.extend(fullalphabet[0:magnitude])
        del(temp[0:magnitude])
    elif direction == "R":
        temp.extend(fullalphabet[-magnitude:])
        temp.extend(fullalphabet)

    return temp

#START CAESAR CYPHER   
#userkey = input("How Do you want too shift your text.    L/R .....")
#usertext = input("What text are you encrypting")
#finalencryptedtext = caesar(userkey,usertext)
#print(finalencryptedtext)


def vernam(key,text):
    fullalphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;[]{}@~!£$%^&*()123456789-=+_/`¬')
    
    for index in len(text):
        keyindex = index % len(key)
        keyletter = key[keyindex] 
        keyletter = fullalphabet.index(keyletter)

        keyvalue = "{0:8b]".format(keyletter)

        textletter = text[index]
        textletter = fullalphabet.index(textletter)

        textvalue = "0:8b".format(textletter)
    return



#MY OWN CYPHUR

def akils_cypher(text):
    text = list(text)
    length = len(text)
    length=length - 1
    encryptedtext = []   
    while length != -1:
        encryptedtext.append(text[length])
        length= length-1
    result = "".join(encryptedtext)
    return result


#akil = input("What is your input?")
#print(akils_cypher(akil))



window = tk.Tk() #CREATES ROOT APPLICATION WINDOW
window.title("Encryption Tool") #CREATES TITLE FOR WINDOW
window.geometry("600x400") #SIZES WINDOW
window.resizable(False, False) #MAKES IT UNSIZEABLE

tk.Label(window, text="Enter text to encrypt:", font=("Arial", 20)).pack()
input_box = scrolledtext.ScrolledText(window, width=70, height=5, font=("Arial", 10))
input_box.pack(pady=5)



button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Label(window, text="KEY: (IF APPLICABLE)", font=("Arial", 20)).pack()
output_box = scrolledtext.ScrolledText(window, width=70, height=5, font=("Arial", 10))
output_box.pack(pady=5)

tk.Button(button_frame, text="Caesar Cipher", width=20,
          command=lambda: run_encryption("caesar")).pack(side="left", padx=5)

tk.Button(button_frame, text="Vernam Cipher", width=20,
          command=lambda: run_encryption("Vernam")).pack(side="left", padx=5)

tk.Button(button_frame, text="Akils Cipher", width=20,
          command=lambda: run_encryption("Akils")).pack(side="left", padx=5)



tk.Label(window, text="Encrypted Output:", font=("Arial", 20)).pack()
output_box = scrolledtext.ScrolledText(window, width=70, height=5, font=("Arial", 10))
output_box.pack(pady=5)

#GEORGE

