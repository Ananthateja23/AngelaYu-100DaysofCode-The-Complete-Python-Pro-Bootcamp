"""
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('Image.jpg', 10)
print(colors)
print(colors[0])
print(colors[0].rgb)
print(tuple(colors[0].rgb))
rgb_color = []
for color in colors:
    rgb_color.append(tuple(color.rgb))

print(rgb_color)
"""

# first install colorgram from PyPI
# then Import colorgram
import colorgram

# extracts the most occured colors
colors = colorgram.extract('Image1.jpg', 30)

# logic to store the colors in a rgb_colors list
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)


# After running the code, copy the output and store it on color_list
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
