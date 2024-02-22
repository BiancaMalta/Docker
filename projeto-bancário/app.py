#imports
from tkinter import *
import os
from PIL import ImageTk, Image

#Main Screen 
master = Tk()
master.title("Projeto Bancário")

#Functions
def finish_red():
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    all_accounts = os.listdir()

    if name == "" or age == "" or gender == "" or password "":
        notif.config(fg="red",text="Preencher todos os campos * ")
        return
    for name_check in all_accounts:
        if name == name_check:
            notif.config(fg="red",text="Conta já existente")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(password+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write('O')
            new_file.close()
            notif.config(fg="green",text="Conta criada")
def register():
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()

    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text="Por favor, insira seus dados abaixo para se registrar", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(register_screen, text="Name", font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age", font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender", font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Pasword", font=('Calibri',12)).grid(row=4,sticky=W)
    notif.grid(row=6,sticky=N,pady=10)

    #Entries
    Entry(register_screen,textvariable=temp_name).grid(row=1,column=0)
    Entry(register_screen,textvariable=temp_age).grid(row=2,column=0)
    Entry(register_screen,textvariable=temp_gender).grid(row=3,column=0)
    Entry(register_screen,textvariable=temp_password,show="+").grid(row=4,column=0)

    #Buttons
    Button(register_screen, text="Registro", command = finish_reg, font=('Calibri',12)).grid(row=5,sticky=N,pady=10)

def login_session():
    all_accounts = os.listdir()
    login_name = temp_login_name.get()
    login_password = temp_login_password.get()

    for name in all accounts:
        if name == login_name:
            file = open(name,"r")
            file_date = file.read()
            file_data = file_data.split('\n')
            password = file_data[1]
            #Account Dashboard
            if login_password == password:
                login_screen.destroy()
                account_dashboard = Toplevel(master)
                account_dashboard.title('Painel')
                Label(account_dashboard, text="Painel da Conta", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
                Label(account_dashboard, text="Bem-vindo"+name, font=('Calibri',12)).grid(row=1,sticky=N,pady=5)
                #Buttons
                Button(account_dashboard, text="Detalhes Pessoais", font=('Calibri',12),width=30).grid(row=2,sticky=N,padx=10)
                Button(account_dashboard, text="Deposito", font=('Calibri',12),width=30,command=deposit).grid(row=3,sticky=N,padx=10)
                Button(account_dashboard, text="Retirada", font=('Calibri',12),width=30,command=withdraw).grid(row=4,sticky=N,padx=10)                
                Label(account_dashboard).grid(row=5,sticky=N,pady=10)

                return
            else:
                login_notif.config(fg="red", text="Senha incorreta!")
                return
    
    login_notif.config(fg="red", text="Conta não encontrada!")
def deposit():
    #Vars
    global amount
    global deposit_notif
    global current_balance_label
    amont = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    deposit_screen = Toplevel(master)
    deposit_screen.title('Deposito')
    #Label
    Label(deposit_screen, text ="Deposito", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(deposit_screen, text="Saldo Atual : R$"+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(deposit_screen, text="Valor :", font=('Calibri',12)).grid(row=2, sticky=W)
    deposit_notif = Label(deposit_screen,font=('Calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    #Entry
    Entry(deposit_screen, textvariable=amount).grid(row=2,column=1)
    #Button
    Button(deposit_screen,text="Finish",font=('Calibri',12),command=finish_deposit).grid(row=3,sticky=W,pady=5)
def finish_deposit():
    if amount.get() "":
        deposit_notif.config(text='Quantidade é necessária!',fg='red')
    if float(amount.get()) <=0:
        deposit_notif.config(text='Conta negativa não é aceita', fg='red')
        return
    file = open(login_name, 'r+')
    file_data = file.read()
    current_balance = details[4]
    update_balance = current_balance
    update_balance = float(update_balance) + float(amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek()
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.config(text="Saldo atual : R$"+str(update_balance),fg="green")
    deposit_notif.config(text="Atualização de saldo", fg="green")
def withdraw():
    #Vars
    global withdraw_amount
    global withdraw_notif
    global current_balance_label
    withdraw_amont = StringVar()
    file = open(login_name, "r")
    file_data = file.read()
    user_details = file_data.split('\n')
    details_balance = user_details[4]
    #Deposit Screen
    withdraw_screen = Toplevel(master)
    withdraw_screen.title('Retirada')
    #Label
    Label(withdraw_screen, text ="Deposito", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    current_balance_label = Label(withdraw_screen, text="Saldo Atual : R$"+details_balance, font=('Calibri',12))
    current_balance_label.grid(row=1,sticky=W)
    Label(withdraw_screen, text="Valor :", font=('Calibri',12)).grid(row=2, sticky=W)
    deposit_notif = Label(withdraw_screen,font=('Calibri',12))
    deposit_notif.grid(row=4,sticky=N,pady=5)
    #Entry
    Entry(withdraw_screen, textvariable=withdraw_amount).grid(row=2,column=1)
    #Button
    Button(withdraw_screen,text="Finish",font=('Calibri',12),command=finish_withdraw).grid(row=3,sticky=W,pady=5)
def finish_withdraw():
    if withdraw_amount.get() "":
        withdraw_notif.config(text='Quantidade é necessária!',fg='red')
    if float(withdraw_amount.get()) <=0:
        withdraw_notif.config(text='Conta negativa não é aceita', fg='red')
        return
    file = open(login_name, 'r+')
    file_data = file.read()
    current_balance = details[4]
    
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_notif.config(text='Fundos Insuficientes',fg='red')
        return
    
    update_balance = current_balance
    update_balance = float(update_balance) - float(withdraw_amount.get())
    file_data = file_data.replace(current_balance, str(update_balance))
    file.seek()
    file.truncate(0)
    file.write(file_data)
    file.close()
    
    current_balance_label.config(text="Saldo atual : R$"+str(update_balance),fg="green")
    withdraw_notif.config(text="Atualização de saldo", fg="green")


def personal_details():
    #Vars
    file = open(login_name,'r')
    file_data = file.read()
    user_details = file.data.split('\n')
    details_name = user_details[0]
    details_age = user_details[2]
    details_gender = user_details[3]
    details_balance = user_detals[4]
    #Personal details screen
    personal_details_screen = Toplevel(master)
    personal_details_screen.title("Detalhes Pessoais")
    #Labels
    Label(personal_details_screen, text="Detalhes Pessoais", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(personal_details_screen, text="Name: "+details_name, font=('Calibri',12)).grid(row=1,sticky=W)
    Label(personal_details_screen, text="Idade: "+details_age, font=('Calibri',12)).grid(row=2,sticky=W)
    Label(personal_details_screen, text="Genero: "+details_gender, font=('Calibri',12)).grid(row=3,sticky=W)
    Label(personal_details_screen, text="Balanço: "+details_balance, font=('Calibri',12)).grid(row=4,sticky=W)


def login():
    #Vars
    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name = StringVar()
    temp_login_password = StringVar()
    #Login Screen
    login_screen = Toplevel(master)
    login_screen.title('Login')
    #Labels
    Label(login_screen, text="Faça login na sua conta", font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(login_screen, text='Nome de usuário', font=('Calibri',12)).grid(row=1,sticky=W)
    login_notif = Label(login_screen, font=('Calibri',12))
    login_notif.grid(row=4,sticky=N)
    #Entry
    Entry(login_screen, textvariable=temp_login_name).grid(row=1,column=1,padx=5)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=2,column=1,padx=5)
    #Button
    Button(login_screen, text="Login", command=login_session, width=15,font=('Calibri',12)).grid(row=3,sticky=W,pady=5,padx=5)

#Image import
img = Image.open('secure.png')
img = Img.resize(150,150)
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text="Banco Personalizado Beta", font=('Calibri',14)).grid(row=0,sticky=N,pady=10)
Label(master, text = "O banco mais seguro que você provavelmente já usou", font=('Calibri,12')).grid(row=1,sticky=N)
Label(master, image=img).grid(row=2,sticky=N,pady=15)

#Buttons
Button(master, text="Registro", font=('Calibri',12),width=20, command=register).grid(row=3,stiky=N)
Button(master, text="Login", font=('Calibri',12),width=20, command=login).grid(row=4,stiky=N,pady=10)


master.mainloop()
