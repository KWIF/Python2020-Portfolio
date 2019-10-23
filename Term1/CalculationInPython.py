#Kendra Davis, Angelina Coronel

# Checked by: Karter Ence, Xander Szykowsy, Jamerson McGuire, and Michael Calhoun

# Logical Error: Bad formatting with ASCII art (shape gets messed up with user values)
# Runtime Error: Entering a string crashes the program (includes using commas in a number)
# Logical Error: input is displayed with no spaces next to questions.
# Logical Error: Does not truncate number as a whole, ends up messing with the ASCII art even more
# Logical Error: Supports entering negative numbers even though that is not physically possible
# Logical Error: Does not truncate decimal points within the ASCII art
# Runtime Error: Crashes when using operators within the input

#Perimeter of a square
squareA = input("Enter Square Side Measurement")
squareResult= (4*float(squareA))
areaResult= float(squareA) **2
squareArt= str.format("""
           {0}
   @--------------@
   |                  |
   |                  |
{0}|                  |{0}
   |                  |
   |                  |
   @--------------@
           {0}""",squareA)
print(squareArt)
print(str.format("Perimeter = {0:.2f}" , squareResult))
 #Area of a Square
print(str.format("Area = {0:.2f}" , areaResult))

circleR = input("Enter Radius")

circleResult = (2*3.14*float(circleR))
circleArt = str.format("""

                    %%%    %%%
          %%%                        %%%

   %%%                                      %%%

 %%%                    {0}                   %%%
                              %%%%%%%%%%%
 %%%                                          %%%

  %%%                                      %%%

        %%%                         %%%

                  %%%     %%%

""",circleR)

print(circleArt)
print(str.format("Circumference {0:.2f}",circleResult))

#Area Of a Triangle

triH = input("Enter Triangle's Height")
triB = input("Enter Triangle's Base")
triResult = float(triH) * float(triB) /2
triArt = str.format("""
              @
              /|\\
             / | \\    
            /  |  \\
           /   |   \\
          /    |    \\
         /     |     \\
        /      |      \\
       /     {1}|      \\
      /        |        \\
     /         |         \\
    /          |          \\
   /           |           \\
  /            |            \\
 /             |             \\
@--------------------------@
               {0}""",triB , triH)
print(triArt)
print(str.format("Area = {0:.2f}" , triResult))

#Vlume of a Cube
cubeArea = input("Enter Edge Size Of The Cube")
cubeResult = float(cubeArea)**3
cubeArt = str.format("""
0 - - - - - - - - - - - - - 0
-\\                          -\\
- \\                         - \\
-  \\                        -  \\
-   \\                       -   \\
-    0 - - - - - - - - - - --- - 0
-    -                      -    -
-    -                      -    -
-    -                      -    -
-    -                      -    -
-    -                      -    -
-    -                      -    -
-    -                      -    -
-    -                      -    -
0 - --- - - - - - - - - - - 0    -
 \\   -                       \\   -
  \\  -                        \\  -
   \\ -                         \\ -
    \\-                          \\-
     0 - - - - - - - - - - - - - 0
                  {0}""" , cubeArea)

print(cubeArt)
print(str.format("Voulme = {0:.2f}" ,cubeResult))
