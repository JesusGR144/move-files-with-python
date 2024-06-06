import tkinter as tk
import shutil
import glob

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    
    window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# def say_hello():
#     name = entry.get()
#     greeting = "¡Hola, {}!".format(name) if name else "¡Hola, mundo!"
#     if checkbox_var.get():
#         greeting += " ¡Has marcado el checkbox!"
#     label.config(text=greeting)

def move_files():
    src_path = entrySrc.get()
    dest_path = entryDest.get()
    file_extension = entryExt.get()

    lblSrc.config(text="Origen: "+src_path)    
    lblDest.config(text="Destino: "+dest_path)

    #Obteniendo el valor actual del checkbox
    search_subfolders = checkbox_var.get()

    # Obtener la lista de archivos con la extensión especificada
    if search_subfolders:
        files_to_move = glob.glob(src_path + '/**/*.' + file_extension, recursive=True)
    else:
        files_to_move = glob.glob(src_path + '/*.' + file_extension)


    try:
        #Mover los archivos
        for file in files_to_move:
            shutil.move(file, dest_path)
        # print("Archivos movidos exitosamente")
        lblStatus.config(text="STATUS: Archivos movidos con éxito", foreground="white")
    except Exception as e:
        # print("Error al mover archivos",e)    
        lblStatus.config(text="STATUS: Error al mover archivos")

    if not files_to_move:
        lblStatus.config(text="STATUS: No se encontraron archivos con la extensión ."+file_extension, foreground="red")

root = tk.Tk()
root.title("Mover archivos")

#Componentes para la ruta de origen
lblSrc = tk.Label(root, text="Ruta origen")
lblSrc.pack(pady=10)

entrySrc = tk.Entry(root)
entrySrc.pack(pady=5)

#Componentes para la ruta de destino
lblDest = tk.Label(root, text="Ruta destino")
lblDest.pack(pady=10)

entryDest = tk.Entry(root)
entryDest.pack(pady=5)

#Componentes para la extension
lblExt = tk.Label(root, text="Extension de los archivos")
lblExt.pack(pady=10)

entryExt = tk.Entry(root)
entryExt.pack(pady=5)

#STATUS
lblStatus = tk.Label(root, text="STATUS")
lblStatus.pack(pady=10)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Busqueda en subcarpetas", variable=checkbox_var)
checkbox.pack(pady=5)

button = tk.Button(root, text="Mover", #command=say_hello#
                   command=move_files)
button.pack(pady=5)

# Obtener el ancho y alto de la ventana
window_width = 300
window_height = 350

# Centrar la ventana en la pantalla
center_window(root, window_width, window_height)

root.mainloop()
