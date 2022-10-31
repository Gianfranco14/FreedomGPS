# FreedomGPS

This project is a mobile application that allows the user to navigate around my school building without any prior knowledge of its layout. The app finds the most optimal route to get the user to their destination and displays the instructions.

There are two folders in this repository,

The Demo App folder contains all files used in the version of our app that we showed to our principal for publication. This includes images, Python files, and Kivy files.

The Updated Code folder only contains our large code base, holding all of our back-end code. This code base has improvements made after the demo version, however, they are not finalized which is why they are not in the application code files. The code for this "main.py" file is very messy but it is the chaos in which I work.

Both folders have a file titled "locations.py" which holds all classrooms of our school. The code then assigns values to different sections of the school based on a set of conditional statements. After, the starting and ending classrooms are given an X and Y position. Finally, our algorithm runs until both coordinates match, printing every instruction on the way.

