'''
Nome:Antonio Jose
Ano:2°
Turno:Matutino
Diciplina: Linguagem de progamação
'''

from tkinter import*
from tkinter import messagebox
import sys
import banco

root = Tk()


def click ():
    nome = ed1.get()
    cpf = ed2.get()
    num = ed3.get()
    cep = ed4.get()
    mail = ed5.get()
    if (str(ed1.get()).isnumeric()):
        messagebox.showwarning('cuidado', 'Nome contem numeros')
    else:
        if nome == "":
            messagebox.showerror('erro', 'Nome vazio')
        else:
            messagebox.showinfo('info', 'Nome correto')
    if mail == "":
        messagebox.showerror('erro', 'Senha vazia')
    else:
        messagebox.showinfo('info', 'Senha correta')
    if (str(ed2.get()).isalpha()):
        messagebox.showwarning('cuidado', 'CPF contem letras')

    else:
        if cpf == "":
            messagebox.showerror('erro', 'CPF vazio')
        else:
            messagebox.showinfo('info', 'CPF correto')
    if (str(ed3.get()).isalpha()):
        messagebox.showwarning('cuidado', 'Numero contem letras')
    else:
        if num == "":
            messagebox.showerror('erro', 'Numero vazio')
        else:
            messagebox.showinfo('info', 'Numero correto')
    if (str(ed4.get()).isalpha()):
        messagebox.showwarning('cuidado', 'CEP contem letras')
    else:
        if cep == "":
            messagebox.showerror('erro', 'CEP vazio')
        else:
            messagebox.showinfo('info', 'CEP correto')
    bt2 = Button(root, text="Cadastrar", width=20, bg='#9400d3', foreground='white', command=click0)
    bt2.place(x=10, y=282)

def click0 ():
    nome = ed1.get()
    cpf = ed2.get()
    num = ed3.get()
    cep = ed4.get()
    mail = ed5.get()
    if nome == ""  or cpf == "" or num == "" or cep == "" or mail == "":
        messagebox.showerror('erro', 'informacoes invalidas')
    else:
        messagebox.showinfo('info', 'Cadastrado')
        bt1 = Button(root, text="Entra", width=20, bg='#9400d3', foreground= 'white', command=click1)
        bt1.place(x=225, y=350)
    if ed1.get() != "":
        Nom = ed1.get()
        Cpf = ed2.get()
        Num = ed3.get()
        Cep = ed4.get()
        Mail = ed5.get()
        edquery="INSERT INTO tabe (Nnome, Ccpf, Nnumr, Ccep, Ssenha) VALUES ('"+Nom+"','"+Cpf+"','"+Num+"','"+Cep+"','"+Mail+"')"
        banco.dml(edquery)
        ed1.delete(0, END)
        ed2.delete(0, END)
        ed3.delete(0, END)
        ed4.delete(0, END)
        ed5.delete(0, END)

        print('Dados Gravados')
    else:
        print('ERRO')
