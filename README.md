# 🚀 Generador de Códigos QR en SVG 🎨

¡Bienvenido al **Generador de Códigos QR en SVG**! Este pequeño pero poderoso script en Python te permite crear códigos QR en formato SVG de manera rápida y sencilla. ¿Necesitas un código QR para tu sitio web, tu perfil de GitHub o simplemente para impresionar a tus amigos? ¡Este es tu lugar! 🎉

## ¿Qué hace este proyecto? 🤔

Este script toma una URL (o cualquier texto que quieras convertir en un código QR) y genera un archivo SVG con un código QR que puedes usar en cualquier lugar. ¡Es como magia, pero con código! ✨

## ¿Cómo funciona? 🛠️

El código utiliza la biblioteca `qrcode` para generar el código QR y luego lo guarda en un archivo SVG utilizando `SvgPathImage`. Aquí tienes un resumen de lo que hace:

1. **Importa las bibliotecas necesarias**: `qrcode` y `SvgPathImage`.
2. **Define la URL** que quieres convertir en un código QR.
3. **Configura el código QR**: tamaño, corrección de errores, etc.
4. **Genera el código QR** y lo guarda en un archivo SVG.

## ¿Cómo lo uso? 🖥️

1. **Clona este repositorio** o descarga el script.
2. **Instala las dependencias** necesarias (si no las tienes ya):
   ```bash
   pip install qrcode[pil]
   ```
3. **Edita el script** y cambia la variable `url` por la URL que quieras convertir.
4. **Ejecuta el script**:
   ```bash
   python generar_qr.py
   ```
5. **¡Listo!** Encuentra tu archivo `qrcode.svg` en el directorio del proyecto.

## Ejemplo de uso 🎯

```python
# URL que quieres transformar en un QR
url = 'https://github.com/tu-usuario/tu-repositorio'

# Generar el QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen SVG del QR
img = qr.make_image(image_factory=SvgPathImage)
img.save('qrcode.svg')
```

## ¿Por qué SVG? 🖼️

- **Escalabilidad**: Los archivos SVG son vectoriales, lo que significa que puedes escalarlos a cualquier tamaño sin perder calidad.
- **Compatibilidad**: Los SVG son compatibles con la mayoría de los navegadores y editores de imágenes.
- **Ligero**: Los archivos SVG suelen ser más pequeños que los formatos de imagen rasterizada como PNG o JPEG.

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes alguna idea para mejorar este proyecto, no dudes en hacer un fork y enviar un pull request. ¡Juntos podemos hacer que este generador de códigos QR sea aún más genial! 🚀

## Licencia 📜

Este proyecto está licenciado bajo la GNU GPL v3, lo que permite la modificación, siempre y cuando se compartan públicamente las mejoras.
