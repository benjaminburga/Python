import secrets
import string
import time
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader

print("Hola, bienvenido al generador de contraseñas")

def show_new_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    new_password = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return new_password

def save_passwords_as_pdf(passwords, dni_list, file_name, user_password):
    file_path = "C:/Users/burga/Desktop/new_Passwords.pdf"
    c = canvas.Canvas(file_path)
    c.setFont("Helvetica", 12)
    y = 750

    for i in range(len(passwords)):
        c.drawString(100, y, str(dni_list[i]))
        c.drawString(200, y, passwords[i])
        y -= 20
    c.save()

    output_pdf = PdfWriter()
    output_pdf.encrypt(user_password, owner_password=None)
    with open(file_path, "rb") as file:
        input_pdf = PdfReader(file)
        for page in input_pdf.pages:
            output_pdf.add_page(page)
        with open(file_path, "wb") as output_file:
            output_pdf.write(output_file)

    print(f"Contraseñas guardadas en '{file_name}.pdf' en su escritorio")

def main():
    passwords = []
    dni_list = []
    while True:
        try:
            file_name = "hash_passwords"
            longitud = int(input("Ingrese la longitud deseada para su contraseña: "))
            dni_user = (input("Ingrese el número de DNI: "))
            password = show_new_password(longitud)
            time.sleep(1)
            print("Generando su nueva contraseña...")
            time.sleep(3)
            print("¡Felicidades! Aquí tiene su nueva contraseña:")
            time.sleep(1)
            print(f"Su nueva contraseña es:\n{password}#{dni_user}")
            passwords.append(password)
            dni_list.append(dni_user)

            store_input = input("¿Desea guardarla en un archivo PDF? (si/no): ")
            if store_input.lower() == "si":
                user_password = input("Ingrese una contraseña para el archivo PDF: ")
                save_passwords_as_pdf(passwords, dni_list, file_name, user_password)
                print("El archivo PDF se ha guardado de forma segura con una contraseña.\n")
                continue
            else:
                break
        except ValueError:
            print("Error")

main()
