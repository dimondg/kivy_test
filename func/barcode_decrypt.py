def decode(image):
    import cv2
    from pyzbar.pyzbar import decode
    from PIL import Image
    image_barcode = Image.open(f"../{image}")
    decoded = decode(image_barcode)
    print(decoded[0].data.decode("utf8"))


decode("IMG_1697.jpg")
