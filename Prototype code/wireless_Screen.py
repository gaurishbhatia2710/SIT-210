#Name : Gaurish Bhatia
#Student ID: 2110994762.
#Remarks : this is the code for the wireless screen part.

import json
from tkinter import *
import tkinter as tk
import pyrebase


        

root = tk.Tk()
root.geometry("1015x530")
root.minsize(1015, 530)
root.maxsize(1015, 530)
global number

root.title('Application')
#-----------------------
config = {
    "apiKey" : "AIzaSyAT15wRlIPqeAtBnYldxOhuj-C2ICgoLEY",
    "authDomain" :"myproject-64613.firebaseapp.com",
    "databaseURL" :"https://myproject-64613-default-rtdb.firebaseio.com",
    "storageBucket" : "http://myproject-64613.appspot.com"
}

firebase = pyrebase.initialize_app(config)
#------------------------------------------------------------------------------
database = firebase.database()
data = {
    "value":2,
}
database.child("connect").set(data)

# 
def home_page():
    global home_frame
    home_frame = tk.Frame(main_frame)
    lb=tk.Label(home_frame,text='Select the Block : ',font=('Bold',42,UNDERLINE))
    btn = Button(main_frame, text = 'S Block',font=('Bold',35),height=1,width=15,command=s_block_frame).place(x=230, y=100)
    btn = Button(main_frame, text = 'P Block', font=('Bold',35),height=1,width=15,command=p_block_frame).place(x=230, y=200)
    btn = Button(main_frame, text = 'D Block', font=('Bold',35),height=1,width=15, command = d_block_frame).place(x=230, y = 300)
    btn = Button(main_frame, text = 'F Block', font=('Bold',35),height=1,width=15, command = f_block_frame).place(x=230, y = 400)
    lb.pack()
    home_frame.pack(pady=20)

def s_block_frame():
    delete_page()
    s_block = tk.Frame(main_frame)
    lb=tk.Label(s_block,text='S Block Elements',font=('Bold',40,UNDERLINE))
    btn = Button(main_frame, text = 'H - Hydrogen',font=(20),height=1,width=20).place(x=150, y=100)
    btn = Button(main_frame, text = 'Li - Lithium',font=(20),height=1,width=20).place(x=150, y=150)
    btn = Button(main_frame, text = 'Na - Sodium',font=(20),height=1,width=20).place(x=150, y=200)
    btn = Button(main_frame, text = 'K - Potasium',font=(20),height=1,width=20).place(x=150, y=250)
    btn = Button(main_frame, text = 'Rb - Rubidium',font=(20),height=1,width=20).place(x=150, y=300)
    btn = Button(main_frame, text = 'Cs - Caesium',font=(20),height=1,width=20).place(x=150, y=350)
    btn = Button(main_frame, text = 'Fr- Francium',font=(20),height=1,width=20).place(x=150, y=400)
    
    btn = Button(main_frame, text = 'He- Helium',font=(20),height=1,width=20).place(x=440, y=100)
    btn = Button(main_frame, text = 'Be - Beryllium',font=(20),height=1,width=20).place(x=440, y=150)
    btn = Button(main_frame, text = 'Mg - Magnesium',font=(20),height=1,width=20).place(x=440, y=200)
    btn = Button(main_frame, text = 'Ca - Calcium',font=(20),height=1,width=20).place(x=440, y=250)
    btn = Button(main_frame, text = 'Sr - Strontium',font=(20),height=1,width=20).place(x=440, y=300)
    btn = Button(main_frame, text = 'Ba - Barium',font=(20),height=1,width=20).place(x=440, y=350)
    btn = Button(main_frame, text = 'Ra - Radium',font=(20),height=1,width=20).place(x=440, y=400)
    lb.pack()
    s_block.pack(pady=20)

