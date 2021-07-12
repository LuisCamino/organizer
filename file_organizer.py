import os
import shutil


# bloque texto
txt_array = [".txt", ".doc", ".docx", "odt", "wri"]
if os.path.isdir('text'):
    for txt_file in os.listdir("./"):
        for tex in txt_array:
            if txt_file.endswith(tex):
                shutil.move(txt_file, "./text")

else:
    os.mkdir("text")
    for txt_file in os.listdir("./"):
        if txt_file.endswith(".txt") or txt_file.endswith(".doc"):
            shutil.move(txt_file, "./text")


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
