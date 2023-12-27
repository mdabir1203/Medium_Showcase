from PIL import Image, ImageChops
import numpy as np

# Paths to the uploaded images
image_paths = [
    "/home/mabbas/a/data/1.jpeg",
    "/home/mabbas/a/data/2.jpeg",
    "/home/mabbas/a/data/3.jpeg",
    "/home/mabbas/a/data/4.jpeg",
    "/home/mabbas/a/data/5.jpeg",
    "/home/mabbas/a/data/6.jpeg"
]

# Load the images
images = [Image.open(path) for path in image_paths]

# Ensure all images are the same size
min_shape = sorted((np.sum(i.size), i.size) for i in images)[0][1]
images = [i.resize(min_shape, Image.LANCZOS) for i in images]

# Create an empty list to store the processed images
frames = []

# Generate frames for the GIF by overlaying the images
for i in range(len(images)):
    # Start with a transparent image
    if i == 0:
        composite_image = Image.new('RGBA', min_shape)
    else:
        composite_image = frames[-1]
    composite_image = ImageChops.multiply(composite_image, images[i].convert('RGBA'))
    frames.append(composite_image)

# Save the frames as a GIF
gif_path = "color_fractal_animation.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], optimize=False, duration=500, loop=0)

gif_path