def p_block_frame():
    delete_page()
    p_block = tk.Frame(main_frame)
    lb=tk.Label(p_block,text='P Block Elements',font=('Bold',30,UNDERLINE))
    btn = Button(main_frame, text = 'Boron  (B)',font=(15),width=15).place(x=20, y=80)
    btn = Button(main_frame, text = 'Carbon  (C)',font=(15),width=15).place(x=20, y=115)
    btn = Button(main_frame, text = 'Nitrogen  (N)',font=(15),width=15).place(x=20, y=150)
    btn = Button(main_frame, text = 'Oxygen  (O)',font=(15),width=15).place(x=20, y=185)
    btn = Button(main_frame, text = 'Fluorine  (F)',font=(15),width=15).place(x=20, y=220)
    btn = Button(main_frame, text = 'Neon  (Ne)',font=(15),width=15).place(x=20, y=255)
    btn = Button(main_frame, text = 'Aluminium  (Al)',font=(15),width=15).place(x=20, y=290)
    btn = Button(main_frame, text = 'Silicon  (Si)',font=(15),width=15).place(x=20, y=325)
    btn = Button(main_frame, text = 'Phosphorus  (P)',font=(15),width=15).place(x=20, y=360)
    btn = Button(main_frame, text = 'Sulfur  (S)',font=(15),width=15).place(x=20, y=395)
    btn = Button(main_frame, text = 'Chlorine  (Cl)',font=(15),width=15).place(x=20, y=430)
    btn = Button(main_frame, text = 'Argon  (Ar)',font=(15),width=15).place(x=20, y=465)

    btn = Button(main_frame, text = 'Gallium  (Ga)',font=(15),width=15).place(x=200, y=80)
    btn = Button(main_frame, text = 'Germanium  (Ge)',font=(15),width=15).place(x=200, y=115)
    btn = Button(main_frame, text = 'Arsenic  (Ar)',font=(15),width=15).place(x=200, y=150)
    btn = Button(main_frame, text = 'Selenium  (Se)',font=(15),width=15).place(x=200, y=185)
    btn = Button(main_frame, text = 'Bromine  (Br)',font=(15),width=15).place(x=200, y=220)
    btn = Button(main_frame, text = 'Krypton  (Kr)',font=(15),width=15).place(x=200, y=255)
    btn = Button(main_frame, text = 'Indium  (In)',font=(15),width=15).place(x=200, y=290)
    btn = Button(main_frame, text = 'Tin  (Sn)',font=(15),width=15).place(x=200, y=325)
    btn = Button(main_frame, text = 'Antimony  (Sb)',font=(15),width=15).place(x=200, y=360)
    btn = Button(main_frame, text = 'Tellurium  (Te)',font=(15),width=15).place(x=200, y=395)
    btn = Button(main_frame, text = 'Iodine  (I)',font=(15),width=15).place(x=200, y=430)
    btn = Button(main_frame, text = 'Xenon  (Xe)',font=(15),width=15).place(x=200, y=465)

    btn = Button(main_frame, text = 'Thallium  (Tl)',font=(15),width=15).place(x=380, y=80)
    btn = Button(main_frame, text = 'Lead  (Pb)',font=(15),width=15).place(x=380, y=115)
    btn = Button(main_frame, text = 'Bismuth  (Bi)',font=(15),width=15).place(x=380, y=150)
    btn = Button(main_frame, text = 'Polonium  (Po)',font=(15),width=15).place(x=380, y=185)
    btn = Button(main_frame, text = 'Astatine  (At)',font=(15),width=15).place(x=380, y=220)
    btn = Button(main_frame, text = 'Antimony  (Sb)',font=(15),width=15).place(x=380, y=255)
    btn = Button(main_frame, text = 'Radon  (Rn)',font=(15),width=15).place(x=380, y=290)
    lb.pack()
    p_block.pack(pady=20)

