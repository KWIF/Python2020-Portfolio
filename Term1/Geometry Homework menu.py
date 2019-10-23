def intro():
    intro = """
    Welcome To Homework Program
    1: Perimeter of a Square
    2:Area of a Square
    3:Circumference of a Circle
    4:Area of a triange
    5:Volume of a Cube
    6:Quit
    """
    print (intro)
def perimSquare():
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
    
def circumCircle():
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

def areaTri():
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

def volCube():
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

def quitOption():
    
    answer = input(""""
    Are you sure?
    A.Yes
    B.No
    """).upper()
    if answer=="A":
        return True
    elif answer=="B":
        return False
        

while True:
    intro()
    choice = input("Choose a Option")
    if choice== "1":
        perimSquare()
    elif choice== "2":
        perimSquare()
    elif choice== "3":
        circumCircle()
    elif choice== "4":
        areaTri()
    elif choice=="5":
        volCube()
    elif choice=="6":
        x=quitOption()
        if x:
            break
        



input("press enter to exit")






        
       
