# Arc length of an angle

def arclength():
    pi=3.14159
    diameter = float(input('Diameter of circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    arc_length = (pi*diameter) * (angle/360)
    print("Arc Length is: ", arc_length)

arclength()
