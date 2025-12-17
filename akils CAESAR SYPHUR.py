import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt


def caesar(key,text):
    fullalphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;[]{}@~!£$%^&*()123456789-=+_/`¬')
    
    direction = key[0]
    direction = direction.upper()


    magnitude = int(key[1::])
    
    text = list(text)

    new_alphabet = alphabet(direction,magnitude)

    cypher = ""

    for i in text:
        try:
            index = fullalphabet.index(i)
            letter = new_alphabet[index]
            cypher = f"{cypher}{letter}"
        except: 
            pass

    

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

def startcaesar(): 
    userkey = input("How Do you want too shift your text.    L/R .....")
    usertext = input("What text are you encrypting")
    finalencryptedtext = caesar(userkey,usertext)
    print(finalencryptedtext)

    caesar(userkey,usertext)



def vernam(key, text):
    fullalphabet = list(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;[]{}@~!£$%^&*()123456789-=+_/`¬'
    )

    result = ""

    for i in range(len(text)):
        text_char = text[i]
        key_char = key[i % len(key)]

        if text_char not in fullalphabet or key_char not in fullalphabet:
            result += text_char
            continue

        text_index = fullalphabet.index(text_char)
        key_index = fullalphabet.index(key_char)

    
        cipher_index = text_index ^ key_index

        result += fullalphabet[cipher_index % len(fullalphabet)]

    return result




#MY OWN CYPHUR

def akils_cyphur(text):
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
#print(akils_cyphur(akil))


class main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.rowconfigure(0, weight= 1)
        self.columnconfigure(0, weight= 1)

        #Renames,Sizes And Creates Window
        self.title('All Of Akils Cyphurs')
        self.geometry('1000x300')
    

        self.menu = Menu(self)

        #Run Program
        self.mainloop()

    

