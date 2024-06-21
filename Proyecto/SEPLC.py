import mysql.connector
from mysql.connector import errorcode
import tkinter as tk
from tkinter import messagebox

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            user='root',  # reemplaza 'tu_usuario' con tu usuario de MySQL
            password='xHMu.&aw12.SD',  # reemplaza 'tu_contraseña' con tu contraseña de MySQL
            host='127.0.0.1',
            database='BASE1'
        )
        return conexion
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está mal con tu usuario o contraseña")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe")
        else:
            print(err)
        return None

def sistema_experto(salidas, protocolo_comunicacion, tipo_plc):
    conexion = conectar_bd()
    if conexion is None:
        return "No se pudo conectar a la base de datos."

    cursor = conexion.cursor()

    query = '''
        SELECT nombre FROM plc
        WHERE salidas = %s AND protocolo_comunicacion = %s AND tipo_plc = %s
        LIMIT 1
    '''
    cursor.execute(query, (salidas, protocolo_comunicacion, tipo_plc))
    
    resultado = cursor.fetchone()
    conexion.close()
    
    if resultado:
        return f"Se recomienda utilizar el PLC: {resultado[0]}"
    else:
        return "No se encontró un PLC que cumpla con los requisitos especificados."

def mostrar_recomendacion():
    salidas = salidas_var.get()
    protocolo_comunicacion = protocolo_comunicacion_var.get()
    tipo_plc = tipo_plc_var.get()

    recomendacion = sistema_experto(salidas, protocolo_comunicacion, tipo_plc)
    messagebox.showinfo("Recomendación del PLC", recomendacion)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto para Elegir PLC")

# Variables para las opciones
salidas_var = tk.StringVar(value="relevador")
protocolo_comunicacion_var = tk.StringVar(value="RS232")
tipo_plc_var = tk.StringVar(value="sin pantalla HMI")

# Crear widgets
tk.Label(ventana, text="Seleccione las características del PLC:").grid(row=0, columnspan=2, pady=10)

tk.Label(ventana, text="Salidas del PLC:").grid(row=1, column=0, sticky='e')
tk.Radiobutton(ventana, text="Relevador", variable=salidas_var, value="relevador").grid(row=1, column=1, sticky='w')
tk.Radiobutton(ventana, text="Transistor NPN", variable=salidas_var, value="transistor npn").grid(row=2, column=1, sticky='w')
tk.Radiobutton(ventana, text="Transistor PNP", variable=salidas_var, value="transistor pnp").grid(row=3, column=1, sticky='w')

tk.Label(ventana, text="Protocolo de Comunicación:").grid(row=4, column=0, sticky='e')
tk.Radiobutton(ventana, text="RS232", variable=protocolo_comunicacion_var, value="RS232").grid(row=4, column=1, sticky='w')
tk.Radiobutton(ventana, text="S7 sobre ISO TCP RFC1006", variable=protocolo_comunicacion_var, value="S7 sobre ISO TCP RFC1006").grid(row=5, column=1, sticky='w')
tk.Radiobutton(ventana, text="Mini DIN8 RS485", variable=protocolo_comunicacion_var, value="Mini DIN8 RS485").grid(row=6, column=1, sticky='w')

tk.Label(ventana, text="Tipo de PLC:").grid(row=7, column=0, sticky='e')
tk.Radiobutton(ventana, text="Sin pantalla HMI", variable=tipo_plc_var, value="sin pantalla HMI").grid(row=7, column=1, sticky='w')
tk.Radiobutton(ventana, text="Con pantalla HMI", variable=tipo_plc_var, value="con pantalla HMI").grid(row=8, column=1, sticky='w')

tk.Button(ventana, text="Obtener Recomendación", command=mostrar_recomendacion).grid(row=9, columnspan=2, pady=20)

# Ejecutar la aplicación
ventana.mainloop()

