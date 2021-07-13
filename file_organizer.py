import os
import shutil


# bloque texto
txt_array = [".txt", ".doc", ".docx", "odt", "wri"]
for txt_file in os.listdir("./"):
    for tex in txt_array:
        fila = txt_file
        filo = tex

        if os.path.isdir('text'):
            if txt_file.endswith(filo):
                shutil.move(fila, "./text")

        else:

            if txt_file.endswith(filo):
                if fila:
                    os.mkdir("text")
                    shutil.move(fila, "./text")


# bloque imagenes
img_array = [".jpg", ".jpeg", ".png"]
if os.path.isdir('img'):
    for img_file in os.listdir("./"):
        if img_file.endswith(".jpg") or img_file.endswith(".png") or img_file.endswith(".jpeg"):
            shutil.move(img_file, "./img")
else:
    os.mkdir("img")
    for img_file in os.listdir("./"):
        if img_file.endswith(".jpg") or img_file.endswith(".png") or img_file.endswith(".jpeg"):
            shutil.move(img_file, "./img")
