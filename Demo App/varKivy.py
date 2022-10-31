screen_helper = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:set text_color get_color_from_hex("#4a4939")
#:set focus_color get_color_from_hex("#e7e4c0")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#b2c5cd")
#:set selected_color get_color_from_hex("#0c6c4d")
 
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color
 
 
<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True
 
 
 
ScreenManager:
    MenuScreen:
    ProfileScreen:
    scr_1:
    scr_2:
    scr_3:
 
<MenuScreen>:  
    name: 'menu'
    primary_palette: 'Indigo'
    Image:
        source: "logo.jpeg"
        pos_hint: {"center_x": 0.5, "center_y": 0.67}
 
    MDTextField:
        hint_text: 'Enter your starting classroom'
        id: startingClassroom
        halign: 'center'
	    size_hint: (0.5,0.12)
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        font_size: sp(22)
        
 
 
    MDTextField:
        hint_text: 'Enter your ending classroom'
        id: endingClassroom
        halign: 'center'
	    size_hint: (0.5,0.12)
        pos_hint: {"center_x": 0.5, "center_y": 0.24}
        font_size: sp(22)
        
        
   
    MDLabel:
        halign: 'center'
        size_hint: (0.8,1)
        pos_hint: {"center_x": 0.5, "center_y": 0.30}
        theme_text_color: "Secondary"
 
    MDLabel:
        halign: "center"
        size_hint: (0.8,1)
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        theme_text_color: "Primary"
        font_style: "H5"
 
    MDLabel:
        text: ""
        id: error_text
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.06}
        font_size: sp(13)
   
    MDLabel:
        text: ""
        id: error_text_start
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        color:(1,245,245)
        font_size: sp(13)
   
    MDLabel:
        text: ""
        id: error_text_end
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.19}
        color:(1,245,245)
        font_size: sp(13)
 
    MDFillRoundFlatButton:
        text: 'Get Directions'
        font_size: sp(17)
        pos_hint: {'center_x':0.5,'center_y':0.13}
        specific_text_color: get_color_from_hex("#ffffff")
        md_bg_color: get_color_from_hex("#414caf")
        on_press: root.testFunction()
        on_release:
            app.ideal = 1
            app.val = app.val + 1 if any(startingClassroom.text in sl for sl in app.halls) else app.val + 0      
           
            app.val1 = app.val1 - 1 if any(endingClassroom.text in sl for sl in app.halls) else app.val1 + 0
            error_text_start.text = "" if any(startingClassroom.text in sl for sl in app.halls) else "Please Enter a Valid Starting Location"
            error_text_end.text = "" if any(endingClassroom.text in sl for sl in app.halls) else "Please Enter a Valid Ending Location"
 
            app.val1 = app.val1 + 1 if endingClassroom.text == startingClassroom.text else app.val1 + 0
 
            root.manager.current = 'profile' if app.val == app.val1 else 'menu'
            error_text.text = "" if app.val == app.val1 else "Please Enter a Valid Location Combination"
            startingClassroom.text = "" if app.val == app.val1 else ""
            endingClassroom.text = "" if app.val == app.val1 else ""
 
 
            root.addText()
 
            app.val = 0
            app.val1 = 2
            app.val2 = 0
            app.val3 = 0
    MDNavigationLayout:
 
        ScreenManager:
 
            MDScreen:
 
                MDToolbar:
                    id: toolbar
                    title: 'Freedom GPS'
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#414caf")
                    specific_text_color: get_color_from_hex("#ffffff")
                    left_action_items:
                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
                    right_action_items:
                        [                             [                             'cellphone-marker', lambda x:                             root.change_screen("menu")                             ]                             ]
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color
           
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: "Freedom GPS"
                    title_color: text_color
                    text: ""
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
 
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: text_color
                    text: "Home"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "menu"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "Tools"
               
                DrawerClickableItem:
                    icon: "map-outline"
                    text_right_color: text_color
                    text: "Map"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_1"
 
 
                DrawerClickableItem:
                    icon: "help-rhombus"
                    text: "Help"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_2"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "More"
 
                DrawerLabelItem:
                    icon: "account-supervisor"
                    text: "Contributors"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_3"
 
   
   
