from locations import *
import global_

def topFirstMove():
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

    #print("FIRST MOVE MOVES" + str(moves))
    
    
    if ((starting in sec300HO1) or (starting in sec307)
            or (starting in sec300HO2)):

        if (locationY == "north"):
          
            startingY += 1
            if (startingY == endY):
              if (startingY == 0):
                arr.append("Turn " + EO + ", go to the 300/400 intersection")
              else:
                if (int(hallway) % 600 <= 13 or int(hallway) % 500 <= 14):
                  arr.append("Turn " + EO + ", go to the 300/600 intersection")
              moves += 1
            else:
              moves += 1
              arr.append("Turn " + EO + ", go to the 300/400 intersection")

        elif (locationY == "south"):
            startingY -= 1
            if (startingY == endY):
              arr.append("Turn " + EO + ", go to the 300/400 intersection")
              if (starting == "307"):
                if (int(hallway) % 200 <= 13 or int(hallway) % 500 <= 14):
                  arr.append("Go to the 300/200 intersection")
              moves += 1
            else:
              moves += 1
              arr.append("Turn " + EO + ", go to the 300/400 intersection")

        elif (locationY == True):
          if (starting == "315"):
            moves += 1
            pass
            
          elif (startingY == 1):
            arr.append("Turn left, go to the 300/600 intersection")
            moves += 1

          elif (startingY == -1):
            arr.append("Turn right, go to the 300/200 intersection")
            moves += 1

          elif (startingY == 0):
            arr.append("Turn right, go to the 300/400 intersection")
            moves += 1
          
          #elif (startingY == 0):
            #arr.append("Turn left, go to the ")

    #elif (starting == 200) or (starting == 600):
    # arr.append('THIS IS A TEST')
    #if (starting % 2 == 0):
    # arr.append("go to the 300/400 intersection")

    elif ((starting in sec500HO1) or (starting in sec500HO2) or (starting in sec500HE1) or (starting in sec500HE2)):
        
        if (int(starting) % 2 == 0):
          if (locationY == "north"):
              startingY += 1
              moves += 1

              if ((starting in sec500HO2) or (starting in sec500HE2)):
                arr.append("Turn " + EO + ", go to the 500/600 intersection")

              elif ((starting in sec500HO1) or (starting in sec500HE1)):
                arr.append("Turn " + EO + ", go to the 400/500 intersection")

          elif (locationY == "south"):
              startingY -= 1
              moves += 1
              
              if ((starting in sec500HO1) or (starting in sec500HE1)):
                arr.append("Turn " + EO + ", go to the 500/200 intersection")
                

              elif ((starting in sec500HO2) or (starting in sec500HE2)):
                arr.append ("Turn " + EO + ", go to the 500/400 intersection")
                

          elif (locationY == True):
            if (startingY == 1):
              arr.append("Turn right, go to the 500/600 intersection")
              moves += 1

            elif (startingY == -1):
              arr.append("Turn left, go to the 500/200 intersection")
              moves += 1
        
        else:
          if (locationY == "north"):
            startingY += 1
            moves += 1
            arr.append("Turn " + EO + ", go to the 500/400 intersection")
          elif (locationY == "south"):
            startingY -= 1
            moves += 1
            arr.append("Turn " + EO + ", go to the 500/400 intersection")

          elif (locationY == True):
            
            if (int(hallway) % 500 <= 14):
              moves += 1
            elif (int(hallway) % 200):
              arr.append("Turn right, go to the 500/200 intersection")
              moves += 1
    
    elif ((starting in secEagleO) or (starting in secEagleE)):
      if (starting in secEagleO):
        EO = "left"
      else:
        EO = "right"
        
      arr.append("Turn " +  EO + ", go to the end of the eagle wing")
      arr.append("Turn left, go to the 200/500 intersection")
      startingX -= 1
      moves += 1
    
    
    else:

        #if (startingY == 1 and startingX == 1):
        # if (int(starting) % 2 == 0):
        #  EO = "left"
        #else:
        # EO = "right"
        # This is not needed (I believe)

        
        if (startingY == 1 and startingX == 1): #so there are six of these large if statements for the 6 main checkpoints
          if (startingY == endY):
                if (int(starting) % 2 == 0):
                  EO = "right"
                else:
                  EO = "left"
                
                startingX += 1
                moves += 1
          else:
          
            if (starting == "601"):
              
              moves += 1
              if (startingY != endY):
                arr.append("Go forward till the 300/600 intersection")
                startingY -= 1
                moves += 1
                if (startingY != endY):
                  arr.append("Go to the 300/400 intersection")
                  startingY -= 1
                  moves += 1
                  if (startingY == endY):
                      #startingY += 1
                    moves += 1
                    if (int(hallway) % 200 <= 21 or int(hallway) % 500 <= 14):
                      arr.append("Go to the 300/200 intersection")
                    #EO = "right"
                  #moves += 1
                  else:
                    moves += 1
                    EO = "left"
                else:
                  arr.append("Go to the 300/400 intersection")  
                  moves += 1
            else:
              arr.append("Turn " + EO + ", go to the 600/300 intersection")
              moves += 1

                        
        elif (startingY == 1 and startingX == 2):
          if (startingY == endY):

                if (int(starting) % 2 == 0):
                  EO = "left"
                else:
                  EO = "right"
                
                startingX -= 1
                moves += 1

          else:        
            arr.append("Turn " + EO + ", go to the 600/500 intersection")
            moves += 1

        elif (startingY == 0 and startingX == 2):
          if (startingY == endY):
                if (int(starting) % 2 == 0):
                  EO = "left"
                else:
                  EO = "right"
                
                startingX -= 1
                moves += 1

          else:
            
            arr.append("Turn " + EO + ", go to the 400/500 intersection")
            moves += 1

        elif (startingY == -1 and startingX == 3):
          startingX -= 1
          moves += 1
      
        elif (startingY == -1 and startingX == 2):
          if (startingY == endY):

                if (int(starting) % 2 == 0):
                  EO = "left"
                else:
                  EO = "right"
                
                startingX -= 1
                moves += 1

          else:
            arr.append("Turn " + EO + ", go to the 200/500 intersection")
            moves += 1

        elif (startingY == -1 and startingX == 1):
        
          if (startingY == endY):
            if (int(starting) % 2 == 0):
               EO = "right"
            else:
                EO = "left"
                
            startingX += 1
            moves += 1

          else:

            if (starting == "200"):
              
              if (startingY != endY):
                arr.append("Go forward till the 300/200 intersection")
                startingY += 1
                moves += 1
                if (startingY != endY):
                  arr.append("Go to the 300/400 intersection")
                  startingY += 1
                  moves += 1
                  if (startingY == endY):
                    #startingY += 1
                    moves += 1
                    if (int(hallway) % 600 <= 13 or int(hallway) % 500 <= 14):
                      arr.append("Go to the 300/600 intersection")
                  #EO = "right"
                
                else:
                  arr.append("Go to the 300/400 intersection")
                  moves += 1

              else:
                moves += 1
                EO = "right"
                


            elif (int(starting) % 2 == 0):
                EO = "left"
                arr.append("Turn " + EO + ", go to the 200/300 intersection")
                moves += 1

        elif (startingY == 0 and startingX == 1):
          if (startingY == endY):

            if (int(starting) % 2 == 0):
               EO = "right"
            else:
                EO = "left"
                
            startingX += 1
            moves += 1

          else:
            arr.append("Turn " + EO + ", go to the 300/400 intersection")
            moves += 1

    #print("END OF FIRST MOVE MOVES" + str(moves))

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
    global_.arrGlobal = arr