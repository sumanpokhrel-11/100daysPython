import colorgram
images = colorgram.extract('hirstSample.jpg',30)

mycolor = []
for i in range(20):
    image = images[i]
    color = image.rgb
    r= color.r
    g = color.g
    b = color.b
    rgb = (r, g, b)
    mycolor.append(rgb)


print(mycolor)