class Menu(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)


        
        self.grid(row = 0, column= 0, rowspan= 1 ,columnspan= 1,sticky= 'nsew')
        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure((0,1,2), weight = 1)
        self.rowconfigure((0,1,2,3,4), weight = 1)

        self.mainbackround = tk.Label(self,text = "Akils Cyphers!", background = 'Dark Slate Blue', fg= 'black', font= ("Helvetica",40,"bold",))

        #CREATE BUTTONS 
        self.VernamButton1 =  tk.Button(self, text = 'Vernam Cypher',font= ("Helvetica",40,"bold",),command= self.VernamCypher)
        self.CaesurButton1 =  tk.Button(self, text = 'Caesar Cypher',font= ("Helvetica",40,"bold",), command= self.CaesarCypher)
        self.AkilButton1 =  tk.Button(self, text = 'Akil Cypher', font= ("Helvetica",40,"bold",), command= self.AkilsCypher)

        self.InfoButton1 =  tk.Button(self, text = 'INFO', font= ("Helvetica",20,"bold",), command= self.infobutton )
        self.F_AButton1 =  tk.Button(self, text = 'Frequency Analysis', font= ("Helvetica",20,"bold"),command= self.displayfreqanalysis )
        self.AsymButton1 =  tk.Button(self, text = 'ASYM/SYM', font= ("Helvetica",20,"bold",),command=self.asymsym )

        #CREATE TEXT BOX
        self.InputBox = tk.Text(self, height=10, width=50)
        self.InputBox.grid(row=0, column=0, padx= 10 , pady= 10, sticky="nsew")

        self.KeyBox = tk.Text(self, height=10, width=50)
        self.KeyBox.grid(row=0, column= 2, padx= 10 , pady= 10, sticky="nsew")

        self.Outputbox = tk.Text(self, height=10, width=50)
        self.Outputbox.grid(row=0, column=3, padx= 10 , pady= 10, sticky="nsew")

        #CREATE TEXT 
        self.InputText = tk.Label(self,text = 'Input', fg = 'white',font= ("Helvetica",25,"bold"))
        self.InputText.grid(row=2, column=0, padx= 10 , pady= 10, sticky="nsew")

        self.KeyText = tk.Label(self,text = 'Key', fg = 'white',font= ("Helvetica",25,"bold"))
        self.KeyText.grid(row=2, column=0, padx= 10 , pady= 10, sticky="nsew")

        self.OutputText = tk.Label(self,text = 'Output', fg = 'white',font= ("Helvetica",25,"bold"))
        self.OutputText.grid(row=2, column=0, padx= 10 , pady= 10, sticky="nsew")

        self.create_layout()

    def create_layout(self):
        self.mainbackround.grid(row = 0, column= 0, rowspan= 1 ,columnspan= 3,sticky= 'nsew')

        #PLACES GRID AND MAKES VISIBLE

        #Cypher Buttons
        self.VernamButton1.grid(row= 1, column= 0, sticky= 'nswe')
        self.CaesurButton1.grid(row= 1, column= 1, sticky= 'nswe')
        self.AkilButton1.grid(row= 1, column= 2, sticky= 'nswe')
        
        #Creates Info,Asym,Frequency Graph Buttons
        self.InfoButton1.grid(row=3, column=0, padx= 5,pady= 5, sticky= 'sw')
        self.F_AButton1.grid(row=3,column=0,padx= 5 ,pady= 5, sticky= 'e')
        self.AsymButton1.grid(row=3,column=1,padx= 5, pady= 5, sticky= 'sw')
        


        #Places Text Box
        self.InputText.grid(row= 2, column= 0, sticky= 'se')
        self.InputBox.grid(row= 2,column= 0 , sticky= 'nswe' )

        self.KeyText.grid(row= 2, column= 1, sticky= 'se')
        self.KeyBox.grid(row= 2,column= 1 , sticky= 'nswe' )

        self.Outputbox.grid(row = 2, column= 2 ,sticky= 'nswe')
        self.OutputText.grid(row= 2,column= 2,sticky= 'se')

    def infobutton(self):
    
            info = tk.Toplevel(self)
            info.title("Information")
            info.geometry("500x450")
            info.resizable(False, False)

            header = tk.Label(info, text="Information", font=("Helvetica", 35, "bold"), bg="Dark Slate Blue", fg="Black",pady=15)
            header.pack(fill="x")

            body = tk.Label(info,text=" My Three Different Ciphers\n\nAkils Cipher, Caesar Cipher, and the Vernam Cipher\n\nAkils Cipher:\nThis cipher is the simplest out of all of them.\nIt works by reversing the inputted text.\nBecause of this, it does not require a key.\n\nCaesar Cipher:\nThis cipher works by shifting each letter in the text by a fixed number.\nFor example, a shift of 3 turns A into D.\nIt requires a key to decide how many letters to shift.\n\nVernam Cipher:\nThis cipher combines the text with a key to create encrypted data.\nEach letter is changed using the corresponding letter from the key.\nIt is very secure when the key is the same length as the message.\n",bg="Dark Slate Blue",fg="black",font=("Helvetica", 14, "bold"),wraplength=450,justify="left",padx=20,pady=20)
            body.pack(fill="both", expand=True)

    def asymsym(self):

        info = tk.Toplevel(self)
        info.title("Information")
        info.geometry("500x350")
        info.resizable(False, False)

        header = tk.Label(info, text="Difference Between Asym/Sym Cyphers", font=("Helvetica", 20, "bold"), bg="Dark Slate Blue", fg="Black",pady=15)
        header.pack(fill="x")

        body = tk.Label(info,text="Symmetric ciphers use the same key to encrypt and decrypt data.\nThey are fast and efficient but require securely sharing the key.\nExamples include AES and DES.\n\nAsymmetric ciphers use two keys: a public key and a private key.\nThe public key encrypts data while the private key decrypts it.\nThey are more secure for key exchange but slower than symmetric ciphers.\nExamples include RSA and ECC.",bg="Dark Slate Blue",fg="black",font=("Helvetica", 15,"bold" ),wraplength=450,justify="left",padx=20,pady=20)
        body.pack(fill="both", expand=True)
        
    




    def CaesarCypher(self):
        """GET USER KEY, GET USER INPUT, AND OUTPUT THE CYPHER"""

        key = self.KeyBox.get(0.0, 'end')
        plain = self.InputBox.get(0.0,'end')
        cyphertext = caesar(key,plain)
        self.Outputbox.delete(0.0, 'end')
        self.Outputbox.insert(0.0, cyphertext)
        
    def VernamCypher(self):
        """GET USER KEY, USER INPUT, AND OUTFIT THE VERNAMH"""

        key = self.KeyBox.get(0.0, 'end')
        plain = self.InputBox.get(0.0,'end')
        cyphertext = vernam(key,plain)
        self.Outputbox.delete(0.0, 'end')
        self.Outputbox.insert(0.0, cyphertext)

        
    def AkilsCypher(self):  
        plain = self.InputBox.get(0.0, "end")
        cyphertext = akils_cyphur(plain)
        self.Outputbox.delete("1.0", "end")
        self.Outputbox.insert("1.0", cyphertext)

    def displayfreqanalysis(self):
        x = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;[]{}@~!£$%^&*()123456789-=+_/`¬')
        y = []
        for i in range (0,88):
            y.append(0)

        encryptedtext = self.Outputbox.get(0.0,"end")

        for i in encryptedtext:
            try:
                characterindex = x.index(i)
                y[characterindex] = y[characterindex] + 1
            except:
                pass
        
        plt.bar(x,y)
        plt.show()





       

        




        
    


        
main()
