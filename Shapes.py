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
       rad = int(input("Enter radius."))
       self.create_circle(rad)

    if user_choice == "2":
       base = int(input("Enter base."))
       height = int(input("Enter height. "))
       self.create_square(base, height)

    if user_choice == "3":
       diag1 = int(input("Enter Diagonal p. "))
       diag2= int(input("Enter Diagnonal q. "))
       self.create_rhombus(diag1, diag2)

    if user_choice != "6":
       self.show_menu()

  def create_circle(self, num):


    intList = []

