# /*
#  * Colocar una marca de agua en un video proporcionado por un usuario,
#  * segun las especificaciones de dicho usuario. 
#  * La posicion de la marca de agua debe ser indicada utilizando como
#  * referencia una grilla de 3x3, o en la totalidad de la imagen.
#  * Ademas debe darse la opcion de guardar el video en disco duro.
#  */

import cv2 

def reproducir_video(video):
    cap = cv2.VideoCapture(video)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    ruta_video = '/home/thinkpad/Escritorio/PythonPracticas/pruebaVideo.mp4'  # Ruta de tu video
    reproducir_video(ruta_video)

if __name__ == '__main__':    
    main()







"""
importamos opencv e intentamos mostrar el video por consola.
"""