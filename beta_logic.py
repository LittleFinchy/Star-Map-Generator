# (x, y) system bounded by a circle

# SETTINGS PAGE
'''
Number of stars - int (0, 1000000)
Background Color - int[index of array of options] (black, white, blue, yellow, )
Star Color - int[index of array of options] (black, white, blue, yellow, )
Rotate Text - int (-180, 180)
Curve Text - int (0, 45)
Size Text - int 
Connect Constellation Stars - bool
Image Size
'''

# ATTRIBUTES OF STARS
'''
Size - int
Amplitude - int
*Cluster - bool
Color (shade%) - float
'''

# ATTRIBUTES OF CONSTELLATIONS
'''
Location - int, int
Size - int
*Rotation - int
*Curvature - int
'''


import random
import math

star_list = []

number_of_stars = 100 #pull data from setting page

star_max_size = 10
star_colors = ["white"] #star colors data comes from settings page, the shade of that color 
ex = 2

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = math.floor(random.random() ** ex * star_max_size) + 1
        self.amp = random.randint(self.size, star_max_size)
        self.color = star_colors[random.randint(0, len(star_colors) - 1)]

    def cluster(self):
        pass #test without first




def star_placer():
    stars_added = 0
    while stars_added < number_of_stars:
        x, y = random.randint(0, 800), random.randint(0, 800)
        #if is_in_circle(x,y):
        temp_star = Star(x,y)
        # add temp star to image -- image += Star(x,y)
        stars_added += 1
        star_list.append(temp_star)
    return star_list


r = 390 #raduis
Xmin = Ymin = 5
Xmax = Ymax = 795

def is_in_circle(x, y):
    confines = r ** 2 - (Xmin ** 2 + Xmax ** 2 + Ymin ** 2 + Ymax ** 2)
    return x ** 2 - x*(Xmin + Xmax) - y*(Ymin + Ymax) + y ** 2 <= confines


sizes = []
test = star_placer()
for item in test:
    sizes.append(item.size)
print(sum(sizes))
print(sizes)

# without fix sum = 458
# with fix sum = 241