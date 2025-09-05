from PIL import Image, ImageDraw

images = []

width = 200
center = width // 2
color_1 = (0, 255, 0)  # Green
color_2 = (255, 0, 0)  # Red
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new("RGB", (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i,
                  center + i, center + i),
                 fill=color_1)
    images.append(im)

# Save the GIF without the deprecated 'optimize' parameter
images[0].save("pillow_imagedraw.gif",
               save_all=True,
               append_images=images[1:],
               duration=10,
               loop=0)  # loop=0 means loop forever