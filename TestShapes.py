import unittest
from Shapes import *

class TestShapes(unittest.TestCase):


# Select a shape:
# 1. Circle
# 2. Square
# 3. Rhombus
# 4. Cube
# 5. Cylinder

# After basic size information is entered, the program will output
 # circumference/area/volume
#  of the shape, and the number of sides for the shape.

  @classmethod
  def setUp(self):
    self.shapes = Shapes()


  def test_circle_circumfrence(self):
    self.assertEqual(self.shapes.create_circle(4), 25.13)

  def test_square_volume(self):
    self.assertEqual(self.shapes.create_square(4), 16)

  def test_Rhombus_area(self):
    self.assertEqual(self.shapes.create_rhombus(4,4), 8)

  def test_cube_surface_area(self):
    self.assertEqual(self.shapes.create_cube(4), 64)

  def test_cylinder_volume(self):
    self.assertEqual(self.shapes.create_cylinder(4,4), 200.96)
    # V=πrh


if __name__ == '__main__':
  unittest.main()
