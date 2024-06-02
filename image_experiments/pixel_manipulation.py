import imageio.v3 as iio
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')


def print_image_info(image):
    height, width, channels = image.shape
    print("Height:", height)
    print("Width:", width)
    print("Number of channels:", channels)


def load_image_as_np_array(image_path):
    image = iio.imread(uri=image_path)
    return np.array(image)


def show_image(image):
    fig, ax = plt.subplots()
    ax.imshow(image)
    plt.show()


def change_pixels(y_pos, x_pos, size, color, source_image):
    h, w, c = source_image.shape
    if y_pos + size > h or x_pos + size > w:
        raise ValueError("The size of the new image is too large")
    y_value_upper = y_pos + size
    x_value_upper = x_pos + size
    source_image[y_pos:y_value_upper, x_pos:x_value_upper] = color
    return source_image


image = load_image_as_np_array("data/hertz.jpg")
print_image_info(image)
show_image(image)
color = []
for i in range(3):
    color.append(input("What color would you like to have? "))
size = input("What size would you like to have? ")
image = change_pixels(400, 800, int(size), color, image)
show_image(image)
