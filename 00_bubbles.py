import simple_draw as sd

sd.resolution = (1200, 600)
'''point = sd.get_point(150, 400)
radius = 50
for i in range(5):
    sd.circle(point, radius)
    radius += 5'''


def buble(point, step, colour):
    radius = 50
    for i in range(3):
        sd.circle(point, radius, colour)
        radius += step


for i in range(100):
    point = sd.random_point()
    colour = sd.random_color()
    buble(point, 10, colour)


'''for i in range(100, 400, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, i)
        buble(point, 10)'''

sd.pause()
