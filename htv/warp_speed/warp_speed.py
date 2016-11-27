from PIL import Image

im = Image.open('warp_speed.5978d1405660e365872cf72dddc7515603f657f12526bd61e56feacf332cccad.jpg', 'r')
width, height = im.size
pixel_values = list(im.getdata())
shifted = []
interval = 8

for c in range(0, 31):
    for i in range(8*c, 8*(c+1)):
        for j in range(8*c, 500+8*c):
            shifted.append(pixel_values[width*i + j])
    for i in range(8*c, 8*(c+1)):
        for j in range(500+8*c+4, 1000):
            shifted.append(pixel_values[width*i + j])
        if c != 30:
            for j in range(0, 8*c+4):
                shifted.append(pixel_values[width*(i+8) + j])
        else:
            for j in range(0, 4*c+2):
                shifted.append(pixel_values[width*(i+2) + j])
            for j in range(0, 4*c+2):
                shifted.append(pixel_values[width*(i+2) + j + 500])

image_out = Image.new(im.mode, (500,8*2*31+4))
image_out.putdata(shifted)
image_out.save('test_out.jpg')
