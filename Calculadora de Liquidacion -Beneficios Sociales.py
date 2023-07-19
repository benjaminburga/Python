import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.messagebox as messagebox
from reportlab.lib.units import inch
from reportlab.lib.colors import Color, lightgrey
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import time
import datetime

cts = []
gratificaciones = []
vacacion = []
sueldo = []
total = []
monthe = []

def calculator_cts():
    salary = float(entry_sueldo.get())
    sueldo.append(salary)
    month = float(entry_meses_cts.get())
    new_month = month * 30
    salary_quarter = salary / 6
    new_salary = salary_quarter + salary
    new_cts = new_salary / 360 * new_month
    cts.append(new_cts)
    label_resultado_cts.config(text=f"Tu CTS sería: {new_cts:.2f}")
    monthe.append(month)

def calculator_gratificacion():
    gratificacion = float(entry_meses_gratificacion.get())
    new_gratificacion = sueldo[0] / 6
    new_gratificacion *= gratificacion
    gratificaciones.append(new_gratificacion)
    label_resultado_gratificacion.config(text=f"Te correspondería: {new_gratificacion:.2f}")

def calculator_vacaciones():
    vacaciones = float(entry_meses_vacaciones.get())
    new_vacaciones = sueldo[0] / 12
    new_vacaciones *= vacaciones
    vacacion.append(new_vacaciones)
    label_resultado_vacaciones.config(text=f"Te correspondería: {new_vacaciones:.2f} por tus vacaciones")

def guardar_resultados(show_cts, show_vacation, show_gratificacion, show_total, ruta_guardado):
    # Crear un nuevo archivo PDF
    fecha = time.strftime("%Y-%m-%d", time.localtime())
    nombre_archivo = f"liquidacion_{fecha}.pdf"
    c = canvas.Canvas(ruta_guardado, pagesize=(8.5 * inch, 11 * inch))
    hora_actual = datetime.datetime.now().strftime("HORA DE RESULTADO : %H:%M")

    c.setFont("Helvetica",9)
    c.setTitle(nombre_archivo)
    c.drawString(450,730,hora_actual )


    # Agregar el logotipo al archivo PDF
    logo_path = "C:/Users/burga/OneDrive/Escritorio/PRACTICES/LOGO PY/logo.png"  # Reemplaza con la ruta real de tu logotipo
    logo = ImageReader(logo_path)
    c.drawImage(logo,18, 670, width=120, height=120)  # Ajusta las coordenadas y dimensiones según tus necesidades


    # Agregar el título al archivo PDF
    c.setFont("Helvetica-Bold", 20)  # Set the font and size for the title
    c.drawString(120, 670, "LIQUIDACION DE BENEFICIOS SOCIALES")  # Specify the position and text for the title
    c.drawString(90, 650 , f"{'-' * 70} ")
    
    
    c.drawCentredString(4.25 * inch, 8.5 * inch, "RESULTADOS")
    c.setFont("Helvetica", 10)
    c.drawCentredString(4.25 * inch, 8.2* inch, fecha)
    c.setFont("Helvetica", 12)

    
    # Agregar el texto con los resultados al archivo PDF
    c.setFont("Helvetica", 12)  # Set the font and size for the text
    c.drawString(100, 490, show_cts)
    c.drawString(100, 470, show_vacation)
    c.drawString(100, 450, show_gratificacion)
    c.drawString(350,430 , f"{'-'* 30}")
    c.drawString(100, 410, f"TOTAL: {' ' * 60 }S/  {show_total:.2f}")


    #Agregar comentario al final del pdf
    c.drawString(40,60,f"Thank you for using our application, currently in development. Please note that the information ")
    c.drawString(40,50 ,f"provided is based on calculations from the Peruvian government and is not a legal document. ")
    c.drawString(30,20,f"{'>' * 30} Benjamin Burga © 2023 {'>' * 30}")
   
    # Agregar marca de agua
    c.saveState()
    c.setFillColor(lightgrey)  # Set the color for the watermark
    c.setFont("Helvetica", 15)
    c.drawCentredString(290, 150, "POWERED BY BENJAMIN BURGA")
    c.restoreState()

    # Guardar y cerrar el archivo PDF
    c.showPage()

    c.save()
    messagebox.showinfo("Guardado exitoso", "El archivo se ha guardado correctamente.")

