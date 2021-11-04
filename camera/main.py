from face_detection import start_recording
from glob import glob
from pymediainfo import MediaInfo
from tkinter import *
from PIL import ImageTk; import os


def main():
    raiz = Tk()
    menu = Menu(raiz)

    raiz.iconbitmap("resources\images\cam.ico")
    raiz.title("GuAI CAM")

    def open_listbox():
        lb = Listbox(raiz)
        lb.pack()
        fl = glob("C:\\Users\\joszamama\\Videos\\GuAI CAM\\*.mp4")
        for f in fl:
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

        lb.bind("<<ListboxSelect>>", lambda x: see_properties())

    # CÁMARA
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Comenzar", command=start_recording)
    menudatos.add_command(label="Detener", command=ord("q"))
    menudatos.add_command(label="Salir", command=raiz.quit)
    menu.add_cascade(label="Cámara", menu=menudatos)

    # DIRECTORIO
    menudatos = Menu(menu, tearoff=0)
    menudatos.add_command(label="Grabaciones", command=open_listbox)
    menu.add_cascade(label="Archivos", menu=menudatos)

    canvas = Canvas(width=430, height=275)
    canvas.pack(expand=YES, fill=BOTH)

    image = ImageTk.PhotoImage(file="resources\images\cam_banner.jpg")
    canvas.create_image(88, 10, image=image, anchor=NW)

    raiz.config(menu=menu)
    raiz.mainloop()


if __name__ == "__main__":
    main()
