import math
import time
class Shapes():

  def show_menu(self):


    print('Select a shape. ')
    print("1. Circle")
    print("2. Square")
    print("3. Rhombus")
    print("4. Cube")
    print("5. Cylinder")
    print("6. Exit")
    user_choice = input(">")

    if user_choice == "1":
       print("Enter radius value.")
       rad = int(input(">"))
       print("The total circumfrence of the Circle is:")
       print(self.create_circle(rad))

    if user_choice == "2":
       print("Enter base value.")
       base = int(input(">"))
       print("Enter height value.")
       height = int(input(">"))
       print("The total volume of the Square is:")
       print(self.create_square(base, height))

    if user_choice == "3":
       print("Enter first diagnol value.")
       diag1 = int(input(">"))
       print("Enter second diagnol value.")
       diag2= int(input(">"))
       print("The total area of the Rhombus is:")
       print(self.create_rhombus(diag1, diag2))

    if user_choice == "4":
       print("Enter edge value.")
       edge = int(input(">"))
       print("The total area of the Cube is:")
       print(self.create_cube(edge))

    if user_choice == "5":
       print("Enter radius value.")
       rads = int(input(">"))
       print("Enter height value.")
       heights = int(input(">"))
       print("The total volume of the Cylinder is:")
       print(self.create_cylinder(rads, heights))

    if user_choice != "6":
       self.show_menu()
    # if user_choice == "6":
    #    quit()

  def create_circle(self, num):
    # C=2πr
    circ = (2 * 3.14 * num)
    sides = 0
    return circ

  def create_square(self, num1, num2):
    # A=a2
    squar = (num1 * num2)
    return squar

  def create_rhombus(self, num1, num2):
    # A=pq / 2
    rhomb = (num1 * num2 / 2)
    return rhomb

  def create_cube(self, num):
    # V=a3
    cub = (num * num * num)
    return cub

  def create_cylinder(self, num1, num2):
    # V=πr2h
    cyli = (3.14 * (num1 * num1) * num2)
    return cyli

if __name__ == '__main__':
  shape = Shapes()
  shape.show_menu()
