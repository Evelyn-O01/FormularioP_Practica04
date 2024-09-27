import tkinter as tk 
from tkinter import Radiobutton, messagebox

def clear ():
    tbNombre.delete (0,tk.END)
    tbApellidos.delete (0,tk.END)
    tbEstatura.delete (0,tk.END)
    tbTelefono.delete (0,tk.END)
    tbEdad.delete (0,tk.END)
    varGenero.set (0)
    
def save():
    nombre = tbNombre.get()
    apellidos = tbApellidos.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    edad = tbEdad.get()
    genero = ""
    if varGenero.get() ==1:
        genero = "Masculino"
    elif varGenero.get() ==2:
        genero = "Femenino"
        
    data = "Nombres: " + nombre + "\nApellidos: " + apellidos + "\nEstatura: " + estatura + "\nTelefono: " + telefono + "\nEdad: " + edad + "\nGenero: " + genero
    with open ("302024Data.txt", "a") as file: 
      file.write(data + "\n\n")
    
    messagebox.showinfo ("Informacion" + "Datos guardados correctamente\n\n", data)

ventana = tk.Tk()
ventana.geometry ("520x500")
ventana.title ("FormularioP")

varGenero = tk.IntVar()

lbNombre = tk.Label (ventana, text = "Nombre: ")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()
lbApellidos = tk.Label (ventana, text = "Apellidos: ")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()
lbEstatura = tk.Label (ventana, text = "Estatura: ")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()
lbTelefono = tk.Label (ventana, text = "Telefono: ")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()
lbEdad = tk.Label (ventana, text = "Edad: ")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()
lbGenero = tk.Label (ventana, text = "Genero: ")
lbGenero.pack()
rbMasculino =  Radiobutton (ventana, text = "Masculino", variable = varGenero, value=1)
rbMasculino.pack ()
rbFemenino = Radiobutton (ventana, text = "Femenino", variable = varGenero, value =2)
rbFemenino.pack()

btnClear = tk.Button (ventana, text = "Borrar valores", command=clear)
btnClear.pack()
btnSave= tk.Button (ventana, text = "Guardar valores" , command=save)
btnSave.pack()
ventana.mainloop()
