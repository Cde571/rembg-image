from rembg import remove

# Ruta de la imagen de entrada y salida
input_path = r"C:\Users\caco2\Desktop\youtube\129734281.jpg"
output_path = r"C:\Users\caco2\Desktop\youtube\129734281_sin_fondo.png"

# Lee la imagen de entrada y crea una nueva imagen sin fondo
with open(input_path, 'rb') as i:
    input_data = i.read()
    output_data = remove(input_data)
    with open(output_path, 'wb') as o:
        o.write(output_data)
