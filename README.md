# Bre3Der

Hi! Thanks for checking this out! Bre3Der is an genetic algorthim that evolves 3D shapes over time.

## Getting Started

### Download
I'd recommend downloading the entire repository by clicking ``Code`` and then the ``Download Zip`` option. If you don't want to download everything, you'll need the following files/folders to get Bre3Der working:
* ``Bre3Der.py``
* ``requirements.txt``
* Shapes folder
* ``phylogenetic.csv``

### Vitural environment

I'd recommend using a virtual environment when interacting with this project. Project was developed in PyCharm using Python 3.8.4.

### Requirements
The  ``requirements.txt``  file contains a list of all the packages you will need to use in order to have the application run successfully. Once a virtual environment has been set up and activated, these requirements can be installed though the command:

``pip install -r requirements.txt``

After the requirements are installed, you can start playing with Bre3Der!

## Using Bre3Der

When the ``Bre3Der.py`` code is run, you will be prompted to enter a username in your console (do not leave this blank please). After pressing ``enter`` a new window will be opened
and you'll be presented with 3 options: From Scratch, Random Existing Shape, or From File.

### From Scratch
This option will present you with either a cube or a pyramid. From here, type the shape number you wish to evolve in the text bar 
on the left-hand side of the window, and either press ``enter`` or click the ``Evolve`` button to start you journey! When you are 
finished evolving your shape, simply press ``esc`` or click the ``Save`` button and your shape will be saved to the file 
displayed on your screen!

### Random Existing Shape
Instead of begging oyur journey from a basic shape, you'll pick up where other people have left off! This option takes 10 random 
shapes from the ``Shapes`` folder and present them to you, allowing you to choose from them. Once again, press ``esc`` or click
``Save`` to end your current journey and save your shape!

### From File
This does exactly what it sounds like, allows you to start from a specific file! By inputting the name of a file into the text 
box on the left side of the window, you can pick up right where you (or someone else) left off last time! Saving is the exact 
same as the other two methods so I won't rehash it here.

### Check your parents!
By opening the ``.csv`` file that appears in the same directory as you ``.py`` files, you can see the parents of all the shapes
previously created. The purpose of this is to generate a phylogenetic tree showing all the different shapes that can be derrived 
from one parent. If you'd like to explore how many different shapes came from the ``cube`` shape, simply have a look for all 
instances of ``cube`` in the ``Parents`` column and open up the respective file in the ``Child`` column! 

You are also able to generate phylogenetic trees using the ``trees.py`` file! Simply execute the script with the ``.csv`` file in the same directory the ``cube.txt`` and ``pyramid.txt`` files will be generated. 

### Send your shapes!
If you would like your shapes to be uploaded to this repo so others can evolve them please email "bre3Der@gmail.com" with a 
zip folder containing all your shapes. Please refrain from changing the names/numbers in any of the files after they've been
saved!

## Feedback
Any feedback would be greatly appreciated!! Feel free to email me at bre3Der@gmail.com! Anything from UI to nitty gritty 
formatting is appreciated.