def d_block_frame():
    delete_page()
    d_block = tk.Frame(main_frame)
    lb = tk.Label(d_block, text ='D Block Element : ',font =('Bold', 20))

    btn = Button(main_frame, text = 'Scandium  (Sc)',font=(10), width = 15).place(x=20, y=80)
    btn = Button(main_frame, text = 'Titanium  (Ti)',font=(7),width=15).place(x=20, y=115)
    btn = Button(main_frame, text = 'Vanadium  (V)',font=(10),width=15).place(x=20, y=150)
    btn = Button(main_frame, text = 'Chromium  (Cr)',font=(10),width=15).place(x=20, y=185)
    btn = Button(main_frame, text = 'Manganese  (Mn)',font=(10),width=15).place(x=20, y=220)
    btn = Button(main_frame, text = 'Iron  (Fe)',font=(10),width=15).place(x=20, y=255)
    btn = Button(main_frame, text = 'Cobalt  (Co)',font=(10),width=15).place(x=20, y=290)
    btn = Button(main_frame, text = 'Nickel  (Ni)',font=(10),width=15).place(x=20, y=325)
    btn = Button(main_frame, text = 'Copper  (Cu)',font=(10),width=15).place(x=20, y=360)
    btn = Button(main_frame, text = 'Zinc  (Zn)',font=(10),width=15).place(x=20, y=395)
    btn = Button(main_frame, text = 'Yttrium  (Y)',font=(10),width=15).place(x=20, y=430)
    btn = Button(main_frame, text = 'Zirconium  (Zr)',font=(10),width=15).place(x=20, y=465)

    btn = Button(main_frame, text = 'Niobium  (Nb)',font=(10),width=15).place(x=200, y=80)
    btn = Button(main_frame, text = 'Molybdenum  (Mo)',font=(10),width=15).place(x=200, y=115)
    btn = Button(main_frame, text = 'Technetium  (Tc)',font=(10),width=15).place(x=200, y=150)
    btn = Button(main_frame, text = 'Ruthenium  (Ru)',font=(10),width=15).place(x=200, y=185)
    btn = Button(main_frame, text = 'Rhodium  (Rh)',font=(10),width=15).place(x=200, y=220)
    btn = Button(main_frame, text = 'Palladium  (Pd)',font=(10),width=15).place(x=200, y=255)
    btn = Button(main_frame, text = 'Silver  (Ag)',font=(10),width=15).place(x=200, y=290)
    btn = Button(main_frame, text = 'Cadmium  (Cd)',font=(10),width=15).place(x=200, y=325)
    btn = Button(main_frame, text = 'Lutetium  (Lu)',font=(10),width=15).place(x=200, y=360)
    btn = Button(main_frame, text = 'Hafnium  (Hf)',font=(10),width=15).place(x=200, y=395)
    btn = Button(main_frame, text = 'Rhenium  (Re)',font=(10),width=15).place(x=200, y=430)
    btn = Button(main_frame, text = 'Osmium  (Os)',font=(10),width=15).place(x=200, y=465)

    btn = Button(main_frame, text = 'Iridium  (Ir)',font=(10),width=15).place(x=380, y=80)
    btn = Button(main_frame, text = 'Platinum  (Pt)',font=(10),width=15).place(x=380, y=115)
    btn = Button(main_frame, text = 'Gold  (Au)',font=(10),width=15).place(x=380, y=150)
    btn = Button(main_frame, text = 'Mercury  (Hg)',font=(10),width=15).place(x=380, y=185)
    btn = Button(main_frame, text = 'Lawrencium  (Lr)',font=(10),width=15).place(x=380, y=220)
    btn = Button(main_frame, text = 'Rutherfordium  (Rf)',font=(10),width=15).place(x=380, y=255)
    btn = Button(main_frame, text = 'Dubnium  (Db)',font=(10),width=15).place(x=380, y=290)
    btn = Button(main_frame, text = 'Seaborgium  (Sg)',font=(10),width=15).place(x=380, y=325)
    btn = Button(main_frame, text = 'Bohrium  (Bh)',font=(10),width=15).place(x=380, y=360)
    btn = Button(main_frame, text = 'Hassium  (Hs)',font=(10),width=15).place(x=380, y=395)
    btn = Button(main_frame, text = 'Meitnerium  (Mt)',font=(10),width=15).place(x=380, y=430)
    btn = Button(main_frame, text = 'Darmstadtium  (Ds)',font=(10),width=15).place(x=380, y=465)

    btn = Button(main_frame, text = 'Roentgenium  (Rg)',font=(10),width=15).place(x=560, y=80)
    lb.pack()
    d_block.pack(pady=20)