def calculator_show():
    label_resultado_cts.config(text=f"CTS: {cts[0]:.2f}")
    label_resultado_gratificacion.config(text=f"Gratificación: {gratificaciones[0]:.2f}")
    label_resultado_vacaciones.config(text=f"Vacaciones: {vacacion[0]:.2f}")
    show_gratificacion = f"Gratificación ({monthe[0]:.1f} meses) : {' ' * 40} S/  {gratificaciones[0]:.2f}"
    show_cts = f"CTS: ({monthe[0]:.1f} meses) : {' ' * 50} S/  {cts[0]:.2f} "
    show_vacation = f"Vacaciones: ({monthe[0]:.1f} meses) : {' ' *40} S/  {vacacion[0]:.2f}"
    show_total = gratificaciones[0] + vacacion[0] + cts[0]
    ruta_guardado = seleccionar_ruta_guardado()
    if ruta_guardado:
        guardar_resultados(show_cts, show_vacation, show_gratificacion, show_total, ruta_guardado)

def seleccionar_ruta_guardado():
    ruta_guardado = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Archivos PDF", "*.pdf")],
        title="Seleccionar ruta de guardado"
    )
    return ruta_guardado

def exit_program():
    time.sleep(1)
    print("Gracias por usar nuestros servicios\n")
    print("POWERED BY BENJAMIN BURGA - BANJUB")
    ventana.destroy()
    messagebox.showinfo("Benjamin Burga says " ,"Gracias por usar la APP EN DESARROLLO \n                Copyright @BANJUB")

def resetear_datos():
    cts.clear()
    gratificaciones.clear()
    vacacion.clear()
    sueldo.clear()
    entry_sueldo.delete(0, tk.END)
    entry_meses_cts.delete(0, tk.END)
    entry_meses_gratificacion.delete(0, tk.END)
    entry_meses_vacaciones.delete(0, tk.END)
    label_resultado_cts.config(text="")
    label_resultado_gratificacion.config(text="")
    label_resultado_vacaciones.config(text="")
    #label_resultado_total.config(text="")

ventana = tk.Tk()
ventana.title("Calculadora de Liquidación")
ventana.geometry("400x600")

label_titulo = ttk.Label(ventana, text="Calculadora de Liquidación ", font=("Arial", 16))
label_titulo.pack(pady=10)

style = ttk.Style()
style.configure("Titulo.TLabel", font=("Arial", 16))
style.configure("Resultado.TLabel", font=("Arial", 12), foreground="blue")
style.configure("Boton.TButton", font=("Arial", 12), foreground="white", background="blue")
style.map("Boton.TButton", foreground=[("active", "white")], background=[("active", "darkblue")])

label_sueldo = ttk.Label(ventana, text="Sueldo:")
label_sueldo.pack()

entry_sueldo = ttk.Entry(ventana,width=30)
entry_sueldo.pack(padx=10 ,pady=10)

label_meses_cts = ttk.Label(ventana, text="Meses para CTS:")
label_meses_cts.pack()

entry_meses_cts = ttk.Entry(ventana)
entry_meses_cts.pack()

btn_calcular_cts = ttk.Button(ventana, text="Calcular CTS", command=calculator_cts)
btn_calcular_cts.pack(pady=10)

label_resultado_cts = ttk.Label(ventana, text="")
label_resultado_cts.pack()

label_meses_gratificacion = ttk.Label(ventana, text="Meses para Gratificación:")
label_meses_gratificacion.pack()

entry_meses_gratificacion = ttk.Entry(ventana)
entry_meses_gratificacion.pack()

btn_calcular_gratificacion = ttk.Button(ventana, text="Calcular Gratificación", command=calculator_gratificacion)
btn_calcular_gratificacion.pack(pady=10)

label_resultado_gratificacion = ttk.Label(ventana, text="")
label_resultado_gratificacion.pack()

label_meses_vacaciones = ttk.Label(ventana, text="Meses para Vacaciones:")
label_meses_vacaciones.pack()

entry_meses_vacaciones = ttk.Entry(ventana)
entry_meses_vacaciones.pack()

btn_calcular_vacaciones = ttk.Button(ventana, text="Calcular Vacaciones", command=calculator_vacaciones)
btn_calcular_vacaciones.pack(pady=10)

label_resultado_vacaciones = ttk.Label(ventana, text="")
label_resultado_vacaciones.pack()

btn_guardar = ttk.Button(ventana, text="SUMAR Y GUARDAR EN PDF ", command=calculator_show , width=45)
btn_guardar.pack(pady=10 ,padx=10)

btn_reset = ttk.Button(ventana, text="Resetear Datos", command=resetear_datos)
btn_reset.pack(pady=10)

btn_exit = ttk.Button(ventana, text="Salir", command=exit_program)
btn_exit.pack(pady=10, padx=10)

label_titulo = ttk.Label(ventana, text="Powered by BENJAMIN BURGA ", font=("Arial", 9))
label_titulo.pack(pady=10)


ventana.mainloop()
