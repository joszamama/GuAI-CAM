from face_detection import start_recording
<<<<<<< HEAD
from glob import glob
from pymediainfo import MediaInfo
from tkinter import *
from PIL import ImageTk; import os
=======
from tkinter import *
import os
from glob import glob 
from pymediainfo import MediaInfo
from PIL import ImageTk
>>>>>>> 465e670a1abbf34594e9cf3e668bd683723c90cd


def main():
    raiz = Tk()
    menu = Menu(raiz)

<<<<<<< HEAD
    raiz.iconbitmap("resources\images\cam.ico")
=======
    raiz.iconbitmap('resources\images\cam.ico')
>>>>>>> 465e670a1abbf34594e9cf3e668bd683723c90cd
    raiz.title("GuAI CAM")

    def open_listbox():
        lb = Listbox(raiz)
        lb.pack()
        fl = glob("C:\\Users\\joszamama\\Videos\\GuAI CAM\\*.mp4")
        for f in fl:
<<<<<<< HEAD
            lb.insert(0, f)

        def fname():
            return lb.get(lb.curselection())

        def play():
            os.startfile(fname())

        lb.bind("<Double-Button>", lambda x: play())

        la = Label(raiz, text="Select a file")
        la.pack()

        def see_properties():
            size = os.path.getsize(fname()) // 1000000
            duration = MediaInfo.parse(fname())
            ms = int(duration.tracks[0].duration / 3600) * 4
            filedata = f"File size: {size:n} MB\n Duration: {ms} seconds"
            la["text"] = filedata

=======
            lb.insert(0,f)
    
        def fname():
            return lb.get(lb.curselection())
        
        def play():
            os.startfile(fname())
    
        lb.bind("<Double-Button>", lambda x: play())
        
        la = Label(raiz, text = "Select a file")
        la.pack()
        
        def see_properties():
            size = os.path.getsize(fname()) // 1000000
            duration = MediaInfo.parse(fname())
            ms = int(duration.tracks[0].duration / 3600) *4
            filedata = f"File size: {size:n} MB\n Duration: {ms} seconds"
            la['text'] = filedata
    
>>>>>>> 465e670a1abbf34594e9cf3e668bd683723c90cd
        lb.bind("<<ListboxSelect>>", lambda x: see_properties())

    # CÁMARA
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Comenzar", command=start_recording)
<<<<<<< HEAD
    menudatos.add_command(label="Detener", command=ord("q"))
=======
    menudatos.add_command(label="Detener", command=ord('q'))
>>>>>>> 465e670a1abbf34594e9cf3e668bd683723c90cd
    menudatos.add_command(label="Salir", command=raiz.quit)
    menu.add_cascade(label="Cámara", menu=menudatos)

    # DIRECTORIO
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Grabaciones", command=open_listbox)
    menu.add_cascade(label="Archivos", menu=menudatos)

    canvas = Canvas(width=430, height=275)
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file="resources\images\cam_banner.jpg")
<<<<<<< HEAD
    canvas.create_image(88, 10, image=image, anchor=NW)
=======
    canvas.create_image(88, 10, image=image, anchor=NW) 
>>>>>>> 465e670a1abbf34594e9cf3e668bd683723c90cd

    raiz.config(menu=menu)
    raiz.mainloop()


<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======

if __name__ == "__main__":
    main()
>>>>>>> 465e670a1abbf34594e9cf3e668bd683723c90cd
