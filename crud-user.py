from tkinter import *
from tkinter import ttk,font
from mysql import create_user 
from mysql import get_end_id
class window():
    
    def __init__(self):
        self.crud  = Tk()
        self.crud.title("Nuevo")
        fuente = font.Font(weight='bold') #Fuente
        #self.crud.geometry("500x400")
        self.crud.resizable(width=False,height=False)
        #labels
        self.lbId = ttk.Label(self.crud,text="Id",font=fuente)
        self.lbUsuario = ttk.Label(self.crud,text="Usuario",font= fuente)
        self.lbPwd = ttk.Label(self.crud,text="Contraseña",font=fuente)
        #variables
        self.id = StringVar()
        self.id.set(str(get_end_id()))
        self.usuario = StringVar()
        self.contraseña = StringVar()
        #ttk Entry and buttons
        self.txtId =  ttk.Entry(self.crud,textvariable=self.id,width=10)
        self.txtUsuario = ttk.Entry(self.crud,textvariable=self.usuario,width=30)
        self.txtPwd = ttk.Entry(self.crud,textvariable=self.contraseña,width=30)
        self.txtSeparator = ttk.Separator(self.crud,orient=HORIZONTAL)
        self.btnAceptar = ttk.Button(self.crud,text="Guardar",command=self.save)
        self.btnClean   = ttk.Button(self.crud,text="Limpiar",command=self.clean)
        self.btnCancel  = ttk.Button(self.crud,text="Cancelar",command=self.crud.destroy)
        #orient pack
        self.lbId.pack(side=TOP,fill=BOTH,expand=True,padx=5,pady=5)
        self.txtId.pack(side=TOP,fill=BOTH,expand=True,padx=5,pady=5) 
        self.lbUsuario.pack(side=TOP,fill= BOTH,expand=True,padx=5,pady=5)
        self.txtUsuario.pack(side=TOP,fill=BOTH,expand=True,padx=5,pady=5)
        self.lbPwd.pack(side=TOP,fill= BOTH,expand=True,padx=5,pady=5)
        self.txtPwd.pack(side=TOP,fill=BOTH,expand=True,padx=5,pady=5)
        self.txtSeparator.pack(side=TOP,fill=BOTH,expand=True,padx=5,pady=5)
        self.btnAceptar.pack(side=LEFT,fill=BOTH,expand=True,padx=5,pady=5)
        self.btnClean.pack(side=LEFT,fill=BOTH,expand=True,padx=5,pady=5)
        self.btnCancel.pack(side=RIGHT,fill=BOTH,expand=True,padx=5,pady=5)
        self.txtUsuario.focus_set()
        self.crud.mainloop()
        
    def save(self):
        if self.usuario.get()!="" and self.contraseña.get()!="":
            if create_user(self.usuario.get(),self.contraseña.get()):
                print("""
USUARIO CREADO EXITOSAMENTE!!!!
name ==> {}
pwd  ==> {}
""".format(self.usuario.get(),self.usuario.get()))
        else:
            print("POR FAVOR RELLENE LOS CAMPOS SOLICITADOS")
    def clean(self):
        self.usuario.set("")
        self.contraseña.set("")
        self.txtUsuario.focus_set()


crud = window()


