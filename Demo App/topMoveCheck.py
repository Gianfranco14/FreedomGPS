from locations import *
import global_


def topMoveCheck():
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
    arr = global_.arrGlobal

    #print("FIRST MOVECHECK MOVES" + str(moves))

    # arr.append('\nin function')
   #  arr.append("TEST: " + str(startingY))
   #  arr.append("TEST: " + str(startingX))
    if (startingY == 1 and startingX == 1):  # Checkpoint (1, 1)
        if (startingY != endY):  #I'm pretty sure we don't need this because of the while loop
            #if (locationY == "north"):
            #arr.append("checkpoint at 1,1")
            #(locationY == "south"):
            #arr.append("checkpoint at 1,1")
            #if (EO == "right"):
              #  arr.append("going down")
            #else:
            EO = "left"
            arr.append("Turn " + EO + ", go to the 300/400 intersection")

            startingY -= 1
            moves += 1

        elif (startingX != endX):
          if (starting == "315"):
            arr.append("Go forward into the 600 hallway")
            startingX += 1
            moves += 1
          
          else:
            #$if (locationY != True):
                #arr.append("Go up to hallway intersection 600/300")
                #pass
              if (startingX != endX):
                  #arr.append("checkpoint at 1,1")
                  #arr.append("New startingY: " + str(startingY))
                  #arr.append("New startingX: " + str(startingX))
                  startingX += 1
                  #arr.append("New startingX: " + str(startingX))
              #if (startingX == endX):
                  #arr.append("\n You've arrived at your destination (hallway)")

    elif (startingY == 1 and startingX == 2):  # Checkpoint (2, 1)
        if (startingY != endY):
            #arr.append("at checkpoint 2,1")
            EO = "right"
            arr.append("Turn " + EO + ", go to 400/500 intersection")
            startingY -= 1

        elif (startingX != endX):
            #if (locationY != True):
                #arr.append("go up to hallway intersection 600/500")
                #pass
            if (startingX != endX):
                #arr.append("checkpoint 2,1")
                startingX -= 1
           # if (startingX == endX):
              #  arr.append("doneXXYYXX kissy")

    elif (startingY == 0 and startingX == 2):  # Checkpoint (2, 0)
        if (startingY != endY):
            if (locationY == "north"):
                if (moves == 1):
                    if ((starting in sec500HO1) or (starting in sec500HO2)
                            or (starting in sec500HE1)
                            or (starting in sec500HE2)):
                        #startingY += 1
                        #arr.append("val")
                        if (startingY != endY):
                          if (int(hallway) % 500 <= 14):
                            startingY += 1

                          else:
                            arr.append("Go to the 600/500 intersection")
                            startingY += 1


                    else:
                        if (int(hallway) % 500 <= 14):
                          pass
                        else:
                          EO = "left"
                          arr.append("Turn " + EO + ", go to the 600/500 intersection")
                          startingY += 1
                else:
                  if (int(hallway) % 600 <= 13 or int(hallway) % 300 <= 15):
                    arr.append("Go to the 500/600 intersection")
                  startingY += 1

            elif (locationY == "south"):
                if (moves == 1):
                    if ((starting in sec500HO1) or (starting in sec500HO2)
                            or (starting in sec500HE1) or (starting in sec500HE2)):
                        #arr.append("val")

                        if (startingY != endY):
                          #if (int(hallway) % 500 >= 0):
                          #  startingY -= 1
                          
                          #else:
                          if (int(hallway) % 200 <= 13 or int(hallway) % 300 <= 15):
                      
                            arr.append("Go to the 500/200 intersection")
                          startingY -= 1

                    else:
                      if (int(hallway) % 200 <= 13 or int(hallway) % 300 <= 15):
                        if ((starting in secEagleO) or (starting in secEagleE)):
                          pass
                        else:
                          EO = "right"
                          arr.append("Turn " + EO + ", go to the 500/200 intersection")
                      startingY -= 1

                else:
                  if (int(hallway) % 200 <= 13 or int(hallway) % 300 <= 15):
                    arr.append("Go to the 500/200 intersection ")
                  startingY -= 1
                    

        elif (startingX != endX):
            #if (locationY != True):
                #arr.append("go to the hallway intersection 400/500")
                #pass
            if (startingX != endX):
                #arr.append("checkpoint 2,0")
                EO = "left"
                #arr.append("Turn " + EO + ", going left")
                startingX -= 1
           # if (startingX == endX):
             #   arr.append("doneXXYYXX kissy")

    elif (startingY == -1 and startingX == 2):  # Checkpoint (2, -1)
        if (startingY != endY):
          if ((starting in secEagleO) or (starting in secEagleE)):
            EO = "right"
          else:
            EO = "left"
          arr.append("Turn " + EO + ", go to the 500/400 intersection")
          startingY += 1

        elif (startingX != endX):
          if ((hallway in secEagleO) or (hallway in secEagleE)):
            if (starting in sec600HO2) or (starting in sec600HE2) or (starting in sec500HO2) or (starting in sec500HE2):
              arr.append("Go to the 500/200 intersection")
            elif ((starting in sec400HO2) or (starting in sec400HE2)):
              arr.append("Turn right, go to the 500/200 intersection")
            startingX += 1

          else:
            
            EO = "right"
            #arr.append("Turn " + EO + ", going left")
            startingX -= 1
            #if (startingX == endX):
             #   arr.append("doneXXYYXX kissy")

    elif (startingY == -1 and startingX == 1):  # Checkpoint (1, -1)
        if (startingY != endY):
            EO = "right"
            arr.append("Turn " + EO + ", go to the 300/400 intersection")
            startingY += 1

        elif (startingX != endX):
            #if (locationY != True):
                # arr.append("go to the hallway intersection 300/200")
                #pass
            if (startingX != endX):
                #arr.append("checkpoint 1,-1")
                if (starting == "200"):
                  startingX += 1
                else:
                  EO = "left"
                  startingX += 1
            #if (startingX == endX):
            #   arr.append("doneXXYYXX kissy")

    elif (startingY == 0 and startingX == 1):  # Checkpoint (1, 0)
      print("AT CHECKPOINT")
      print(moves)
      if (startingY != endY):
          if (locationY == "north"):
              if (moves == 1):
                  if ((starting in sec300HO1) or (starting in sec307)
                          or (starting in sec300HO2)):
                      if (startingY != endY):
                        if (int(hallway) % 300 <= 15):
                          startingY += 1
                          arr.append("Go to the 300/600 intersection")
                        
                        else:
                          startingY += 1
                          arr.append("Go to the 300/600 intersection")
                      
                  else:
                    EO = "right"
                    print("WHY!")
                    arr.append("Turn " + EO + ", go to the 300/600 intersection")
                    startingY += 1
              else:
                  startingY += 1
                  print("TESTING")
                  if ((hallway in sec307) or (hallway in sec300HO1)):
                    pass
                  else:
                    arr.append("Go to the 300/600 intersection")
                  #startingY += 1

          elif (locationY == "south"):
              if (moves == 1):
                  if ((starting in sec300HO1) or (starting in sec307)
                          or (starting in sec300HO2)):
                      if (startingY != endY):
                        if (int(hallway) % 300 >= 0):
                          #arr.append(startingY)
                          startingY -= 1
                          if (int(hallway) % 300 <= 15):
                            moves += 1
                          else:
                            
                            arr.append("Go to the 300/200 intersection")
                            moves += 1

                        else:
                          arr.append("Go to the 300/400 intersection")
                          startingY -= 1
                          #moves += 1
                      
                  else:
                    EO = "left"
                    if (int(hallway) % 200 <= 13 or int(hallway) % 500 <= 14):
                      arr.append("Turn " + EO + ", go to the 300/200 intersection")
                    startingY -= 1
              else:
                startingY -= 1
                if (startingY == endY):
                  if (int(hallway) % 200 <= 21 or int(hallway) % 500 <= 14):
                    arr.append("Go to the 300/200 intersection")
                  else:
                    pass
                else:
                  arr.append("Go to the 300/200 intersection")
                
          

      elif (startingX != endX):
          #if (locationY != True):
              #arr.append("go to the hallway intersection 300/400")
              #pass
        if (startingX > endX):
          startingX -= 1
          
        else:
          if (locationY == "north"):
            EO = "right"

          elif (locationY == "south"):
            EO = "left"
          startingX += 1
          #if (startingX == endX):
    elif (startingY == 0 and startingX == 0):
      if (locationX == "west"):
        if (int(starting) % 400 <= 11):
          arr.append("Go into the main hallway")
          
        elif (locationY == "north"):
          arr.append("Turn left, go into the main hallway")
          
        elif (locationY == "south"):
          arr.append("Turn right, go into the main hallway")
          
        arr.append("Turn right, go down the main hallway until the fine arts hallway and turn left")
        startingX -= 1
      elif (locationX == "east"):
        #this if for going from left to right
        arr.append("Turn right, go down the main hallway until the main office hallway, then turn left until the 300/400 intersection")
        startingX += 1
        

    elif (startingY == 0 and startingX == -1):
      pass

    elif (startingY == 1 and startingX == 0):
      if(locationX == "west"):
        
        if(int(starting)  % 600 <= 13):
          arr.append("Go forward into the main hallway")
          
        elif(locationY == "north"):  #You can replace with else, check if transfer is true then make them turn right not left
          arr.append("Turn left, go forward into the main hallway")
        elif(locationY == "south"):
          arr.append("Turn right, go forward into the main hallway")
        
        arr.append("Turn left, go forward to the athletic hallway, turn right")
        startingX -= 1
      elif(locationX == "east"):
        arr.append("Turn left, go forward until the counseling hallway, turn right and go forward until the 300/600 intersection")
        startingX += 1

    #print("END OF MOVECHECK MOVES" + str(moves))

    print("THIS IS MOVES " + str(moves))
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
    print("THIS IS GLOBAL MOVES " + str(global_.moves))
    global_.EO = EO
    global_.Turning = Turning
    global_.starting = starting
    global_.hallway = hallway
    global_.arrGlobal = arr