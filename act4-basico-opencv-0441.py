# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
import win32gui
import win32con
import os
from PIL import Image
nombre_ventana = 'img taehbb Ramirez Azul NC 0441 '
cv2.namedWindow(nombre_ventana)


print("+-+-+-+-Ramirez Azul NC 0441+-+-+-+-+")
# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")  # Imprime el título de la sección en la consola.
nombre_ventana = 'Gpo 3Himg taehbb Ramirez Azul NC 0441 ' # Linea nueva
taehbb = cv2.imread('taehbb.jpg')  # Lee la imagen 'sample_image.jpg' y la guarda como matriz en 'img'.
cv2.namedWindow(nombre_ventana) # linea nueva

if taehbb is None:  # Verifica si la variable 'img' está vacía (es decir, si no encontró el archivo).
    print("Error: No se pudo leer 'sample_image.jpg'. Revisa el nombre y ubicación.")  # Muestra mensaje de error.
    sys.exit()  # Detiene inmediatamente la ejecución del programa para evitar fallos posteriores.
else:  # Si la imagen sí se cargó correctamente...
    print("Imagen cargada exitosamente.")  # Confirma en consola que la imagen está lista.

    
# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN")  # Imprime el título de la segunda sección.
height, width, channels = taehbb.shape  # Extrae el alto (filas), ancho (columnas) y canales de color de la matriz.
print(f"Dimensiones de la imagen: {width}x{height} píxeles")  # Muestra el ancho por el alto en consola.
print(f"Número de canales de color: {channels}")  # Muestra cuántos canales tiene (3 para BGR: Azul, Verde, Rojo).
print(f"Tipo de dato de la imagen: {taehbb.dtype}")  # Muestra el tipo de dato (uint8 = enteros de 0 a 255).
print(f"Total de datos/píxeles: {taehbb.size}")  # Muestra la cantidad total de valores numéricos en la matriz.

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL")  # Imprime el título de la tercera sección.
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")  # Instrucción para el usuario.
cv2.imshow('Imagen taehbb Original Ramirez Azul NC 0441', taehbb)  # Abre una ventana llamada 'Imagen Original' y muestra la imagen cargada.
cv2.imshow(nombre_ventana, taehbb)
cv2.waitKey(0)  # Pausa el programa infinitamente hasta que el usuario presione una tecla.
## ---cargando icono--

Image.open('icono.jpg').save('icono_temp.ico', format='ICO', sizes=[(32, 32)])

hwnd = win32gui.FindWindow(None, 'Imagen taehbb Original  Ramirtez Azul NC 0441')
hicon = win32gui.LoadImage(0, 'icono_temp.ico', win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE)
win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_SMALL, hicon)


# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")  # Imprime el título de la cuarta sección.
pixel_taehbb = taehbb.copy()  # Crea una copia exacta de la imagen original para no dañar la original.

y, x = 100, 150  # Define las coordenadas a analizar: fila (Y) = 100, columna (X) = 150.
pixel = pixel_taehbb[y, x]  # Obtiene los 3 valores de color [Azul, Verde, Rojo] del píxel en esa posición.
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")  # Imprime los valores BGR del píxel en consola.

pixel_taehbb[y, x] = [0, 0, 255]  # Cambia el color de ese único píxel a Rojo puro (0 Azul, 0 Verde, 255 Rojo).
cv2.circle(pixel_taehbb, (x, y), 15, (0, 255, 255), 2)  # Dibuja un círculo amarillo alrededor para poder verlo a simple vista.

cv2.imshow('Pixel Modificado Ramirez Azul NC 0441', pixel_taehbb)  # Muestra la imagen con el píxel alterado y señalado.
cv2.waitKey(0)  # Espera a que se presione una tecla para continuar.

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI) Ramirez Azul NC 0441")  # Imprime el título de la quinta sección.
roi_taehbb = taehbb.copy()  # Crea una nueva copia limpia de la imagen original.

roi = roi_taehbb[50:200, 100:300]  # Recorta una sub-matriz desde la fila 50 a 200 y columna 100 a 300.
cv2.rectangle(roi_taehbb, (100, 50), (300, 200), (0, 255, 0), 2)  # Dibuja un rectángulo verde marcando la zona recortada.

cv2.imshow('Imagen con ROI marcada Ramirez Azul NC 0441', roi_taehbb)  # Muestra la imagen completa con el recuadro verde.
cv2.waitKey(0)  # Espera a que se presione una tecla.

cv2.imshow('ROI Extraida (Recorte) Ramirez Azul NC 0441', roi)  # Muestra únicamente el pedazo recortado en una ventana aparte.
cv2.waitKey(0)  # Espera a que se presione una tecla.
# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")  # Imprime el título de la sexta sección.
b, g, r = cv2.split(taehbb)  # Divide la imagen a color en 3 matrices independientes: Azul (b), Verde (g) y Rojo (r).

