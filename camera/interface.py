from face_detection import start_recording
from tkinter import *


def ventana_principal():
    raiz = Tk()
    menu = Menu(raiz)

    # CÁMARA
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Comenzar", command=start_recording)
    menudatos.add_command(label="Detener", command=ord('q'))
    menudatos.add_command(label="Salir", command=raiz.quit)
    menu.add_cascade(label="Cámara", menu=menudatos)

    raiz.config(menu=menu)
    raiz.mainloop()

while True:
    ventana_principal()