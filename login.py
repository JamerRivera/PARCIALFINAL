import tkinter as tk
from tkinter import PhotoImage, Toplevel

def abrir_informacion():
    info_ventana = Toplevel()
    info_ventana.title("Información")
    info_ventana.geometry("800x600")
    info_ventana.config(bg="white")

    opciones = ["AQUI PUEDES ENCONTRAR INFORMACIÓN SOBRE LA UNIVERSIDAD"]
    for opcion in opciones:
        label = tk.Label(info_ventana, text=opcion, font=("Arial", 12), bg="white", fg="black")
        label.pack(pady=10)

def abrir_configuracion():
    config_ventana = Toplevel()
    config_ventana.title("Configuración")
    config_ventana.geometry("800x600")
    config_ventana.config(bg="white")

    opciones = ["AQUI CONFIGURAS ToDO ESTA EN FASE BETA"]
    for opcion in opciones:
        label = tk.Label(config_ventana, text=opcion, font=("Arial", 12), bg="white", fg="black")
        label.pack(pady=10)

def cerrar_sesion(ventana):
    ventana.destroy()

def unitecnar():
    ventana = tk.Tk()
    ventana.title("Unitecnar")
    ventana.geometry("800x600")
    ventana.config(bg="black")

    superior = tk.Frame(ventana, bg="navy", height=50)
    superior.pack(side="top", fill="x")

    correo = tk.Label(superior, text="jamersdlg@gmail.com", font=("Arial", 12), bg="#333333", fg="white", anchor="e", padx=20)
    correo.pack(side="right", pady=10)

    titulo = tk.Label(superior, text="ANTONIO DE AREVALO UNITECNAR", font=("Arial", 18, "bold"), bg="#333333", fg="white", anchor="w", padx=20)
    titulo.pack(side="left", pady=10)

    frame_contenido = tk.Frame(ventana, bg="darkblue", height=600)
    frame_contenido.pack(fill="both", expand=True)

    barra_lateral = tk.Frame(frame_contenido, bg="#222222", width=180, height=600, padx=5, pady=5)
    barra_lateral.pack(side="left", fill="y")

    try:
        imagen_icono = PhotoImage(file=r"C:\Users\jamer\Desktop\PARCIAL3FINAL\imagenes\perfil.png").subsample(4, 4)
        label_imagen = tk.Label(barra_lateral, image=imagen_icono, bg="#222222")
        label_imagen.pack(pady=10)
    except:
        label_imagen = tk.Label(barra_lateral, text="Icono", bg="navy", fg="white", width=15, height=5)
        label_imagen.pack(pady=10)

    opciones = ["Inicio", "Perfil", "Imagen", "Información", "Configuración", "Cerrar sesión"]
    for opcion in opciones:
        if opcion == "Configuración":
            button = tk.Button(barra_lateral, text=opcion, bg="#222222", fg="white", width=18, height=2, relief="flat", anchor="w", command=abrir_configuracion)
        elif opcion == "Cerrar sesión":
            button = tk.Button(barra_lateral, text=opcion, bg="#222222", fg="white", width=18, height=2, relief="flat", anchor="w", command=lambda: cerrar_sesion(ventana))
        elif opcion == "Información":
            button = tk.Button(barra_lateral, text=opcion, bg="#222222", fg="white", width=18, height=2, relief="flat", anchor="w", command=abrir_informacion)
        else:
            button = tk.Button(barra_lateral, text=opcion, bg="#222222", fg="white", width=18, height=2, relief="flat", anchor="w")
        button.pack(pady=5)

    separator = tk.Frame(frame_contenido, bg="white", height=2)
    separator.pack(side="left", fill="x")

    contenedor_imagen = tk.Frame(frame_contenido, bg="navy", width=600, height=600)
    contenedor_imagen.pack(side="right", fill="both", expand=True)

    try:
        imagen_grande = PhotoImage(file=r"C:\Users\jamer\Desktop\PARCIAL3FINAL\imagenes\logo.png")
        label_imagen_grande = tk.Label(contenedor_imagen, image=imagen_grande)
        label_imagen_grande.pack(fill="both", expand=True)
    except:
        label_imagen_grande = tk.Label(contenedor_imagen, text="", bg="lightgray", width=50, height=25)
        label_imagen_grande.pack(fill="both", expand=True)

    ventana.mainloop()

if __name__ == "__main__":
    unitecnar()