<ProfileScreen>:
    name: 'profile'
 
    MDToolbar:
        title: 'Freedom GPS'
        pos_hint: {'top': 1}
        md_bg_color: get_color_from_hex("#414caf")
        right_action_items:
            [                             [                             'cellphone-marker', lambda x:                             root.change_screen("menu")                             ]                             ]
 
    MDLabel:
        text: 'Directions'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.82}
        font_size: sp(22)
 
    MDLabel:
        id: name_text
        text: ""
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        font_size: 22
 
    MDFillRoundFlatButton:
        text: 'Choose another destination'
        font_size: sp(17)
        specific_text_color: get_color_from_hex("#ffffff")
        md_bg_color: get_color_from_hex("#414caf")
        pos_hint: {'center_x':0.5,'center_y':0.13}
        on_release: root.manager.current = 'menu'; root.on_leave()
    MDNavigationLayout:
 
        ScreenManager:
 
            MDScreen:
 
                MDToolbar:
                    id: toolbar
                    title: 'Freedom GPS'
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#414caf")
                    specific_text_color: get_color_from_hex("#ffffff")
                    left_action_items:
                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
                    right_action_items:
                        [                             [                             'cellphone-marker', lambda x:                             root.change_screen("menu")                             ]                             ]
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color
 
            MDNavigationDrawerMenu:
 
                MDNavigationDrawerHeader:
                    title: "Freedom GPS"
                    title_color: text_color
                    text: ""
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
               
 
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: text_color
                    text: "Home"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "menu"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "Tools"
 
                DrawerClickableItem:
                    icon: "map-outline"
                    text_right_color: text_color
                    text: "Map"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_1"
 
 
                DrawerClickableItem:
                    icon: "help-rhombus"
                    text: "Help"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_2"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "More"
 
                DrawerLabelItem:
                    icon: "account-supervisor"
                    text: "Contributors"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_3"
 
 
 
 
<scr_1>:
    name: 'scr_1'
    MDLabel:
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
    
        FitImage:
            source: "bottomFloor.png"
            size: (700,700)
            height: 500
            size_hint_x: 1
            halign: 'center'
            pos_hint: {"center_x": 0.5, "center_y": 1}
            


            
    MDNavigationLayout:
 
        ScreenManager:
 
            MDScreen:
 
                MDToolbar:
                    id: toolbar
                    title: 'Freedom GPS'
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#414caf")
                    specific_text_color: get_color_from_hex("#ffffff")
                    left_action_items:
                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
                    right_action_items:
                        [                             [                             'cellphone-marker', lambda x:                             root.change_screen("menu")                             ]                             ]
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color
 
            MDNavigationDrawerMenu:
 
                MDNavigationDrawerHeader:
                    title: "Freedom GPS"
                    title_color: text_color
                    text: ""
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
 
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: text_color
                    text: "Home"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "menu"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "Tools"
   
 
                DrawerClickableItem:
                    icon: "map-outline"
                    text_right_color: text_color
                    text: "Map"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_1"
 
 
                DrawerClickableItem:
                    icon: "help-rhombus"
                    text: "Help"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_2"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "More"
 
                DrawerLabelItem:
                    icon: "account-supervisor"
                    text: "Contributors"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_3"
 
 
 
 
