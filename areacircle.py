def arearectangle(length, width):
        area = length * width
        print(area)


def areatriangle(length, width, height):
        area = (1/2 * (width * height))
        print(area)


def areacircle(radius):
        area = 3.14 * (radius ** 2)
        print(area)


def areasquare(length):
        area = length * length
        print(area)

def main():
    arearectangle(5, 2)
    areatriangle(5, 2, 3)
    areacircle(3)
    areasquare(4)
main()

def circle_area(radius):
    return  3.14 * (radius ** 2)

def main():
    x = circle_area(5) 
    print(x)
main()
    