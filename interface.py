import tkinter as tk
from tkinter import ttk
from writetopdf import Invoice
import orgdatabase as odb
import customerdatabase as cdb
import os



root = tk.Tk()
ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

#biticon = "testico.ico"
#root.iconbitmap(biticon)
root.title("PS Faktura")
root.geometry("800x600")
root.config(background="white")

label3 = ttk.Label(root, text = "KID: ", background = "white")
label3.place(x = 10, y = 45)

KID = ttk.Entry(root)
KID.place(x = 110, y = 45)   

label = ttk.Label(root, text = "Kontonummer: ", background = "white")
label.place(x = 10, y = 70)

kontonr = ttk.Entry(root)
kontonr.place(x = 110, y = 70)


label2 = ttk.Label(root, text = "Pris: ", background = "white")
label2.place(x = 10, y = 95)

price = ttk.Entry(root)
price.place(x = 110, y = 95)   

def get_price(a):
    b = a.split(",")
    if len(b) == 2:
        kroner = b[0]
        ore = b[1]
    
    else:
        b = a.split(".")
        if len(b) == 2:
            kroner = b[0]
            ore = b[1]
        
        else:
            kroner = b[0]
            ore = '0'
    return kroner, ore



def create_faktura():
    invoice = Invoice(KID.get(), get_price(price.get())[0], get_price(price.get())[1], kontonr.get(), orgnr.get())
    invoice()
    os.startfile(KID.get() + ".pdf")
    
create_button = ttk.Button(root, text ="Lag faktura", command = create_faktura)
create_button.place(x = 714, y = 545)

        
menubar = tk.Menu(root)  
file = tk.Menu(menubar, tearoff=0)  
file.add_command(label="Ny")  
file.add_command(label="Åpne")  
file.add_command(label="Lukke")  
  
file.add_separator()  
file.add_command(label="Avslutt", command=root.destroy)  
  
menubar.add_cascade(label="Fil", menu=file)  
edit = tk.Menu(menubar, tearoff=0)   

orgdata = []
odb.get_org_values(orgdata)    
if len(orgdata) == 0:
    orgdata.append("Se innstillinger")
    
orgnr = tk.StringVar(root)    
def orgmenu(orgdata):
    #orgnr.set(orgdata[0])
    orgnrmenu = ttk.OptionMenu(root, orgnr, orgdata[0], *orgdata)
    orgnrmenu.place(x = 110, y = 10)
    orgnrmenu.config(width = 50)
    
orgmenu(orgdata)       
    
def delete_orgs():
    odb.delete_org_values()
    orgdata.clear()
    orgdata.append("Se innstillinger")
    orgmenu(orgdata)
    orgnr.set(orgdata[0])

def org_popup():
    win = tk.Toplevel()
    win.geometry("300x80")
    win.title("Legg til organisasjonsnummer")
#    win.iconbitmap(biticon)
    def add_org():
        if orgdata[0] ==  "Se innstillinger":
            orgdata.remove("Se innstillinger")
            
        odb.add_org_values(orgname.get(), orginput.get())
        orgdata.append(str(orgname.get()) + ": " + str(orginput.get()))
        orgnr.set(str(orgname.get()) + ": " + str(orginput.get()))
        orgmenu(orgdata)
        win.destroy()
        
    orginput = ttk.Entry(win)
    orginput.place(x = 70, y = 10)
    labelorgnr = tk.Label(win, text="Orgnr: ")
    labelorgnr.place(x = 0, y = 10)
    orgname = ttk.Entry(win)
    orgname.place(x = 70, y = 35)
    labelname = tk.Label(win, text="Navn: ")
    labelname.place(x = 0, y = 35)
    
    create_button = ttk.Button(win, text ="Legg til", command = add_org)
    create_button.place(x = 211, y = 20)
    

  
org_label = ttk.Label(root, text = "Orgnr: ", background = "white")
org_label.place(x = 10, y = 10)
edit.add_command(label="Slett alle organisasjoner", command = delete_orgs)  
edit.add_command(label="Legg til organisasjon", command = org_popup)

menubar.add_cascade(label="Instillinger", menu=edit)  


def about_popup():
    win = tk.Toplevel()
#    win.iconbitmap(biticon)
    win.geometry("500x500")
    win.title("Om Faktura")

hjelp = tk.Menu(menubar, tearoff=0)  
hjelp.add_command(label="Om", command = about_popup)  
menubar.add_cascade(label="Hjelp", menu=hjelp)  




customerdata = []
cdb.get_cust_values(customerdata)    
if len(customerdata) == 0:
    customerdata.append('Trykk på "Ny kunde"')
    
customernr = tk.StringVar(root)    
def custmenu(customerdata):
    customermenu = ttk.Combobox(root)#, customernr, customerdata[0], *customerdata)
#    for item in customerdata:
#        customermenu.insert('end', item)
    customermenu['values'] = customerdata
    customermenu.place(x = 110, y = 150)
    customermenu.config(width = 50)
    
custmenu(customerdata)  

def customer_popup():
    win = tk.Toplevel()
    win.geometry("300x100")
    win.title("Legg til kunde")
#    win.iconbitmap(biticon)
    def add_customer():
        if customerdata[0] ==  'Trykk på "Ny kunde"':
            customerdata.remove('Trykk på "Ny kunde"')
            
        cdb.add_cust_values(customername.get(), customeradr.get())
        customerdata.append(str(customername.get()) + ": " + str(customeradr.get()))
        customernr.set(str(customername.get()) + ": " + str(customeradr.get()))
        custmenu(customerdata)
        win.destroy()
        
    customername = ttk.Entry(win)
    customername.place(x = 70, y = 10)
    labelname = tk.Label(win, text="Navn: ")
    labelname.place(x = 0, y = 10)    
    customeradr = ttk.Entry(win)
    customeradr.place(x = 70, y = 35)
    labeladr = tk.Label(win, text="Adresse: ")
    labeladr.place(x = 0, y = 35)

    
    create_button = ttk.Button(win, text ="Legg til", command = add_customer)
    create_button.place(x = 211, y = 50) 
    
cust_button = ttk.Button(root, text ="Ny kunde", command = customer_popup)
cust_button.place(x = 450, y = 145)
cust_button.config(width = 10)

cust_label = ttk.Label(root, text = "Kunde: ", background = "white")
cust_label.place(x = 10, y = 150)

root.config(menu=menubar)  
root.mainloop() 




































