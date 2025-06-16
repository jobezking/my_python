import geometry_calculations as geo

radius = 5
area = geo.calculate_area_circle(radius)
circumference = geo.calculate_circumference_circle(radius)

print(f"Area of circle: {area}")
print(f"Circumference of circle: {circumference}")

rect = geo.Rectangle(4, 6)
rect_area = rect.calculate_area()
rect_perimeter = rect.calculate_perimeter()

print(f"Area of rectangle: {rect_area}")
print(f"Perimeter of rectangle: {rect_perimeter}")