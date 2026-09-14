import tkinter as tk


def saludar(entrada_nombre: tk.Entry, etiqueta_saludo: tk.Label) -> None:
    """Función que obtiene el nombre del cuadro de texto

    y actualiza la etiqueta con un saludo personalizado.
    """
    nombre: str = entrada_nombre.get().strip()

    if nombre:
        etiqueta_saludo.config(text=f"¡Hola, {nombre}! Bienvenido a Tkinter.")
    else:
        etiqueta_saludo.config(
            text="Por favor, introduce tu nombre.", fg="#ff4d4d"
        )


def crear_interfaz() -> None:
    """Función para inicializar y configurar la interfaz gráfica con Tkinter."""
    # Crear la ventana principal (640x480)
    ventana: tk.Tk = tk.Tk()
    ventana.title("Saludo Personalizado")
    ventana.geometry("640x480")
    ventana.configure(bg="#f4f4f9")

    # Título principal
    titulo: tk.Label = tk.Label(
        ventana,
        text="Aplicación de Saludo",
        font=("Arial", 22, "bold"),
        bg="#f4f4f9",
        fg="#333333",
    )
    titulo.pack(pady=40)

    # Etiqueta de instrucción para el cuadro de texto
    lbl_instruccion: tk.Label = tk.Label(
        ventana,
        text="Escribe tu nombre:",
        font=("Arial", 14),
        bg="#f4f4f9",
        fg="#555555",
    )
    lbl_instruccion.pack(pady=5)

    # Cuadro de texto (Entry) para que el usuario escriba su nombre
    entrada_nombre: tk.Entry = tk.Entry(
        ventana, font=("Arial", 14), width=30, justify="center"
    )
    entrada_nombre.pack(pady=10)
    # Enfocar el cursor automáticamente en el cuadro de texto
    entrada_nombre.focus()

    # Botón para disparar la acción de saludar
    # Usamos lambda para poder pasarle los argumentos a la función 'saludar'
    boton_saludar: tk.Button = tk.Button(
        ventana,
        text="Saludar",
        font=("Arial", 14, "bold"),
        bg="#4CAF50",
        fg="white",
        padx=15,
        pady=5,
        command=lambda: saludar(entrada_nombre, etiqueta_saludo),
    )
    boton_saludar.pack(pady=20)

    # Etiqueta donde se mostrará el resultado del saludo (inicialmente vacía)
    etiqueta_saludo: tk.Label = tk.Label(
        ventana,
        text="",
        font=("Arial", 16),
        bg="#f4f4f9",
        fg="#2196F3",
    )
    etiqueta_saludo.pack(pady=30)

    # Iniciar el bucle principal de la aplicación
    ventana.mainloop()


if __name__ == "__main__":
    crear_interfaz()