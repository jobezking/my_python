def calculate_diameter_circle(radius: float) -> float:
  """This function calculates the diameter of a circle.
  Arg:
      radius, a float representing the circle's radius
  Returns:
      the diameter of a circule (float) 
  Raises:
        ValueError: If radius is zero.
  """
  if radius < 0:
    raise ValueError("Radius cannot be negative.")
 
  return 2 * radius