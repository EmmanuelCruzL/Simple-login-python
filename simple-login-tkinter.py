# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk, font
from mysql import login
import getpass

class Aplicion():
    ventana = 0
    posx_y = 0
    def __init__(self):

        self.raiz = Tk()
        self.raiz.title("Acceso")
        fuente = font.Font(weight='bold') #Fuente
        self.raiz.geometry("250x200")
        self.raiz.resizable(width=False,height=False)
        self.lbUsuario = ttk.Label(self.raiz,text="Usuario",font= fuente)
        self.lbPwd = ttk.Label(self.raiz,text="Contraseña",font=fuente)
        self.usuario = StringVar()
        self.contraseña = StringVar()
        #self.usuario.set(getpass.getuser())
        #self.contraseña.set(getpass.getpass)
        self.txtUser = ttk.Entry(self.raiz,textvariable=self.usuario,width=30)
        self.txtPwd  = ttk.Entry(self.raiz,textvariable=self.contraseña,width=30)
        self.txtSeparator = ttk.Separator(self.raiz,orient=HORIZONTAL)
        self.btnAcept = ttk.Button(self.raiz,text="Aceptar",command=self.aceptar)
        self.btnCancel = ttk.Button(self.raiz,text="Cancelar",command=quit)

        #positions
        self.lbUsuario.pack(side=TOP,fill= BOTH,expand=True,padx=5,pady=5)
        self.txtUser.pack(side=TOP,fill=BOTH,expand=True,padx=5,pady=5)
        self.lbPwd.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.txtPwd.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.txtSeparator.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.btnAcept.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.btnCancel.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
        self.txtPwd.focus_set()
        self.raiz.mainloop()

    def aceptar(self):
        if login(self.usuario.get(), self.contraseña.get()):
            print("Acceso permitido")
            print("Usuario:  " ,self.txtUser.get())
            print("Contraseña:", self.txtPwd.get())
        else:
            print("Acceso denegado")
            self.error()
            self.contraseña.set("")
            self.txtPwd.focus_set()

    def error(self):
        Aplicion.dialogo =Toplevel()
        Aplicion.ventana+=1
        Aplicion.posx_y +=50
        #self.dialogo.geometry("3")
        self.dialogo.resizable(0,0)
        ident = self.dialogo.winfo_id()
        self.dialogo.title("Error")
        fuente = font.Font(weight='bold')
        lbError =ttk.Label(self.dialogo,text="ERROR CONTRASEÑA",font=fuente)
        btn     =ttk.Button(self.dialogo,text="Aceptar",command=self.dialogo.destroy)
        lbError.pack(side=TOP,padx=20,pady=20)
        btn.pack(side=BOTTOM,padx=20,pady=20)
        self.dialogo.transient(master=self.raiz)
        self.dialogo.grab_set()
        self.raiz.wait_window(self.dialogo)


def main():
    mi_app =Aplicion()

if __name__ == '__main__':
    main()
