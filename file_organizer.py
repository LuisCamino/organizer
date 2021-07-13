import os
import shutil


# bloque texto
txt_array = [".txt", ".doc", ".docx", ".odt", ".wri"]
for txt_file in os.listdir("./"):
    for tex in txt_array:
        current_text = txt_file
        target_text = tex

        if os.path.isdir('text'):
            if txt_file.endswith(target_text):
                shutil.move(current_text, "./text")

        else:
            if txt_file.endswith(target_text):
                if current_text:
                    os.mkdir("text")
                    shutil.move(current_text, "./text")


# bloque imagenes
img_array = [".jpg", ".png", ".jpeg", ".tif", ".tiff", ".svg"]
for img_file in os.listdir("./"):
    for im in img_array:
        current_img = img_file
        target_img = im

        if os.path.isdir('img'):
            if img_file.endswith(target_img):
                shutil.move(current_img, "./img")

        else:
            if img_file.endswith(target_img):
                if current_img:
                    os.mkdir("img")
                    shutil.move(current_img, "./img")

# bloque pdf
pdf_array = [".pdf", ".PDF"]
for pdf_file in os.listdir("./"):
    for pf in pdf_array:
        current_pdf = pdf_file
        target_pdf = pf

        if os.path.isdir('pdf'):
            if pdf_file.endswith(target_pdf):
                shutil.move(current_pdf, "./pdf")

        else:
            if pdf_file.endswith(target_pdf):
                if current_pdf:
                    os.mkdir("pdf")
                    shutil.move(current_pdf, "./pdf")
