from PIL import Image

def set_image(image_path: str) -> Image:
    img = Image.open(image_path)
    img_width, img_height = img.size
    # TODO resize and return the resized img
    return img

if __name__ == "__main__":
    print("Image module")