<scr_2>:
    name: 'scr_2'
    MDLabel:
        text: 'Just input your starting classroom and destination, and we will show you how to get there!'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        font_size: sp(22)
        
    MDLabel:
        text: 'Follow the instructions given and make sure to use the hallway indicators at each hallway intersection.'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.50}
        font_size: sp(22)
        
    MDLabel:
        text: 'If you need more assistance, click on the map icon in the toolbar to see a map of where you are going.'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        font_size: sp(22)
        
    MDLabel:
        text: 'Stay safe out there and get to class!!!'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.10}
        font_size: sp(22)
        
    MDNavigationLayout:
 
        ScreenManager:
 
            MDScreen:
 
                MDToolbar:
                    id: toolbar
                    title: 'Freedom GPS'
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#414caf")
                    specific_text_color: get_color_from_hex("#ffffff")
                    left_action_items:
                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
                    right_action_items:
                        [                             [                             'cellphone-marker', lambda x:                             ScreenManager.change_screen("menu")                             ]                             ]
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color
 
            MDNavigationDrawerMenu:
 
                MDNavigationDrawerHeader:
                    title: "Freedom GPS"
                    title_color: text_color
                    text: ""
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
               
 
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: text_color
                    text: "Home"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "menu"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "Tools"
               
                DrawerClickableItem:
                    icon: "map-outline"
                    text_right_color: text_color
                    text: "Map"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_1"
 
 
                DrawerClickableItem:
                    icon: "help-rhombus"
                    text: "Help"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_2"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "More"
 
                DrawerLabelItem:
                    icon: "account-supervisor"
                    text: "Contributors"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_3"
 
 
<scr_3>:
    name: 'scr_3'
    MDLabel:
        text: 'Full-Stack Developer'
        halign: 'center'
        bold: True
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
        font_size: sp(25) 
        
    MDLabel:
        text: 'Gianfranco Vivanco'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.68}
        font_size: sp(20)
        
    MDLabel:
        text: 'Back-end Developer'
        halign: 'center'
        bold: True
        pos_hint: {"center_x": 0.5, "center_y": 0.58}
        font_size: sp(25) 
        
    MDLabel:
        text: 'Arjun Rao'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.51}
        font_size: sp(20)
        
    MDLabel:
        text: 'Front-end Developer'
        halign: 'center'
        bold: True
        pos_hint: {"center_x": 0.5, "center_y": 0.41}
        font_size: sp(25) 
    
    MDLabel:
        text: 'William Tuck'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.34}
        font_size: sp(20)
        
    MDLabel:
        text: 'Sponsor'
        halign: 'center'
        bold: True
        pos_hint: {"center_x": 0.5, "center_y": 0.25}
        font_size: sp(25)
        
    MDLabel:
        text: 'Kevin Cabaniss'
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        font_size: sp(20)
        
    MDLabel:
        text: "Special thanks to Mr. Cabaniss' 3rd block class for being our testers"
        halign: 'center'
        pos_hint: {"center_x": 0.5, "center_y": 0.15}
        font_size: sp(15)
        
    
    MDNavigationLayout:
 
        ScreenManager:
 
            MDScreen:
 
                MDToolbar:
                    id: toolbar
                    title: 'Freedom GPS'
                    pos_hint: {'top': 1}
                    md_bg_color: get_color_from_hex("#414caf")
                    specific_text_color: get_color_from_hex("#ffffff")
                    left_action_items:
                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
                    right_action_items:
                        [                             [                             'cellphone-marker', lambda x:                             root.change_screen("menu")                             ]                             ]
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color
 
            MDNavigationDrawerMenu:
 
                MDNavigationDrawerHeader:
                    title: "Freedom GPS"
                    title_color: text_color
                    text: ""
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
               
 
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: text_color
                    text: "Home"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "menu"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "Tools"
 
                DrawerClickableItem:
                    icon: "map-outline"
                    text_right_color: text_color
                    text: "Map"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_1"
 
 
                DrawerClickableItem:
                    icon: "help-rhombus"
                    text: "Help"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_2"
 
                MDNavigationDrawerDivider:
 
                MDNavigationDrawerLabel:
                    text: "More"
 
                DrawerLabelItem:
                    icon: "account-supervisor"
                    text: "Contributors"
                    on_press:
                        nav_drawer.set_state("close")
                        root.manager.current = "scr_3"
 
 
 
"""
