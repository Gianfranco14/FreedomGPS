
from locations import * # Import statements

# print(hallways) # Prints all options
print() # New line
starting = str(input("Where are you starting? ")).lower() # query for user to input starting position

#while (starting in sl for sl in starting):
# starting = str(input("Not a classroom "))

while (any(starting in sl for sl in hallways) == False): # Checks if starting location is in a list
    starting = str(input("Not a classroom, please enter a valid room ")).lower() # If not then print not a classroom and ask for another one
    if any(starting in sl for sl in hallways):
        pass

hallway = str(input("What room do you need to go to? ")).lower()

while ((any(hallway in sl for sl in hallways) == False)) or (hallway == starting):
    if (starting == hallway):
      hallway = str(input("You are at that classroom! Please pick another destination ")).lower()
    else:
      hallway = str(input("Not a classroom ")).lower()
    
    if any(hallway in sl for sl in hallways): 
      pass

print()
# print(type(hallway))

#any hallway in sl for sl in hallways

i = 0
e = 0
startingX = 0
startingY = 0
endX = 0
endY = 0
locationX = ""
locationY = ""
moving = ""
moves = 0
EO = ""
Turning = ""
transfer = False

#x = [[1, 2, 3], [2, 3, 4]]
#print("Is it in any index: " + str(any(hallway in sl for sl in hallways)))

#nested while loop, use two looping varibles for the while loops. One for the sub list and the index of that sub list ([i][e], something like that)

#running through each index of each list might take to long so we might have to find the list first then the Index

#best

def numString(string):
  return int(string[1:])


while (starting not in hallways[i]):
    i += 1

else:
    while (starting not in hallways[i][e]):
        # print('in loop')
        e += 1

    else:
        # print("index found")
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
        #print("\nList number: " + str(i))
        # print(i)

        #print("Sublist number: " + str(e))
        # print(e)

        #print("Room number: " + str(hallways[i][e]))
        # print(hallways[i][e])
       #  print("index found")
      #while coding, if you want to use these print statements you can uncomment them
        pass 

  
if ((starting in sec200HE1) or (starting in sec300HO1)
        or (starting in sec300HO2) or (starting in sec307)
        or (starting in sec400HO1) or (starting in sec400HE1)
        or (starting in sec600HO1) or (starting in sec600HE1)):
    startingX = 1
          
elif ((starting in secL200HE1) or (starting in secL400HE1)
      or (starting in secL400HO1) or (starting in secL600HE1)
      or (starting in secL600HO1)):
  startingX = "1"
  
elif ((starting in sec200HE1) or (starting in sec200HE2)
      or (starting in sec200HO1) or (starting in sec500HE1)
      or (starting in sec500HO2) or (starting in sec500HE2)
      or (starting in sec400HO2) or (starting in sec600HO2)
      or (starting in sec600HE2) or (starting in sec400HE2) 
      or (starting in sec500HO1)):
    startingX = 2
        
elif((starting in secL200HO1) or (starting in secL200HE2) 
     or (starting in secL400HE2) or (starting in secL400HO2) 
     or (starting in secL600HE2) or (starting in secL600HO2) 
     or (starting in secL500HO1) or (starting in secL500HE1) 
     or (starting in secL500HE2) or (starting in secL500HO2)):
  startingX = "2"
        
elif ((starting in secCafe) or (starting in secMainEntrance)
      or (starting in secAuditorium) or (starting in secMediaCenter)
      or (starting in secMainOffice) or (starting in secClinic) 
      or (starting in secCounseling)):
  print("")
  startingX = 0

elif ((starting in secMainGym) or (starting in secAuxGym)
      or (starting in secWeightRoom) or (starting in secWrestling)
      or (starting in secBand) or (starting in secGuitar)
      or (starting in secChorusOrchestra) or (starting in secDrama)
      or (starting in secArt1) or (starting in secArt2)):
  startingX = -1

elif ((starting in secEagleO) or (starting in secEagleE)):
    startingX = 3

elif ((starting in secLEagleE) or (starting in secLEagleO)):
  startingX = "3"
  

if ((starting in sec300HO1) or (starting in sec600HE1)
        or (starting in sec600HE2) or (starting in sec600HO1)
        or (starting in sec600HO2) or (starting in sec500HE2)
        or (starting in sec500HO2) or (starting in secCafe)
        or (starting in secMainGym) or (starting in secAuxGym) 
        or (starting in secWeightRoom) or (starting in secWrestling)
        or (starting in secCounseling)):
    print("startY = 1")      
    startingY = 1

elif ((starting in secL600HE1) or (starting in secL600HO1) 
      or (starting in secL600HE2) or (starting in secL600HO2)
      or (starting in secL500HO2) or (starting in secL500HE2)):
  startingY = "1"
    

elif ((starting in sec300HO2) or (starting in sec200HE1)
      or (starting in sec200HE2) or (starting in sec200HO1)
      or (starting in sec500HO1) or (starting in sec500HE1) 
      or (starting in secEagleO) or (starting in secEagleE)):
    startingY = -1

elif ((starting in secL200HO1) or (starting in secL200HE2) 
      or (starting in secL200HE1) or (starting in secL500HO1) 
      or (starting in secL500HE1)):
  startingY = "-1"

elif ((starting in secL400HE1) or (starting in secL400HO1) 
      or (starting in secL400HO2) or (starting in secL400HE2)):
  startingY = "0"

else:
    print("startY = 0")
    startingY = 0



  

if ((hallway in sec200HE1) or (hallway in sec300HO1) or (hallway in sec300HO2)
        or (hallway in sec307) or (hallway in sec400HO1)
        or (hallway in sec400HE1) or (hallway in sec600HO1)
        or (hallway in sec600HE1)):
    endX = 1
          
elif ((hallway in secL200HE1) or (hallway in secL400HE1)
      or (hallway in secL400HO1) or (hallway in secL600HE1)
      or (hallway in secL600HO1)):
  endX = "1"

elif ((hallway in sec200HE1) or (hallway in sec200HE2)
      or (hallway in sec500HE1) or (hallway in sec500HO2)
      or (hallway in sec500HE2) or (hallway in sec400HO2)
      or (hallway in sec600HO2) or (hallway in sec600HE2)
      or (hallway in sec400HE2) or (hallway in sec500HO1)
      or (hallway in sec200HO1)):
    endX = 2
        
elif((hallway in secL200HO1) or (hallway in secL200HE2) 
     or (hallway in secL400HE2) or (hallway in secL400HO2) 
     or (hallway in secL600HE2) or (hallway in secL600HO2) 
     or (hallway in secL500HO1) or (hallway in secL500HE1) 
     or (hallway in secL500HE2) or (hallway in secL500HO2)):
  endX = "2"
        
elif ((hallway in secCafe) or (hallway in secMainEntrance)
      or (hallway in secAuditorium) or (hallway in secMediaCenter)
      or (hallway in secMainOffice) or (hallway in secClinic)
      or (hallway in secCounseling)):
  endX = 0

elif ((hallway in secMainGym) or (hallway in secAuxGym)
      or (hallway in secWeightRoom) or (hallway in secWrestling)
      or (hallway in secBand) or (hallway in secGuitar)
      or (hallway in secChorusOrchestra) or (hallway in secDrama)
      or (hallway in secArt1) or (hallway in secArt2)):
  endX = -1

elif ((hallway in secEagleE) or (hallway in secEagleO)):
    endX = 3

elif ((hallway in secLEagleE) or (hallway in secLEagleO)):
  endX = "3"

if ((hallway in sec300HO1) or (hallway in sec600HE1) or (hallway in sec600HE2)
        or (hallway in sec600HO1) or (hallway in sec600HO2)
        or (hallway in sec500HE2) or (hallway in sec500HO2)
        or (hallway in secCafe) or (hallway in secMainGym)
        or (hallway in secAuxGym) or (hallway in secWeightRoom) 
        or (hallway in secWrestling) or (hallway in secCounseling)):
    endY = 1
          
