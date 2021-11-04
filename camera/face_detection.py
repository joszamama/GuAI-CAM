import cv2
import time
import datetime
import variables as VAR
from send_email import send_email


def start_recording():
    cap = cv2.VideoCapture(0)
    
    face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    detection = False
    detection_stopped_time = None
    timer_started = False
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,  # Frame a analizar.
                                            1.05,  # Entre 1 y 1.5, menor es más certero y más lento.
                                            6)  # Coincidencias mínimas a encontrar en cada nodo. Más alto, más intenso.

        if len(faces) > 0:
            if detection:
                timer_started = False
            else:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                output = cv2.VideoWriter(
                    f"recordings/{current_time}.mp4", fourcc, VAR.FRAME_RATE, frame_size)
                print("Grabando...")
        
        elif detection:
            if timer_started:
                if time.time() - detection_stopped_time >= VAR.SECONDS_TO_WAIT:
                    detection = False
                    timer_started = False
                    output.release()
                    print("Fin de la grabación")
                    send_email(VAR.MESSAGE + "http://host/directorio/" + current_time + ".mp4")
            else:
                timer_started = True
                detection_stopped_time = time.time()
        

        if detection:
            output.write(frame)
        
        cv2.imshow("Camera", frame)
        
        if cv2.waitKey(1) == ord('q'):
            break

    output.release()
    cap.release()
    cv2.destroyAllWindows()