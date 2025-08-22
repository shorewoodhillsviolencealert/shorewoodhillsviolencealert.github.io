import qrcode

data = "shorewoodhillsviolencealert.github.io"

img = qrcode.make(data)

img.save("shva_qrcode.png")
