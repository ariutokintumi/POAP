import qrcode
from PIL import Image

def generate_qr(link, filename):
    # Create a QR instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% or less errors can be corrected
        box_size=12,  # size of each box in the QR grid
        border=2,  # Border size
    )

    # Add data to the QR instance
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR instance
    img = qr.make_image(fill_color="black", back_color="white")

    dpi_value = 300  # Dots per inch for printing
    img = img.resize((int(4 * dpi_value / 2.54), int(4 * dpi_value / 2.54)))  # Resize to 4x4 cm at 300 dpi
    img.save(filename, 'JPEG', quality=95)

def main():
    with open("links.txt", "r") as file:
        links = file.readlines()
        for i, link in enumerate(links):
            link = link.strip()  # Remove any whitespace
            generate_qr(link, f"QR_{i+1}.jpeg")

if __name__ == "__main__":
    main()
