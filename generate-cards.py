from PIL import Image

def place_qr_on_template(qr_path, template_path, output_path, top_left, bottom_right):
    # Open the template and QR image
    with Image.open(template_path) as template, Image.open(qr_path) as qr:
        # Resize the QR to fit into the specified square
        qr = qr.resize((bottom_right[0] - top_left[0], bottom_right[1] - top_left[1]))
        
        # Paste the QR code onto the template at the specified position
        template.paste(qr, top_left)
        
        # Save as PNG for lossless compression
        template.save(output_path, 'PNG')

def main():
    template_path = "template.png"
    top_left = (586, 145)
    bottom_right = (755, 312)
    
    # Process 1000 QR codes
    for i in range(1, 1001):
        qr_path = f"QR_{i}.jpeg"
        output_path = f"templated_QR_{i}.png"
        place_qr_on_template(qr_path, template_path, output_path, top_left, bottom_right)

if __name__ == "__main__":
    main()
