from geometry_calculations import calculate_area_circle, Rectangle, calculate_circumference_circle

radius = 5
area = calculate_area_circle(radius)
circumference = calculate_circumference_circle(radius)

print(f"Area of circle: {area}")
print(f"Circumference of circle: {circumference}")

rect = Rectangle(4, 6)
rect_area = rect.calculate_area()
rect_perimeter = rect.calculate_perimeter()

print(f"Area of rectangle: {rect_area}")
print(f"Perimeter of rectangle: {rect_perimeter}")