def click1 ():
    jen = Tk()
    root.destroy()
    jen.resizable(0, 0)
    class Application():
        def __init__(self):
            self.jen = jen
            self.jen.resizable(0, 0)
            self.tela()
            self.botoes()
            self.widgets_frame()
            jen.mainloop()

        def tela(self):
            self.jen.title(" Açai Da Sul ")
            self.jen.configure(background='#46295a')
            self.jen.geometry("600x400")
            self.jen.resizable(0, 0)
            self.jen.maxsize(width=900, height=700)
            self.jen.minsize(width=350, height=250)

        def botoes(self):
            self.frame_1 = Button(jen, text="Entra", width=20, bg='#9400d3', foreground='white', command=click2)
            self.frame_1.place(x=225, y=350)

        def widgets_frame(self):
            self.lb_codigo = Label(self.jen, text="⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⣿", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.01)
            self.lb_codigo = Label(self.jen, text="⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.06)
            self.lb_codigo = Label(self.jen, text="⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.11)
            self.lb_codigo = Label(self.jen, text="⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠋", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.16)
            self.lb_codigo = Label(self.jen, text="⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⢀", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.21)
            self.lb_codigo = Label(self.jen, text="⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.26)
            self.lb_codigo = Label(self.jen, text="⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.31)
            self.lb_codigo = Label(self.jen, text="⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⠃", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.36)
            self.lb_codigo = Label(self.jen, text="⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⠃", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.41)
            self.lb_codigo = Label(self.jen, text="⣿⣿⣿⣿⣿ ⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠄", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.46)
            self.lb_codigo = Label(self.jen, text="⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⣿⣦ ⣾⣿⣿⣿⣿⣛⠛⠁", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.51)
            self.lb_codigo = Label(self.jen, text="⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.56)
            self.lb_codigo = Label(self.jen, text="⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.61)
            self.lb_codigo = Label(self.jen, text="⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃", font=('Times', 10, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.0001, rely=0.66)
            self.lb_codigo = Label(self.jen, text=("Bem vindo clinte"), font=('Times', 9, 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.71, rely=0.8)
            self.lb_codigo = Label(self.jen, text="Açai da sul", font=('Times', 40, 'italic', 'bold',),
                                   bg='#46295a', foreground='white')
            self.lb_codigo.place(relx=0.50, rely=0.09)
    Application()

def click2 ():
    jan = Tk()
    class Application():
        def __init__(self):
            self.jan = jan
            self.tela()
            self.botoes()
            self.widgets_frame()
            jan.mainloop()

        def tela(self):
            self.jan.title(" Açai Da Sul ")
            self.jan.configure(background='#46295a')
            self.jan.geometry("600x400")
            self.jan.resizable(0, 0)
            self.jan.maxsize(width=900, height=700)
            self.jan.minsize(width=350, height=250)

        def botoes(self):
            self.frame_1 = Button(self.jan, bd=1.4, bg='#9400d3', foreground= 'white',
                                  text="Promoções", font=('Times', 11, 'italic'))
            self.frame_1.place(relx=0.2, rely=0.9,
                               relwid=0.2, relheight=0.06)
            self.frame_2 = Button(self.jan, bd=1.4, bg='#9400d3', foreground= 'white',
                                  text="Cardapio", font=('Times', 11, 'italic'))
            self.frame_2.place(relx=0.6, rely=0.9,
                               relwid=0.2, relheight=0.06)
            self.frame_3 = Button(self.jan, bd=1.4, bg='#9400d3', foreground= 'white',
                                  text="↵", font=('Times', 11,))
            self.frame_3.place(relx=0.578, rely=0.3,
                               relwid=0.05, relheight=0.06)
            self.frame_4 = Button(self.jan, bd=1.4, bg='#9400d3', foreground='white',
                                  text="Sair", font=('Times', 11,), command = click3)
            self.frame_4.place(relx=0.9, rely=0.10,
                               relwid=0.06, relheight=0.07)

        def widgets_frame(self):
            self.lb_codigo = Label(self.jan, text="Pedidos", font=('Times', 15, 'italic', 'bold',), bg='#46295a', foreground= 'white')
            self.lb_codigo.place(relx=0.45, rely=0.2)
            self.pedido_entry = Entry(self.jan, bg='#9400d3')
            self.pedido_entry.place(relx=0.37749, rely=0.298, relwid=0.2, relheight=0.062)
            self.pedido_entry = Entry(self.jan, bg='#9400d3')
            self.pedido_entry.place(relx=0.2, rely=0.4, relwid=0.6, relheight=0.3)
            self.lb_codigo = Label(self.pedido_entry, text="Bem vindo(a) a nossa pagina!!!",
                                   font=('Times', 12, 'italic', 'bold'), bg='#9400d3', foreground= 'white')
            self.lb_codigo.place(relx=0.222, rely=0.04)
            self.lb_codigo = Label(self.pedido_entry, text=" Aqui voçe encontra os melhores preços do mercado ",
                                   font=('Times', 12, 'italic', 'bold'), bg='#9400d3', foreground= 'white')
            self.lb_codigo.place(relx=0.02, rely=0.2)
            self.lb_codigo = Label(self.pedido_entry, text=" Autor: Antonio Jose ", font=('Times', 8, 'italic', 'bold'),
                                   bg='#9400d3', foreground= 'white')
            self.lb_codigo.place(relx=0.0046, rely=0.83)
    Application()

def click3 ():
    mess=messagebox.askyesno('sair', 'Voce tem certeza que quer sair ?',)
    if (mess==True):
        sys.exit()
    else:
        messagebox.showinfo('info', 'saida cancelada')


ed1 = Entry (root,  bg='#9400d3')
ed1.place(x= 10, y= 30, relwid=0.6, relheight=0.05)
ed5 = Entry (root,  bg='#9400d3')
ed5.place(x= 10, y= 75, relwid=0.4, relheight=0.05)
ed3 = Entry (root,  bg='#9400d3')
ed3.place(x= 10, y= 120, relwid=0.4, relheight=0.05)
ed4 = Entry (root,  bg='#9400d3')
ed4.place(x= 10, y= 165, relwid=0.4, relheight=0.05)
ed2 = Entry (root,  bg='#9400d3')
ed2.place(x= 10, y= 210, relwid=0.4, relheight=0.05)
ed6 = Entry (root,  bg='#9400d3')
ed6.place(x= 350, y= 130, relwid=0.32, relheight=0.25)


bt = Button(root, text= "Verificar", width=20,  bg='#9400d3', foreground= 'white', command = click)
bt.place(x=10, y=255)



lb1 = Label (root, text="Nome", bg='#46295a', foreground= 'white')
lb1.place(x= 10, y= 9)
lb2 = Label (root, text="CPF", bg='#46295a', foreground= 'white')
lb2.place(x= 10, y= 187)
lb3 = Label (root, text="Numero", bg='#46295a', foreground= 'white')
lb3.place(x= 10, y= 97)
lb4 = Label (root, text="CEP", bg='#46295a', foreground= 'white')
lb4.place(x= 10, y= 142)
lb5 = Label (root, text="Senha", bg='#46295a', foreground= 'white')
lb5.place(x= 10, y= 54)
lb6 = Label (root, text="Aviso", bg='#46295a', foreground= 'white')
lb6.place(x= 350, y= 130)
lb7 = Label (root, text="Ao realizar o cadastro voçe", bg='#9400d3', foreground= 'white')
lb7.place(x= 351, y= 155)
lb8 = Label (root, text="esta concordando com os termos", bg='#9400d3', foreground= 'white')
lb8.place(x= 351, y= 180)
lb8 = Label (root, text="e as politicas de privacidade. ", bg='#9400d3', foreground= 'white')
lb8.place(x= 351, y= 205)





root.geometry("600x400")
root.configure(background='#46295a')
root.resizable(0, 0)
root.title(" Açai Da Sul ")
root.mainloop ()