def f_block_frame():
    delete_page()
    f_block = tk.Frame(main_frame)
    lb = tk.Label(f_block, text ='D Block Element : ',font =('Bold', 20))

    btn = Button(main_frame, text = 'Lanthanum  (La)',font=(10),width=15).place(x=20, y=80)
    btn = Button(main_frame, text = 'Cerium  (Ce)',font=(10),width=15).place(x=20, y=115)
    btn = Button(main_frame, text = 'Praseodymium  (Pr)',font=(2),width=15).place(x=20, y=150)
    btn = Button(main_frame, text = 'Promethium  (Nd)',font=(10),width=15).place(x=20, y=185)
    btn = Button(main_frame, text = 'Samarium  (Sm)',font=(10),width=15).place(x=20, y=220)
    btn = Button(main_frame, text = 'Europium  (Eu)',font=(10),width=15).place(x=20, y=255)
    btn = Button(main_frame, text = 'Gadolinium  (Gd)',font=(10),width=15).place(x=20, y=290)
    btn = Button(main_frame, text = 'Terbium  (Tb)',font=(10),width=15).place(x=20, y=325)
    btn = Button(main_frame, text = 'Dysprosium  (Dy)',font=(10),width=15).place(x=20, y=360)
    btn = Button(main_frame, text = 'Holmium  (Ho)',font=(10),width=15).place(x=20, y=395)
    btn = Button(main_frame, text = 'Erbium  (Er)',font=(10),width=15).place(x=20, y=430)
    btn = Button(main_frame, text = 'Thulium  (Tm)',font=(10),width=15).place(x=20, y=465)

    btn = Button(main_frame, text = 'Ytterbium  (Yb)',font=(10),width=15).place(x=200, y=80)
    btn = Button(main_frame, text = 'Lutetium  (Lu)',font=(10),width=15).place(x=200, y=115)
    btn = Button(main_frame, text = 'Actinium  (Ac)',font=(10),width=15).place(x=200, y=150)
    btn = Button(main_frame, text = 'Thorium  (Th)',font=(10),width=15).place(x=200, y=185)
    btn = Button(main_frame, text = 'Protactinium  (Pa)',font=(10),width=15).place(x=200, y=220)
    btn = Button(main_frame, text = 'Uranium  (U)',font=(10),width=15).place(x=200, y=255)
    btn = Button(main_frame, text = 'Neptunium  (Np)',font=(10),width=15).place(x=200, y=290)
    btn = Button(main_frame, text = 'Plutonium  (Pu)',font=(10),width=15).place(x=200, y=325)
    btn = Button(main_frame, text = 'Americium  (Am)',font=(10),width=15).place(x=200, y=360)
    btn = Button(main_frame, text = 'Curium  (Cm)',font=(10),width=15).place(x=200, y=395)
    btn = Button(main_frame, text = 'Berkelium  (Bk)',font=(10),width=15).place(x=200, y=430)
    btn = Button(main_frame, text = 'Californium  (Cf)',font=(10),width=15).place(x=200, y=465)

    btn = Button(main_frame, text = 'Einstenium  (Es)',font=(10),width=15).place(x=380, y=80)
    btn = Button(main_frame, text = 'Fermium  (Fm)',font=(10),width=15).place(x=380, y=115)
    btn = Button(main_frame, text = 'Mendelevium  (Md)',font=(10),width=15).place(x=380, y=150)
    btn = Button(main_frame, text = 'Nobelium  (No)',font=(10),width=15).place(x=380, y=185)
    lb.pack()
    f_block.pack(pady=20)

