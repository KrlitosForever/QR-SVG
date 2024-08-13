import qrcode
from qrcode.image.svg import SvgPathImage

# URL que quieres transformar en un QR
url = 'https://tu-url-aqui.com'

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
