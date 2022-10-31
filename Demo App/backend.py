from locations import *
from topFirstMove import *
from topMoveCheck import *
from topClassroom import *
import global_
from kivymd.uix.label import MDLabel


def backend(s1):
    i = global_.i
    e = global_.e
    startingX = global_.startingX
    startingY = global_.startingY
    endX = global_.endX
    endY = global_.endY
    locationX = global_.locationX
    locationY = global_.locationY
    moving = global_.moving
    moves = global_.moves
    EO = global_.EO
    Turning = global_.Turning
    starting = global_.starting
    hallway = global_.hallway

    #s1 = self.manager.get_screen('menu')
        
    starting = s1.ids.startingClassroom.text

    while (any(starting in sl for sl in hallways) == False): # Checks if starting location is in a list
        return ValueError

         

    if any(starting in sl for sl in hallways):
        pass

    hallway = s1.ids.endingClassroom.text
    print("THIS IS HALLWAY " + hallway)

    while ((any(hallway in sl for sl in hallways) == False)) or (hallway == starting):
        return ValueError
    
    if any(hallway in sl for sl in hallways): 
      pass
        

        
    while ((any(hallway in sl for sl in hallways) == False)) or (hallway == starting):
        '''
        if (starting == hallway):
            hallway = str(input("You are at that classroom! Please pick another destination "))
        else:
            hallway = str(input("Not a classroom "))
        '''
        
        if any(hallway in sl for sl in hallways): 
            pass

    print()

    #best
    while (starting not in hallways[i]):
        i += 1

    else:
        while (starting not in hallways[i][e]):
            # print('in loop')
            e += 1

        else:
            pass

    i = 0
    e = 0

    while (hallway not in hallways[i]):
        i += 1
        #print('upper')
    else:
        while (hallway not in hallways[i][e]):
            # print('in loop')
            e += 1

        else:
            pass 
        

    # print(hallway in sec200HO1)

    if ((starting in sec200HE1) or (starting in sec300HO1)
            or (starting in sec300HO2) or (starting in sec307)
            or (starting in sec400HO1) or (starting in sec400HE1)
            or (starting in sec600HO1) or (starting in sec600HE1)):
        startingX = 1

    elif ((starting in sec200HE1) or (starting in sec200HE2)
        or (starting in sec200HO1) or (starting in sec500HE1)
        or (starting in sec500HO2) or (starting in sec500HE2)
        or (starting in sec400HO2) or (starting in sec600HO2)
        or (starting in sec600HE2) or (starting in sec400HE2) 
        or (starting in sec500HO1)):
        startingX = 2

    else:
        startingX = 3

    if ((starting in sec300HO1) or (starting in sec600HE1)
            or (starting in sec600HE2) or (starting in sec600HO1)
            or (starting in sec600HO2) or (starting in sec500HE2)
            or (starting in sec500HO2)):
        startingY = 1
        

    elif ((starting in sec300HO2) or (starting in sec200HE1)
        or (starting in sec200HE2) or (starting in sec200HO1)
        or (starting in sec500HO1) or (starting in sec500HE1) or (starting in secEagleO) or (starting in secEagleE)):
        startingY = -1

    else:
        startingY = 0

    if ((hallway in sec200HE1) or (hallway in sec300HO1) or (hallway in sec300HO2)
            or (hallway in sec307) or (hallway in sec400HO1)
            or (hallway in sec400HE1) or (hallway in sec600HO1)
            or (hallway in sec600HE1)):
        endX = 1

    elif ((hallway in sec200HE1) or (hallway in sec200HE2)
        or (hallway in sec500HE1) or (hallway in sec500HO2)
        or (hallway in sec500HE2) or (hallway in sec400HO2)
        or (hallway in sec600HO2) or (hallway in sec600HE2)
        or (hallway in sec400HE2) or (hallway in sec500HO1) or (hallway in sec200HO1)):
        endX = 2

    else:
        endX = 3

    if ((hallway in sec300HO1) or (hallway in sec600HE1) or (hallway in sec600HE2)
            or (hallway in sec600HO1) or (hallway in sec600HO2)
            or (hallway in sec500HE2) or (hallway in sec500HO2)):
        endY = 1

    elif ((hallway in sec300HO2) or (hallway in sec200HE1)
        or (hallway in sec200HE2) or (hallway in sec200HO1)
        or (hallway in sec500HO1) or (hallway in sec500HE1) or (hallway in secEagleO) or (hallway in secEagleE)):
            
        endY = -1

    else:
        endY = 0

    # print(starting in sec600HE2)
    #print("Starting coordinates: " + str(startingX) + "," + str(startingY))
    # print(str(startingX) + "," +  str(startingY))
    #print("Ending coordinates: " + str(endX) + "," + str(endY))
    # print(str(endX) + "," + str(endY))

    #while (startingX != endX):
    if (endX > startingX):
        locationX = "east"
        #print("First direction to go to: " + locationX)
        # print(locationX)
    elif (endX < startingX):
        locationX = "west"
        #print("First direction to go to: " + locationX)

        # print(locationX)
    else:
        moving = "y"
        #print("same X")

    #Find x then do movements then find Y

    if (endY > startingY):
        locationY = "north"
        #print("Second direction to go to: " + locationY)
        #print()
        # print(locationY)
    elif (endY < startingY):
        locationY = "south"
        #print("Second direction to go to: " + locationY)
        #print()
        # print(locationY)
    else:
        moving = "x"
        #print("The rooms are on the same y-axis")
        #print()
        locationY = True



    ## EO DECLARATION 
    if ((starting in sec300HO1) or (starting in sec307)
            or (starting in sec300HO2)):

        if (locationY == 'north'):
            EO = "left"
            #print("\nIf you are in the 300 hallway and going North, then turn" + EO)
            #print("User is going to turn " + EO)


        elif (locationY == "south"):
            EO = "right"
            #print("If you are in the 300 hallway and going South, then turn " + EO)
            #print("User is going to turn " + EO)


    elif ((starting in sec500HO1) or (starting in sec500HO2)
        or (starting in sec500HE1) or (starting in sec500HE2)):

        if (locationY == "north"):
            if (int(starting) % 2 == 0):
                EO = "right"
                #print( "If you are in an even numbered 500 room and you are going North, turn" + EO)
                #print("User is going to turn " + EO)

            else:
                EO = "left"
                #print( "If you are in an odd numbered 500 room and you are going North, turn " + EO)
                #print("User is going to turn " + EO)


        elif (locationY == "south"):
            if (int(starting) % 2 == 0):
                EO = "left"
                #print("If you are in an even numbered 500 room and you are going South, turn " + EO)
                #print("User is going to turn " + EO)

            else:
                EO = "right"
                #print( "If you are in an odd numbered 500 room and you are going South, turn " + EO)
                #print("User is going to turn " + EO)

    else:

        if (startingX == 1):
            if (int(starting) % 2 == 0):
                EO = "left"
            else:
                EO = "right"

        elif (startingX == 2):
            if (int(starting) % 2 == 0):
                EO = "right"
            else:
                EO = "left"

    global_.i = i
    global_.e = e
    global_.startingX = startingX
    global_.startingY = startingY
    global_.endX = endX
    global_.endY = endY
    global_.locationX = locationX
    global_.locationY = locationY
    global_.moving = moving
    global_.moves = moves
    global_.EO = EO
    global_.Turning = Turning
    global_.starting = starting
    global_.hallway = hallway

    
    while (startingX != endX or startingY != endY):
        i = global_.i
        e = global_.e
        startingX = global_.startingX
        startingY = global_.startingY
        endX = global_.endX
        endY = global_.endY
        locationX = global_.locationX
        locationY = global_.locationY
        moving = global_.moving
        moves = global_.moves
        EO = global_.EO
        Turning = global_.Turning
        starting = global_.starting
        hallway = global_.hallway

        if (moves > 0):
            print("testing2")
            topMoveCheck()
            global_.moves += 1

        else:
            print("testing1")
            topFirstMove()


    if ((startingX == endX) and (startingY == endY)):
        print("testing3")
        topClassroom()
    
    print(moves)
    

                