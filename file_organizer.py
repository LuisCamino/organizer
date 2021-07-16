import os
import shutil


# bloque texto
txt_array = [".txt", ".TXT", ".doc", ".DOC",
             ".docx", ".DOCX", ".odt", ".ODT", ".wri", ".WRI"]
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
img_array = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png",
             ".PNG", ".tif", ".TIF", ".tiff", ".TIFF", ".svg", ".SVG"]
for img_file in os.listdir("./"):
    for im in img_array:
        current_img = img_file
        target_img = im

        if os.path.isdir('photos'):
            if img_file.endswith(target_img):
                shutil.move(current_img, "./photos")

        else:
            if img_file.endswith(target_img):
                if current_img:
                    os.mkdir("photos")
                    shutil.move(current_img, "./photos")

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

# bloque presentaciones
pst_array = [".pptx", ".PPTX", ".pptm", ".PPTM", ".ppt", ".PPT"]
for pst_file in os.listdir("./"):
    for pst in pst_array:
        current_pst = pst_file
        target_pst = pst

        if os.path.isdir('presentations'):
            if pst_file.endswith(target_pst):
                shutil.move(current_pst, "./presentations")

        else:
            if pst_file.endswith(target_pst):
                if current_pst:
                    os.mkdir("presentations")
                    shutil.move(current_pst, "./presentations")

# bloque calc
clc_array = [".csv", ".CSV", ".xlsx",
             ".XLSX", ".xls", ".XLS", ".xlt", ".XLT", ]
for clc_file in os.listdir("./"):
    for clc in clc_array:
        current_clc = clc_file
        target_clc = clc

        if os.path.isdir('calc'):
            if clc_file.endswith(target_clc):
                shutil.move(current_clc, "./calc")

        else:
            if clc_file.endswith(target_clc):
                if current_clc:
                    os.mkdir("calc")
                    shutil.move(current_clc, "./calc")

# bloque calc
cmp_array = [".rar", ".RAR", ".zip", ".ZIP", ".tar.gz",
             ".TARG.GZ", ".7zip", ".7ZIP", ".7z", ".7Z"]
for cmp_file in os.listdir("./"):
    for cmp in cmp_array:
        current_cmp = cmp_file
        target_cmp = cmp

        if os.path.isdir('rar'):
            if cmp_file.endswith(target_cmp):
                shutil.move(current_cmp, "./rar")

        else:
            if cmp_file.endswith(target_cmp):
                if current_cmp:
                    os.mkdir("rar")
                    shutil.move(current_cmp, "./rar")

# bloque programas
exe_array = [".lnk", ".LNK", ".exe", ".EXE"]
for exe_file in os.listdir("./"):
    for exe in exe_array:
        current_exe = exe_file
        target_exe = exe

        if os.path.isdir('programs'):
            if exe_file.endswith(target_exe):
                shutil.move(current_exe, "./programs")

        else:
            if exe_file.endswith(target_exe):
                if current_exe:
                    os.mkdir("programs")
                    shutil.move(current_exe, "./programs")


# bloque videos
vid_array = [".mp4", ".MP4", ".mov", ".MOV",
             ".flv", ".FLV", ".wmv", ".WMV", ".avi", ".AVI", ".asf", ".ASF"]
for vid_file in os.listdir("./"):
    for vid in vid_array:
        current_vid = vid_file
        target_vid = vid

        if os.path.isdir('videos'):
            if vid_file.endswith(target_vid):
                shutil.move(current_vid, "./videos")

        else:
            if vid_file.endswith(target_vid):
                if current_vid:
                    os.mkdir("videos")
                    shutil.move(current_vid, "./videos")
