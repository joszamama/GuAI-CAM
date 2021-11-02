from face_detection import start_recording
from tkinter import *
from tkinter import messagebox


def ventana_principal():
    raiz = Tk()
    menu = Menu(raiz)

    #DATOS
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Cargar", command=start_recording)
    menudatos.add_command(label="Listar", command=ord('q'))
    menudatos.add_command(label="Salir", command=raiz.quit)
    menu.add_cascade(label="Datos", menu=menudatos)

    raiz.config(menu=menu)
    raiz.mainloop()

while True:
    ventana_principal()