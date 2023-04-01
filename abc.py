import qrcode
import img
qr = qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)

y = """
Name : Vishwajeet Kumar Sudhanshu,
Gender: Male,
Branch: AI/ML,
Year: 1st Year.
"""
qr.add_data(y)
qr.make(fit=True)
img = qr.make_image(fill_color = 'red',back_color='white')
img.save("vishwajeet.png")