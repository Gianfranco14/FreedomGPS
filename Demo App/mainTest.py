from cgi import test
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp
from varKivy import screen_helper
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.toolbar import MDToolbar
from kivy.properties import ObjectProperty, StringProperty
import time
from threading import Thread
from backend import *
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivy.uix.image import Image
import global_
from kivy.core.window import Window, WindowBase
from kivy.lang import Builder
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.app import App
from kivy.base import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
 
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"
 
 
 
 
arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
labels = []
errorMessage = ""
 
 
class MenuScreen(Screen):
   
 
    def addText(self):
        #make testText a var outside all classes
        arr = global_.arrGlobal
        global labels
 
        s2 = self.manager.get_screen('profile')
        #s2.add_widget(Label(text="test", pos_hint={"center_x": 0.5, "center_y": 0.3 }))
 
 
        position = 0.483
        lowerPosition = position
        upperPosition = position
        div = 0
        if (len(arr) == 0):
            s2.label = MDLabel(
            halign = "center",
            text = "",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.483},  #0.7 == top
            )
            labels.append(s2.label)
            s2.add_widget(s2.label)
 
        elif (len(arr) == 1):
            s2.label = MDLabel(
            halign = "center",
            text = arr[0],
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.483},  #0.7 == top
            )
            labels.append(s2.label)
            s2.add_widget(s2.label)
 
        else:
            difference = 0.45 / (len(arr) - 1)
 
            if (len(arr) % 2 != 0):
                #make if statement for one arg
 
 
                center = int((len(arr) - 1) / 2)
 
                s2.label = MDLabel(
                halign = "center",
                text = arr[center],
                size_hint = (0.8,1),
                pos_hint = {"center_x": 0.5, "center_y": 0.483},  #0.7 == top
                )
                labels.append(s2.label)
                s2.add_widget(s2.label)
 
                if center < 2:
                    div = 2
 
                elif 2 < center < 4:
                    div = 1
                   
                elif center == 2:
                    div = 1.2
 
                else:
                    div = 0.9
 
                down = center
                up = center
                for i in range(center):
 
                    lowerPosition = (lowerPosition - difference/div)
                    upperPosition = (upperPosition + difference/div)
                    down = down - 1
                    up = up + 1
 
                    s2.label = MDLabel(
                    halign = "center",
                    text = arr[up],
                    size_hint = (0.8,1),
                    pos_hint = {"center_x": 0.5, "center_y": lowerPosition},  #0.7 == top
                    )
                    labels.append(s2.label)
                    s2.add_widget(s2.label)
 
                    s2.label = MDLabel(
                    halign = "center",
                    text = arr[down],
                    size_hint = (0.8,1),
                    pos_hint = {"center_x": 0.5, "center_y": upperPosition},  #0.7 == top
                    )
                    labels.append(s2.label)
                    s2.add_widget(s2.label)
 
            else:
                #make if statement for two args
                center = int((len(arr) + 1) / 2)
 
                if (len(arr) == 2):
                    s2.label = MDLabel(
                    halign = "center",
                    text = arr[0],
                    size_hint = (0.8,1),
                    pos_hint = {"center_x": 0.5, "center_y": 0.5 + difference/7},  #0.7 == top
                    )
                    labels.append(s2.label)
                    s2.add_widget(s2.label)
 
                    s2.label = MDLabel(
                    halign = "center",
                    text = arr[1],
                    size_hint = (0.8,1),
                    pos_hint = {"center_x": 0.5, "center_y": 0.5 - difference/7},  #0.7 == top
                    )
                    labels.append(s2.label)
                    s2.add_widget(s2.label)
 
                else:
 
               
 
                    s2.label = MDLabel(
                    halign = "center",
                    size_hint = (0.8,1),
                    pos_hint = {"center_x": 0.5, "center_y": 0.483},  #0.7 == top
                    )
                    labels.append(s2.label)
                    s2.add_widget(s2.label)
 
                    if center < 3:
                        div = 2
 
                    elif 3 < center < 5:
                        div = 1
                       
                    elif center == 3:
                        div = 1.2
 
                    else:
                        div = 0.9
 
                    up = int(len(arr)/2) - 1    # going up
                    down = int(len(arr)/2)      # bottom up
 
                    for i in range(int((len(arr)/2))):
                        down = down - 1
                        up = up + 1
 
                        if (i == 0):
                            lowerPosition = (lowerPosition - ((difference/div)/2))
                            upperPosition = (upperPosition + ((difference/div)/2))
                        else:
                            lowerPosition = (lowerPosition - difference/div)
                            upperPosition = (upperPosition + difference/div)
 
                       
 
                        s2.label = MDLabel(
                        halign = "center",
                        text = arr[up],
                        size_hint = (0.8,1),
                        pos_hint = {"center_x": 0.5, "center_y": lowerPosition},  #0.7 == top
                        )
                        labels.append(s2.label)
                        s2.add_widget(s2.label)
 
                        s2.label = MDLabel(
                        halign = "center",
                        text = arr[down],
                        size_hint = (0.8,1),
                        pos_hint = {"center_x": 0.5, "center_y": upperPosition},  #0.7 == top
                        )
                        labels.append(s2.label)
                        s2.add_widget(s2.label)
 
 
    def testFunction(self):
        global_.i = 0
        global_.e = 0
        global_.startingX = 0
        global_.startingY = 0
        global_.endX = 0
        global_.endY = 0
        global_.locationX = ""
        global_.locationY = ""
        global_.moving = ""
        global_.moves = 0
        global_.EO = ""
        global_.Turning = ""
        global_.starting = ""
        global_.hallway = ""
        global_.arrGlobal = []
        global errorMessage
        s1 = self.manager.get_screen('menu')
        print("THIS IS S1 " + str(s1))
 
        starting = s1.ids.startingClassroom.text
        ending = s1.ids.endingClassroom.text
       
 
       
 
        if (starting == "" or ending == ""):
            #print("Please choose your classrooms")
            errorMessage = "Please enter two classrooms"
 
            #s1.ids.startingClassroom.text = ""#
            #s1.ids.endingClassroom.text = ""#
 
        elif (starting == ending):
            #print("?")
            #print("Please enter a valid classroom")
            errorMessage = "Please choose a different ending location"
           
            #s1.ids.startingClassroom.text = ""#
            #s1.ids.endingClassroom.text = ""#
 
 
       
        #For some reason starting == ending does both of these conditionals so all you need is the two above
        elif (any(starting in sl for sl in hallways) == False):
            #s1.ids.startingClassroom.text = ""#
            #s1.ids.endingClassroom.text = ""#
            #print("Starting classroom does not exist")
            errorMessage = "Please enter a valid starting classroom"
       
        elif (any(ending in sl for sl in hallways) == False):
            #s1.ids.startingClassroom.text = ""#
            #s1.ids.endingClassroom.text = ""#
            #print("Ending classroom does not exist")
            errorMessage = "Please enter a valid ending classroom"
       
   
       
 
        try:
            backend(s1)
 
        except ValueError:
            print("this don't work")
 
        arr = global_.arrGlobal
        print(errorMessage)
           
   
 
        #s2.ids.name_text.text = "test"
    pass
 
 
class ProfileScreen(Screen):
    def on_leave(self):
       
       
        for i in range(len(labels)):
            self.remove_widget(labels[i])
       
        s1 = self.manager.get_screen('menu')
        s1.ids.startingClassroom.text = ""
        s1.ids.endingClassroom.text = ""
 
        Window.release_all_keyboards()
 
 
    pass
 
 
class scr_1(Screen):
    pass
 
class scr_2(Screen):
    pass
 
class scr_3(Screen):
    pass
 
 
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(scr_1(name='scr_1'))
sm.add_widget(scr_2(name='scr_2'))
sm.add_widget(scr_3(name='scr_3'))
 
 
 
class DemoApp(MDApp):
    global errorMessage
    val = 0
    val1 = 2
    val2 = 0
    val3 = 0
    ideal = 1
    halls = hallways
    error1 = 0
    error2 = 0
    errMessage = errorMessage
    print(errorMessage)
    print(errMessage)
   
    def flip(self):
        print("working...")
 
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        screen = Builder.load_string(screen_helper)
        return screen
 
 
 
DemoApp().run()
