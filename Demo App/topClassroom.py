from locations import *
import global_


def topClassroom():
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

  #print("FIRST TOP CLASSROOM MOVES" + str(moves))

  #arr.append("in loop")
  #arr.append("Go to classroom xxx")
  if ((startingY == 1) and (startingX == 1)):
    if (locationX == ''):
        if (int(hallway) % 600 <= 13):
          if (int(starting) % 600 <= 13):
            if (int(hallway) > int(starting)):
              if (int(hallway) % 600 <= 5 and int(hallway) % 2 != 0):
                if (int(starting) % 2 == 0):
                  Turning = "left"
                
    
                if (int(hallway) % 2 == 0):
                  EO = "left"
                else:
                  EO = "right"
              else:
                Turning = "right"
                
                if (int(hallway) % 2 == 0):
                  EO = "right"
                else:
                  EO = "left"
                
            else:
              Turning = "left" ## was left
            #if (int(starting) % 2 == 0):
             # Turning = "left"
            #else:
            #  Turning = "right"
              if (starting == "601"):
                if (int(hallway) % 2 == 0):
                  EO = "right"
                else:
                  EO = "left"
              else:
                
                if (int(hallway) % 2 == 0):
                  EO = "left"
                else:
                  EO = "right"
    
            arr.append("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
          else:
            if (starting == "315"):
              if (int(hallway) % 2 == 0):
                  EO = "right"
              else:
                  EO = "left"
              arr.append("Go down the 600 hallway and " + hallway + " will be on your " + EO)
            else:
              if (hallway != "601"):
                
                #arr.append("go to the 300/600 intersection")
                if (int(hallway) % 2 == 0):
                  EO = "right"
                else:
                  EO = "left"
                  
                arr.append("Turn right, go down the 600 hallway and " + hallway + " will be on your " + EO)
              else:
                arr.append("Turn left, 601 will be on your right")
        elif (int(hallway) % 300 <= 15):
          if (int(starting) % 600 <= 13):
            if (starting == "601"):
              arr.append("Go down the 300 hallway and " + hallway + " will be on your right")
            else:
              if (int(starting) % 2 == 0):
                Turning = "left"
              else:
                Turning = "right"
              arr.append("Turn " + Turning + ", go to the 600/300 intersection")
              arr.append("Turn left, go down the 300 hallway and " + hallway + " will be on your right")
          else:
            if (int(starting) % 300 <= 15 and moves < 2):
              if (int(hallway) > int(starting)):
                Turning = "left"
                EO = "left"
              else:
                Turning = "right"
                EO = "right"
  
              arr.append("Turn " + Turning + ", go down the 300 hallway and " + hallway + " will be on your " + EO)
              
            else:    
              arr.append("Go down the 300 hallway and " + hallway + " will be on your left")


    else:
      if (int(hallway) % 600 <= 13):
        if (int(starting) % 600 <= 13):
          if (int(starting) % 2 == 0):
            Turning = "left"
          else:
            Turning = "right"
            
          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"
            
          arr.append("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
        else:
          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"
          if (starting == "315"):
            arr.append("Go down the 600 hallway and " + hallway + " will be on your " + EO)

          #arr.append("Go to the 500/600 intersection")
          arr.append("Turn left, go down the 600 hallway and " + hallway + " will be on your " + EO)
            
      elif (int(hallway) % 300 <= 15):
        arr.append("Turn left, go to the 600/300 intersection")
        arr.append("Turn left, go down the 300 hallway and " + hallway + " will be on your right")
        
  elif (startingY == 1 and startingX == 2):
    
    if ((locationX == '') or (starting in secEagleO) or (starting in secEagleE)):
      if (int(hallway) % 500 <= 14):
        if (int(starting) % 500 <= 14):
          if (locationY == True):
            if (int(hallway) % 500 > int(starting) % 500):
              if (int(hallway) % 2 == 0):
                EO = "right"
              else:
                EO = "left"
                
              if (int(starting) % 2 == 0):
                Turning = "right"
              else:
                Turning = "left"
            else:
              if (int(hallway) % 2 == 0):
                EO = "left"
              else:
                EO = "right"
                
              if (int(starting) % 2 == 0):
                Turning = "left"
              else:
                Turning = "right"   
            arr.append("Turn " + Turning + ", go down the 500 hallway and " + hallway + " will be on your " + EO)
          else:
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            if (int(starting) % 2 == 0):
              Turning = "right"
            else:
              Turning = "left"
            arr.append("Go down the 500 hallway and " + hallway + " will be on your " + EO)
        elif (int(starting) % 600 <= 13):
          if (int(starting) % 2 == 0):
              EO = "right"
          else:
              EO = "left"
          arr.append("Turn " + EO + ", go to the 600/500 intersection")
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
          arr.append("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
          
        else:
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
            
          if (int(starting) % 400 <= 13):
            
            arr.append("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)
          else:
            arr.append("Go down the 500 hallway and " + hallway + " will be on your " + EO)
            
      elif (int(hallway) % 600 <= 13):
        if (int(starting) % 600 <= 13):
          if (int(hallway) > int(starting)):
            if (hallway == "609" and starting == "604"):
              Turning = "left"
              EO = "right"
            else:              
              if (int(starting) % 2 == 0):
                Turning = "right"
              else:
                Turning = "left"
                
              if (int(hallway) % 2 == 0):
                EO = "right"
              else:
                EO = "left"
          else:
            if (starting == "609"):
              Turning = "left"
              if (int(hallway) % 2 == 0):
                EO = "right"
              else:
                EO = "left"
            else:
              if (int(starting) % 2 == 0):
                Turning = "left"
              else:
                Turning = "right"
                
              if (int(hallway) % 2 == 0):
                EO = "left"
              else:
                EO = "right"
          arr.append("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
        else:
          if (moves == 0):
            if (int(starting) % 2 == 0):
                EO = "right"
            else:
                EO = "left"
              
            arr.append("Turn " + EO + ", go to the 500/600 intersection")
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
          arr.append("Turn left, go down the 600 hallway and " + hallway + " will be on your " + EO)
    else:
      if (int(hallway) % 600 <= 13):
        if (int(starting) % 600 <= 13):
          if (int(starting) % 2 == 0):
            Turning = "right"
          else:
            Turning = "left"
            
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
          arr.append("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
          
        else:
          if (starting == "315"):
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            arr.append("Go down the 600 hallway and " + hallway + " will be on your " + EO)
            
          else:
            if (int(hallway) % 2 == 0):
                EO = "right"
            else:
                EO = "left"
            arr.append("Turn right, go down the 600 hallway and " + hallway + " will be on your " + EO)
        
      elif (int(hallway) % 500 <= 14):
        if (starting == "315"):
          arr.append("Go to the 600/500 intersection")
        else:
          arr.append("Turn right, go to the 600/500 intersection")
        if (int(hallway) % 2 == 0):
            EO = "left"
        else:
            EO = "right"
        arr.append("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
        
  elif (startingY == 0 and startingX == 2):
    if (locationX == ""):
      
      #arr.append("Go to the 500/400 intersection")
      
      if (int(hallway) % 2 == 0):
          EO = "left"
      else:
          EO = "right"
        
      if (locationY == "south"):
        
        arr.append("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      elif (locationY == "north"):
        
        arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      elif (locationY == True):
        if (int(starting) % 400 <= 13):
          if (int(hallway) > int(starting)):
            if (starting == "404" and hallway == "407"):
              Turning = "left"
              EO = "right"
            else:
              if (int(starting) % 2 == 0):
                Turning = "right"
              else:
                Turning = "left"
              if (int(hallway) % 2 == 0):
                EO = "right"
              else:
                EO = "left"
            
            arr.append("Turn " + Turning + ", go down the 400 hallway and " + hallway + " will be on your " + EO)
          else:
            if (starting == "407"):
              Turning = "left"
              if (int(hallway) % 2 == 0):
                EO = "right"
              else:
                EO = "left"
                
            else:
              if (int(starting) % 2 == 0):
                Turning = "left"
              else:
                Turning = "right"
  
              if (int(hallway) % 2 == 0):
                EO = "left"
              else:
                EO = "right"
            
            arr.append("Turn " + Turning + ", go down the 400 hallway and " + hallway + " will be on your " + EO)
      else:
        
        arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      #arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
    else:
      if ((starting in secEagleO) or (starting in secEagleE)):
        if (int(hallway) % 2 == 0):
          EO = "left"
        else:
          EO = "right"
        arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
      else:
        if (int(hallway) % 2 == 0):
            EO = "right"
        else:
            EO = "left"
        if (locationY == "south"):
          arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
        elif (locationY == "north"):
          arr.append("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
        elif (locationY == True):
          if (int(starting) % 2 == 0):
            Turning = "right"
          else:
            Turning = "left"
          arr.append("Turn "+ Turning +", go down the 400 hallway and " + hallway + " will be on your " + EO)
          
  elif (startingY == -1 and startingX == 3):
    if (starting == "307"):
      arr.append("Go to the 300/200 intersection")
    
    if (int(starting) % 200 <= 13 and locationY == True):
      if (int(starting) % 2 == 0):
        if (int(starting) % 2 == 0):
          Turning = "right"
        else:
          Turning = "left"
        arr.append("Turn " + Turning + ", go into the eagle wing") 

    else:
      arr.append("Turn left, go into the eagle wing")
      #I wanna do go down the 200 hall but I can't do that because of the way this shit is set up
        
    if (hallway in secEagleE):
      EO = "left"
    else:
      EO = "right"    
    arr.append("Turn right, go down the eagle wing and " + hallway + " will be on your " + EO)
        

  elif (startingY == -1 and startingX == 2):   
    if ((starting in secEagleO) or (starting in secEagleE)):
      if (int(hallway) % 2 == 0):
        EO = "left"
      else:
        EO = "right"
      arr.append("Go down the 200 hallway and " + hallway + " will be on your " + EO)
        
    elif (locationX == ''):
      if (int(hallway) % 500 <= 14):
        if (int(starting) % 500 <= 14):
          if (locationY == True):
            if (int(hallway) % 500 > int(starting) % 500):
              
              if (starting == "504" and hallway != "506"):
                Turning = "left"
                EO = "right"
                
              else:
                if (int(starting) % 2 == 0):
                    Turning = "right"
                else:
                    Turning = "left" 
                  
                if (int(hallway) % 2 == 0):
                    EO = "right"
                else:
                    EO = "left"
            else:
              if (starting == "505" and hallway == "504"):
                Turning = "left"
                EO = "right"
              else:
                if (int(starting) % 2 == 0):
                  Turning = "left"
                else:
                  Turning = "right"
                
                if (int(hallway) % 2 == 0):
                  EO = "left"
                else:
                  EO = "right"
           
            arr.append("Turn " + Turning + ", go down the 500 hallway and " + hallway + " will be on your " + EO)
            
          else:
            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            arr.append("Go down the 500 hallway and " + hallway + " will be on your " + EO)
        else:
          if (int(starting) % 600 <= 13):
            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            arr.append("Go down the 500 hallway and " + hallway + " will be on your " + EO)

          elif (int(starting) % 400 <= 13):
            if (int(starting) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            arr.append("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
            
          else:
            if (int(starting) < 400 and int(starting) % 200 <= 13):

              if (int(starting) % 2 == 0):
                  EO = "right"
              else:
                  EO = "left"
            else:
              EO = "left"

            print("BRUH")
            arr.append("Turn " + EO + ", go to the 200/500 intersection")
            
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            
            arr.append("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)
    
      elif (int(hallway) % 200 <= 13):
        if (moves == 0):
          if (int(starting) % 200 <= 13):
            if (int(hallway) > int(starting)):
            
              if (int(starting) % 2 == 0):
                  Turning = "right"
              else:
                  Turning = "left"
                
              if (int(hallway) % 2 == 0):
                EO = "right"
              else:
                EO = "left"
  
            else:
              if (int(starting) % 2 == 0):
                  Turning = "left"
              else:
                  Turning = "right"
                
              if (int(hallway) % 2 == 0):
                EO = "left"
              else:
                EO = "right"
            arr.append("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
          else:
            if (int(starting) % 2 == 0):
              Turning = "left"
            else:
              Turning = "right"

            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            arr.append("Turn " + Turning + ", go to the 500/200 intersection")
            arr.append("Turn right, go down the 200 hallway and " + hallway + " will be on your " + EO)
        else:
          if ((starting in secEagleO) or (starting in secEagleE)):
            pass
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
            
          arr.append("Turn right, go down the 200 hallway and " + hallway + " will be on your " + EO)
          #arr.append("Turn " + EO + ", go to the 500/200 intersection") 
        #if (int(hallway) % 2 == 0):
        #  EO = "left"
        #else:
        #  EO = "right"
      
          
    else:
      if (int(hallway) % 200 <= 13):
        if (moves == 1):
        #if (int(starting) % 200 <= 13):
          if (int(starting) % 2 == 0):
            Turning = "right"
          else:
            Turning = "left"
                
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
          
          arr.append("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
        else:
          Turning = EO
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
          
          arr.append("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
          
      elif (int(hallway) % 500 <= 15):
        if (int(hallway) % 2 == 0):
          EO = "right"
        else:
          EO = "left"
        if ((starting in secEagleO) or (starting in secEagleE)):
          arr.append("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
        else:
          if (int(starting) < 400 and int(starting) % 200 <= 13):

            if (int(starting) % 2 == 0):
                EO = "right"
            else:
                EO = "left"
          else:
            EO = "left"

          arr.append("Turn " + EO + ", go to the 200/500 intersection")

          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"

          print("???")
          arr.append("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)
          
  elif (startingY == -1 and startingX == 1):
    if (locationX == ''):
      if (int(hallway) % 300 <= 15):
        if (int(starting) % 300 <= 15 and moves < 1):
          if (locationY == True):
            if (int(starting) > int(hallway)):
              Turning = "right"
              EO = "right"
   
            else:
              Turning = "left"
              EO = "left"
              
            arr.append("Turn " + Turning + ", go down the 300 hallway and " + hallway + " will be on your " + EO)
            
          else:
            arr.append("Go down the 300 hallway and " + hallway + " will be on your right")
            
        elif (int(starting) % 200 <= 13 and moves <= 1):
          if (starting == "200"):
            arr.append("Go down the 300 hallway and " + hallway + " will be on your left")
            
          else:
            arr.append("Turn " + EO + ", go to the 200/300 intersection")
            arr.append("Turn right, go down the 300 hallway and " + hallway + " will be on your left")
          
        else:
          if (int(starting) % 400 <= 13):
            arr.append("Turn left, go down the 300 hallway and " + hallway + " will be on your right")
            
          else:       
            arr.append("Go down the 300 hallway and " + hallway + " will be on your right")
        
      elif (int(hallway) % 200 <= 13):
        if (int(starting) % 200 <= 13 and moves < 1):
          if (int(hallway) > int(starting)):
            arr.append("Turn right, go down the 200 hallway and " + hallway + " will be on your right")
          else:
            arr.append("Turn left, go down the 200 hallway and " + hallway + " will be on your left")
        else:
          if (hallway == "200"):
            if (moves == 0):
              arr.append("Turn right, classroom 200 is right ahead")
            else:
              arr.append("Classroom 200 is right ahead")
            
          else:
            if (moves < 1):
              arr.append("Turn right, go to the 300/200 intersection")
            
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
              
            arr.append("Turn left, go down the 200 hallway and " + hallway + " will be on your " + EO)
          #THIS IS FOR THE SAME X AND Y ON THE 200  
  
    else: 
      if (int(hallway) % 300 <= 15):
        if (int(starting) % 200 <= 13 and moves <= 1):
          if (int(starting) % 2 == 0):
            EO = "left"
          else:
            EO = "right"
          arr.append("Turn " + EO + ", go to the 200/300 intersection")
        else:
          if ((starting in secEagleO) or (starting in secEagleE)):
            arr.append("Go to the 200/300 intersection")
          else:     
            arr.append("Turn right, go to the 200/300 intersection")
          
        arr.append("Turn right, go down the 300 hallway and " + hallway + " will be on your left")
        
      elif (int(hallway) % 200 <= 13):
        if (int(starting) % 200 <= 13 and moves <= 1):
          if (int(starting) % 2 == 0):
            Turning = "left"
          else:
            Turning = "right"

          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"

          
          
          arr.append("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
          
        else:
        
          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"

          if ((starting in secEagleE) or (starting in secEagleO)):
            arr.append("Go down the 200 hallway and " + hallway + " will be on your " + EO)
          else:
            arr.append("Turn right, go down the 200 hallway and " + hallway + " will be on your " + EO)
        
          
  elif (startingY == 0 and startingX == 1):
    if (locationX == ''):
      if (hallway == "307"):
        if (locationY == "north"):
          arr.append("Go down the 300 hallway and 307 will be on your left")
        elif (locationY == "south"):
          arr.append("307 is on your right")
        elif (locationY == True):
          if (int(starting) % 2 == 0):
            Turning = "left"
          else:
            Turning = "right"
            
          arr.append("Turn " + Turning + ", go to the 400/300 intersection")
          arr.append("Turn right, go down the 300 hallway and 307 will be on your left")
          
      elif (int(hallway) % 400 <= 11):
        if (locationY == "north"):
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
          
          arr.append("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
        elif (locationY == "south"):
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
            
          arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)

        elif (locationY == True):
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
    
      
          arr.append("Turn right, go to the 300/400 interseciton")
          arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
    else:    
      if (locationY == "south"):
        if (int(hallway) % 2 == 0):
            EO = "left"
        else:
            EO = "right"
            
        arr.append("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      elif (locationY == "north"):
        if (hallway == "307"):
          arr.append("Turn left, go to the 400/300 intersection")
          arr.append("Turn right and 307 will be on your left")
        else:
            
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
          
          
          arr.append("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)

  #print("FIRST TOP CLASSROOM MOVES" + str(moves))
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