elif ((hallway in secL600HE1) or (hallway in secL600HO1) 
      or (hallway in secL600HE2) or (hallway in secL600HO2)
      or (hallway in secL500HO2) or (hallway in secL500HE2)):
  endY = "1"

elif ((hallway in sec300HO2) or (hallway in sec200HE1)
      or (hallway in sec200HE2) or (hallway in sec200HO1)
      or (hallway in sec500HO1) or (hallway in sec500HE1)
      or (hallway in secEagleO) or (hallway in secEagleE)):
    endY = -1

elif ((hallway in secL200HO1) or (hallway in secL200HE2) 
      or (hallway in secL200HE1) or (hallway in secL500HO1) 
      or (hallway in secL500HE1)):
  endY = "-1"
        
elif ((hallway in secL400HE1) or (hallway in secL400HO1) 
      or (hallway in secL400HO2) or (hallway in secL400HE2)):
  endY = "0"

else:
    endY = 0

print(str(startingX) + ", " + str(startingY))
print(str(endX) + ", " + str(endY))


# TODO: Change locationX and locationY in this area for new rooms
# Work on firstMove
# Finish classroom



#while (startingX != endX):
if (int(endX) > int(startingX)):
    print("Look at this: " + str(startingX) + ", " + str(endX))
    locationX = "east"
    # print(locationX)
elif (int(endX) < int(startingX)):
    locationX = "west"
    #print("First direction to go to: " + locationX)

    # print(locationX)
else:
    moving = "y"
    #print("same X")

#Find x then do movements then find Y

if (int(endY) > int(startingY)):
    locationY = "north"
    #print("Second direction to go to: " + locationY)
    #print()
    # print(locationY)
elif (int(endY) < int(startingY)):
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
  if (isinstance(startingX, int)):
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
          
  else:
    if (startingX == "1"):
      if (numString(starting) % 2 == 0):
        EO = "left"
      else:
        EO = "right"

    elif (startingX == "2"):
      if (numString(starting) % 2 == 0):
        EO = "right"
      else:
        EO = "left"


   #  print("Test: " + EO)

#set EO, use it, then change it. Get rid of the other EO declaration 


#207 to 602. this looks fine, problem elsewhere
#Nevermind.

#if in 300 or 500, just go to the y, they need to go north or south
'''
Once at checkpoint, check what hallway they want to go to, in order to determine what direction their going

i.e.
*
hallway = 405
at mid left checkpoint (400 hallway to the right, 300 on top and bottom, main hall on the right)
if hallway in sec400HO1 or sec400HE1 or sec400HE2:
  go left
*

Doing this for every turn at the checkpoints will make it so that it will automaticly turn

***THIS IS ONLY WHEN THE X AND Y ARE EQUAL!***
'''

if (isinstance(startingY, int) == True and isinstance(endY, int) == False):
  transfer = True
  endY = int(endY)
  
elif (isinstance(startingY, int) == False and isinstance(endY, int) == True):
  transfer = True
  endY = str(endY) 
else:
  transfer = False
  





# Here are dictionaries

if startingX <= 0:
  #put dict looping code
  #have tester = starting
  for singleDict in dicts:
    for dictKey in singleDict:
      if(starting in singleDict[dictKey]):
        starting = dictKey
        break

if endX <= 0:
  #put dict looping code
  #have tester = starting
  for singleDict in dicts:
    for dictKey in singleDict:
      if(hallway in singleDict[dictKey]):
        hallway = dictKey
        break

print(locationX)
print(locationY)