cv2.imshow('Canal Azul (Escala de grises) Ramirez Azul NC 0441', b)  # Muestra la intensidad del canal azul en tonos de gris.
cv2.imshow('Canal Verde (Escala de grises) Ramirez Azul NC 0441', g)  # Muestra la intensidad del canal verde en tonos de gris.
cv2.imshow('Canal Rojo (Escala de grises) Ramirez Azul NC 0441', r)  # Muestra la intensidad del canal rojo en tonos de gris.
cv2.waitKey(0)  # Pausa el programa mientras observas las 3 ventanas en blanco y negro.

zeros = np.zeros_like(b)  # Crea una matriz llena de ceros (negro) del mismo tamaño que un canal.
blue_taehbb = cv2.merge([b, zeros, zeros])  # Une el canal azul real con verde y rojo en cero (solo se ve azul).
green_taehbb = cv2.merge([zeros, g, zeros])  # Une el canal verde real con azul y rojo en cero (solo se ve verde).
red_taehbb = cv2.merge([zeros, zeros, r])  # Une el canal rojo real con azul y verde en cero (solo se ve rojo).

cv2.imshow('Canal Azul (Coloreado) Ramirez Azul NC 0441',blue_taehbb)  # Muestra la imagen filtrada únicamente en color azul.
cv2.imshow('Canal Verde (Coloreado)  Ramirez Azul NC 0441', green_taehbb)  # Muestra la imagen filtrada únicamente en color verde.
cv2.imshow('Canal Rojo (Coloreado)  Ramirez Azul NC 0441', red_taehbb)  # Muestra la imagen filtrada únicamente en color rojo.
cv2.waitKey(0)  # Espera a que se presione una tecla para avanzar.

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")  # Imprime el título de la séptima sección.
resized_taehbb = cv2.resize(taehbb, (400, 300))  # Cambia el tamaño exacto de la imagen a 400px de ancho por 300px de alto.
cv2.imshow('Redimensionada a 400x300  Ramirez Azul NC 0441', resized_taehbb)  # Muestra la imagen con sus nuevas dimensiones fijas.
cv2.waitKey(0)  # Espera a que se presione una tecla.

half_size = cv2.resize(taehbb, None, fx=0.5, fy=0.5)  # Reduce la imagen a la mitad (50% en ancho y 50% en alto).
double_size = cv2.resize(taehbb, None, fx=1.5, fy=1.5)  # Amplía la imagen un 50% extra (escala 1.5x).

cv2.imshow('Mitad de tamano (0.5x) Ramirez Azul NC 0441', half_size)  # Muestra la versión reducida.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.imshow('Ampliada (1.5x)', double_size)  # Muestra la versión ampliada.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")  # Imprime el título de la octava sección.
height, width = taehbb.shape[:2]  # Obtiene nuevamente el alto y ancho actual de la imagen original.
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)  # Calcula la matriz para girar 45° desde el centro.
rotated_img = cv2.warpAffine(taehbb, rotation_matrix, (width, height))  # Aplica la rotación matemática sobre la imagen.

cv2.imshow('Imagen Rotada (45 grados) Ramirez Azul NC 0441', rotated_img)  # Muestra la imagen inclinada 45 grados.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")  # Imprime el título de la novena sección.
horizontal_flip = cv2.flip(taehbb, 1)  # Voltea la imagen horizontalmente (código 1 = efecto espejo).
cv2.imshow('Volteo Horizontal (Espejo) Ramirez Azul NC 0441', horizontal_flip)  # Muestra el volteo horizontal.
cv2.waitKey(0)  # Espera a que se presione una tecla.

vertical_flip = cv2.flip(taehbb, 0)  # Voltea la imagen verticalmente (código 0 = de cabeza).
cv2.imshow('Volteo Vertical (De cabeza) Ramirez Azul NC 0441', vertical_flip)  # Muestra el volteo vertical.
cv2.waitKey(0)  # Espera a que se presione una tecla.

both_flip = cv2.flip(taehbb, -1)  # Voltea en ambos ejes al mismo tiempo (código -1 = horizontal + vertical).
cv2.imshow('Volteo en Ambos Ejes Ramirez Azul NC 0441', both_flip)  # Muestra el volteo combinado.
cv2.waitKey(0)  # Espera a que se presione una tecla.

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")  # Imprime el título de la décima sección.
result = cv2.imwrite('rotated_taehbb.jpg', rotated_img)  # Guarda la imagen rotada en el disco duro como 'rotated_taehbb.jpg'.

if result:  # Comprueba si el guardado devolvió True (verdadero).
    print("Imagen rotada guardada exitosamente como 'rotated_taehbb.jpg'")  # Confirma que el archivo se creó.
else:  # Si ocurrió algún problema de permisos o ruta...
    print("Error: No se pudo guardar la imagen rotada.")  # Notifica el fallo en consola.

cv2.destroyAllWindows()  # Cierra todas las ventanas gráficas abiertas por OpenCV para liberar memoria RAM.
# Cierra todas las ventanas gráficas abiertas por OpenCV para liberar memoria RAM.

print("\n¡Todas las operaciones se completaron con éxito!") # Mensaje final de cierre en la terminal. 