def compound_page():
    compound_frame = tk.Frame(main_frame)
    lb=tk.Label(compound_frame,text='Select the compound name : ',font=('Bold',30,UNDERLINE))
    btn = Button(main_frame, text = 'Hydrochloric Acid  (HCl)',font=(40),width=40,height=1).place(x=70, y=85)
    btn = Button(main_frame, text = 'Sulphuric Acid  (H2SO4)',font=(40),width=40,height=1).place(x=70, y=135)
    btn = Button(main_frame, text = 'Ammonia  (NH3)',font=(30),width=40,height=1).place(x=70, y=185)
    btn = Button(main_frame, text = 'Nitric Acid  (HNO3)',font=(30),width=40,height=1).place(x=70, y=235)
    btn = Button(main_frame, text = 'Methane  (CH4)',font=(30),width=40,height=1).place(x=70, y=285)
    btn = Button(main_frame, text = 'Phenol  (C6H6O)',font=(30),width=40,height=1).place(x=70, y=335)
    btn = Button(main_frame, text = 'Ethanol  (C2H5OH)',font=(30),width=40,height=1).place(x=70, y=385)
    btn = Button(main_frame, text = 'Acetone  (C3H6O',font=(30),width=40,height=1).place(x=70, y=435)
    btn = Button(main_frame, text = 'Sulfur Trioxide  (SO3)',font=(30),width=40,height=1).place(x=70, y=485)
    btn = Button(main_frame, text = 'Chlorine  (Cl2)',font=(30),width=40,height=1).place(x=70, y=535)
    lb.pack()
    compound_frame.pack(pady=20)

def close():
    root.destroy()

# 
def exit_page():
    exit_frame = tk.Frame(main_frame)
    lb=tk.Label(exit_frame,text='Exit Page',font=('Bold',20))
    lb.pack()
    exit_button = Button(exit_frame, text="Exit",command = close)
    exit_button.pack(pady=20)
    exit_frame.pack(pady=20)

# To delete the old Page
def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()

# To hide the Indicator
def hide_indicator():
    element_indicate.config(bg='#c3c3c3')
    compound_indicate.config(bg='#c3c3c3')
    exit_indicate.config(bg='#c3c3c3')

# Indicator Color Change
def indicate(lb,page):
    hide_indicator()
    lb.config(bg='#158aff')
    delete_page()
    page()

#------------------------------------------------------------------------------

# gray side area
option_frame = tk.Frame(root,bg='#c3c3c3')
option_frame.pack(side=tk.LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=150,height =700)

# white side area
main_frame = tk.Frame(root,highlightbackground='black',highlightthickness=3)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(width=865,height =700)
lb=tk.Label(main_frame,text='Welcome To \n\n The World Of \n\n Periodic Table',font=('Bold',40,UNDERLINE)).pack(pady=100)

# Button
element_btn = tk.Button(option_frame,text='Element',font=('Bold' , 20), fg='#158aff',bd=0,bg='#c3c3c3',command=lambda:indicate(element_indicate,home_page))
element_btn.place(x=8,y=150)
compound_btn = tk.Button(option_frame,text='Compound',font=('Bold' , 20), fg='#158aff',bd=0,bg='#c3c3c3',command=lambda:indicate(compound_indicate,compound_page))
compound_btn.place(x=6,y=200)
exit_btn = tk.Button(option_frame,text='Exit',font=('Bold' , 20), fg='#158aff',bd=0,bg='#c3c3c3',command=lambda:indicate(exit_indicate,exit_page))
exit_btn.place(x=8,y=250)

# Indicator buttons
element_indicate = tk.Label(option_frame, text='',bg='#c3c3c3')
element_indicate.place(x=3,y=160,width=6,height=40)
compound_indicate = tk.Label(option_frame, text='',bg='#c3c3c3')
compound_indicate.place(x=3,y=210,width=6,height=40)
exit_indicate = tk.Label(option_frame, text='',bg='#c3c3c3')
exit_indicate.place(x=3,y=260,width=6,height=40)

root.mainloop()