#new
def topFirstMove(): # Arjuan gotta work here now
  # hardcode left to right bc right side is already built
  # include cafeteria and media center and all that
  # first move for the left rooms should get them to the doorway of main hallway i.e. double doors next to aux gym or double doors next to main gym
    global moves
    global startingY
    global startingX
    global EO
    global moving

  # LEFT SIDE TIME LET'S GOOO
    print("firstMove works")
    
    
    if ((starting in sec300HO1) or (starting in sec307) or (starting in sec300HO2)):

        if (locationY == "north"):
            startingY += 1
            print("StartingY: " + str(startingY))
            if (startingY == endY):
              if (startingY == 0):
                print("Turn " + EO + ", go to the 300/400 intersection")
              elif(locationX == "west"):
                print("5 Turn left, go to the 300/600 interesection")
              else:
                if (int(hallway) % 600 <= 13 or int(hallway) % 500 <= 14):
                  print("0 Turn " + EO + ", go to the 300/600 intersection")
              moves += 1
            else:
              moves += 1
              print("Turn " + EO + ", go to the 300/400 intersection")

        elif (locationY == "south"):
            startingY -= 1
            if (startingY == endY):
              print("Turn " + EO + ", go to the 300/400 intersection")
              if (starting == "307"):
                if (int(hallway) % 200 <= 13 or int(hallway) % 500 <= 14):
                  print("Go to the 300/200 intersection")
              moves += 1
            else:
              moves += 1
              print("Turn " + EO + ", go to the 300/400 intersection")

        elif (locationY == True):
          if (starting == "315"):
            moves += 1
            pass
            
          elif (startingY == 1):
            print("1 Turn left, go to the 300/600 intersection")
            moves += 1

          elif (startingY == -1):
            print("Turn right, go to the 300/200 intersection")
            moves += 1

          elif (startingY == 0):
            print("Turn right, go to the 300/400 intersection")
            moves += 1
          
          #elif (startingY == 0):
            #print("Turn left, go to the ")

    #elif (starting == 200) or (starting == 600):
    # print('THIS IS A TEST')
    #if (starting % 2 == 0):
    # print("go to the 300/400 intersection")

    elif ((starting in sec500HO1) or (starting in sec500HO2) or (starting in sec500HE1) or (starting in sec500HE2)):
        
        if (int(starting) % 2 == 0):
          if (locationY == "north"):
              startingY += 1
              moves += 1

              if ((starting in sec500HO2) or (starting in sec500HE2)):
                print("Turn " + EO + ", go to the 500/600 intersection")

              elif ((starting in sec500HO1) or (starting in sec500HE1)):
                if (startingY == endY and transfer == True):
                  pass
                else:
                  print("Turn " + EO + ", go to the 400/500 intersection")

          elif (locationY == "south"):
              startingY -= 1
              moves += 1
              
              if ((starting in sec500HO1) or (starting in sec500HE1)):
                print("Turn " + EO + ", go to the 500/200 intersection")
                

              elif ((starting in sec500HO2) or (starting in sec500HE2)):
                print ("Turn " + EO + ", go to the 500/400 intersection")
                

          elif (locationY == True):
              
            if (startingY == 1):
              if (int(starting) % 2 == 0):
                EO = "right"
              else:
                EO = "left"

              print("Turn " + EO + ", go to the 500/600 intersection")
              moves += 1

            elif (startingY == -1):
              if (int(starting) % 2 == 0):
                EO = "left"
              else:
                EO = "right"

              print("Turn " + EO + ", go to the 500/200 intersection")
              moves += 1
        
        else:
          if (locationY == "north"):
            startingY += 1
            moves += 1
            print("Turn " + EO + ", go to the 500/400 intersection")
            
          elif (locationY == "south"):
            startingY -= 1
            moves += 1
            print("Turn " + EO + ", go to the 500/400 intersection")
            

          elif (locationY == True):
            
            if (int(hallway) % 500 <= 14):
              pass
            
            elif (int(hallway) % 200 <= 21):
              print("Turn right, go to the 500/200 intersection")

            elif (endX < 1):
              print("Turn left, go to the 500/600 intersection")
            moves += 1
              

    elif ((starting in secEagleO) or (starting in secEagleE)):
      if (starting in secEagleO):
        EO = "left"
      else:
        EO = "right"
        
      print("Turn " +  EO + ", go to the end of the eagle wing")
      print("Turn left, go to the 200/500 intersection")
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
          
          if (startingX > endX):
            if (int(starting) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            
            print("Turn " + EO + ", go to the 600/300 intersection")
            startingX -= 1 #NOT WORKING!!!!!!
            moves += 1
            print(startingX)
            print(startingY)
          else:
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
                  print("Go forward till the 300/600 intersection")
                  startingY -= 1
                  moves += 1
                  if (startingY != endY):
                    print("1 Go to the 300/400 intersection")
                    startingY -= 1
                    moves += 1
                    if (startingY == endY):
                        #startingY += 1
                      moves += 1
                      if (int(hallway) % 200 <= 21 or int(hallway) % 500 <= 14):
                        print("Go to the 300/200 intersection")
                      #EO = "right"
                    #moves += 1
                    else:
                      moves += 1
                      EO = "left"
                      
                  else:
                    print("2 Go to the 300/400 intersection")
                    moves += 1
                    
              else:
                print("Turn " + EO + ", go to the 600/300 intersection")
                moves += 1

                        
        elif (startingY == 1 and startingX == 2):
          if (locationX != "" and startingX < endX):
            if (int(starting) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            

            
            startingX -= 1
          else:

            if (startingY == endY):

                  if (int(starting) % 2 == 0):
                    EO = "left"
                  else:
                    EO = "right"
                  
                  print("Turn " + EO +", go to the 600/300 intersection")
                  
                  startingX -= 1
                  moves += 1

            else:        
              print("Turn " + EO + ", go to the 600/500 intersection")
              print("RIGHT HERE RIGHT NOW?")
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
            
            print("Turn " + EO + ", go to the 400/500 intersection")
            moves += 1

        elif (startingY == -1 and startingX == 3):
          startingX -= 1
          moves += 1
      
        elif (startingY == -1 and startingX == 2):

          if (locationX != "" and startingX < endX):
          
            if (int(starting) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            if (startingY == endY):
                pass
            else:
              
              print("Turn " + EO + ", go to the 200/300 intersection") #$
            startingX -= 1
            moves += 1

          else:
            print("Turn " + EO + ", go to the 200/500 intersection")
            moves += 1

        elif (startingY == -1 and startingX == 1):
        
          if (locationX != "" and startingX < endX):
            if (int(starting) % 2 == 0):
               EO = "right"
            else:
                EO = "left"

            if (startingY != endY): #was == but I changed it to !=
              pass
            else:
              print("Turn " + EO +", go to the 200/500 intersection")
            startingX += 1
            moves += 1

          else:

            if (starting == "200"):
              
              if (startingY != endY):
                print("Go forward till the 200/300 intersection")
                moves += 1
                if (startingY != endY):
                  print("Go to the 300/400 intersection")
                  startingY += 1
                  moves += 1
                  if (startingY == endY):
                    #startingY += 1
                    moves += 1
                    if (int(hallway) % 600 <= 13 or int(hallway) % 500 <= 14):
                      print("TESTING1")
                      print("Go to the 300/600 intersection")
                
                  #EO = "right"
                else:
                  print("4 Go to the 300/400 intersection")
                  moves += 1
              else:
                moves += 1
                EO = "right"
                


            elif (int(starting) % 2 == 0):
                EO = "left"
                print("Turn " + EO + ", go to the 200/300 intersection")
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
            print("Turn " + EO + ", go to the 300/400 intersection")
            moves += 1

            # Arjuan start here 
        elif (startingY == 0 and startingX == -1):
          if(locationX != "east"):
            startingY += 1
          else:
            if(starting in secArt1 or starting in secArt2 or starting in secDrama):
              EO = "right"
            elif(starting in secBand or starting in secGuitar or starting in secChorusOrchestra):
              EO = "left"

            print("Turn " + EO + " go forward until the intersection, turn left, go forward until the double doors") #the start of the atheltic hallway
            print("1 Turn right and go forward until the next set of double doors") #the end of the athletic hallway
            startingX += 1
            moves += 1

        elif (startingY == 1 and startingX == -1):
          if(locationX != "east"): #here2
            print("Turn right, go forward until the last double doors on your left")
            print("Turn left, go forward until the first hallway on your right")
            startingY -= 1
          else:
            if (starting in secWeightRoom):
              print("Go to the start of the athletic hallway")
              print("Go to the end of the athletic hallway")
              
              
            elif (starting in secWrestling):
              print("Turn right")
              print("Turn left, to the entrance of the athletic hallway")
              print("Turn right, go to the end of the atheletic hallway")
              
              
            elif (starting in secMainGym or starting in secAuxGym):
              if (starting in secMainGym):
                EO = "left"
              else:
                EO = "right" #here
                
              print("Turn " + EO + " go into the main hallway")
            moves += 1
              
        elif (startingY == 1 and startingX == 0):
          if(locationX == "east"):
            if(starting in secCafe):
              print("Turn left, go forward in the main hallway until the first hallway on your left")
              print("Turn left, go into this hallway and keep going forward until the 300/600 intersection")
            elif(starting in secCounseling):
              print("Turn right, go forward until the 300/600 intersection")
            startingX += 1
          elif(locationX == "west"):
            if(starting in secCafe):
              print("Turn left, go forward in the main hallway until the first hallway on your right")
              print("Turn right, go into this hallway until the second set of double doors")
            elif(starting in secCounseling):
              print("Turn left, go forward into the main hallway, then turn left and go forward until the first hallway on your right")
              print("Turn right and go forward into this hallway until the second set of double doors")
            startingX -= 1
          elif(locationY == "south"):
            if(starting in secCafe):
              print("Go forward in the main hallway until the first hallway on your right")
            elif(starting in secCounseling):
              print("Turn left, go forward into the main hallway, then turn left and go forward until the first hallway on your right")
            startingY -= 1
          moves += 1
        
        elif (startingY == 0 and startingX == 0):
          print("This works")
          print(locationX)
          if(locationX == "east"): # go to 300/400
            if(starting in secMainEntrance):
              print("Go forward until the first hallway on your right")
              print("Turn right and go forward until the 300/400 intersection")
            elif(starting in secAuditorium):
              print("Turn left, go forward until the first hallway on your right")
              print("Turn right and go forward until the 300/400 intersection")
            elif(starting in secMediaCenter):
              print("Turn right, go forward, turn right and go forward until the 300/400 intersection")
            elif(starting in secMainOffice):
              print("Turn left, go forward, turn left and go forward until the 300/400 intersection")
            elif(starting in secClinic):
              print("Turn left and go forward until the 300/400 intersection")
            startingX += 1
          elif(locationX == "west"): # go to fine arts hallway 
            print("Here now")
            print(starting)
            if(starting in secMainEntrance):
              print("Go forward until the first hallway on your left")
              print("Turn left and go down the fine arts hallway")
            elif(starting in secAuditorium):
              print("Turn left, go forward until the first hallway on your left")
              print("Turn left, go forward until the double doors on your left")
            elif(starting in secMediaCenter):
              print("Turn left, go forward into the main hallway")
              print("Turn right, go forward until the first hallway on your left")
              print("Turn left, go forward until the double doors on your left")
            elif(starting in secMainOffice):
              print("Finally here")
              print("Turn right, go forward into the main hallway")
              print("Turn right, go forward until the first hallway on your left")
              print("Turn left, go forward until the double doors on your left")
            elif(starting in secClinic):
              print("Turn right, go forward into the main hallway")
              print("Turn right, go forward until the first hallway on your left")
              print("Turn left, go forward until the double doors on your left")
            startingX -= 1
            print(startingX)
          else:
            print("Go forward until the second hallway on your right")
            startingY += 1
          moves += 1
          
              
            
  

            
          if(locationX == "east"):
              if(starting in secArt1 or starting in secArt2):
                print("Turn right, go forward until the intersection, turn left, go forward until the double doors")
                print("4 Turn right and go forward until the next set of double doors")
                startingX = 0
              elif(starting in secGuitar or starting in secBand):
                print("Turn left and go forward until the intersection, then turn left go forward until the double doors")
                print("3 Turn right and go forward until the next set of double doors")
                startingX = 0
              elif(starting in secChorusOrchestra):
                print("Turn left go forward until the double doors")
                print("2 Turn right and go forward until the next set of double doors")
                startingX = 0
              elif(starting in secWrestling):
                print("Turn right and go forward, then turn left and go forward until the double doors") 
                startingX = 0
            

              
'''
    else:
      print("man....")
      if (startingY == 1 and startingX == 1):
          print("Turn " + EO + ", go to the 600/300 intersection")
          moves += 1

      elif (startingY == 1 and startingX == 2):
          print("Turn " + EO + ", go to the 600/500 intersection")
          moves += 1

      elif (startingY == 0 and startingX == 2):
          print("Turn " + EO + ", go to the 400/500 intersection")
          moves += 1

      elif (startingY == -1 and startingX == 2):
          print("Turn " + EO + ", go to the 200/500 intersection")
          moves += 1

      elif (startingY == -1 and startingX == 1):
          if (int(starting) % 2 == 0):
              EO = "left"

          print("Turn " + EO + ", go to the 300/200 intersection")
          moves += 1

      elif (startingY == 0 and startingX == 1):
          print("Turn " + EO + ", go to the 300/400 intersection")
          moves += 1
'''

# Function works fine, while loop is problem
def topMoveCheck():

   # print("in movecheck")
    global startingX
    global startingY
    global EO
    global moves
    global locationX 
    global locationY
   #  print(locationX + ", " + locationY)

   # print(str(startingX) + ", " + str(startingY))
    """
    print('\nin function')
    print("TEST: " + str(startingY))
    print("TEST: " + str(startingX))
    """
    if (startingY == 1 and startingX == 1):  # Checkpoint (1, 1)
        print("Checkpoint (1, 1)")
        print(str(locationX) + ", " + str(locationY))
        print(str(startingX) + ", " + str(startingY))

        if (startingY != endY):  #I'm pretty sure we don't need this because of the while loop\
          startingY -= 1
          
          if (startingY == endY and transfer == True):
            pass
            
          else:
            if(locationX == "west"):
              startingX -= 1
              startingY += 1
              locationY == "south"
              print("Hello: " + str(startingX) + ", " + str(startingY))

            else:  
              EO = "left"
              print("Turn " + EO + ", go to the 300/400 intersection")


            
            moves += 1

        elif (startingX != endX):
          if (starting == "315"):
            print("Go forward into the 600 hallway")
            startingX += 1
            moves += 1
          
          else:
            if(locationX == "west"):
              if (endX <= 0):
                #if ((int(starting) % 600 <= 13) or (14 <= int(starting) % 500 <= 8)):
                  #print("")
                print("Turn left") #change print statement (logic good) Ask Arjun about this
              startingX -= 1
            
            elif(locationX == "east"):
            #$if (locationY != True):
                #print("Go up to hallway intersection 600/300")
                #pass
                print("Here now (1, 1)")
                startingX += 1
                

    elif (startingY == 1 and startingX == 2):  # Checkpoint (2, 1)
        print("Checkpoint (2, 1)")
        if (startingY != endY):
            #print("at checkpoint 2,1")
            startingY -= 1
            if (startingY == endY and transfer == True):
              pass
            else:
              EO = "right"
              print("Turn " + EO + ", go to 400/500 intersection")
              

        elif (startingX != endX):
            #if (locationY != True):
                #print("go up to hallway intersection 600/500")
                #pass
            if (startingX != endX):
                #print("checkpoint 2,1")
                startingX -= 1
                print("Turn left, go to the 600/300 intersection") #was "go to the 600/300 intersection"
                print("StartingX = " + str(startingX))

    elif (startingY == 1 and startingX == 0):
      print("Checkpoint 0, 1")
      if(locationX == "west"):
        
        if(int(starting) % 600 <= 13 or (8 <= int(starting) % 500 <= 14)):
          print("Go forward into the main hallway")
          
        elif(locationY == "north"):  #You can replace with else, check if transfer is true then make them turn right not left
          print("testing")
          #if (starting == "307"):
           # print("2 Turn left, go to the 300/600 intersection")

          print("Turn left, go forward into the main hallway")
          print("here?????")
        elif(locationY == "south"): #change to transfer
          print("bruh")
          print("Turn right, go forward into the main hallway")
        
        print(str(startingX) + ", " + str(startingY))
        print(str(endX) + ", " + str(endY))
        print("Turn left, go forward until the athletic hallway")
        print("Turn right, go forward into the athletic hallway")
        startingX -= 1
        moves += 1
        locationY = "south"

      elif(locationX == "east"):
        print("Turn left, go forward until the counseling hallway, turn right and go forward until the 300/600 intersection")
        startingX += 1
        moves += 1

    elif (startingY == 0 and startingX == 2):  # Checkpoint (2, 0)]
      #check if there is x movement and change it
      if (startingX != endX):
        if (locationY == "north"):
          if (int(hallway) % 400 <= 13 and int(hallway) < 600):
            print("met")
            pass
          elif ((int(hallway) % 300 <= 15 and int(hallway) < 600) or (startingX > endX)):
            print("hsould be in")
            if (hallway == "307"):
              pass
            else:
              print("Turn left, go to the 400/300 intersection")

          print("huh")
          startingX -= 1
            
        elif (locationY == "south"): #NOT WORKING
          if (int(hallway) % 200 <= 13 and int(hallway) < 413):
            print("Go to the 500/200 intersection")
            startingY -= 1
            pass
          elif (int(hallway) % 500 >= 8):
            print("Turn right, go to the 400/300 intersection") #NEW!!!
            print("getting")
            startingX -= 1
      else:
          if (startingY != endY):
              if (locationY == "north"):
                  if (moves == 1):
                      if ((starting in sec500HO1) or (starting in sec500HO2)
                              or (starting in sec500HE1)
                              or (starting in sec500HE2)):
                          #startingY += 1
                          #print("val")
                          if (startingY != endY):
                            if (int(hallway) % 500 <= 14):
                              startingY += 1
  
                            else:
                              print("Go to the 600/500 intersection")
                              startingY += 1
  
  
                      else:
                          if (int(hallway) % 500 <= 14):
                            pass
                          else:
                            EO = "left"
                            print("Turn " + EO + ", go to the 600/500 intersection")
                            startingY += 1
                  else:
                    if (int(hallway) % 600 <= 13 or int(hallway) % 300 <= 15):
                      print("Go to the 500/600 intersection")
                    startingY += 1
  
              elif (locationY == "south"):
                  if (moves == 1):
                      if ((starting in sec500HO1) or (starting in sec500HO2)
                              or (starting in sec500HE1) or (starting in sec500HE2)):
                          #print("val")
  
                          if (startingY != endY):
                            #if (int(hallway) % 500 >= 0):
                            #  startingY -= 1
                            
                            #else:
                            if (int(hallway) % 200 <= 13 or int(hallway) % 300 <= 15):
                        
                              print("Go to the 500/200 intersection")
                            startingY -= 1
  
                      else:
                        if (int(hallway) % 200 <= 13 or int(hallway) % 300 <= 15):
                          if ((starting in secEagleO) or (starting in secEagleE)):
                            pass
                          else:
                            EO = "right"
                            print("Turn " + EO + ", go to the 500/200 intersection")
                        startingY -= 1
  
                  else:
                    if (int(hallway) % 200 <= 13 or int(hallway) % 300 <= 15):
                      print("Go to the 500/200 intersection ")
                    startingY -= 1
                      
  
          elif (startingX != endX):
              #if (locationY != True):
                  #print("go to the hallway intersection 400/500")
                  #pass
              if (startingX != endX):
                  #print("checkpoint 2,0")
                  EO = "left"
                  #print("Turn " + EO + ", going left")
                  startingX -= 1
             # if (startingX == endX):
               #   print("doneXXYYXX kissy")

    elif (startingY == -1 and startingX == 2):  # Checkpoint (2, -1)
        if (startingY != endY):
          
          startingY += 1
          if (startingY == endY and transfer == True):
              pass
          else:
              
            if ((starting in secEagleO) or (starting in secEagleE)):
              EO = "right"
            else:
              EO = "left"
              
            print("Turn " + EO + ", go to the 500/400 intersection")
            print("test3")

        elif (startingX != endX):
          if ((hallway in secEagleO) or (hallway in secEagleE)):
            if (starting in sec600HO2) or (starting in sec600HE2) or (starting in sec500HO2) or (starting in sec500HE2):
              print("Go to the 500/200 intersection")
            elif ((starting in sec400HO2) or (starting in sec400HE2)):
              print("Turn right, go to the 500/200 intersection")
            startingX += 1

          else:
            
            EO = "right"
            print("Turn " + EO + ", go to the 200/300 intersection") #was not here before
            startingX -= 1
            #if (startingX == endX):
             #   print("doneXXYYXX kissy")

    elif (startingY == -1 and startingX == 1):  # Checkpoint (1, -1) #********
        if (startingY != endY):
          
            startingY += 1
            if (startingY == endY and transfer == True):
                pass
            else:
              
              EO = "right"
              print("Turn " + EO + ", go to the 300/400 intersection")

        elif (startingX != endX):
            #if (locationY != True):
                # print("go to the hallway intersection 300/200")
                #pass
            if (startingX != endX):
                #print("checkpoint 1,-1")
                if (starting == "200"):
                  startingX += 1
                else:
                  EO = "left"
                  startingX += 1
            #if (startingX == endX):
            #   print("doneXXYYXX kissy")

    elif (startingY == 0 and startingX == 1):  # Checkpoint (1, 0)
        print("AT CHECKPOINT")
        print(moves)
      #check if x movement and change it
        if (startingX > endX):
          #print("Turn left, go forward into the main hallway")
          startingX -= 1


        elif (startingX != endX and int(hallway) % 600 > 13):
          if (locationY == "north"):
            if (int(hallway) % 500 <= 14):
              print("Turn right, go to the 400/500 intersection")
              startingX += 1
            else:
              if ((moves > 2) and (startingX > endX) or ((int(starting) % 400 <= 11) and (startingX > endX)) or ((int(starting) % 500 <= 6 )and (startingX > endX))):
                print("Turn right, go to the 300/600 intersection")
                print("donda")
              else:
                print("Go to the 300/600 intersection")  
              print(locationX)
              startingY += 1
              

          elif (locationY == "south"): #NOT WORKING
            if (int(hallway) % 200 <= 13 and int(hallway) < 413): #may not have purpose
              pass
            elif (int(hallway) % 500 <= 14):
              print("Turn left, go to the 400/500 intersection")
            startingX += 1
          
          elif(locationX == "west"):
            if(locationY == "north"):
              print("Turn left, go into the main hallway")
            elif(locationY == "south"):
              print("Turn right, go into the main hallway")
            else:
              print("Go into the main hallway")
            startingX -= 1
        else:
          print("in")
    
          if (startingY != endY):
              if (locationY == "north"):
                  print("test")
                  if (moves == 1):
                      if ((starting in sec300HO1) or (starting in sec307)
                              or (starting in sec300HO2)):
                          if (startingY != endY):
                            if (int(hallway) % 300 <= 15):
                              startingY += 1
                              print("Go to the 300/600 intersection")
                            
                            else:
                              startingY += 1
                              print("Go to the 300/600 intersection")
                          
                          else:
                            startingY += 1
                            print("Go to the 300/600 intersection")
                        
                      else:
                        EO = "right"
                        print("3 Turn " + EO + ", go to the 300/600 intersection")
                        startingY += 1
                  else:
                    startingY += 1
                    if ((hallway in sec307) or (hallway in sec300HO1)):
                      pass
                    else:
                      print("TEST2")
                      
                      print("Go to the 300/600 intersection")
                    #startingY += 1

              elif (locationY == "south"):
                if (moves == 1):
                    if ((starting in sec300HO1) or (starting in sec307)
                            or (starting in sec300HO2)):
                        if (startingY != endY):
                          if (int(hallway) % 300 >= 0):
                            #print(startingY)
                            startingY -= 1
                            if (int(hallway) % 300 <= 15):
                              moves += 1
                            else:
                            
                              print("5 Go to the 300/400 intersection")
                              startingY -= 1
                              #moves += 1
                          
                    else:
                      EO = "left"
                      if (int(hallway) % 200 <= 13 or int(hallway) % 500 <= 14):
                        print("Turn " + EO + ", go to the 300/200 intersection")
                      startingY -= 1
                else:
                  startingY -= 1
                  if (startingY == endY):
                    if (int(hallway) % 200 <= 21 or int(hallway) % 500 <= 14):
                      print("staruUUUU2")
                      print("Go to the 300/200 intersection") ####
                    else:
                      print("hold on")
                      pass
                
                  else:
                    print("Go to the 300/200 intersection")
                    
            

          elif (startingX != endX):
            print("TESTINGING")
              #if (locationY != True):
                  #print("go to the hallway intersection 300/400")
                  #pass
            if (startingX > endX):
              print("Turn left, go into the main hallway")
              startingX -= 1
              
            else:
              if (locationY == "north"):
                EO = "right"

              elif (locationY == "south"):
                EO = "left"
              startingX += 1
              #if (startingX == endX):+
    elif (startingY == 0 and startingX == 0):
      if (locationX == "west"):
        if (int(starting) % 400 <= 11):
          print("Go into the main hallway")
          
        elif (locationY == "north"):
          print("Turn left, go into the main hallway")
          
        elif (locationY == "south"):
          print("Turn right, go into the main hallway")
          
        print("Turn right, go down the main hallway until the fine arts hallway and turn left")
        startingX -= 1
        print(startingY == endY)
        moves += 1
      elif (locationX == "east"):
        #this if for going from left to right
        # fix this shiz
        print("Turn right, go down the main hallway until the main office hallway, then turn left and go forward until the 300/400 intersection")
        startingX += 1
        moves += 1
          

    elif (startingY == 0 and startingX == -1):
      #new shiz
      if(locationX == "west"):
        startingY += 1
      
      if(locationX == "east"):
        if(locationY == "north"):
          print("Turn left, go forward until the first hallway on your right")
          startingY += 1
          
      """
      if(locationX == "west"):
        turn left, go to end of finearts hallway, turn right, go up (update y to 1)
        """
      # MoveCheck only updates starting Y, in for startingY == 1 and startingX == -1 check if there is movement in locationY using locationY == "north", give directions as if you were starting from the fine arts hallway and then if the locationY is not north (else statement), then do it in the athletic hallway and vice versa for (-1, 1)
    
    elif (startingY == 1 and startingX == -1):
      if(locationY == "south"):
        print("Turn right, go forward until the hallway on your left")
        #  print("Turn right")
        # Marker ting
        startingY -= 1
        startingX += 1
        print("this happens")
        locationX = "east"
      elif(locationY == True):
        print(str(startingX) + ", " + str(startingY))
        print(locationY)
        startingX += 1
        print("Turn left, go forward until the first hallway on your right")
      else:
        print("This thing is a thing")
        print("Starting: " + "(" + str(startingX) + ", " + str(startingY) + ")")
        print("Ending: " + "(" + str(endX) + ", " + str(endY) + ")")
        print("LocationX, LocationY: " + "(" + str(locationX) + ", " + str(locationY) + ")")
        







def topClassroom():
  print("in classroom")
  global EO
  global startingX
  global startingY
  global Turning
  global locationX
  global locationY

  if (startingY == 1 and startingX == 0):
    if(locationX == "west"):
      if(hallway in secCafe):
        print("Go into the main hallway, turn right, the cafeteria is straight ahead")
      elif(hallway in secCounseling):
        print("The counseling hallway is on your left")
    elif(locationX == "east"):
      if(hallway in secCafe):
        print("The cafeteria is straight ahead")
      elif(hallway in secCounseling):
        print("Turn right, go forward and the counseling office will be on your right")
    elif(locationX == "" and locationY == True):
      if(hallway == "1101"):
        print("Turn left, go forward until the first hallway on your left")
        print("Turn left, go forward and counseling will be on your right")
      elif(hallway == "700"):
        print("1 Turn left, go forward into the main hallway")
        print("Turn right, go forward and the cafeteria is straight ahead")
    else:
      if(hallway == "1101"):
        print("Turn right, go forward and counseling will be on your right")
      elif(hallway == "700"):
        print("Go forward, the cafeteria is straight ahead")
    


  elif(startingY == 0 and startingX == 0):
    if(locationX == "west"):
      if(hallway in secAuditorium):
        print("Go forward into the main hallway")
        print("Turn left, go down the main hallway and the auditorium will be on your right")
      elif(hallway in secMediaCenter):
        if(starting in sec300HO1 or starting in sec307):
          EO = "right"
        elif(locationY == "north"):
          EO = "left"
        print("Turn " + EO + ", go into the main hallway, the media center/library is on your left")
      elif(hallway in secMainOffice):
        print("Go forward into the main hallway, the main office is on your right")
        
      elif(hallway in secMainEntrance):
        print("Go forward into the main hallway, the main entrance is on your left")
        
      elif(hallway in secClinic):
        print("The clinc is on your right")
        
    elif(locationX == "east"):
      if(hallway in secAuditorium):
        print("Go forward and the doors to the auditorium will be on your right")
        
      elif(hallway in secMediaCenter):
        print("Turn left and the media center/library is on your right")
        
      elif(hallway in secMainOffice):
        print("Turn left and the main office is on your left")
        
      elif(hallway in secMainEntrance):
        if(starting == "1106" or starting == "1103"):
          print("The main entrance is straight ahead")
        else:
          print("Go forward into the main hallway, the main entrance is on your right")
        
      elif(hallway in secClinic):
        print("Turn left, go forward and the clinc is on your left")

    else: # start here 7/22
    #  auditorium, main office, clinic, and media center
      if(hallway in secAuditorium):
        print("Go forward and the doors to the auditorium will be on your left")
        
      elif(hallway in secMediaCenter):
        print("Go forward and the doors to the media center/library will be on your right")
        
      elif(hallway in secMainOffice):
        print("Go forward and the doors to the main office will be on your right")
        
      elif(hallway in secClinic):
        print("Go forward until the first hallway on your right")
        print("Turn right and go forward, the clinic is on the left")
      
      elif(hallway in secMainEntrance):
        if(starting == "801"):
          print("Go forward into the main hallway and turn right")
        
        elif(starting == "100"):
          print("Turn left and go forward into the main hallway, then turn left")
        
        elif(starting == "1102"):
          print("Go forward into the main hallway and turn right")
        
        elif(starting == "1104"):
          print("Turn right and go forward into the main hallway, then turn left")

        print("The main entrance is straight ahead")


  elif(startingY == 1 and startingX == -1):
    if(locationX == "west"):
  #    print(moves)
      if(locationY == "north"):
        if(hallway == "902"): 
          if((starting in secMainOffice) or (starting in secAuditorium) or (starting in secMediaCenter) or (starting in secClinic) or (starting in secMainEntrance)):
            Turning = "right"
            EO = "left"
          else:
            Turning = "left"
            EO = "right"
          print("Turn " + Turning + ", go down the hallway and wrestling will be on the " + EO)
        elif(hallway == "913"):
          print("Turn right, go down the hallway and enter your designed locker room hallway")
        elif(hallway == "1103"): # aux gym
          print("Turn right, go to the end of the athletic hallway")
          print("Turn right, go forward and the auxiliary gym will be on your right")
        elif(hallway == "1106"): # main gym
          print("Turn right, go to the end of the athletic hallway")
          print("Turn right, go forward and the main gym will be on your left")
      else:
        if(hallway == "902"):
          print("Turn left, go down the hallway and wrestling will be on your right")
        elif(hallway == "913"):
          print("Go down the hallway and enter your designated locker room hallway")
    else: # start here
   #   print(moves)
      print("in second if statement")
      if(locationY == "north"):
        if(hallway == "902"): 
          # Issue here, 301 to 902 test case
          print(locationX)
          print("Turn right, go down the hallway and wrestling will be on the left")
        elif(hallway == "913"):
          print("Turn right, go down the hallway and enter your designed locker room hallway")
      else:
        if(hallway == "902"):
          if(starting == "1106" or starting == "1103"):
            if(starting == "1106"):
              EO = "right"
            elif(starting == "1103"):
              EO = "left"
            print("Turn " + EO + ", go down the hallway until the second set of double doors")
          print("Turn left, go down the hallway and wrestling will be on your right")
        elif(hallway == "913"):
          print("Go down the hallway and enter your designated locker room hallway")
  #print("in loop")
  #print("Go to classroom xxx")

  elif((startingY == 0) and (startingX == -1)):
    
    if(starting == "902" or starting == "913"):
      locationX = "east"

    if(locationX == "west"):
      print("Go forward until the double doors on the left")
      EO = "left"
      """
      if(hallway == "804"):
        print("Go forward until the fine arts door on your left")
        print("Turn left, go forward until the first hallway on your right")
        print("Turn right, the art classroom will be on your left")
      elif(hallway == "802"):
        print("Go forward until the fine arts door on your left")
        print("Turn left, go forward until the first hallway on your right")
        print("Turn right, the drama classroom will be the first door on your left")
      elif(hallway == "803"):
        print("Go forward until the fine arts door on your left")
        print("Turn left, go forward and 803 will be on your right")
      elif(hallway == "805"):
        print("Go forward until the fine arts door on your left")
        print("Turn left, go forward until the first hallway on your right")
        print("TUrn right, the guitar classroom will be on your right")
      elif(hallway == "807"):
        print("Go forward until the fine arts door on your left")
        print("Turn left, go forward until the first hallway on your right")
        print("TUrn right, the band classroom will be on your right")
      elif(hallway == "806"):
        print("Go forward until the fine arts door on your left")
        print("Turn left, go forward until the first hallway on your right")
        print("Turn right, the art classroom will be on your left")
        """
    elif(locationX == "east"):
      EO = "right"
    
    if(int(hallway) % 2 == 0):
      print("Turn " + EO + ", go forward into the fine arts hallway until the first hallway on your right")
      print("Turn right and go forward, your destination will be on your left")
    elif(hallway == "803"):
      print("Turn " + EO + ", go forward into the fine arts hallway and 803 will be on your right")
    else:
      print("Turn " + EO + ", go forward into the fine arts hallway until the first hallway on your right")
      print("Turn right and go forward, your destination will be on your right")


    # if(hallway % 2 != )
    """else:
      if(hallway == "804"):
      elif(hallway == "801"):
      elif(hallway == "802"):
      elif(hallway == "803"):
      elif(hallway == "805"):
      elif(hallway == "807"):
      elif(hallway == "806"):
      # TODO: idk wake up tomorrow early and finish classroom
"""
  elif ((startingY == 1) and (startingX == 1)):
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
    
            print("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
          else:
            if (starting == "315"):
              if (int(hallway) % 2 == 0):
                  EO = "right"
              else:
                  EO = "left"
              print("Go down the 600 hallway and " + hallway + " will be on your " + EO)
            else:
              if (hallway != "601"):
                
                #print("go to the 300/600 intersection")
                if (int(hallway) % 2 == 0):
                  EO = "right"
                else:
                  EO = "left"
                  
                print("Turn right, go down the 600 hallway and " + hallway + " will be on your " + EO)
              else:
                print("Turn left, 601 will be on your right")
        elif (int(hallway) % 300 <= 15):
          if (int(starting) % 600 <= 13):
            if (starting == "601"):
              print("Go down the 300 hallway and " + hallway + " will be on your right")
            else:
              if (int(starting) % 2 == 0):
                Turning = "left"
              else:
                Turning = "right"
              print("Turn " + Turning + ", go to the 600/300 intersection")
              print("9 Turn left, go down the 300 hallway and " + hallway + " will be on your right")
          else:
            if (int(starting) % 300 <= 15 and moves < 2):
              if (int(hallway) > int(starting)):
                Turning = "left"
                EO = "left"
              else:
                Turning = "right"
                EO = "right"
  
              print("1 Turn " + Turning + ", go down the 300 hallway and " + hallway + " will be on your " + EO)
              
            else:    
              print("Go down the 300 hallway and " + hallway + " will be on your left")


    else:
      if (int(hallway) % 600 <= 13):
        print("TESTING")
        if (int(starting) % 600 <= 13):
          if (int(starting) % 2 == 0):
            Turning = "left"
          else:
            Turning = "right"
            
          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"
            
          print("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
        else:
          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"
          if (starting == "315"):
            print("Go down the 600 hallway and " + hallway + " will be on your " + EO)

          #print("Go to the 500/600 intersection")
          #change this !!!!!!!!!!!!!!!!!
          if (hallway == "601"):
            print("Turn left, 601 will be on your right")
          else:
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            print("Turn right, go down the 600 hallway and " + hallway + " will be on your " + EO)
          
          
            
      elif (int(hallway) % 300 <= 15):
        #print("Turn left, go to the 600/300 intersection")

        if (int(starting) % 200 <= 13 and int(starting) < 300):
          print("Go down the 300 hallway and " + hallway + " will be on your left")
        else:
          if (hallway in sec300HO2):
            Turning = "left"
            EO = "right"
          else:
            Turning = "right"
            EO = "left"
          print("Turn " + Turning + ", go down the 300 hallway and " + hallway + " will be on your " + EO )
          print("OP 2") #I changed 'turn right' to 'turn left' because the new paths should use this conditional again ... I think. Change if needed
          
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
            print("Turn " + Turning + ", go down the 500 hallway and " + hallway + " will be on your " + EO)
          else:
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            if (int(starting) % 2 == 0):
              Turning = "right"
            else:
              Turning = "left"
            print("Go down the 500 hallway and " + hallway + " will be on your " + EO)
        elif (int(starting) % 600 <= 13):
          if (int(starting) % 2 == 0):
              EO = "right"
          else:
              EO = "left"
          print("Turn " + EO + ", go to the 600/500 intersection")
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
          print("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
          
        else:
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
            
          if (int(starting) % 400 <= 13):
            
            print("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)
          else:
            print("Go down the 500 hallway and " + hallway + " will be on your " + EO)
            
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
          print("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
        else:
          if (moves == 0):
            if (int(starting) % 2 == 0):
                EO = "right"
            else:
                EO = "left"
              
            print("Turn " + EO + ", go to the 500/600 intersection")
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
          print("Turn left, go down the 600 hallway and " + hallway + " will be on your " + EO)
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
          print("Turn " + Turning + ", go down the 600 hallway and " + hallway + " will be on your " + EO)
          
        else:
          if (starting == "315"):
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            print("Go down the 600 hallway and " + hallway + " will be on your " + EO)
            
          else:
            if (int(hallway) % 2 == 0):
                EO = "right"
            else:
                EO = "left"
            print("Turn right, go down the 600 hallway and " + hallway + " will be on your " + EO)
        
      elif (int(hallway) % 500 <= 14):
        if (starting == "315"):
          print("Go to the 600/500 intersection")
        else:
          print("Turn right, go to the 600/500 intersection")
        if (int(hallway) % 2 == 0):
            EO = "left"
        else:
            EO = "right"
        print("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
        
  elif (startingY == 0 and startingX == 2):
    if (locationX == ""):
      
      #print("Go to the 500/400 intersection")
      
      if (int(hallway) % 2 == 0):
          EO = "left"
      else:
          EO = "right"
        
      if (locationY == "south"):
        
        print("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      elif (locationY == "north"):
        
        print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
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
            
            print("Turn " + Turning + ", go down the 400 hallway and " + hallway + " will be on your " + EO)
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
            
            print("Turn " + Turning + ", go down the 400 hallway and " + hallway + " will be on your " + EO)
      else:
        
        print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      #print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
    else:
      if ((starting in secEagleO) or (starting in secEagleE)):
        if (int(hallway) % 2 == 0):
          EO = "left"
        else:
          EO = "right"
        print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
      else:
        if (int(hallway) % 2 == 0):
            EO = "right"
        else:
            EO = "left"
        if (locationY == "south"):
          print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
        elif (locationY == "north"):
          print("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
        elif (locationY == True):
          if (int(starting) % 2 == 0):
            Turning = "right"
          else:
            Turning = "left"
          print("Turn "+ Turning +", go down the 400 hallway and " + hallway + " will be on your " + EO)
          
  elif (startingY == -1 and startingX == 3):
    if (starting == "307"):
      print("Go to the 300/200 intersection")
    
    if (int(starting) % 200 <= 13 and locationY == True):
      if (int(starting) % 2 == 0):
        if (int(starting) % 2 == 0):
          Turning = "right"
        else:
          Turning = "left"
        print("Turn " + Turning + ", go into the eagle wing") 

    else:
      print("Turn left, go into the eagle wing")
      #I wanna do go down the 200 hall but I can't do that because of the way this shit is set up
        
    if (hallway in secEagleE):
      EO = "left"
    else:
      EO = "right"    
    print("Turn right, go down the eagle wing and " + hallway + " will be on your " + EO)
        

  elif (startingY == -1 and startingX == 2):   
    if ((starting in secEagleO) or (starting in secEagleE)):
      if (int(hallway) % 2 == 0):
        EO = "left"
      else:
        EO = "right"
      print("Go down the 200 hallway and " + hallway + " will be on your " + EO)
        
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
           
            print("Turn " + Turning + ", go down the 500 hallway and " + hallway + " will be on your " + EO)
            
          else:
            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            print("Go down the 500 hallway and " + hallway + " will be on your " + EO)
        else:
          if (int(starting) % 600 <= 13):
            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            print("Go down the 500 hallway and " + hallway + " will be on your " + EO)
            
          elif (int(starting) % 400 <= 13):
            if (int(starting) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            print("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
            
          else:
            
            if (int(starting) % 2 == 0):
                EO = "right"
            else:
                EO = "left"
            print("Turn " + EO + ", go to the 200/500 intersection")
            
          
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            print("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)
    
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
            print("HERE")
            print("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
          else:
            if (int(starting) % 2 == 0):
              Turning = "left"
            else:
              Turning = "right"

            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            print("Turn " + Turning + ", go to the 500/200 intersection")
            print("Turn right, go down the 200 hallway and " + hallway + " will be on your " + EO)
        else:
          if ((starting in secEagleO) or (starting in secEagleE)):
            pass
          if (int(hallway) % 2 == 0):
              EO = "left"
          else:
              EO = "right"
            
          print("Turn right, go down the 200 hallway and " + hallway + " will be on your " + EO)
          #print("Turn " + EO + ", go to the 500/200 intersection") 
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
          
          
          print("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
        else:
          
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
          print("Turn left, go down the 200 hallway and " + hallway + " will be on your " + EO) ##CHANGED 
          
      elif (int(hallway) % 500 <= 15):
        print("TEST")
        if ((starting in sec300HO2) or (starting in sec307)):
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"

          if ((starting in secEagleO) or (starting in secEagleE)):
            print("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
            
          else:
            if (int(starting) < 400 and int(starting) % 200 <= 13):
              if (int(starting) % 2 == 0):
                  Turning = "right"
              else:
                  Turning = "left"
            else:
              print("staruUUUU")
              Turning = "left"
              
            print("Turn " + Turning + ", go to the 200/500 intersection")
            print("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)

        else:
          if (int(starting) % 200 <= 13 and int(starting) < 300):
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
            print("Turn left, go down the 500 hallway and " + hallway + " will be on your " + EO)
          
          else:
            if (int(hallway) % 2 == 0):
              EO = "left"
            else:
              EO = "right"
            
            print("Turn right, go down the 500 hallway and " + hallway + " will be on your " + EO)
            

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
              
            print("3 Turn " + Turning + ", go down the 300 hallway and " + hallway + " will be on your " + EO)
            
          else:
            print("Go down the 300 hallway and " + hallway + " will be on your right")
            
        elif (int(starting) % 200 <= 13 and moves <= 1):
          if (starting == "200"):
            print("Go down the 300 hallway and " + hallway + " will be on your left")
            
          else:
            print("Turn " + EO + ", go to the 200/300 intersection")
            print("4 Turn right, go down the 300 hallway and " + hallway + " will be on your left")
          
        else:
          if (int(starting) % 400 <= 13):
            print("5 Turn left, go down the 300 hallway and " + hallway + " will be on your right")
            
          else:       
            print("please") 
            print("Go down the 300 hallway and " + hallway + " will be on your right")
        
      elif (int(hallway) % 200 <= 13):
        if (int(starting) % 200 <= 13 and moves < 1):
          if (int(hallway) > int(starting)):
            print("Turn right, go down the 200 hallway and " + hallway + " will be on your right")
          else:
            print("Turn left, go down the 200 hallway and " + hallway + " will be on your left")
        else:
          if (hallway == "200"):
            if (moves == 0):
              print("Turn right, classroom 200 is right ahead")
            else:
              print("Classroom 200 is right ahead")
            
          else:
            if (moves < 1):
              print("Turn right, go to the 300/200 intersection")
            
            if (int(hallway) % 2 == 0):
              EO = "right"
            else:
              EO = "left"
              
            print("Turn left, go down the 200 hallway and " + hallway + " will be on your " + EO)
          #THIS IS FOR THE SAME X AND Y ON THE 200  
  
    else: 
      if (int(hallway) % 300 <= 15):

        if (((int(starting) % 200 <= 13) and (moves <= 1))):
          if (int(starting) % 2 == 0):
            EO = "left"
          else:
            EO = "right"
          
          print("Turn " + EO + ", go to the 200/300 intersection")
          print("Turn right, go down the 300 hallway and " + hallway + " will be on your left")
          
        else:
          if ((starting in secEagleO) or (starting in secEagleE)):
            print("Go to the 200/300 intersection")
            print("Turn right, go down the 300 hallway and " + hallway + " will be on your left")
          elif (locationY == True):
            print("Turn right, go down the 300 hallway and " + hallway + " will be on your left") ### I changed this. The original (Go down the 300 hallway and " + hallway + " will be on your right)
          else:
            print("Turn left, go down the 300 hallway and " + hallway + " will be on your right")
        
        print("OP 1")
        
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

          
          
          print("Turn " + Turning + ", go down the 200 hallway and " + hallway + " will be on your " + EO)
          
        else:
        
          if (int(hallway) % 2 == 0):
            EO = "left"
          else:
            EO = "right"

          if ((starting in secEagleE) or (starting in secEagleO)):
            print("Go down the 200 hallway and " + hallway + " will be on your " + EO)
          else:
            print("Turn right, go down the 200 hallway and " + hallway + " will be on your " + EO)
        
          
  elif (startingY == 0 and startingX == 1):
    if (locationX == ''):
      if (hallway == "307"):
        if (locationY == "north"):
          print("Go down the 300 hallway and 307 will be on your left")
        elif (locationY == "south"):
          print("307 is on your right")
        elif (locationY == True):
          if (int(starting) % 2 == 0):
            Turning = "left"
          else:
            Turning = "right"
            
          print("Turn " + Turning + ", go to the 400/300 intersection")
          print("8 Turn right, go down the 300 hallway and 307 will be on your left")
          
      elif (int(hallway) % 400 <= 11):
        if (locationY == "north"):
          
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
          
          print("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
        elif (locationY == "south"):
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
            
          print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)

        elif (locationY == True):
          if (int(hallway) % 2 == 0):
            EO = "right"
          else:
            EO = "left"
    
      
          print("Turn right, go to the 300/400 interseciton")
          print("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO)
          
    else:    
      if (locationY == "south"):
        if (int(hallway) % 2 == 0):
            EO = "left"
        else:
            EO = "right"
            
        print("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO)
        
      elif (locationY == "north"):

        if (int(hallway) % 2 == 0):
            EO = "right"
        else:
            EO = "left"
        if (int(starting) % 200 <= 13 and int(hallway) < 400):
          print("why")
          print("Go down the 300 hallway and " + hallway + " will be on your left")
        else:
          
          if (hallway == "307"):
            print("Turn left, go to the 400/300 intersection")
            print("Turn right and 307 will be on your left")
            
          else:  
            print("Turn right, go down the 400 hallway and " + hallway + " will be on your " + EO) ## was ("Turn left, go down the 400 hallway and " + hallway + " will be on your " + EO) 
    




    
print()
      
    #coming down left and right will be different then if they are facing up

#if statements

# Make if statements to determine which direction the person needs to go to get to a checkpoint, once they're at a checkpoint bring them into the checkpoint loop to get them to their designated hallway.

# This while loop has logical error somewhere
if (isinstance(endX, int)):
  print("This is a int")
  print(type(endX))
  
  if (transfer):
    while (startingY != endY):
      if (moves > 0):
            topMoveCheck()
            moves += 1
     
      else:
          topFirstMove()

    #run transfer function that will take them down the nearest stairs (at their checkpoint)
    #run botMovecheck
      
    pass
  else:
    
  
    while (startingX != endX or startingY != endY):
        #print("Number of moves: " + str(moves))
        #input("bruh pleast")
    
        if (moves > 0):
            topMoveCheck()
            moves += 1
     
        else:
            topFirstMove()
    
    
    if ((startingX == endX) and (startingY == endY)):
      
      """
        print("\nFinal startingX: " + str(startingX))
        print("Final startingY: " + str(startingY))
        print("Desired endX: " + str(endX))
        print("Desired endY: " + str(endY))
      """
      topClassroom()
      
else:

  
  print("This is a string")
  print(type(startingX))

  if (transfer):
    while (startingY != endY):
      if (moves > 0):
            topMoveCheck()
            moves += 1
      else:
          topFirstMove()

    #run transfer function that will take them down the nearest stairs (at their checkpoint)
    #run botMovecheck
print(moves)




    # print(moves)

        #print("\nI'm so stupid")
        #print(str(startingX) + ", " + str(startingY))
       #print(input("bruh"))

        #if (locationY != endY):
        # print("\nmoving X")

        #else: #(locationX == endX):
        # print("\nmoving Y")



        #split if statements into Y and X don't have four different if statements. Have two if statements with two in them, Y and X

#old version
'''

while (hallway not in hallways[i][e]):
  print('in loop')
  e += 1

  if (e + 1 > len(hallways[i])):
    i += 1
    e = 0
    print(i)
    #print("\n")
else:
  print(i)
  print(e)
  print('found index')

'''

#we can make a function that holds if statements to connect the sections

#print('Hello World!')
#yo - Shaan