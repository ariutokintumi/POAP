from PIL import Image

def combine_images(image_paths, output_path, rows, cols, gap): 
    # Open the images
    images = [Image.open(path) for path in image_paths]

    # Determine the size for the combined image
    img_width, img_height = images[0].size
    total_width = cols * img_width + (cols - 1) * gap
    total_height = rows * img_height + (rows - 1) * gap

    # Create a blank white image
    combined_img = Image.new("RGB", (total_width, total_height), "white")

    # Place each image onto the combined image
    for idx, img in enumerate(images):
        row = idx // cols
        col = idx % cols
        x = col * (img_width + gap)
        y = row * (img_height + gap)
        combined_img.paste(img, (x, y))

    combined_img.save(output_path)

def main():
    # Customizable parameters
    total_images = 1000
    rows = 6
    cols = 2
    gap = 5
    images_per_combined = rows * cols

    for i in range(0, total_images, images_per_combined):
        image_paths = [f"templated_QR_{j+1}.png" for j in range(i, i + images_per_combined) if j < total_images]
        output_path = f"combined_{i//images_per_combined + 1}.png"
        combine_images(image_paths, output_path, rows, cols, gap)

if __name__ == "__main__":
    main()
