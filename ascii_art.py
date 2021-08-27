import PIL.Image

ASCII_CHARS_II = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
# SPACE = " "

# ASCII_CHARS_II = [" ", ".", ",", ":", ";", "+", "o", "x", "%", "#", "@"]

# Resizing image


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)

# Converting image to greyscale


def greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()

    characters = "".join([ASCII_CHARS_II[pixel // 25] for pixel in pixels])
    return (characters)


def main(new_width=100):
    path = input("Enter the path to the image field: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image!")

    # Convert image to ASCII
    new_image_data = pixel_to_ascii(greyscale(resize_image(image)))

    # Format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    # print(ascii_image)
    # print(SPACE)
    # Save the string to a file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
        # f.write(SPACE)

main()
