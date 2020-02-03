import math

pi = math.pi

class picture:
    def __init__(self, n, w, h):
        self.name = n
        self.width, self.height = (w, h)
        self.pixels = [[[0, 1, 2] for i in range(self.width)] for j in range(self.height)]

def coolify_pic(g):
    a = 1
    b = 1
    for x in range(g.width):
        for y in range(g.height):
            n = g.pixels[x][y]
            n[0] = a % 256
            n[1] = b % 256
        a = a + 1
        b = b + 2

# int(math.sin(pi * a))
# int(math.cos(pi * b))

def print_pic(g):
    s = ""
    for x in range(g.width):
        for y in range(g.height):
            n = g.pixels[x][y]
            s += str(n[0]) + " " + str(n[1]) + " " + str(n[2]) + " "
        s += "\n"
    #print(s)
    return s

n = picture('image', 500, 500)
coolify_pic(n)
#print_pic(n)

f = open("image.ppm", "w")
f.write("P3\n500 500\n255\n")

f.write(print_pic(n))


f.close()
print('image.ppm')
